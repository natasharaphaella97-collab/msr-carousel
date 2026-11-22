import sys, os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps
from collections import deque

FONT_BOLD = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
FONT_MED = '/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf'
PINK = (222, 110, 154)
PURPLE = (150, 130, 200)
DARK = (70, 50, 85)
BG = (255, 245, 249)

def logo_transparent(path):
    im = Image.open(path).convert('RGBA')
    w, h = im.size; px = im.load(); seen=set()
    q = deque([(0,0),(w-1,0),(0,h-1),(w-1,h-1)])
    while q:
        x,y = q.popleft()
        if (x,y) in seen or x<0 or y<0 or x>=w or y>=h: continue
        r,g,b,a = px[x,y]
        if r>235 and g>235 and b>235:
            seen.add((x,y)); px[x,y]=(255,255,255,0)
            q.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
    return im.crop(im.getbbox())

def crop_border(im):
    im = im.convert('RGB'); w,h = im.size; px = im.load()
    def is_border(c):
        r,g,b = c; return (r>150 and g<90 and b<90)
    def row_border(y): return sum(is_border(px[x,y]) for x in range(0,w,4)) > (w/4)*0.8
    def col_border(x): return sum(is_border(px[x,y]) for y in range(0,h,4)) > (h/4)*0.8
    top=0
    while top<h//4 and row_border(top): top+=1
    bot=h-1
    while bot>h*3//4 and row_border(bot): bot-=1
    left=0
    while left<w//4 and col_border(left): left+=1
    right=w-1
    while right>w*3//4 and col_border(right): right-=1
    if top==0 and left==0 and bot==h-1 and right==w-1: return im
    pad=6
    return im.crop((left+pad, top+pad, right-pad+1, bot-pad+1))

def brand(src, out, title, subtitle, S=1080):
    photo = crop_border(Image.open(src))
    canvas = Image.new('RGBA', (S,S), BG+(255,))
    d = ImageDraw.Draw(canvas)

    # header band
    band_h = 230
    d.rectangle((0,0,S,band_h), fill=(255,255,255,255))
    d.line([(0,band_h),(S,band_h)], fill=PINK+(255,), width=6)

    logo = logo_transparent(os.path.join(os.path.dirname(os.path.abspath(__file__)),'UsagiUtopia.jpg'))
    lw = 300; lh = int(logo.size[1]*lw/logo.size[0])
    logo = logo.resize((lw,lh), Image.LANCZOS)
    canvas.alpha_composite(logo, (44, (band_h-lh)//2))

    # title block right of logo
    tx = 44+lw+36; tw = S - tx - 40
    def wrap(text, font, maxw):
        words=text.split(); lines=[]; cur=''
        for w_ in words:
            t=(cur+' '+w_).strip()
            if d.textlength(t, font=font)<=maxw: cur=t
            else: lines.append(cur); cur=w_
        if cur: lines.append(cur)
        return lines
    f2 = ImageFont.truetype(FONT_MED, 30)
    sub_lines = wrap(subtitle, f2, tw)
    lh2 = 38
    size=60
    while True:
        f1 = ImageFont.truetype(FONT_BOLD, size)
        lines = wrap(title, f1, tw)
        lh1 = size*1.12
        total = lh1*len(lines) + 8 + lh2*len(sub_lines)
        if total <= band_h-30 or size<=34: break
        size -= 2
    y = (band_h - total)//2
    for l in lines:
        d.text((tx, y), l, font=f1, fill=DARK); y += lh1
    y += 10
    for l in sub_lines:
        d.text((tx, y), l, font=f2, fill=PINK); y += lh2

    # photo area
    area = (0, band_h+6, S, S)
    aw, ah = area[2]-area[0], area[3]-area[1]
    ph = ImageOps.contain(photo, (aw, ah), Image.LANCZOS).convert('RGBA')
    canvas.alpha_composite(ph, (area[0]+(aw-ph.size[0])//2, area[1]+(ah-ph.size[1])//2))

    canvas.convert('RGB').save(out, 'JPEG', quality=92, optimize=True)
    print(out)

if __name__ == '__main__':
    brand(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

def brand_tall(src, out, title, subtitle, W=1080):
    photo = Image.open(src).convert('RGB')
    ph = ImageOps.contain(photo,(W,4000), Image.LANCZOS)
    band_h=230
    canvas = Image.new('RGBA',(W, band_h+6+ph.size[1]), BG+(255,))
    d=ImageDraw.Draw(canvas)
    d.rectangle((0,0,W,band_h), fill=(255,255,255,255)); d.line([(0,band_h),(W,band_h)], fill=PINK+(255,), width=6)
    logo=logo_transparent(os.path.join(os.path.dirname(os.path.abspath(__file__)),'UsagiUtopia.jpg')); lw=300; lh=int(logo.size[1]*lw/logo.size[0])
    canvas.alpha_composite(logo.resize((lw,lh), Image.LANCZOS),(44,(band_h-lh)//2))
    tx=44+lw+36; tw=W-tx-40
    def wrap(text,font,maxw):
        words=text.split(); lines=[]; cur=''
        for w_ in words:
            t=(cur+' '+w_).strip()
            if d.textlength(t,font=font)<=maxw: cur=t
            else: lines.append(cur); cur=w_
        if cur: lines.append(cur)
        return lines
    f2=ImageFont.truetype(FONT_MED,30); sub=wrap(subtitle,f2,tw); size=60
    while True:
        f1=ImageFont.truetype(FONT_BOLD,size); lines=wrap(title,f1,tw); lh1=size*1.12
        total=lh1*len(lines)+8+38*len(sub)
        if total<=band_h-30 or size<=34: break
        size-=2
    y=(band_h-total)//2
    for l in lines: d.text((tx,y),l,font=f1,fill=DARK); y+=lh1
    y+=10
    for l in sub: d.text((tx,y),l,font=f2,fill=PINK); y+=38
    canvas.alpha_composite(ph.convert('RGBA'),(0,band_h+6))
    canvas.convert('RGB').save(out,'JPEG',quality=92,optimize=True); print(out, canvas.size)
