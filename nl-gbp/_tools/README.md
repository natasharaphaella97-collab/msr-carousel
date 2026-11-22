# GBP Nail Lab (Google Maps) — autopilot

Tujuan: tiap hari ada 1 foto produk Nail Lab / Usagi Utopia di Google Business Profile, supaya orang yang cari nama produk (PARTY! gel polish, rubber base, soft gel tip, dll) nemu Nail Lab.

## Isi folder
- `brand.py` — `brand_tall(src, out, title, subtitle)`: header putih + logo Usagi Utopia kiri + nama produk kanan + garis pink, foto utuh di bawah. Font Poppins.
- `UsagiUtopia.jpg` — logo.
- `products.json` — daftar produk yang BENAR dijual (dari foto Nana). Cadangan Canva hanya boleh pakai produk dari sini.
- `log.json` — {"_last_notify": tanggal notif terakhir ke Nana, "entries": [...]} riwayat: tanggal, file, produk, sumber (inbox/canva/reuse). Dipakai supaya produk nggak diulang <14 hari.
- `../inbox/` — foto mentah dari Nana yang belum diproses. Kalau Nana kirim foto produk di chat, push mentahnya ke sini (nama file = nama produk kalau tahu, contoh `party-top-coat__raw.jpg`), dan tulis nama produknya di `../inbox/NOTES.md`.

## Aturan gambar
- Hapus: icon tag IG, badge nomor slide ("2/6"), logo toko/distributor lain (mis. Fanku Beauty). Nama merek di kemasan (PARTY!, Berry) tetap.
- Cadangan Canva: JANGAN gambar botol/kemasan/produk (Canva ngarang botol palsu). Cukup visual kuku/manicure/nail art + nama produk. Lalu tetap lewat `brand_tall` biar ada logo Usagi.
- Nama file SEO: `<produk>-<detail>-usagi-utopia-surabaya.jpg`, huruf kecil, pakai `-`.

## Aturan post (Metricool brand 7774098, timezone Asia/Bangkok)
- Per hari: `gmb` publication 10:00 WIB (teks) + `gmb` photo 10:05 WIB (gambar sama, teks kosong).
- Teks: tanpa @handle, tanpa nomor HP/WA, tanpa alamat. Tutup dengan "Tanya stok dan harga lewat tombol chat di profil ini." atau "mampir langsung ke studio". Jangan sebut harga. Sebut "Nail Lab Surabaya Barat (Usagi Utopia Nail Supplies)".
