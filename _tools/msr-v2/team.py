"""MSR format 'Tim AI' (ala jayantcreates) dalam gaya MSR v2. Output out/<slug>/slide-N.png"""
import asyncio, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
from playwright.async_api import async_playwright
IS='/home/claude/work/fonts/fontsource-newsreader/files/newsreader-latin-500-'
SER=f"@font-face{{font-family:IS;src:url({gen.b64(IS+'normal.woff2','font/woff2')})}}@font-face{{font-family:IS;font-style:italic;src:url({gen.b64(IS+'italic.woff2','font/woff2')})}}"
CSS = gen.CSS + SER + """
.tag{position:absolute;left:70px;top:230px;background:#FFE7DC;color:#C2410C;border-radius:14px;padding:10px 24px;font-weight:800;font-size:32px;letter-spacing:.06em}
body.or .tag{background:rgba(255,255,255,.22);color:#fff}
h2{position:absolute;left:70px;right:60px;top:300px;font-family:IS;font-weight:400;font-size:108px;letter-spacing:-.025em;line-height:1.02}
h1{font-family:IS!important;font-weight:400!important;letter-spacing:-.025em!important;line-height:1.02!important}
h1 .r,h2 .r{background:none!important;-webkit-background-clip:initial!important;color:#D9481F!important;font-style:italic;padding:0 8px 0 0}
body.or h2 .r{color:#141414!important}
h2 .r{padding:0 4px 8px}
h2 .l{display:block;white-space:nowrap}
body.or h2 .r{background:none;-webkit-background-clip:initial;color:#141414}
.lead{position:absolute;left:70px;right:90px;font-size:38px;line-height:1.35;font-weight:600;color:#333}
body.or .lead{color:#fff}
.pan{position:absolute;left:110px;right:110px;background:#16171B;border-radius:34px;color:#EDEDED;padding:0 0 36px;box-shadow:0 30px 60px rgba(0,0,0,.22);overflow:hidden}
.ph{display:flex;align-items:center;justify-content:space-between;padding:24px 34px;border-bottom:2px solid #26272D;font-family:SM;font-size:30px;letter-spacing:.08em}
.ph b{color:#F2793A;margin-right:10px}
.live{color:#7CE38B;font-size:28px} .live:before{content:'● '}
.pb{padding:30px 34px 0}
.lbl{font-family:SM;font-size:28px;color:#F2793A;letter-spacing:.1em;margin:6px 0 12px}
.chip{display:inline-block;background:#26272D;border-radius:999px;padding:8px 22px;margin:0 10px 12px 0;font-size:32px;font-weight:700}
.it{background:#FBF7F2;color:#141414;border-radius:20px;padding:20px 24px;margin-bottom:16px;font-size:34px;font-weight:700;line-height:1.25}
.it small{display:block;font-family:SM;font-size:28px;color:#C2410C;font-weight:700;margin-bottom:4px}
.tile{width:150px;height:150px;border-radius:34px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:80px;font-family:'Noto Color Emoji';box-shadow:0 10px 24px rgba(0,0,0,.15)}
.tl{font-family:'Inter Display';font-weight:900;font-size:84px;color:#F2552C;font-family:'Inter Display'}
.dash{flex:1;border-top:6px dashed #F2793A;margin:0 16px}
.thumb{background:#fff;border-radius:16px;height:200px;position:relative;overflow:hidden}
.thumb:after{content:'✓';position:absolute;right:10px;top:10px;width:44px;height:44px;border-radius:50%;background:#7CE38B;color:#141414;font-weight:900;font-size:30px;display:flex;align-items:center;justify-content:center}
"""

def hd(n, N): return f'<div class=rings></div><div class=hd><div class=mono>M</div><div><b>Nana</b><span>@manusiaslowrespond</span></div></div><div class=cnt>0{n} <i>/ 0{N}</i></div>'
def panel(name, body, top=820): return f'<div class=pan style="top:{top}px"><div class=ph><span><b>✳</b>{name}</span><span class=live>AKTIF</span></div><div class=pb>{body}</div></div>'
def role(n, N, tag, a, b, lead, pan, lead_top=580, pan_top=740):
    return hd(n, N) + f'<div class=tag>{tag}</div><h2 data-fit style="font-size:108px"><span class=l>{a}</span><span class="l r">{b}</span></h2><div class=lead style="top:{lead_top}px">{lead}</div>' + pan.replace('top:820px', f'top:{pan_top}px')

