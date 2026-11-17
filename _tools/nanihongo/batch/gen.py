import asyncio, json, os, sys
sys.path.insert(0, '/home/claude/nanihongo/p01')
from playwright.async_api import async_playwright

CSS = open('/home/claude/nanihongo/p01/render.py').read().split('CSS = """')[1].split('"""')[0]
CSS += """
.jp{white-space:nowrap}
.chips{display:flex;flex-wrap:wrap;gap:18px;margin-top:40px}
.chip{background:#1B2340;color:#F6F1E7;font-weight:800;font-size:44px;padding:16px 28px;border-radius:14px}
.cover .chip{background:#F6F1E7;color:#1B2340}
"""
R = "<span class='red'>{}</span>"
PINK = "<span style='color:#FF4D5E'>{}</span>"

def cover(tag, head, sub):
    return f"""<body class='cover'><div class='sun' style='width:560px;height:560px;right:-160px;top:-140px'></div>
<div class='pad' style='top:250px'><span class='tag'>{tag}</span><div class='h1'>{head}</div>
<div class='p' style='color:#cfd5e6'>{sub}</div></div></body>"""
def text(head, *ps, tag=None, dark=False, top=240):
    t = f"<span class='tag'>{tag}</span>" if tag else ""
    col = " style='color:#cfd5e6'" if dark else ""
    pp = "".join(f"<div class='p'{col}>{p}</div>" for p in ps)
    mt = "margin-top:40px" if tag else ""
    sun = "" if dark else "<div class='sun' style='width:300px;height:300px;right:-90px;bottom:-90px'></div>"
    return f"<body{' class=cover' if dark else ''}>{sun}<div class='pad' style='top:{top}px'>{t}<div class='h2' style='{mt}'>{head}</div>{pp}</div></body>"
def rows(tag, items, foot=None):
    r = "".join(f"<div class='row'><div class='l'>{a}{('<small>'+j+'</small>') if j else ''}</div><div class='r'>{b}</div></div>" for a, j, b in items)
    f = f"<div class='p' style='font-weight:800'>{foot}</div>" if foot else ""
    return f"<body><div class='pad' style='top:170px'><span class='tag'>{tag}</span><div style='margin-top:30px'>{r}</div>{f}</div></body>"
def big(tag, num, h, p):
    return f"<body><div class='pad' style='top:230px'><span class='tag'>{tag}</span><div class='big red' style='margin-top:50px'>{num}</div><div class='h2' style='margin-top:30px;font-size:72px'>{h}</div><div class='p'>{p}</div></div></body>"
def chips(tag, head, items, dark=False):
    c = "".join(f"<span class='chip'>{i}</span>" for i in items)
    return f"<body{' class=cover' if dark else ''}><div class='pad' style='top:200px'><span class='tag'>{tag}</span><div class='h2' style='margin-top:40px;font-size:80px'>{head}</div><div class='chips'>{c}</div></div></body>"
def cta(q, p="Tulis di komen."):
    return f"""<body class='cover'><div class='sun' style='width:420px;height:420px;right:-120px;bottom:-120px'></div>
<div class='pad' style='top:300px'><div class='h1' style='font-size:92px;margin-top:0'>{q}</div><div class='p' style='color:#cfd5e6'>{p}</div></div></body>"""

