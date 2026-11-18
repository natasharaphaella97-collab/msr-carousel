import asyncio, sys, base64, os
from playwright.async_api import async_playwright
REPO='/home/claude/msr-carousel'
slugs=sys.argv[1:]
CSS="""*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;background:#F6F1E7;font-family:'Inter','Noto Sans CJK JP',sans-serif;position:relative;overflow:hidden}
.sun{position:absolute;border-radius:50%;background:#C8102E}
.tag{position:absolute;left:50px;top:250px;background:#C8102E;color:#fff;font-weight:900;font-size:40px;padding:14px 28px;border-radius:10px;letter-spacing:1px}
img{position:absolute;left:50px;top:360px;width:980px;height:1225px;border-radius:24px;box-shadow:0 20px 60px rgba(0,0,0,.45)}
.ft{position:absolute;left:50px;top:1625px;color:#1B2340;font-weight:800;font-size:42px}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        for s in slugs:
            src=f"{REPO}/nanihongo-{s}/s1.jpg"
            d=base64.b64encode(open(src,'rb').read()).decode()
            html=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='sun' style='width:520px;height:520px;right:-180px;top:-160px'></div><div class='sun' style='width:300px;height:300px;left:-120px;bottom:-110px'></div><img src='data:image/jpeg;base64,{d}'><div class='ft'>Geser & save di feed ya 🇯🇵</div></body></html>"
            await pg.set_content(html); await pg.wait_for_timeout(200)
            os.makedirs(f"{REPO}/nanihongo-{s}",exist_ok=True)
            await pg.screenshot(path=f"/home/claude/nanihongo/story/{s}.png")
            from PIL import Image
            Image.open(f"/home/claude/nanihongo/story/{s}.png").convert('RGB').save(f"{REPO}/nanihongo-{s}/story2.jpg",quality=92)
        await b.close()
asyncio.run(main())
