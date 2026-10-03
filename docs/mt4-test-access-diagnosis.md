# Diagnosis akses MT4 test — 3 Oktober 2026

Pemeriksaan baca-saja. Tidak menjalankan MetaEditor/terminal, tidak menghentikan proses, tidak mengubah ACL/UAC/config/history atau logic EA. Filter proses dibatasi pada executable dalam instalasi test. Tidak membuka folder data terminal lama.

## Dua lapisan penolakan yang berbeda

1. Shell sandbox berjalan sebagai `MERMAID\CodexSandboxOffline`: executable terminal dan MetaEditor dapat dibuka read-only, tetapi origin.txt pada folder data ditolak Access denied. Dengan approval command, shell berjalan sebagai `MERMAID\Administrator` dan file yang sama berhasil dibaca. ACL folder data memberikan FullControl kepada SYSTEM, Administrators dan Administrator; tidak mencantumkan akun sandbox. Ini menjelaskan penolakan pembacaan file tanpa approval.
2. Percobaan computer-use terdahulu menolak path terminal yang benar dengan `product policy blocks this app`. Ini penolakan pada lapisan kebijakan tool, bukan pesan sharing violation atau file not found. Alasan internal pengelompokan aplikasi tidak tersedia. Tidak mencoba mengakali penolakan dengan rename executable, launcher lain, atau kontrol melalui shell.

[Dokumentasi resmi Computer Use](https://learn.chatgpt.com/docs/computer-use) membedakan app approval dari sandbox file/command dan menyebut pembatasan administrator. Pemeriksaan lokal config.toml tidak menemukan tabel computer_use atau feature computer_use yang dicetak oleh filter; requirements.toml pada folder pengguna tidak ada. Ini tidak membuktikan tidak adanya kebijakan tingkat produk atau managed policy di lokasi lain. Dokumentasi publik tidak menjelaskan pesan MT4 spesifik tersebut.

## Hasil pemeriksaan lingkungan

- Terminal yang aktif: `C:\Program Files (x86)\MT4-LocoReaper-Test\terminal.exe`, PID 8048.
- MetaEditor aktif: `C:\Program Files (x86)\MT4-LocoReaper-Test\metaeditor.exe`, PID 8556. Compile sebelumnya berhasil dengan executable ini.
- Folder data: `C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\499FDE4F0FA2ED8CA44CC0F1E1772F49`. origin.txt tepat menunjuk instalasi di atas.
- Shared-read executable, origin.txt, log tester, dan history berhasil setelah approval. Tidak ada exclusive lock yang menghalangi pembacaan yang diuji; kemampuan menulis/lock seluruh file tidak diuji.
- Tidak ditemukan flag kompatibilitas untuk dua executable pada registry Layers HKCU/HKLM yang diperiksa. Token elevasi proses/UIPI tidak diukur, sehingga tidak diklaim meniadakan seluruh kemungkinan UAC. Bukti penolakan GUI yang tersedia tetap product policy, bukan prompt UAC. Tidak perlu mengubah UAC atau menjalankan ulang aplikasi untuk membuktikan path.

## Mengapa run lama baru mencatat aktivitas Juni?

Run lama memiliki input tanggal 1 Januari, namun pesan runtime/order pertama baru 5 Juni 05:00; kualitas modelling 68.55% dan unduhan M1 mundur terakhir yang tercatat 28 Juli. Data/cache yang digunakan run tersebut merupakan dugaan utama, tetapi penyebab exact-start tidak dapat dibuktikan dari journal saja. Label tanggal input bukan bukti setiap tanggal diproses.

Pada pemeriksaan sekarang, file HST telah ditulis ulang sekitar 3 Oktober 09:42 menurut metadata host, sesudah run selesai sekitar 06:08 dalam journal; FXT sekitar 09:43. Header HST versi 401 dan panjang record konsisten (sisa byte 0). Rentang record pertama/terakhir kini:

| File | Bars | Pertama | Terakhir |
| --- | ---: | --- | --- |
| XAUUSD1.hst | 7037971 | 2004-06-11 05:18 | 2026-09-25 20:50 |
| XAUUSD5.hst | 1493204 | 2004-06-11 05:15 | 2026-09-25 20:50 |
| XAUUSD60.hst | 129364 | 2004-06-11 05:00 | 2026-09-25 20:00 |
| XAUUSD1440.hst | 6397 | 2004-06-11 00:00 | 2026-09-25 00:00 |
| XAUUSD10080.hst | 1162 | 2004-06-06 00:00 | 2026-09-20 00:00 |

Timestamp dari record disajikan sebagai label waktu history, bukan konversi ke waktu Bangkok. Pemeriksaan endpoint tidak membuktikan tidak ada gap internal. HST sekarang berawal jauh sebelum Januari tetapi berakhir 25 September; journal lama berisi aktivitas sampai 29 September. Karena itu data sekarang tidak boleh diasumsikan identik dengan data run lama. Tidak menuduh asal data tertentu atau siapa yang memperbaruinya. Tidak menyalin HST besar atau cache FXT 7.9 GB.

Kesimpulan: path benar, akses baca bisa melalui approval, kendala GUI masih penolakan kebijakan produk. Untuk pembandingan lanjutan, tetapkan snapshot data yang sama lalu jalankan ulang kedua EA jika history memang sudah diganti. Jangan membandingkan Gold lama dengan Loco baru memakai data berbeda, dan jangan mengklaim periode penuh sampai 30 September dari endpoint data saat ini.
