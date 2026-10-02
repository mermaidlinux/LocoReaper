# Audit warning tanpa perubahan source

Pemeriksaan statis lanjutan, 2 Oktober 2026, terhadap source pada commit `815024d`. Tidak ada source yang diedit, EA dijalankan, atau backtest dilakukan. Temuan berikut juga berlaku pada Gold pembanding, sesuai pembalikan rename/branding yang telah diverifikasi.

## Cakupan dan kesimpulan

Kedua hasil compile menyebut 0 error dan 264 warning, tetapi masing-masing log hanya menyediakan 100 rincian. Seluruh 100 rincian yang tersedia dipetakan dalam [inventaris warning](warning-inventory.md). Audit ini tidak mengklaim telah menelaah 164 warning yang tidak tercetak, seluruh strategi, atau perilaku runtime. Menghilangkan warning hanya dengan cast atau mengabaikan return value tidak membuktikan bahwa masalah sudah selesai.

Prioritas tertinggi dari rincian yang tersedia adalah penanganan operasi order gagal dan satuan slippage. Warning variabel belum diinisialisasi memang benar, tetapi dampaknya lebih terbatas daripada yang mungkin disimpulkan dari pesan compiler saja.

## 1. Catatan internal dihapus tanpa konfirmasi OrderDelete — prioritas tinggi

Pada Loco baris 2750 dan 2783, `OrderDelete` dipanggil untuk membatasi jumlah pending order. Baris 2751–2757 dan 2784–2790 kemudian mengosongkan slot `LR_Global198_Double_do_Array`, tanpa percabangan berdasarkan hasil penghapusan. Pemicu masalah: penghapusan ditolak/gagal sementara ticket masih ditemukan dalam array. Akibat potensial: pending order masih ada di server, tetapi catatan internal ticket/harga dihapus dan pesan penghapusan tetap dicetak.

Ini merupakan inferensi langsung dari alur source, bukan insiden runtime yang sudah diamati. Perbaikan yang kelak perlu ditinjau adalah pembaruan state hanya setelah keberhasilan dikonfirmasi, dengan kebijakan error/retry yang eksplisit. Itu mengubah perilaku saat gagal dan belum diterapkan.

## 2. Penutupan Jumat dianggap selesai walaupun operasi gagal — prioritas tinggi, bersyarat

Blok baris 2611 mensyaratkan Jumat, `Hour() >= FridayStopHour`, dan flag `LR_Global305_Bool_bo` belum aktif. Operasi pada 2691/2695/2698 tidak memeriksa hasil. Baris 2702 tetap mengaktifkan flag, sehingga blok yang sama tidak mencoba lagi selama flag tetap aktif; reset non-Jumat terlihat pada 2705–2707.

Jika penutupan/penghapusan gagal, order dapat tersisa walaupun jalur ini sudah ditandai selesai. Ini tidak membuktikan bahwa jalur pengelolaan lain tidak mungkin menutupnya. Default `FridayStopHour=25` di baris 51 membuat kondisi jam tersebut tidak tercapai dalam jam normal 0–23; skenario perlu input jam Jumat yang valid untuk mengaktifkan jalur. Jangan menganggap temuan ini terpicu dengan default tersebut.

## 3. Satuan slippage dan status setelah OrderClose — prioritas tinggi untuk ditinjau

`LR_CurrentSpreadPrice` dihitung sebagai Ask minus Bid (antara lain baris 932, 1869, 2715), yaitu selisih harga. Pada baris 4328 nilai itu langsung menjadi argumen slippage `OrderClose`, yang menurut API adalah integer dalam points. Konversi ke integer juga membuang pecahan. Contoh ilustratif, bukan data broker aktual: selisih harga 0.25 dengan point 0.01 setara 25 points, tetapi cast integer dari 0.25 menghasilkan 0.

Baris 4329 langsung `return(true)` tanpa memeriksa hasil `OrderClose`; nilai true di sini tidak dapat dipakai sebagai bukti order sudah ditutup. Arti keseluruhan return fungsi dan dampak ke caller masih memerlukan penelusuran tambahan sebelum merancang perbaikan.

Enam warning slippage lain (2691, 2695, 4378, 4381, 4420, 4423) memakai `LR_Global038_Double_do`, yang dideklarasikan bernilai 5000.0 pada baris 134. Nilai integer 5000 sendiri tidak kehilangan pecahan pada konversi; satuan dan toleransi yang dimaksud tetap harus ditinjau. Jangan otomatis menyamakan seluruh warning 43 dengan kerusakan numerik aktual.

## 4. Variabel lokal belum diinisialisasi — cacat terkonfirmasi, dampak trading belum ditemukan

Dalam `init()` (501–1181), `LR_Temp001_Bool_bo` dideklarasikan pada 512 dan dibaca pada 1159 tanpa assignment sebelumnya. `IsDemo()` pada 1157 dipanggil tanpa menyimpan hasilnya. Nama lokal sama di fungsi lain tidak menginisialisasi variabel dalam scope ini.

