import asyncio
from playwright.async_api import async_playwright

W, H = 1080, 1350
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:'Inter','Noto Sans CJK JP',sans-serif;color:#1B2340;background:#F6F1E7;overflow:hidden;position:relative}
.pad{position:absolute;left:84px;right:150px;top:150px}
.tag{display:inline-block;background:#C8102E;color:#fff;font-weight:800;font-size:34px;padding:10px 22px;border-radius:8px;letter-spacing:1px}
.h1{font-weight:900;font-size:118px;line-height:1.02;letter-spacing:-2px;margin-top:40px}
.h2{font-weight:900;font-size:92px;line-height:1.06;letter-spacing:-1.5px}
.p{font-weight:500;font-size:50px;line-height:1.35;margin-top:36px}
.red{color:#C8102E}
.jp{font-family:'Noto Sans CJK JP';font-weight:900}
.sun{position:absolute;border-radius:50%;background:#C8102E}
.row{display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px solid #1B2340;padding:34px 0}
.row .l{font-size:48px;font-weight:700}
.row .l small{display:block;font-family:'Noto Sans CJK JP';font-size:34px;font-weight:700;color:#C8102E;margin-top:6px}
.row .r{font-size:58px;font-weight:900}
.big{font-weight:900;font-size:200px;letter-spacing:-4px;line-height:1}
.box{background:#1B2340;color:#F6F1E7;border-radius:24px;padding:44px 48px;margin-top:44px}
.cover{background:#1B2340;color:#F6F1E7}
"""

slides = {
1: """<body class='cover'>
<div class='sun' style='width:560px;height:560px;right:-160px;top:-140px;opacity:.95'></div>
<div class='pad' style='top:250px'>
<span class='tag'>KERJA DI JEPANG 2026</span>
<div class='h1'>Gaji <span style='color:#FF4D5E'>¥200.000</span>.<br>Yang masuk rekening berapa?</div>
<div class='p' style='color:#cfd5e6'>Hitungan realistis, bukan angka brosur.</div>
</div></body>""",
2: """<body>
<div class='sun' style='width:300px;height:300px;right:-90px;bottom:-90px'></div>
<div class='pad' style='top:260px'>
<div class='h2'>Angka di brosur itu <span class='red'>gaji kotor.</span></div>
<div class='p'>Sebelum masuk rekening, slip gaji di Jepang dipotong dulu: asuransi, pensiun, dan pajak.</div>
<div class='p'>Jadi berapa yang beneran kamu terima?</div>
</div></body>""",
3: """<body>
<div class='pad' style='top:150px'>
<span class='tag'>POTONGAN WAJIB / BULAN</span>
<div style='margin-top:30px'>
<div class='row'><div class='l'>Asuransi kesehatan<small>健康保険</small></div><div class='r'>±¥10.000</div></div>
<div class='row'><div class='l'>Pensiun<small>厚生年金</small></div><div class='r'>±¥18.300</div></div>
<div class='row'><div class='l'>Asuransi kerja<small>雇用保険</small></div><div class='r'>±¥1.000</div></div>
<div class='row'><div class='l'>Pajak penghasilan<small>所得税</small></div><div class='r'>±¥4.000</div></div>
</div>
<div class='p' style='font-weight:800'>Total ±¥33.000 hilang tiap bulan.</div>
</div></body>""",
4: """<body>
<div class='pad' style='top:230px'>
<span class='tag'>TAHUN PERTAMA</span>
<div class='p' style='margin-top:40px'>Yang masuk rekening:</div>
<div class='big red' style='margin-top:20px'>±¥166rb</div>
<div class='h2' style='margin-top:30px'>≈ Rp19 juta</div>
<div class='p'>Belum dipotong sewa, makan, dan transport.</div>
</div></body>""",
5: """<body class='cover'>
<div class='pad' style='top:200px'>
<span class='tag'>JEBAKAN TAHUN KE-2</span>
<div class='h2' style='margin-top:40px'>Mulai Juni tahun ke-2, gajimu <span style='color:#FF4D5E'>turun lagi.</span></div>
<div class='p' style='color:#cfd5e6'>Ada pajak penduduk <span class='jp' style='color:#fff'>住民税</span> (juminzei), dihitung dari gaji tahun pertama.</div>
<div class='p' style='color:#cfd5e6'>±¥8.000/bulan → sisa <b style='color:#fff'>±¥158rb</b>.</div>
</div></body>""",
6: """<body>
<div class='pad' style='top:220px'>
<span class='tag'>KABAR BAIKNYA</span>
<div class='h2' style='margin-top:40px'>Iuran pensiun bisa diklaim balik <span class='red'>sebagian</span> waktu pulang.</div>
<div class='p'>Namanya <span class='jp red'>脱退一時金</span> (dattai ichijikin). Ajukan setelah keluar dari Jepang.</div>
</div></body>""",
7: """<body class='cover'>
<div class='sun' style='width:420px;height:420px;right:-120px;bottom:-120px'></div>
<div class='pad' style='top:300px'>
<div class='h1' style='font-size:92px;margin-top:0'>Gaji yang dijanjikan ke kamu berapa?</div>
<div class='p' style='color:#cfd5e6'>Tulis di komen + bidang kerjanya.</div>
</div></body>""",
}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': W, 'height': H})
        for i, body in slides.items():
            await pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head>{body}</html>")
            await pg.wait_for_timeout(200)
            await pg.screenshot(path=f"/home/claude/nanihongo/p01/s{i}.png")
        await b.close()

asyncio.run(main())
