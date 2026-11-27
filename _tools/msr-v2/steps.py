"""MSR: 1 chat AI, posting ke semua sosmed (via Metricool). Output out/t02-1chat9sosmed"""
import asyncio, os
import gen, team
from team import CSS, hd, panel, role
from playwright.async_api import async_playwright
N = 9
EXTRA = """
.chipp{display:flex;align-items:center;gap:16px;background:#fff;border:2px solid #EEE;border-radius:24px;padding:30px 24px;font-size:36px;font-weight:800;box-shadow:0 8px 20px rgba(0,0,0,.05)}
.chipp i{font-style:normal;font-family:'Noto Color Emoji';font-size:38px}
.row{display:flex;align-items:center;justify-content:space-between;padding:16px 0;border-bottom:2px solid #26272D;font-size:32px}
.row:last-child{border-bottom:0}
.ok{color:#7CE38B;font-weight:800;font-size:28px}
.me2{background:#26272D;border-radius:20px;padding:18px 22px;margin-left:120px;font-size:32px;line-height:1.35}
.ai2{background:#FBF7F2;color:#141414;border-radius:20px;padding:18px 22px;margin-top:18px;font-size:32px;line-height:1.45}
.ai2 b{color:#D9481F}
.th{background:#fff;border-radius:12px;height:150px;position:relative}
.th:before{content:'';position:absolute;left:12px;right:12px;top:16px;height:16px;border-radius:5px;background:#141414}
.th:after{content:'';position:absolute;left:12px;width:55%;top:42px;height:16px;border-radius:5px;background:#F2552C}
"""
PL = [('📸', 'Instagram'), ('🎵', 'TikTok'), ('👍', 'Facebook'), ('🧵', 'Threads'), ('▶️', 'YouTube'), ('💼', 'LinkedIn'), ('📌', 'Pinterest'), ('📍', 'Google Maps'), ('🦋', 'Bluesky')]
S = []
# 1 cover
S.append(f"""<div class=rings></div>
<div style="position:absolute;left:0;right:0;top:80px;text-align:center"><span style="background:#F3F3F3;border-radius:12px;padding:8px 22px;font-size:30px;font-weight:700;color:#555">Cuan pakai AI</span></div>
<h1 data-fit style="top:160px;font-size:124px;left:70px;right:70px"><span class=l>1 chat AI,</span><span class="l r">posting ke 9 sosmed.</span></h1>
<div style="position:absolute;left:0;right:0;top:470px;display:flex;justify-content:center"><div class=tile style="width:180px;height:180px"><span class=tl style="font-size:84px">AI</span></div></div>
<div style="position:absolute;left:538px;top:650px;width:4px;height:50px;background:#F2793A"></div>
<div style="position:absolute;left:60px;right:60px;top:700px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px">""" + ''.join(f'<div class=chipp><i>{e}</i>{t}</div>' for e, t in PL) + """</div>
<div class=note style="top:1180px;color:#C2410C;font-weight:700;font-size:40px">Geser, ini caranya →</div>""")
# 2
S.append(role(2, N, 'LANGKAH 1', 'Sambungin akunmu', 'sekali aja.',
    'Login ke tiap sosmed lewat aplikasi penjadwal kayak Metricool. Cukup sekali.',
    panel('AKUN TERSAMBUNG', ''.join(f'<div class=row><span>{e} {t}</span><span class=ok>✓ Tersambung</span></div>' for e, t in PL[:5]))))
# 3
S.append(role(3, N, 'LANGKAH 2', 'Sambungin Metricool', 'ke AI.',
    'Tambahkan konektor Metricool di Claude, login, lalu izinkan aksesnya. Sekali saja.',
    panel('KONEKTOR', '<div style="font-size:28px;color:#9A9AA3;margin-bottom:10px">Nama konektor</div><div style="background:#26272D;border-radius:16px;padding:18px 22px;font-size:36px;font-weight:800">Metricool</div><div style="background:#FBF7F2;color:#7A2A1E;border-radius:16px;padding:16px 22px;font-size:30px;margin-top:22px">Login Metricool &amp; izinkan sekali.</div><div style="display:flex;justify-content:flex-end;margin-top:24px"><span style="background:#F2552C;color:#fff;border-radius:16px;padding:16px 40px;font-size:34px;font-weight:800">Hubungkan</span></div>')))