Cabang hanya mengatur `LR_Global312_Bool_bo=true` setelah flag diset false pada 1156. Pencarian seluruh source menemukan flag itu hanya pada deklarasi 408 dan dua assignment 1156/1161; tidak ditemukan pembacaan. Karena itu belum ada bukti bahwa warning ini memengaruhi keputusan order pada source sekarang. Menulis `LR_Temp001_Bool_bo=IsDemo()` mungkin terlihat masuk akal, tetapi maksud penulis belum terbukti; tidak diterapkan sebagai perbaikan otomatis.

## 5. Klasifikasi seluruh 42 rincian warning konversi

| Kelompok | Jumlah | Baris Loco | Penilaian statis |
| --- | ---: | --- | --- |
| Digit simbol double ke int | 3 | 922, 1155, 1868 | Nilai digit normal bersifat bulat; warning tipe bukan bukti presisi hilang pada nilai normal. |
| Waktu ke double | 1 | 931 | Perlu mempertahankan semantik waktu; tidak ditemukan bukti kehilangan presisi timestamp normal dari baris ini saja. |
| Rasio freeze level ke int | 1 | 994 | Pemotongan pecahan dapat menghasilkan nilai di bawah rasio pembanding. Validasi terhadap spesifikasi simbol diperlukan. |
| Durasi dikali 60 ke int | 1 | 1069 | Pecahan detik dapat terpotong; jangan mengganti pembulatan tanpa spesifikasi. |
| Slippage double ke int | 7 | 2691, 2695, 4328, 4378, 4381, 4420, 4423 | Lihat temuan satuan slippage di atas. |
| Ticket long ke parameter int | 12 | 2750, 2783, 4222, 4227, 4235, 4240, 4244, 4249, 4254, 4259, 4264, 4323 | Nilai yang ditelusuri berasal dari ticket MT4; widening lalu narrowing tidak otomatis berarti overflow aktual. |
| Ticket double ke long | 1 | 2866 | Perlu invariant array: ticket integer, tidak rusak/bercampur nilai pecahan. |
| Ticket long ke array double | 7 | 2940, 2962, 2984, 3006, 3885, 4111, 4290 | Penyimpanan ticket melalui beberapa tipe menyulitkan audit; belum ada bukti ticket aktual kehilangan presisi. |
| Penyebut sizing ke int | 5 | 3249, 3253, 3257, 3261, 3265 | Pemotongan memengaruhi penyebut lot pada 3269/3273. Cabang Risk=1234 dan UseWeightedLots=false; default UseWeightedLots=true. Input MaxAllowedDD=0 akan menjadi pembagi nol jika jalur tercapai; tidak terlihat guard dalam blok ini. |
| Limit order long ke int | 2 | 3826, 4052 | Bergantung rentang nilai limit broker; belum ada overflow yang diamati. |
| Slippage dalam blok tidak terjangkau | 2 | 3863, 4089 | Berada di bawah `if(1==0)` pada 3856/4082; tidak mengeksekusi konversi pada source sekarang. |

## 6. Seluruh 57 rincian return value yang diabaikan

Log yang tersedia memuat 36 OrderDelete, 16 OrderClose, dan 5 OrderModify. Inventaris mencatat seluruh lokasinya. Risiko umumnya adalah kegagalan tidak ditangani di titik pemanggilan; konsekuensi tidak boleh disamaratakan karena state setelah setiap panggilan berbeda. Contoh dengan alur konkret telah ditelusuri di bagian 1–3.

Pada 4222/4227/4235/4240/4323, nilai SL/TP lokal diubah sebelum OrderModify yang hasilnya tidak diperiksa. Jika server menolak, nilai lokal yang dipakai selanjutnya dapat berbeda dari order server. Konfirmasi ulang state dan kebijakan menangani error perlu ditentukan sebelum perbaikan.

## Keputusan tahap ini

Pertahankan kedua source dan EX4 baseline. Jangan memperbaiki salah satu sebelum pembandingan baseline, karena perubahan penanganan gagal, pembulatan, atau satuan akan mengubah eksperimen. Backtest pembanding belum dijalankan dan tidak membuktikan ketahanan terhadap semua kegagalan server; pengujian kegagalan terpisah diperlukan untuk temuan di atas.

Untuk 164 warning yang belum tersedia, langkah selanjutnya adalah mencari keluaran diagnostik tambahan dari compiler/editor yang sama. Tidak digunakan trik mengubah source atau menonaktifkan warning demi membuka sisa daftar pada audit ini.

## Referensi primer

- [Inisialisasi variabel MQL4](https://docs.mql4.com/basis/variables/initialization): variabel lokal tanpa inisialisasi tidak memiliki nilai awal yang dapat diandalkan.
- [OrderClose](https://docs.mql4.com/trading/orderclose): ticket/slippage bertipe int, slippage dalam points, hasil boolean.
- [OrderDelete](https://docs.mql4.com/trading/orderdelete): keberhasilan dilaporkan melalui boolean.
- [Konversi tipe MQL4](https://docs.mql4.com/basis/types/casting): konversi pecahan ke integer membuang pecahan; konversi rentang tipe dapat kehilangan data.
