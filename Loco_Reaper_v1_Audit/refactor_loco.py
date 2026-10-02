from pathlib import Path
import re, json, hashlib, collections, zipfile

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'upload' / 'The Gold Reaper @sp77forex.mq4'
OUTPUT = ROOT / 'Loco_Reaper_v1.mq4'
AUDIT = ROOT / 'loco_audit'
AUDIT.mkdir(exist_ok=True)
original_bytes = SOURCE.read_bytes()
original = original_bytes.decode('utf-16')
branding = [
    ('#property copyright  "Telegram @Sp77Forex"', '#property copyright  "TernakSukses"'),
    ('#property version    "4.1"', '#property version    "1.00"'),
    ('"The Gold Reaper V4.1"', '"Loco Reaper v1"'),
    ('"The Gold Reaper V4.1 - OneChartSetup"', '"Loco Reaper v1 - OneChartSetup"'),
]
baseline = original
for old, new in branding:
    assert baseline.count(old) == 1
    baseline = baseline.replace(old, new)

# Strings, character/date/color literals, and comments are indivisible tokens.
LEX = re.compile(r'(?P<comment>//[^\r\n]*|/\*[\s\S]*?\*/)|(?P<string>"(?:\\[\s\S]|[^"\\])*"|\'(?:\\[\s\S]|[^\'\\])*\')|(?P<identifier>[^\W\d]\w*)|(?P<other>[\s\S])')
def lex(text):
    result = [(m.lastgroup, m.group()) for m in LEX.finditer(text)]
    assert ''.join(t for _, t in result) == text
    return result

tokens = lex(baseline)
identifiers = {t for k,t in tokens if k == 'identifier'}
code = ''.join(t if k not in ('comment','string') else ' ' * len(t) for k,t in tokens)
types = collections.defaultdict(set)
for typ, name in re.findall(r'\b(bool|int|long|double|float|string|datetime|uint|char|uchar|short|ushort|ulong)\s+([^\W\d]\w*)',code):
    types[name].add(typ)

mapping = {}
reasons = {}
for name in sorted(identifiers):
    if name.startswith(('总_', '子_', '临_', '木_')):
        parts = name.split('_')
        scope = {'总':'Global','子':'Local','临':'Temp','木':'Arg'}[parts[0]]
        index = parts[2] if parts[0] == '临' else parts[1]
        tag = parts[1] if parts[0] == '临' else parts[2]
        actual = types.get(name,set())
        type_name = next(iter(actual)).capitalize() if len(actual)==1 else 'Value'
        # Preserve the source tag to distinguish separate identifiers even
        # when their real declared types coincide.
        array_tag = '_Array' if any(p.startswith('si') or p=='ko' for p in parts[3:]) else ''
        mapping[name] = f'LR_{scope}{int(index):03d}_{type_name}_{tag}{array_tag}'
        reasons[name] = 'neutral; scope/index and declared type; no inferred trading role'
    elif re.fullmatch(r'lizong_\d+', name):
        mapping[name] = f'LR_EngineRoutine{int(name.split("_")[1]):02d}'
        reasons[name] = 'neutral function name; original routine number retained'

verified = {
    '总_336_st_3130': 'LR_CurrentSymbol',
    '总_190_in_518': 'LR_SymbolDigits',
    '总_93_in_1F0': 'LR_ActiveMagicNumber',
    '总_334_st_3120': 'LR_ActiveOrderComment',
    '总_229_do_1E00': 'LR_NormalizedPriceUnit',
    '总_221_do_1A80': 'LR_StopLevelPriceDistance',
    '总_309_do_2898': 'LR_FreezeLevelPriceDistance',
    '总_1_do_0': 'LR_CurrentSpreadPrice',
    'lizong_11': 'LR_FindEntrySwingHigh',
    'lizong_13': 'LR_FindAuxiliarySwingHigh',
    'SuperProfits77': 'LR_IsAmericanDST',
}
for old,new in verified.items():
    assert old in identifiers
    mapping[old] = new
    reasons[old] = 'role established from source assignments or function body; not a behavior change'

# Strategy IDs are extracted from each loader's literal order-comment suffix.
for n in range(37,46):
    match = re.search(r'\bvoid\s+lizong_'+str(n)+r'\s*\(\)\s*\{([\s\S]*?)(?=\bvoid\s+lizong_'+str(n+1)+r'\s*\()',baseline)
    assert match, n
    suffixes = re.findall(r'ST1_Comment\s*\+\s*"_XAUUSD_(\d+)"', match.group(1))
    assert len(suffixes)==1, (n,suffixes)
    mapping[f'lizong_{n}'] = f'LR_LoadStrategy{int(suffixes[0]):02d}'
    reasons[f'lizong_{n}'] = 'strategy number verified against source order-comment suffix'

