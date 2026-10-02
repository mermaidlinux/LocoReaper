# Percobaan pembandingan 2 Oktober 2026 — terhambat akses MT4

Pengguna telah mengizinkan backtest dan menggantikan larangan sebelumnya. Status saat ini: **compile selesai; smoke test dan backtest belum berjalan; kesamaan hasil trading belum terbukti**.

## Pengaturan yang diminta

H1, target 1 Januari–30 September 2026, deposit USD 2.000, Every tick, default source, optimization OFF dan visual OFF. Simbol harus Gold/USD yang benar-benar tersedia di Exness pengujian. Spread tetap harus diambil saat persiapan dan dicatat dalam points. Leverage harus dicatat dari tester dan disamakan. Nama simbol/suffix, spread, leverage efektif dan data untuk periode bersama belum dapat diverifikasi; tidak ada nilai rekaan yang digunakan.

## Compile ulang selesai

MetaEditor: `C:\Program Files (x86)\MT4-LocoReaper-Test\metaeditor.exe`, file version `5.0.0.2423`. Source disalin tanpa perubahan ke folder lokal `build/comparison-20261002/` dan dikompilasi berurutan. Hasil baru:

| Source | Errors | Warnings | Durasi log | EX4 bytes |
| --- | ---: | ---: | ---: | ---: |
| TS_Gold_Reaper_v4.1 | 0 | 264 | 185 ms | 261056 |
| Loco_Reaper_v1 | 0 | 264 | 200 ms | 261456 |

SHA-256 source Gold: `33ba69c2f12e1d320a7e583d330443c6b56b5ae25f4ee33a450db57cb5e1fc54`.

SHA-256 source Loco: `32d8e3a57ce0ead9cadfac014d3eb90fbf3ed565f9b151fdbeff9644d7c5000e`.

Hash semua artefak lokal ada dalam `artifact-hashes.json`. Log yang disimpan di sini diubah menjadi UTF-8 dan prefix path workspace disingkat; hash `.log` dalam manifest merujuk log mentah lokal, bukan salinan teks ini. EX4 hasil compile ulang berbeda ukuran dari compile sebelumnya; tidak ada klaim binary reproducibility. Bukti kesamaan yang dituju tetap hasil tester, bukan kesamaan byte EX4.

## Bukti hambatan akses

Snapshot proses memverifikasi terminal pengujian masih berjalan dari path yang benar, PID 5260. `origin.txt` tetap menunjuk instalasi pengujian dan data folder `499FDE4F0FA2ED8CA44CC0F1E1772F49`. Tool computer-use `list_apps` dan `list_windows` tidak mengembalikan jendela MT4 pengujian. Percobaan menampilkan aplikasi melalui API resmi:

```text
sky.launch_app({app: 'C:\Program Files (x86)\MT4-LocoReaper-Test\terminal.exe'})
=> product policy blocks this app: C:\Program Files (x86)\MT4-LocoReaper-Test\terminal.exe
```

Ini penolakan kebijakan produk pada tool kontrol aplikasi, bukan compile error atau bukti kegagalan login broker. Tidak dicoba jalur kontrol alternatif untuk melewati penolakan tersebut. Tidak ada klik tester, pemasangan EA ke chart, penghentian terminal, atau perubahan akun/config. Terminal lain tidak disentuh.

## History dan kebutuhan source

Inventaris baca-saja folder data pengujian menemukan folder server `Exness-Trial8`. Isinya mencakup `symbols.raw`, `symbols.sel`, `symgroups.raw`, serta HST H4 untuk EURUSD, GBPUSD, USDCHF, USDJPY. Pencarian seluruh history tidak menemukan HST Gold/XAU; direktori `tester/history` tidak berisi file. Karena itu belum ada rentang Gold bersama yang bisa dinyatakan siap, termasuk rentang pendek. Ini menggambarkan cache lokal saat pemeriksaan, bukan pernyataan bahwa broker tidak menyediakan history Gold.

Source memanggil M1, M5, H1, D1, W1 secara eksplisit, dan loader strategi mengatur timeframe numerik termasuk M15 dan H4. Ada konfigurasi M30 untuk aturan candle; kebutuhan nyata bergantung cabang default yang aktif. Persiapan harus menyediakan data intraday dan timeframe pendukung, bukan hanya chart H1. Rentang dan warm-up belum terverifikasi karena tidak ada history Gold lokal.

Pencarian source tidak menemukan API GlobalVariable*, FileOpen/Read/Write/Delete/Seek/Close, iCustom, atau MathSrand. Namun terdapat MathRand, TimeGMT/TimeLocal, dan WebRequest; tidak disimpulkan bahwa seluruh state lingkungan sudah terkendali. Dua test harus dimulai dengan kondisi terminal/tester yang sama dan input default identik. Randomization=0 tidak cukup untuk menyatakan semua penggunaan MathRand hilang, karena ada panggilan lain pada baris 2809.

## Langkah yang masih diperlukan

Akses kontrol MT4 melalui jalur yang diizinkan produk perlu tersedia, atau pengguna menjalankan bagian tester secara manual dan menyediakan hasilnya. Setelah itu: deteksi simbol, ambil spread, verifikasi leverage/history, smoke test, lalu pasangan backtest berurutan dengan state awal sama. Jika target penuh tidak tersedia, gunakan rentang Gold bersama yang terverifikasi dan laporkan batasnya. Nol transaksi tidak cukup menjadi bukti kesamaan. Belum ada transaksi atau modifikasi order yang dapat dibandingkan pada percobaan ini.
