"""MSR v2 carousel generator — gaya putih (ala aiagently).
Usage: python3 gen.py [slug ...]  -> out/<slug>/slide-N.png
"""
import asyncio, base64, json, os, sys
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
def b64(p,m): return f"data:{m};base64,"+base64.b64encode(open(p,'rb').read()).decode()
F='/home/claude/work/fonts/fontsource-space-mono-5.3.0/files/space-mono-latin-700-normal.woff2'
SM=b64(F,'font/woff2'); AV=b64(HERE+'/av.jpg','image/jpeg')
CUTS={k:b64(f'{HERE}/cut/{k}_c.png','image/png') for k in ['pal','eif','stu']}
RED='#E63B2E'
NR='/home/claude/work/fonts/fontsource-newsreader/files/newsreader-latin-500-'
SERIF=f"@font-face{{font-family:IS;src:url({b64(NR+'normal.woff2','font/woff2')})}}@font-face{{font-family:IS;font-style:italic;src:url({b64(NR+'italic.woff2','font/woff2')})}}"
CSS=SERIF+f"""@font-face{{font-family:SM;src:url({SM})}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1440px;overflow:hidden;position:relative;background:#fff;font-family:'Inter',sans-serif;color:#141414}}
.rings{{position:absolute;inset:0;background:
radial-gradient(circle at 8% 32%,transparent 419px,#EEE 420px,#EEE 422px,transparent 423px),
radial-gradient(circle at 96% 62%,transparent 499px,#EEE 500px,#EEE 502px,transparent 503px)}}
.hd{{position:absolute;left:56px;top:56px;display:flex;align-items:center;gap:22px}}
.mono{{width:104px;height:104px;border-radius:50%;background:#141414;color:#fff;display:flex;align-items:center;justify-content:center;font-family:'Inter Display';font-weight:900;font-size:56px;letter-spacing:-.04em}}
.hd img{{width:104px;height:104px;border-radius:50%;border:4px solid #141414;object-fit:cover}}
.hd b{{display:block;font-family:'Inter Display';font-weight:900;font-size:40px;letter-spacing:-.02em}}
.hd span{{font-size:30px;color:#777}}
.cnt{{position:absolute;right:56px;top:74px;border:3px solid #DDD;border-radius:999px;padding:8px 30px;font-family:'Inter Display';font-weight:900;font-size:36px}}
.cnt i{{font-style:normal;color:#BBB;font-weight:500}}
.kick{{position:absolute;left:0;right:0;top:225px;display:flex;align-items:center;justify-content:center;gap:22px;font-weight:800;font-size:30px;letter-spacing:.22em;color:#C2410C;white-space:nowrap}}
.kick:before,.kick:after{{content:'';width:120px;height:2px;background:#CCC}}
h1{{font-family:IS;font-weight:500;letter-spacing:-.025em;line-height:1.02;text-align:center;position:absolute;left:40px;right:40px}}
h1 .l{{display:block;white-space:nowrap}}
.r{{color:#D9481F;font-style:italic;padding:0 8px 0 0}}
.note{{position:absolute;left:70px;right:70px;text-align:center;font-size:36px;color:#555;line-height:1.35}}
.card{{background:#fff;border:2px solid #EAEAEA;border-radius:28px;box-shadow:0 10px 30px rgba(0,0,0,.05)}}
.stk{{position:absolute;left:56px;right:56px;display:flex;flex-direction:column;gap:34px}}
.stk .note{{position:static}}
.win{{border-radius:30px;overflow:hidden;box-shadow:0 24px 50px rgba(0,0,0,.10);border:2px solid #E6E6E6;background:#fff}}
.bar{{height:62px;background:#F4F4F4;display:flex;align-items:center;gap:12px;padding:0 26px;font-family:SM;font-size:28px;color:#777}}
.bar i{{width:18px;height:18px;border-radius:50%;display:inline-block}}
.ico{{width:96px;height:96px;border-radius:24px;display:flex;align-items:center;justify-content:center;font-size:50px;font-family:'Noto Color Emoji';flex:none}}
.me{{background:#F1F1F1;border-radius:24px;padding:20px 26px;margin-left:110px;font-size:33px;line-height:1.4}}
.ai{{background:#FFF4EE;border:2px solid #FFD9C7;border-radius:24px;padding:20px 26px;margin-top:20px;margin-right:30px;font-size:33px;line-height:1.42}}
.ai .who{{font-weight:800;color:{RED};font-size:30px;margin-bottom:6px}}
table{{width:100%;border-collapse:collapse;font-size:40px}}
td{{padding:14px 0}} td:last-child{{text-align:right;font-weight:800}}
body.or{{background:#F2552C;color:#fff}}
body.or .rings{{opacity:.25;filter:invert(1)}}
body.or .hd span{{color:rgba(255,255,255,.85)}}
body.or .mono{{background:#fff;color:#F2552C}}
body.or .cnt{{border-color:rgba(255,255,255,.5)}} body.or .cnt i{{color:rgba(255,255,255,.6)}}
body.or .kick:before,body.or .kick:after{{background:rgba(255,255,255,.6)}} body.or .kick{{color:#fff}}
body.or h1 .r{{color:#141414}}
body.or .note{{color:#fff}} body.or .note b{{color:#141414!important}}
body.or .card,body.or .win{{color:#141414;border-color:transparent;box-shadow:0 18px 40px rgba(120,30,0,.25)}}
tr.t td{{border-top:3px dashed #DDD;padding-top:22px;color:{RED};font-weight:900}}
"""
BARS='<div class=bar><i style="background:#FF5F57"></i><i style="background:#FEBC2E"></i><i style="background:#28C840"></i><span style="margin:0 auto">{}</span></div>'
ICOBG=['#EAF1FF','#FFF3D6','#FFE4E4','#E6F7EA']

