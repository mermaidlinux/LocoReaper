# Pemeriksaan lingkungan dan compile — 2 Oktober 2026

## Repository dan cakupan

Folder kerja: `C:\LocoReaper`. Saat pemeriksaan awal folder belum memiliki repository Git. `git ls-remote --symref https://github.com/mermaidlinux/LocoReaper.git` berhasil (exit 0) tanpa referensi: remote kosong. Repository lokal diinisialisasi dengan branch `main`, origin diarahkan ke URL tersebut. Tidak ada clone, penghapusan, penimpaan source, atau force push.

Paket audit sudah berbentuk direktori, berisi source, README, script refactor, rename map, dan verification JSON. Tidak ditemukan ZIP/RAR/7z untuk diekstrak. Salinan source utama dan audit identik. Metadata verifikasi lama tetap dipertahankan sebagai bukti historis; laporan ini mencatat pemeriksaan terbaru.

## Lingkungan pengujian terverifikasi

| Komponen | Path / versi |
| --- | --- |
| Terminal MT4 | `C:\Program Files (x86)\MT4-LocoReaper-Test\terminal.exe` |
| Versi terminal | `4.0.0.1479` |
| MetaEditor | `C:\Program Files (x86)\MT4-LocoReaper-Test\metaeditor.exe` |
| Versi MetaEditor | `5.0.0.2423` |
| Folder data | `C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\499FDE4F0FA2ED8CA44CC0F1E1772F49` |

Isi `origin.txt` pada folder data menunjuk tepat ke instalasi pengujian. Daftar origin folder data lainnya menunjukkan instalasi terpisah. Snapshot proses menemukan satu MT4 lama aktif, dua MT5 aktif, terminal pengujian, dan MetaEditor pengujian. Instalasi MT4 lama lainnya ditemukan melalui origin folder data, tetapi tidak terlihat sebagai proses aktif saat snapshot. Path terminal lama yang mengandung pengenal akun tidak dimasukkan ke dokumentasi publik.

Proses yang sama tetap ditemukan setelah compile. Tidak ada perintah stop/restart terminal, perubahan akun, konfigurasi terminal, penyalinan EA ke folder data, atau backtest. Snapshot proses bukan audit integritas seluruh file terminal; folder akun/config/history tidak dibaca atau disalin.

## Integritas source dan perbedaan baseline

SHA-256 sebelum dan setelah compile:

| File | SHA-256 |
| --- | --- |
| Gold Reaper pengguna | `33ba69c2f12e1d320a7e583d330443c6b56b5ae25f4ee33a450db57cb5e1fc54` |
| Loco utama dan audit | `32d8e3a57ce0ead9cadfac014d3eb90fbf3ed565f9b151fdbeff9644d7c5000e` |
| Baseline audit yang direkonstruksi | `4dd736b5d36414fb53c9aafa04aeffcc6972e692f43a9affea6173eefa704f60` |

Rename identifier dibalik menggunakan `rename_map.json`, dengan string dan komentar dipertahankan, kemudian empat perubahan branding dibalik. Hash hasil rekonstruksi tepat sama dengan `original_sha256` dalam verification JSON. Dibanding source Gold pengguna, hanya dua baris teks panel berbeda:

| Baris | Gold pengguna | Baseline audit |
| --- | --- | --- |
| 6222 | `TS Gold Reaper V4.1` | `The Gold Reaper V4.1` |
| 6226 | `TS Gold Reaper V4.1 - OneChartSetup` | `The Gold Reaper V4.1 - OneChartSetup` |

Selisih ini dilaporkan sebelum compile. File asli tidak diubah. Rekonstruksi hanya disimpan dalam `build/` yang diabaikan Git. Pemeriksaan ini mendukung kesamaan source setelah rename/branding dibalik, bukan bukti kesamaan hasil trading atau backtest.

## Metode compile

Kedua source disalin ke `C:\LocoReaper\build` yang baru dibuat. MetaEditor dari instalasi pengujian dipanggil secara berurutan dengan argumen berikut:

```text
/compile:"C:\LocoReaper\build\TS_Gold_Reaper_v4.1.mq4" /log:"C:\LocoReaper\build\gold-compile.log"
/compile:"C:\LocoReaper\build\Loco_Reaper_v1.mq4" /log:"C:\LocoReaper\build\loco-compile.log"
```

| Source | Error | Warning menurut ringkasan | EX4 (byte) | Waktu dalam log |
| --- | ---: | ---: | ---: | ---: |
| Gold | 0 | 264 | 261768 | 203 ms |
| Loco | 0 | 264 | 260776 | 205 ms |

Kedua proses compiler mengembalikan exit code 1; keberhasilan ditentukan dari ringkasan log yang eksplisit dan EX4 baru yang dihasilkan, bukan asumsi exit code 0. Log mentah dan EX4 tetap lokal di `build/`. Salinan teks log untuk Git hanya mengubah encoding menjadi UTF-8 dan mengganti prefix path lokal menjadi `build/`.

## Warning yang tersedia dan keterbatasan log

Masing-masing log hanya memuat **100 rincian warning**, walaupun ringkasannya menyebut 264. Karena itu, 164 warning lainnya tidak dapat dirinci dari log ini.

| Kode | Jumlah rincian per source | Makna |
| --- | ---: | --- |
| 43 | 42 | Potensi kehilangan data karena konversi tipe |
| 60 | 1 | Variabel lokal berpotensi dipakai sebelum diinisialisasi |
| 83 | 57 | Nilai balik OrderDelete/OrderClose/OrderModify perlu diperiksa |

Warning 60 berada pada baris 1159: `临_bo_1` di Gold dan `LR_Temp001_Bool_bo` di Loco. Setelah nama tersebut dinormalisasi dan kolom diabaikan, urutan, nomor baris, kode, dan pesan dari seluruh 100 warning yang tersedia cocok. Tidak diklaim bahwa 164 rincian yang tidak tercetak sudah dibandingkan.

**Belum dilakukan perbaikan warning atau perubahan logika. Backtest belum dijalankan.** Hasil compile ini perlu diperiksa sebelum menentukan pekerjaan berikutnya.

## Pemeriksaan file untuk Git

File yang disiapkan hanya source asli, paket audit, `.gitignore`, `.gitattributes`, README, dan laporan/log compiler teks. Pencarian pola kredensial pada source dan file audit tidak menemukan password, token, atau private key. Pemanggilan API AccountBalance/AccountInfo dan URL waktu publik merupakan kode program, bukan konfigurasi akun tersimpan. Tidak ada folder data terminal yang dimasukkan. Semua file asal berukuran kurang dari 1 MB.

Identitas author Git telah diberikan pengguna: `mermaidlinux <mermaidsuccess@gmail.com>`, untuk konfigurasi lokal repository ini. Status commit/push harus diperiksa melalui Git, bukan disimpulkan dari keberadaan laporan ini. Jika autentikasi diperlukan, gunakan login browser Git Credential Manager atau `gh auth login --web`; jangan menempelkan password/token ke chat atau menyimpannya dalam repository.