T = "KERJA DI JEPANG 2026"
POSTS = {
"02-ikusei-shuro": [
 cover(T, "Program magang Jepang " + PINK.format("dihapus") + " April 2027.", "Ini penggantinya."),
 text("Namanya " + R.format("Ikusei Shuro") + " <span class='jp'>育成就労</span>", "Gantiin program magang (<span class='jp'>技能実習</span>) yang jalan sejak 1993.", "Mulai berlaku 1 April 2027."),
 rows("YANG BERUBAH", [("Lama program", "", "maks. 3 thn"), ("Pindah perusahaan", "", "boleh*"), ("Bahasa Jepang awal", "", "±N5"), ("Jalur lanjut", "", "SSW 1 → 2")], "*dengan syarat tertentu"),
 text("Dulu maks. 5 tahun. Sekarang 3 tahun, lalu " + R.format("lanjut SSW."), "Jalurnya jelas: Ikusei Shuro → SSW 1 → SSW 2 → bisa sampai izin tinggal permanen."),
 text("Yang paling penting: kamu " + PINK.format("boleh pindah") + " perusahaan.", "Di sistem lama, pindah hampir nggak mungkin. Syarat lengkapnya di post berikutnya.", dark=True),
 cta("Kamu berangkat sebelum atau sesudah April 2027?"),
],
"03-pindah-perusahaan": [
 cover(T, "Mulai 2027 boleh " + PINK.format("pindah perusahaan") + " di Jepang.", "Tapi nggak bisa langsung."),
 text("Di sistem baru Ikusei Shuro, pindah atas kemauan sendiri boleh setelah kerja " + R.format("1–2 tahun") + " di tempat yang sama.", "Lamanya tergantung bidang kerjamu."),
 chips("TUNGGU 2 TAHUN", "8 bidang ini:", ["Perawat lansia", "Manufaktur", "Konstruksi", "Galangan kapal", "Bengkel mobil", "Pabrik makanan", "Restoran", "Daur ulang"]),
 chips("TUNGGU 1 TAHUN", "9 bidang ini:", ["Cleaning gedung", "Linen", "Hotel", "Kereta", "Gudang logistik", "Pertanian", "Perikanan", "Kehutanan", "Industri kayu"], dark=True),
 rows("SYARAT PINDAH", [("Bahasa Jepang", "", "±N4"), ("Tes skill dasar", "", "lulus"), ("Bidang kerja", "", "tetap sama")], "Perawat lansia: syarat bahasanya lebih tinggi."),
 cta("Bidang kerjamu masuk yang 1 tahun atau 2 tahun?"),
],
"04-umr-2026": [
 cover(T, "UMR Jepang naik lagi. Tokyo sekarang " + PINK.format("¥1.280/jam."), "Cek prefektur kamu."),
 text("Upah minimum Jepang dihitung " + R.format("per jam") + ", dan beda tiap prefektur.", "Naik tiap tahun. Tahun ini berlaku bertahap Oktober–Desember 2026."),
 big("RATA-RATA NASIONAL", "¥1.177", "per jam", "Naik ¥56 dari ¥1.121. Kenaikan terbesar ke-2 dalam sejarah."),
 rows("TERTINGGI", [("Tokyo", "東京都", "¥1.280"), ("Kanagawa", "神奈川県", "¥1.279"), ("Osaka", "大阪府", "¥1.231")], "Daerah Tohoku, Kyushu, Shikoku banyak yang masih di bawah ¥1.100."),
 text("¥1.177 × 8 jam × 21 hari ≈ " + PINK.format("¥198rb/bulan."), "Itu gaji kotor, sebelum dipotong pajak dan asuransi.", dark=True),
 cta("Kamu bakal ditempatkan di prefektur mana?"),
],
"05-ssw-restoran": [
 cover("SSW / TOKUTEI GINOU", "Mau SSW bidang restoran? Pendaftarannya " + PINK.format("lagi ditutup."), "Ini yang perlu kamu tahu."),
 text("Tiap bidang SSW punya " + R.format("kuota."), "Kalau kuotanya penuh, pendaftaran baru disetop."),
 big("RESTORAN 外食", "53.000", "kuota SSW 1 sudah penuh", "Pendaftaran baru ditutup sejak 13 April 2026."),
 text("Yang " + R.format("udah pegang") + " visa SSW restoran: aman.", "Perpanjangan untuk pemegang lama nggak terpengaruh."),
 chips("BIDANG BARU", "Dibuka, rekrut mulai ±2027:", ["Gudang logistik", "Linen", "Daur ulang"], dark=True),
 cta("Kamu lagi siapin SSW bidang apa?"),
],
"06-biaya-hidup": [
 cover(T, "Biaya hidup sebulan di Jepang, " + PINK.format("rinciannya begini."), "Biar bisa hitung sisa tabungan."),
 text("Yang paling nentuin cuma " + R.format("2 hal:"), "1. Kamu di kota besar atau daerah.", "2. Dapat asrama dari perusahaan atau nggak."),
 rows("PENGELUARAN / BULAN", [("Makan (masak sendiri)", "", "¥30–40rb"), ("Listrik, gas, air", "光熱費", "¥8–15rb"), ("Internet & SIM", "", "¥3–5rb"), ("Transport (asrama dekat)", "", "±¥0")]),
 rows("TOTAL BIAYA HIDUP", [("Daerah + asrama", "", "±¥60rb"), ("Tokyo / Osaka", "", "¥100–130rb")], "Belum termasuk potongan pajak & asuransi."),
 text("Selisihnya bisa " + PINK.format("±¥50rb/bulan."), "Setahun ±¥600rb ≈ Rp68 juta. Gaji kota besar belum tentu sisa lebih banyak.", dark=True),
 cta("Pilih gaji gede di kota, atau biaya hidup murah di daerah?"),
],
"07-potongan-asrama": [
 cover("HAK PEKERJA", "Gajimu dipotong buat asrama & makan? " + PINK.format("Cek dulu ini."), "Nggak semua potongan otomatis sah."),
 text("Potongan yang " + R.format("otomatis") + " cuma pajak dan asuransi sosial.", "Itu diatur undang-undang, semua pekerja kena."),
 text("Sewa asrama, listrik, makan, seragam " + R.format("baru sah") + " kalau ada perjanjian tertulis.", "Perjanjian antara perusahaan dan wakil pekerja: <span class='jp red'>労使協定</span>."),
 rows("YANG PERLU KAMU CEK", [("Potongannya ada di kontrak?", "", "✓"), ("Nominalnya jelas?", "", "✓"), ("Tertulis per item di slip?", "", "✓")]),
 text("Simpan kontrak dan " + PINK.format("slip gaji tiap bulan."), "Itu bukti paling kuat kalau nanti ada masalah.", dark=True),
 cta("Asramamu nanti dipotong berapa per bulan?"),
],
"08-hourensou": [
 cover("BUDAYA KERJA", "Kata pertama yang diajarin bos Jepang: " + PINK.format("<span class='jp'>報連相</span>"), "Hou-ren-sou."),
 text("Bunyinya mirip " + R.format("<span class='jp'>ほうれん草</span>") + " (bayam).", "Tapi artinya kebiasaan kerja paling dasar di Jepang."),
 rows("HOU-REN-SOU", [("Lapor hasil & progress", "報告 houkoku", "1"), ("Kabari info (telat, izin)", "連絡 renraku", "2"), ("Tanya sebelum ambil keputusan", "相談 soudan", "3")]),
 text("Telat 5 menit pun, kabari " + R.format("sebelum") + " jam masuk.", "Bukan pas udah sampai."),
 text("Salah kecil bisa dimaafin. Yang bikin masalah: " + PINK.format("nggak lapor."), dark=True),
 cta("Dari 3 ini, mana yang paling susah buat kamu?"),
],
}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        for name, slides in POSTS.items():
            d = f"/home/claude/nanihongo/batch/{name}"; os.makedirs(d, exist_ok=True)
            for i, body in enumerate(slides, 1):
                await pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head>{body}</html>")
                await pg.wait_for_timeout(150)
                await pg.screenshot(path=f"{d}/s{i}.png")
        await b.close()
asyncio.run(main())
