# Review smoke test Gold — bukti diberikan pengguna

Status: Gold menghasilkan transaksi dan journal penyelesaian. Belum ada hasil Loco untuk dibandingkan; belum menguji target Januari–September 2026 penuh. Bukti berupa screenshot Report dan teks journal yang diberikan pengguna, bukan laporan HTML asli atau verifikasi EX4 yang terpasang.

## Pengaturan dan hasil

Pengaturan yang sebelumnya ditunjukkan pengguna: TS_Gold_Reaper_v4.1, XAUUSD tanpa suffix, H1, Every tick, 21–26 September 2026, spread tetap 168 points, deposit USD 2000. Journal mengonfirmasi simbol/H1, spread 168, input pada 21 September 00:00, aktivitas hingga 25 September, dan penyelesaian. Batas akhir tick persis tidak tercetak. Leverage efektif belum tersedia.

Screenshot Report: net profit 3.29 USD, gross profit 3.29, gross loss -0.00, 3 trades, semua short dan profit, tidak ada long terisi. Absolute drawdown 0.14 USD; maximal/relative drawdown 17.80 USD (0.88%). Modelling quality 90.00%, mismatched chart errors 0, ticks modelled 1237607. Angka bars pada screenshot terbaca 1113, tetapi journal menyebut 113 bars. Perlu laporan HTML untuk rekonsiliasi; jangan menyatakan screenshot/journal telah cocok seluruhnya.

Journal akhir: 1236607 tick events, 113 bars, 1237607 bar states; waktu proses 13:08.797, total 13:22.625. Tick events dan bar states adalah label berbeda, tidak disamakan. Modelling quality 90% bukan bukti data tick riil, akurasi 90% atau kelengkapan semua timeframe. Unduhan M1 terlihat sampai entri 18 September 14:33; tidak membuktikan kecukupan warm-up W1/D1 atau data Januari.

## Tiga posisi yang terisi

Semua waktu adalah waktu simulasi journal pada 23 September 2026; semua posisi sell 0.01 lot.

| Ticket | Waktu entry | Harga entry | SL setelah modifikasi 13:43:00 | TP | Waktu exit | Harga SL yang disebut tester |
| --- | --- | ---: | ---: | ---: | --- | ---: |
| 22 | 13:42:27 | 4294.063 | 4292.607 | 4279.501 | 13:44:38 | 4292.607 |
| 21 | 13:42:27 | 4293.863 | 4293.359 | 4269.500 | 14:09:04 | 4293.359 |
| 18 | 13:42:28 | 4293.273 | 4291.929 | 4278.151 | 13:44:36 | 4291.929 |

Ketiganya keluar melalui stop loss yang telah bergeser di bawah harga entry sell, konsisten dengan profit. Harga fill final, biaya dan profit tiap posisi harus dikonfirmasi dari Results/HTML. Journal memuat 40 pembuatan pending order, 21 penghapusan, 3 aktivasi menjadi posisi, dan 3 modifikasi. Ini bukan 40 closed trades. Pending order buy juga dibuat walaupun tidak ada posisi long terisi.

## Error GMT dan default input

Dua pesan `Error when reading GMT URL. Error code =4060` diikuti pesan fallback VPS dan `DST_US on`. [Dokumentasi WebRequest](https://docs.mql4.com/common/webrequest) menyatakan fungsi tidak tersedia dalam Strategy Tester. Menambahkan URL whitelist bukan solusi untuk pembatasan tester; jangan mengubah setting keamanan atau AutoGMT untuk pasangan baseline ini.

Pemeriksaan salinan source audit: baris 1272–1274 memilih Broker_GMT_OFFSET_Summer ketika DST_US aktif; pada 1370–1383 cabang MQL_TESTER menggunakan TimeCurrent dikurangi offset yang dipilih. Karena itu pesan fallback VPS saja tidak membuktikan waktu VPS aktual dipakai pada perhitungan tersebut. Nilai summer input journal adalah 3; kecocokan offset dengan histori broker belum diverifikasi.

Journal menunjukkan Risk=1234, UseWeightedLots=1, StartLots=0.01, Randomization=0 dan AutoGMT=1. Lot transaksi 0.01 bukan bukti pengguna memilih fixed lot. Parameter string tidak semuanya tercetak; file input default lengkap belum dibuktikan dengan ekspor. Baris awal load/remove EURCHF mendahului load XAUUSD dan bukan transaksi test XAUUSD.

## Berikutnya

Simpan report HTML Gold dan preset default sebelum mengganti EA. Jalankan Loco manual dengan periode/spread/deposit/input dan kondisi terminal yang sama; simpan Report, Results dan journal terpisah. Pertahankan history untuk kedua run. Bila data bertambah/berubah, ulang Gold dengan data yang sama agar pembandingan adil. Cocokkan seluruh event order berdasarkan waktu simulasi dan parameter, bukan jam eksekusi komputer atau profit akhir saja. Jika ada selisih, lakukan ulang baseline untuk menilai repeatability sebelum menyimpulkan beda strategi.

## Catatan workspace

Pada pemeriksaan ini Git menunjukkan `Loco_Reaper_v1.mq4` dan `TS_Gold_Reaper_v4.1.mq4` hilang dari folder utama (status D). Penyebab belum diketahui. Source audit masih tersedia dan versi asli tersimpan dalam Git. Penghapusan tidak dimasukkan ke commit review dan tidak dipulihkan secara diam-diam.