assert len(set(mapping.values())) == len(mapping), 'rename collision'
assert not (set(mapping.values()) & identifiers), 'collision with existing identifier'
assert all(re.fullmatch(r'[A-Za-z_]\w*',v) and len(v)<=63 for v in mapping.values())
assert not re.search(r'__\w+__', code), 'name-sensitive compiler macro requires review'
renamed = ''.join(mapping.get(t,t) if k=='identifier' else t for k,t in tokens)
inverse = {new:old for old,new in mapping.items()}
restored = ''.join(inverse.get(t,t) if k=='identifier' else t for k,t in lex(renamed))
assert restored == baseline, 'inverse transformation differs'
for old,new in reversed(branding):
    assert restored.count(new)==1
    restored=restored.replace(new,old)
assert restored.encode('utf-16') == original_bytes, 'not byte-identical to original'

new_tokens = lex(renamed)
assert len(new_tokens)==len(tokens)
assert all((a==b and (y==mapping.get(x,x) if a=='identifier' else x==y))
           for (a,x),(b,y) in zip(tokens,new_tokens))
assert not any(any(ord(c)>127 for c in t) for k,t in new_tokens if k=='identifier')
assert len(renamed.splitlines())==len(original.splitlines())
OUTPUT.write_bytes(renamed.encode('utf-16'))

counts = collections.Counter(t for k,t in tokens if k=='identifier')
entries = [{'old':old,'new':new,'occurrences':counts[old],'basis':reasons[old]} for old,new in sorted(mapping.items())]
(AUDIT/'rename_map.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha = lambda b:hashlib.sha256(b).hexdigest()
result = {
    'original_sha256':sha(original_bytes),
    'output_sha256':sha(OUTPUT.read_bytes()),
    'source_lines':len(original.splitlines()),
    'renamed_identifiers':len(mapping),
    'renamed_occurrences':sum(counts[n] for n in mapping),
    'renamed_functions':sum(n.startswith('lizong_') or n=='SuperProfits77' for n in mapping),
    'neutral_names':sum(reasons[n].startswith('neutral') for n in mapping),
    'inverse_byte_comparison':'PASS',
    'token_comparison':'PASS',
    'name_collision_check':'PASS',
    'all_code_identifiers_ascii':'PASS',
    'compiler':'NOT RUN - MetaEditor/MT4 unavailable',
    'backtest':'NOT RUN - MT4 and matched test data unavailable',
}
(AUDIT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(AUDIT/'README.txt').write_text('''Loco Reaper v1 - TernakSukses

Tahap revisi: seluruh identifier internal tersamarkan diganti secara konsisten.
Nama netral menunjukkan peran trading belum dipetakan secara semantik.
Ini belum merupakan dokumentasi lengkap seluruh strategi.
Nama input publik, enum publik, serta event init/deinit/OnTick dipertahankan.
Rumus, literal trading, string order, magic number, urutan kode, kondisi,
tipe data, komentar asli, encoding UTF-16 dan line ending CRLF dipertahankan.
Komentar asli bisa masih memuat nama fungsi lama; gunakan rename_map.json.
Perubahan branding: copyright, versi, dan dua judul panel saja.
ST1_Comment tetap The Gold Reaper untuk menjaga perilaku sumber asli.

VERIFIKASI
Setelah semua rename dan empat perubahan branding dibalik, byte hasil
sama persis dengan file asli. Pemetaan satu-ke-satu dan bebas benturan nama.
Token selain identifier identik dengan baseline yang telah diberi branding.
Pemeriksaan ini bukan hasil compile atau bukti kesamaan backtest.
MetaEditor dan MT4 tidak tersedia pada lingkungan pengerjaan.

LANGKAH MT4
Compile source asli dan revisi menggunakan build MetaEditor yang sama.
Bandingkan error/warning, lalu backtest dengan terminal, simbol, timeframe,
data tick, rentang tanggal, spread, modal, leverage, dan input identik.
Samakan GMT dan faktor eksternal. Cocokkan seluruh entry, arah, lot,
modifikasi SL/TP, pending, waktu exit, serta hasil transaksi.
Simpan laporan dan journal keduanya untuk diperiksa bila ada perbedaan.

REPRODUKSI
refactor_loco.py menggunakan Python standard library.
Taruh source asli di upload/The Gold Reaper @sp77forex.mq4 lalu jalankan
python refactor_loco.py. Script menghasilkan source, peta, dan bukti pemeriksaan.
''',encoding='utf-8')
with zipfile.ZipFile(ROOT/'Loco_Reaper_v1_Audit.zip','w',zipfile.ZIP_DEFLATED) as z:
    z.write(OUTPUT,OUTPUT.name)
    z.write(Path(__file__),'refactor_loco.py')
    for f in sorted(AUDIT.iterdir()): z.write(f,f.name)
print(json.dumps(result,indent=2))
