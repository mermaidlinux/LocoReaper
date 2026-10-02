# Gold vs Loco: laporan smoke test cocok

## Kesimpulan

**PASS untuk kesamaan isi laporan HTML pada test pendek ini.** Kedua tabel HTML identik secara case-sensitive tanpa normalisasi angka, waktu, ticket, parameter, atau whitespace. Tidak ditemukan baris aktivitas yang berbeda. Ini belum bukti kesamaan pada periode penuh Januari–September 2026 atau semua kondisi pasar.

## Bukti dan metode

Laporan diberikan pengguna sesudah menjalankan tester manual. HTML mentah disimpan hanya di `build/` lokal yang diabaikan Git. Hash SHA-256:

- Gold: `7d06b7550de6727da1138aa706d0a1c6387e69f902938a6d0947d644a1e57099`
- Loco: `1263ddf67a3619b75ef410c6d572bbcc7e207e27ad6356b79a5a85e1247a9dba`

Pembandingan mengambil tepat dua blok `<table>...</table>` dari masing-masing HTML: tabel pengaturan/statistik dan tabel aktivitas order. Keduanya identik. Tabel aktivitas masing-masing berisi 70 baris data ditambah satu header. Seluruh HTML juga identik setelah hanya mengganti nama EA dengan placeholder bersama dan nama file gambar grafik dengan placeholder bersama. File gambar grafik sendiri belum dibandingkan.

## Pengaturan dan hasil identik

| Item | Gold dan Loco |
| --- | --- |
| Terminal/server dalam laporan | Build 1479 / Exness-Trial8 |
| Simbol/timeframe/model | XAUUSD / H1 / Every tick |
| Rentang permintaan | 21–26 September 2026 |
| Rentang yang dilaporkan | 21 September 00:00 – 25 September 20:00 |
| Input EA | Seluruh 57 parameter dalam laporan cocok |
| Deposit / spread | 2000 / 168 points |
| Bars in test / ticks modelled | 1113 / 1237607 |
| Modelling quality / mismatch errors | 90.00% / 0 |
| Closed trades | 3 sell, semua 0.01 lot, semua profit |
| Net profit / saldo akhir | 3.29 / 2003.29 |
| Maximum drawdown | 17.80 (0.88%) |

Urutan 70 aktivitas cocok termasuk nomor baris, waktu yang tercetak, jenis, ticket, lot, harga, SL, TP, profit dan balance. Terdiri dari 18 buy stop, 22 sell stop, 21 delete, 3 sell terisi, 3 modify, dan 3 s/l. Jadi kesamaan tidak disimpulkan hanya dari profit akhir.

## Batas kesimpulan dan pekerjaan berikutnya

- HTML mencatat waktu hanya sampai menit. Journal Loco belum diberikan, sehingga waktu hingga detik, error GMT dan pesan runtime belum dibandingkan.
- Leverage efektif tidak dicantumkan dalam kedua HTML. Kesamaan nilai leverage belum dibuktikan secara independen.
- Kesamaan jumlah tick/statistik tidak menggantikan hash file history atau verifikasi seluruh spesifikasi simbol dan state sebelum run.
- Kedua report sama-sama mencatat 1113 bars. Journal Gold sebelumnya mencatat 113 bars; penyebab perbedaan penghitung report/journal belum diverifikasi.
- Ini data Every tick hasil modelling, bukan bukti penggunaan tick riil. Kualitas 90% tidak membuktikan history Januari–September lengkap.
- Tidak ada perubahan source atau perbaikan warning dalam tahap ini. Dua penghapusan source di working tree tetap di luar commit dokumentasi.

Berikutnya: simpan dan bandingkan journal Loco, lalu jalankan Gold dan Loco pada target 1 Januari–30 September 2026 dengan kondisi identik. Verifikasi cakupan history dan leverage sebelum mengklaim target penuh telah diuji; gunakan rentang bersama terverifikasi jika history target tidak tersedia.

## Pembaruan: journal gabungan sudah dibandingkan

Pengguna memberikan journal gabungan dengan SHA-256 `d65c8af249068049fbf1413b62b023e9acd65a528b55b83d38c71709a16e5f08`. Salinan mentah hanya disimpan dalam build lokal, tidak diunggah. Temuan bagian ini menggantikan status journal Loco belum tersedia di atas.

Journal berisi tiga run: satu Gold selesai, satu Loco dihentikan lewat tombol Stop pada waktu simulasi 21 September 00:19:17 (3537 tick events), dan satu Loco berikutnya selesai. Run terhenti dipisahkan dan tidak digunakan sebagai pembanding hasil penuh. Tidak diasumsikan siapa yang menekan Stop.

Run dipisahkan mulai baris inputs sampai ringkasan tick events. Pada pasangan run selesai, jam eksekusi komputer di prefix journal dan nama EA dinormalisasi; waktu simulasi hingga detik, urutan, nilai dan isi pesan tidak diubah. Masing-masing memiliki **81 baris bertimestamp simulasi dan seluruhnya identik**, termasuk **70 aktivitas order**. Tidak ditemukan perbedaan pertama. Dua error GMT 4060, pesan fallback/DST dan pergantian hari juga cocok. Hasil normalisasi tidak mencakup baris unduhan history, load/remove EA atau durasi eksekusi komputer.

| Penghitung journal selesai | Gold | Loco |
| --- | ---: | ---: |
| Tick events | 1236607 | 1236607 |
| Bars | 113 | 113 |
| Bar states | 1237607 | 1237607 |
| Durasi proses | 13:08.797 | 15:10.297 |

Durasi eksekusi berbeda, tetapi semua timestamp simulasi dan aktivitas yang tercatat sama. Penyebab durasi berbeda tidak ditentukan dan bukan bukti perbedaan logika. Kedua journal sama-sama 113 bars, sementara kedua HTML sama-sama 1113; tidak ada perbedaan Gold vs Loco pada masing-masing jenis bukti, walaupun penyebab perbedaan penghitung antarjenis bukti belum diverifikasi.

Kesimpulan diperkuat: **PASS kesamaan hasil yang tercatat pada smoke test, hingga resolusi detik dalam journal**. Ini tidak membuktikan tidak adanya state tersimpan hanya karena hasil sama; leverage, hash data/spesifikasi, dan target periode penuh tetap belum diverifikasi. Tidak dilakukan perbaikan strategi.
