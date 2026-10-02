Loco Reaper v1 - TernakSukses

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