N = 9
TH = lambda c: f'<div class=thumb style="background:{c}"><div style="position:absolute;left:14px;right:14px;top:20px;height:22px;border-radius:6px;background:rgba(0,0,0,.75)"></div><div style="position:absolute;left:14px;width:60%;top:54px;height:22px;border-radius:6px;background:#F2552C"></div><div style="position:absolute;left:14px;right:40px;bottom:20px;height:70px;border-radius:10px;background:rgba(0,0,0,.12)"></div></div>'

S = []
# 1 cover
S.append(f"""<div class=rings></div>
<div style="position:absolute;left:0;right:0;top:80px;text-align:center"><span style="background:#F3F3F3;border-radius:12px;padding:8px 22px;font-size:30px;font-weight:700;color:#555">Cuan pakai AI</span></div>
<div style="position:absolute;left:180px;right:180px;top:200px;height:280px;border-radius:999px;background:#FFF7F2;border:3px solid #FFD9C7;display:flex;align-items:center;justify-content:center;gap:20px;box-shadow:0 20px 50px rgba(242,85,44,.15)">
<div class=tile style="width:150px;height:150px"><span class=tl>AI</span></div><div style="width:120px;border-top:6px dashed #F2793A"></div><div class=tile>📱</div></div>
<h1 data-fit style="top:540px;font-size:140px"><span class=l>Tim sosmed</span><span class="l r">isinya cuma AI.</span></h1>
<div style="position:absolute;left:80px;right:80px;top:930px;background:#fff;border:3px solid #E6E6E6;border-radius:34px;padding:34px 36px;display:flex;align-items:center;gap:24px;box-shadow:0 14px 30px rgba(0,0,0,.07)">
<span style="font-size:44px;color:#F2552C;font-weight:900">✳</span><span style="flex:1;font-size:44px;font-weight:600">urus sosmed tokoku<span style="color:#F2552C">|</span></span>
<span style="width:84px;height:84px;border-radius:20px;background:#F2552C;color:#fff;display:flex;align-items:center;justify-content:center;font-size:48px;font-weight:900">↑</span></div>
<div class=note style="top:1110px;color:#C2410C;font-weight:700;font-size:42px">Geser, kenalan sama timnya →</div>""")
# 2 setup
S.append(role(2, N, 'PERSIAPAN', 'Sambungin ke', 'akun sosmedmu.',
    'Lewat aplikasi penjadwal kayak Metricool, AI bisa bikin jadwal posting dan baca angka akunmu.',
    panel('PERSIAPAN', '<div style="display:flex;align-items:center;justify-content:center;padding:40px 0 20px"><div class=tile><span class=tl style="font-size:70px">AI</span></div><div class=dash></div><div class=tile>📅</div><div class=dash></div><div class=tile>📱</div></div><div style="text-align:center;font-size:40px;font-weight:800;color:#7CE38B">Tersambung ✓</div><div style="text-align:center;font-size:30px;color:#9A9AA3;margin-top:8px">jadwal · posting · angka</div>'),
    lead_top=580, pan_top=760))
# 3 periset
S.append(role(3, N, 'PERISET', 'Intip konten', 'kompetitor.',
    'Kirim link atau screenshot konten mereka. AI bedah mana yang paling rame.',
    panel('PERISET', '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">' + ''.join(TH(c) for c in ['#FDE7DC', '#E7EEFF', '#FFF3D6', '#E6F7EA', '#F3E8FF', '#FFE4E4']) + '</div><div style="font-size:40px;font-weight:900;margin-top:24px"><span style="color:#F2793A">12</span> konten dibedah</div>'),
    pan_top=730))
# 4 analis
S.append(role(4, N, 'ANALIS', 'Cari tahu kenapa', 'bisa rame.',
    'Hook, kata-kata yang dipakai, dan alasan orang nyimpen.',
    panel('ANALIS', '<div class=lbl>HOOK</div><div style="font-size:34px;line-height:1.5;margin-bottom:18px">"Jangan jualan sebelum tahu ini…"<br>"Ternyata ini alasannya sepi"<br>"Cuma 5 menit, beres"</div><div class=lbl>KATA KUAT</div><div><span class=chip>ternyata</span><span class=chip>gratis</span><span class=chip>cuma</span><span class=chip>rahasia</span></div>'),
    pan_top=730))
# 5 penulis (orange)
S.append(role(5, N, 'PENULIS', 'Tulis ide', 'seminggu penuh.',
    'Berdasarkan yang udah terbukti jalan di nichemu.',
    panel('PENULIS', '<div class=it><small>IDE 1</small>3 kesalahan foto produk</div><div class=it><small>IDE 2</small>Balas "kok mahal?" tanpa diskon</div><div class=it><small>IDE 3</small>Modal 1 cup, jual berapa?</div><div class=it style="margin-bottom:0"><small>IDE 4</small>Caption yang bikin orang nanya</div>'),
    pan_top=730))
