# Rencana pembandingan baseline — belum dijalankan

Tujuan: memeriksa apakah Gold dan Loco dengan source sekarang menghasilkan urutan transaksi dan hasil identik dalam kondisi yang sama. Ini bukan optimasi strategi. Source tidak diperbaiki dulu agar baseline tetap dapat dibandingkan.

## Artefak dan lingkungan yang sudah pasti

- Terminal: instalasi `MT4-LocoReaper-Test` dan folder data yang diverifikasi dalam laporan lingkungan.
- Compiler yang digunakan: MetaEditor 5.0.0.2423, kedua source 0 error / 264 warning.
- Gold dan Loco: hash source dalam laporan lingkungan; EX4 lokal dalam `build/`, tidak diunggah ke Git.
- Kedua run dilakukan berurutan, satu EA per run. Tidak memasang EA ke chart aktif.
- Terminal lama dan semua MT5 berada di luar cakupan pekerjaan.

## Parameter yang belum ditetapkan

| Parameter | Status |
| --- | --- |
| Nama simbol tepat termasuk suffix broker | Belum dipilih; jangan mengasumsikan XAUUSD tanpa suffix |
| Broker/server sumber harga dan spesifikasi kontrak | Belum diperiksa |
| Timeframe chart | Belum dipilih |
| Rentang tanggal dan data pemanasan | Belum dipilih |
| Model tick, asal data, cakupan dan gap | Belum diperiksa |
| Spread tetap dalam points | Belum dipilih |
| Modal, mata uang deposit, leverage | Belum dipilih |
| File input identik | Belum dibuat; default source adalah kandidat baseline |
| Offset waktu dan DST untuk periode uji | Belum diverifikasi |

Jangan mengubah konfigurasi akun atau memakai data terminal lain untuk mengisi parameter ini secara diam-diam. Kedua run harus menggunakan data dan spesifikasi yang sama. Catat parameter efektif dari tester, bukan hanya nilai yang diinginkan.

## Default source yang perlu dipahami

`Randomization=0`, `AutoGMT=true`, offset winter=2/summer=3, `FridayStopHour=25`, `Risk=1234`, dan `UseWeightedLots=true`. Nilai ini dibaca dari source, bukan preset tester aktif. Default jam Jumat tidak mengaktifkan jalur penutupan Jumat pada jam 0–23. Default weighted lots tidak menjalankan cabang sizing non-weighted yang dibahas dalam audit warning. Offset default belum membuktikan kecocokan dengan broker/periode uji.

## Bukti yang harus disimpan sesudah run diizinkan

Simpan input efektif, hash data/input/EX4, laporan tester, journal, model/spread/spesifikasi simbol, serta waktu run. Laporan yang mungkin memuat identitas akun tetap lokal; hanya ringkasan yang sudah diperiksa boleh masuk Git. Data harga besar tidak masuk Git.

Bandingkan jumlah dan urutan transaksi, strategi/comment, arah, lot, waktu dan harga entry/exit, pending order, perubahan SL/TP, biaya, balance, equity, dan drawdown. Ticket boleh berbeda antar-run; cocokkan berdasarkan karakteristik transaksi, bukan nomor ticket saja. Laporan ringkas tester mungkin tidak mencatat semua perubahan order; tandai bukti yang tidak tersedia, jangan mengklaim kesamaan penuh berdasarkan net profit saja.

Jika ada selisih, cari kejadian pertama yang berbeda dan kondisi sebelumnya. Jangan melakukan optimasi atau perbaikan di tengah pasangan run. Simpan hasil sebagai bukti sebelum menentukan perubahan.

## Batas kelulusan

Run tidak dapat dibandingkan jika data, input, spread atau spesifikasi berbeda, ada gap material, atau salah satu run error. Kesamaan hasil dalam satu backtest hanya mendukung kesamaan dalam skenario itu. Jalur kegagalan OrderDelete/OrderClose/OrderModify memerlukan pengujian kegagalan terpisah; backtest normal tidak cukup untuk menutup temuan tersebut.