def head(n,N): return f'<div class=rings></div><div class=hd><div class=mono>M</div><div><b>Nana</b><span>@manusiaslowrespond</span></div></div><div class=cnt>0{n} <i>/ 0{N}</i></div>'
def h1(a,b,top,size=118): return f'<h1 style="top:{top}px;font-size:{size}px" data-fit><span class=l>{a}</span><span class="l r">{b}</span></h1>'

def cover(p):
    c=p['cover']
    pill='#F3F3F3;color:#555' if not p.get('orange') else 'rgba(255,255,255,.2);color:#fff'
    line='#141414' if p.get('orange') else RED
    return f"""<div class=rings></div>
<div style="position:absolute;left:0;right:0;top:78px;text-align:center"><span style="background:{pill};border-radius:12px;padding:8px 22px;font-size:30px;font-weight:700">Cuan pakai AI</span></div>
{h1(c['a'],c['b'],150,140)}
<svg style="position:absolute;left:190px;top:490px" width="700" height="30"><path d="M5 20 Q350 2 695 16" stroke="{line}" stroke-width="8" fill="none" stroke-linecap="round"/></svg>
<div class=win style="position:absolute;left:70px;right:70px;top:590px;transform:rotate(-2deg)">{BARS.format('chat dengan AI')}<div style="padding:44px 40px">
<div style="display:flex;align-items:center;gap:22px;margin-bottom:30px"><div class=ico style="width:110px;height:110px;font-size:60px;background:#FFE7DC">{c['ico']}</div><b style="font-size:50px;line-height:1.15;font-family:'Inter Display';font-weight:900;letter-spacing:-.02em">{c['t']}</b></div>
<div class=me style="font-size:44px;margin-left:100px;padding:26px 30px">{c['q']}</div>
<div class=ai style="font-size:46px;margin-right:0;margin-top:28px;padding:26px 30px"><div class=who>✳ AI</div>{c['ans']}</div></div></div>"""

def bukti(p,n,N):
    b=p['bukti']
    return head(n,N)+f"""<div class=kick>BUKTI DULU</div>{h1('Hasil asli','dari AI.',290)}
<div class=stk style="top:560px"><div class=win>{BARS.format("chat dengan AI")}<div style="padding:28px">
<div class=me>{b['me']}</div><div class=ai><div class=who>✳ AI</div>{b['ai']}</div></div></div>
<div class=note>Kok bisa? Geser, ini caranya →</div></div>"""

def masalah(p,n,N):
    m=p['masalah']
    items="".join(f'<div class=card style="display:flex;align-items:center;gap:30px;padding:36px 34px"><div class=ico style="background:{ICOBG[i]}">{e}</div><b style="font-family:\'Inter Display\';font-weight:900;font-size:44px;letter-spacing:-.02em;line-height:1.15">{t}</b></div>' for i,(e,t) in enumerate(m['items']))
    return head(n,N)+f"""<div class=kick>MASALAHNYA</div>{h1(m['a'],m['b'],290)}
<div style="position:absolute;left:56px;right:56px;top:570px;display:flex;flex-direction:column;gap:26px">{items}</div>"""