# 6 desainer
S.append(role(6, N, 'DESAINER', 'Bikin slide', '& videonya.',
    'Carousel, video teks, sampai template yang bisa dipakai ulang.',
    panel('DESAINER', '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">' + ''.join(f'<div><div class=thumb style="height:260px;background:{c}"></div><div style="text-align:center;font-family:SM;font-size:28px;color:#F2793A;margin-top:12px">{t}</div></div>' for c, t in [('#FFFFFF', 'CAROUSEL'), ('#F2552C', 'VIDEO'), ('#FFF3D6', 'TEMPLATE')]) + '</div><div style="font-size:40px;font-weight:900;margin-top:26px">Konten jadi, <span style="color:#F2793A">kamu tinggal cek.</span></div>'),
    pan_top=730))
# 7 penjadwal
days = ''.join(f'<div style="background:#26272D;border-radius:16px;padding:16px 0;text-align:center"><div style="font-family:SM;font-size:28px;color:#9A9AA3">{d}</div><div style="font-size:32px;font-weight:900;color:#7CE38B;margin-top:6px">10.00</div></div>' for d in ['SEN', 'SEL', 'RAB', 'KAM', 'JUM', 'SAB', 'MIN'][:6])
S.append(role(7, N, 'PENJADWAL', 'Jadwalin', 'tiap hari.',
    'Posting jalan sendiri di jam yang kamu pilih.',
    panel('PENJADWAL', '<div style="display:flex;align-items:center;justify-content:space-between;background:#26272D;border-radius:18px;padding:20px 26px;margin-bottom:22px"><b style="font-size:38px">Posting otomatis</b><span style="width:110px;height:60px;border-radius:999px;background:#7CE38B;position:relative"><span style="position:absolute;right:6px;top:6px;width:48px;height:48px;border-radius:50%;background:#fff"></span></span></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">' + days + '</div>'),
    pan_top=730))
# 8 data
bars = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:10px"><div style="width:100%;height:{h}px;border-radius:12px;background:{"#F2552C" if w else "#3A3B42"}"></div><span style="font-family:SM;font-size:28px;color:{"#F2793A" if w else "#9A9AA3"}">#{i+1}</span></div>' for i, (h, w) in enumerate([(120, 0), (180, 0), (330, 1), (150, 0), (210, 0)]))
S.append(role(8, N, 'DATA', 'Baca angkanya,', 'ulangi pemenang.',
    'Lihat views & yang disimpan, lalu bikin lagi yang mirip.',
    panel('DATA', '<div style="display:flex;gap:18px;height:380px;align-items:flex-end">' + bars + '</div><div class=lbl style="margin-top:24px">PEMENANG MINGGU INI</div><div style="font-size:44px;font-weight:900">Konten #3 → <span style="color:#F2793A">bikin versi 2</span></div>'),
    pan_top=730))
# 9 penutup
S.append(hd(9, N) + f"""<div class=kick>GILIRANMU</div><h1 data-fit style="top:290px;font-size:118px"><span class=l>Tim mana yang</span><span class="l r">paling kamu butuh?</span></h1>
<div class=stk style="top:600px;gap:22px">""" + ''.join(f'<div class=card style="display:flex;align-items:center;gap:26px;padding:28px 34px"><div class=ico style="background:{bg};width:84px;height:84px;font-size:44px">{e}</div><b style="font-size:44px;font-family:\'Inter Display\';font-weight:900;letter-spacing:-.02em">{t}</b></div>' for e, bg, t in [('🔎', '#EAF1FF', 'Periset'), ('✍️', '#FFF3D6', 'Penulis'), ('🎨', '#FFE4E4', 'Desainer'), ('📅', '#E6F7EA', 'Penjadwal')]) +
 '<div class=note style="margin-top:14px;color:#333;font-weight:700;font-size:38px">Kirim ke temen yang ngurus sosmed sendirian 📱</div></div>')

async def main(slug='t01-timsosmed'):
    os.makedirs(f'{gen.HERE}/out/{slug}', exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1440})
        for i, h in enumerate(S, 1):
            cls = 'or' if i == 5 else ''
            await pg.set_content(f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body class="{cls}">{h}</body></html>')
            await pg.evaluate(gen.FIT); await pg.wait_for_timeout(250)
            await pg.screenshot(path=f'{gen.HERE}/out/{slug}/slide-{i}.png')
        await b.close()
asyncio.run(main())
