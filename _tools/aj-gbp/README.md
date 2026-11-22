# Abadi Jaya GBP watermark
Template disetujui Nana 12 Nov 2026: logo bulat kiri + "Toko Listrik" putih kecil + "ABADI JAYA" kuning besar (Poppins Black, RGB 254,200,20), soft shadow, posisi atas/bawah otomatis (area lebih tenang). Tanpa tagline, tanpa alamat.
Pakai: copy brand_aj.py + logo_icon.png ke /home/claude/aj, download Poppins-Black.ttf ke /tmp/fonts/, lalu
  python3 -c "import sys;sys.path.insert(0,'/home/claude/aj');from brand_aj import brand;brand('in.jpg','out.jpg')"
Nama file: <isi-foto>-toko-listrik-abadi-jaya-surabaya.jpg. Foto ke aj-gbp/YYYY-MM/.