def trik(p,n,N):
    t=p['trik']
    return head(n,N)+f"""<div class=kick>TRIKNYA</div>{h1(t['a'],t['b'],290)}
<div class=stk style="top:580px"><div class=card style="padding:46px 48px;font-size:44px;line-height:1.45">{t['body']}</div>
<div style="display:flex;align-items:center;gap:24px;background:#FFF4EE;border-radius:24px;padding:30px 36px;font-size:38px;font-weight:700;color:#7A2A1E"><span style="font-family:'Noto Color Emoji';font-size:46px">💡</span>{t['note']}</div></div>"""

def cek(p,n,N):
    c=p['cek']
    items="".join(f'<div class=card style="display:flex;align-items:center;gap:28px;padding:36px 36px;font-size:44px;font-weight:800;line-height:1.2"><span style="width:58px;height:58px;border:5px solid #141414;border-radius:14px;flex:none"></span>{t}</div>' for t in c)
    return head(n,N)+f"""<div class=kick>CEK DULU</div>{h1('Sebelum','lanjut…',290,130)}
<div class=stk style="top:600px;gap:26px">{items}
<div class=note style="margin-top:20px">Ada yang belum kecentang?<br>Slide berikutnya wajib kamu <b style="color:{RED}">simpan</b>.</div></div>"""

def hasil(p,n,N):
    h=p['hasil']
    rows="".join(f'<tr{" class=t" if i==len(h["rows"])-1 else ""}><td>{a}</td><td>{b}</td></tr>' for i,(a,b) in enumerate(h['rows']))
    return head(n,N)+f"""<div class=kick>CONTOH HASILNYA</div>{h1(h['a'],h['b'],290)}
<div class=stk style="top:580px"><div class=card style="padding:30px 44px">{h.get('pre','')}<table>{rows}</table></div>
<div class=note>{h['note']}</div></div>"""

def prompt(p,n,N):
    pr=p['prompt']
    return head(n,N)+f"""<div class=kick>SCREENSHOT INI</div>{h1('Copas','prompt-nya.',290)}
<div class=stk style="top:560px"><div class=win style="background:#16171B;border-color:#16171B">{BARS.format('prompt.txt').replace('#F4F4F4','#222328').replace('#777','#999')}
<div style="padding:36px 40px;font-family:SM;font-size:32px;line-height:1.6;color:#EDEDED">{pr['text']}</div></div>
<div class=note style="color:#333;font-weight:700;font-size:38px">{pr['share']}</div></div>"""

def pages(p):
    N=7
    return [cover(p),bukti(p,2,N),masalah(p,3,N),trik(p,4,N),cek(p,5,N),hasil(p,6,N),prompt(p,7,N)]

FIT="""for(const h of document.querySelectorAll('[data-fit]')){let s=parseFloat(h.style.fontSize);const W=h.clientWidth;
while([...h.querySelectorAll('.l')].some(l=>l.scrollWidth>W)&&s>60){s-=2;h.style.fontSize=s+'px'}}"""

async def render(slugs):
    data=json.load(open(HERE+'/posts.json'))
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1440})
        for slug in slugs:
            p=data[slug]; os.makedirs(f'{HERE}/out/{slug}',exist_ok=True)
            for i,h in enumerate(pages(p),1):
                cls='or' if (i==5 or (i==1 and p.get('orange'))) else ''
                await pg.set_content(f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body class="{cls}">{h}</body></html>')
                await pg.evaluate(FIT); await pg.wait_for_timeout(250)
                # overflow check: anything below 1440?
                over=await pg.evaluate("Math.max(...[...document.querySelectorAll('.card,.win,.note')].map(e=>e.getBoundingClientRect().bottom))")
                if over>1380: print('WARN overflow',slug,i,over)
                await pg.screenshot(path=f'{HERE}/out/{slug}/slide-{i}.png')
        await b.close()
if __name__=='__main__':
    data=json.load(open(HERE+'/posts.json'))
    asyncio.run(render(sys.argv[1:] or list(data)))