# 4
S.append(role(4, N, 'LANGKAH 3', 'Tanya AI,', 'akun apa aja?',
    'Pakai bahasa biasa. AI sebutin akun yang bisa dia posting.',
    panel('CHAT', '<div class=me2>Akun sosmed mana aja yang bisa kamu posting?</div><div class=ai2>Lewat Metricool aku bisa posting ke:<br><b>✓</b> Instagram @tokomu<br><b>✓</b> TikTok @tokomu<br><b>✓</b> Facebook Toko Kamu<br><b>✓</b> Threads @tokomu</div>')))
# 5 (orange)
S.append(role(5, N, 'LANGKAH 4', 'Bikin carousel-nya', 'di chat yang sama.',
    'Kasih catatan atau idemu. AI bikin slide-nya, kamu cek dulu.',
    panel('CHAT', '<div class=me2>Jadiin catatan ini carousel 7 slide, ukuran TikTok.</div><div class=ai2>Siap, ini 7 slide-nya:</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px">' + '<div class=th></div>' * 7 + '</div>')))
# 6
S.append(role(6, N, 'LANGKAH 5', 'Caption beda', 'tiap sosmed.',
    'Minta AI tulis caption yang cocok buat masing-masing platform.',
    panel('RENCANA POSTING', ''.join(f'<div class=it><small>{p} · BESOK 19.00</small>{c}</div>' for p, c in [('TIKTOK', 'Capek upload satu-satu? Ini caranya 👇'), ('INSTAGRAM', 'Simpan dulu, praktekin malam ini.'), ('THREADS', 'jujur, upload 5 kali itu buang waktu')]))))
# 7
S.append(role(7, N, 'LANGKAH 6', 'Masuk antrian,', 'kamu tinggal cek.',
    'Semua terjadwal di Metricool. Mau ganti jam atau caption, tinggal bilang.',
    panel('ANTRIAN', ''.join(f'<div class=row><span>{e} {t}</span><span class=ok>{s}</span></div>' for e, t, s in [('🎵', 'TikTok · carousel', 'Terjadwal'), ('📸', 'Instagram · carousel', 'Terjadwal'), ('👍', 'Facebook · post', 'Terjadwal'), ('🧵', 'Threads · teks', 'Terjadwal')]))))
# 8
S.append(hd(8, N) + """<div class=tag>YANG BERUBAH</div><h2 data-fit style="font-size:108px"><span class=l>Dulu vs</span><span class="l r">sekarang.</span></h2>
<div class=stk style="top:560px;gap:24px">
<div class=card style="padding:34px 40px;background:#F3F1EE;border-color:#F3F1EE"><div style="font-weight:800;letter-spacing:.12em;color:#999;font-size:30px;margin-bottom:12px">DULU</div><div style="font-size:38px;line-height:1.6;color:#666">Download slide<br>Buka 5 aplikasi, upload 5 kali<br>Tulis caption satu-satu<br>Atur jadwal 5 kali</div></div>
<div class=card style="padding:34px 40px;background:#FFF1EA;border-color:#FFD9C7"><div style="font-weight:800;letter-spacing:.12em;color:#C2410C;font-size:30px;margin-bottom:12px">SEKARANG</div><div style="font-size:40px;line-height:1.6;color:#D9481F;font-weight:800">1 chat ke AI<br>Caption beda tiap sosmed<br>Kamu cek, beres</div></div></div>""")
# 9
S.append(hd(9, N) + """<div class=kick>GILIRANMU</div><h1 data-fit style="top:290px;font-size:118px"><span class=l>Bikin sekali,</span><span class="l r">posting di mana-mana.</span></h1>
<div class=stk style="top:600px;gap:22px">
<div class=card style="padding:34px 40px;font-size:44px;font-weight:800;text-align:center;line-height:1.35">Selama ini kamu upload<br>ke berapa sosmed? 🤔</div>
<div style="display:flex;gap:20px;justify-content:center">""" + ''.join(f'<div class=card style="padding:22px 40px;font-size:42px;font-weight:900">{x}</div>' for x in ['1', '2–3', '4+']) + """</div>
<div class=note style="margin-top:20px;color:#333;font-weight:700;font-size:38px">Kirim ke temen yang upload satu-satu 📲</div></div>""")

async def main(slug='t02-1chat9sosmed'):
    os.makedirs(f'{gen.HERE}/out/{slug}', exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1440})
        for i, h in enumerate(S, 1):
            cls = 'or' if i == 5 else ''
            await pg.set_content(f'<html><head><meta charset=utf-8><style>{CSS}{EXTRA}</style></head><body class="{cls}">{h}</body></html>')
            await pg.evaluate(gen.FIT); await pg.wait_for_timeout(250)
            await pg.screenshot(path=f'{gen.HERE}/out/{slug}/slide-{i}.png')
        await b.close()
asyncio.run(main())
