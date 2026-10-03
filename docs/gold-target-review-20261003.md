# Gold target run — review 3 Oktober 2026

Status: run Gold selesai, tetapi **periode Januari–September penuh belum terbukti teruji**. Belum ada pasangan Loco untuk run panjang ini. Bukti: screenshot Report dan dua journal harian yang diberikan pengguna. HTML run panjang belum diberikan.

Screenshot: deposit 2000, spread 168, net profit 859.97, gross profit 1168.64, gross loss -308.67, profit factor 3.79, 69 closed trades (47 short, 22 long), 55 menang dan 14 kalah; maximum drawdown 255.10 (11.59%). Modelling quality 68.55%, mismatched chart errors 0, report bars 1995 dan ticks modelled 24186258. Nilai tersebut bukan bukti profit masa depan atau kesamaan Gold/Loco.

## Periode dan data

Journal tanggal 2 berisi run-run smoke sebelumnya serta awal run panjang; journal tanggal 3 melanjutkan run panjang melewati tengah malam. Run panjang dipisahkan mulai baris inputs Gold terakhir. Baris inputs menyebut 2026.01.01 00:00:00, tetapi pesan runtime pertama dan pending order pertama baru pada **2026.06.05 05:00:00**. Aktivitas order terakhir yang tercatat pada **2026.09.29 16:00:00**. Timestamp tersebut bukan bukti timestamp tick terakhir; perlu field Period dari HTML dan pemeriksaan data sebelum menetapkan rentang efektif persis. Tidak ada bukti aktivitas runtime Januari–Mei dalam run ini.

Journal memuat unduhan M5 mundur hingga entri 2025.12.31 02:30; keberadaan unduhan M5 itu tidak membuktikan kelengkapan H1/M1 atau bahwa tester benar-benar memproses Januari. Unduhan M1 terakhir yang tercatat dalam rangkaian mundur adalah 2026.07.28 06:41. Ini indikasi keterbatasan cakupan timeframe kecil; bukan inventaris lengkap file history yang mungkin sudah ada. Kualitas modelling turun dari smoke 90% menjadi 68.55%. Penyebab spesifik dan cakupan tiap timeframe belum diverifikasi. Mismatched errors 0 tidak membuktikan data lengkap.

## Penyelesaian dan event

Ringkasan akhir: 24186158 tick events, 1894 bars, 24186258 bar states, proses 6:28:30.312, total 6:30:21.391. Tidak ada stop-button pada run panjang yang diekstrak. Log menyebut 383 pembuatan pending, 299 penghapusan, 225 modifikasi, 69 aktivasi posisi, 38 exit stop-loss, dan 31 exit take-profit. Jumlah exit cocok dengan 69 transaksi screenshot. Exit lewat SL tidak selalu rugi karena SL dapat bergeser ke area profit.

Dua error GMT 4060 pada awal aktivitas muncul seperti smoke; input AutoGMT tetap 1. Tidak ada perbaikan atau perubahan input yang dilakukan oleh asisten. Leverage efektif, batas tanggal setting akhir, snapshot data sebelum run, dan hash EX4 terpasang belum diverifikasi.

## Bukti lokal dan tindak lanjut

Snapshot mentah hanya di `build/target-review-20261003/`, diabaikan Git:

- `20261002.log`: SHA-256 `81aca0f88eefe80e7e9a8b2518667c3f360e6b8f3a7d1a0da0877aff6065b4adb`.
- `20261003.log`: SHA-256 `f9c94eb9b5e3c5ceea869cc427a2237ee4d41d8ee19f3acab006d24cf77f1ab3`.

Simpan dan periksa HTML Gold sebelum mengganti run, untuk mengetahui Period dan tabel event lengkap. Pertahankan akun, spesifikasi dan cache history untuk pasangan Loco. Jika data diperbaiki/ditambah, Gold dan Loco harus diuji ulang dengan data baru yang sama. Hasil pasangan dengan cache saat ini hanya boleh disebut pembandingan pada rentang/data yang benar-benar tersedia, bukan pengujian penuh Januari–September.
