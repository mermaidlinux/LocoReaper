# Loco Reaper

Source dan paket audit yang dipertahankan tanpa perubahan logika trading.

- `TS_Gold_Reaper_v4.1.mq4`: source Gold Reaper yang diberikan pengguna; pembanding asli, tidak diedit.
- `Loco_Reaper_v1.mq4`: source Loco Reaper utama.
- `Loco_Reaper_v1_Audit/`: paket audit yang sudah diekstrak sebelum pemeriksaan; seluruh file asli dipertahankan.
- [Laporan lingkungan, perbandingan, dan compile](docs/environment-and-compile.md).
- [Audit warning dan prioritas temuan](docs/warning-review.md), dengan [inventaris 100 rincian warning yang tersedia](docs/warning-inventory.md).
- [Rencana pembandingan backtest, belum dijalankan](docs/backtest-plan.md).
- [Compile ulang dan hambatan akses tester pada percobaan pembandingan](docs/comparison-20261002/status.md).
- `docs/gold-compile.txt` dan `docs/loco-compile.txt`: hasil compiler dalam UTF-8, path workspace disingkat.

Hasil compile 2 Oktober 2026: kedua source menghasilkan EX4 dengan **0 error, 264 warning** menggunakan executable MetaEditor yang sama. Rincian log hanya memuat 100 warning per source. Belum ada perbaikan warning, pemasangan EA, atau backtest.

File source UTF-16 dipertahankan byte demi byte melalui `.gitattributes`. Output compiler, data pasar, konfigurasi terminal, dan kredensial dikecualikan melalui `.gitignore`. Jangan menjalankan `refactor_loco.py` langsung dalam folder audit: script tersebut menulis output dan memerlukan baseline dengan nama/path tertentu. Pemeriksaan kali ini tidak menjalankan script tersebut.
