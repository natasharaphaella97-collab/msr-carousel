import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
F='/tmp/fonts/Poppins-Black.ttf'
def brand(src,out,logo='/home/claude/aj/logo_icon.png'):
    im=Image.open(src).convert('RGB')
    w,h=im.size
    if min(w,h)<1080:
        s=1080/min(w,h); im=im.resize((round(w*s),round(h*s)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,60,2)); w,h=im.size
    m=round(w*0.04); lh=round(w*0.17)
    lg=Image.open(logo).convert('RGBA'); lg=lg.resize((round(lg.width*lh/lg.height),lh),Image.LANCZOS)
    fb=ImageFont.truetype(F,round(w*0.085)); fs=ImageFont.truetype(F,round(w*0.036))
    d=ImageDraw.Draw(im)
    bb=d.textbbox((0,0),'ABADI JAYA',font=fb); sb=d.textbbox((0,0),'Toko Listrik',font=fs)
    gap=round(w*0.008); th=(sb[3]-sb[1])+gap+(bb[3]-bb[1]); bw=lg.width+round(w*0.025)+max(bb[2],sb[2])
    g=np.array(im.convert('L').filter(ImageFilter.FIND_EDGES)).astype(float)
    band=lh+2*m
    top=g[:band,:bw+2*m].mean(); bot=g[h-band:,:bw+2*m].mean()
    y0=m if top<=bot else h-m-lh
    tx=m+lg.width+round(w*0.025); ty=y0+(lh-th)//2
    sh=Image.new('RGBA',im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    o=round(w*0.004)
    sd.text((tx+o,ty-sb[1]+o),'Toko Listrik',font=fs,fill=(0,0,0,255))
    sd.text((tx+o,ty+(sb[3]-sb[1])+gap-bb[1]+o),'ABADI JAYA',font=fb,fill=(0,0,0,255))
    sd.ellipse((m+o,y0+o,m+lg.width+o,y0+lh+o),fill=(0,0,0,200))
    sh=sh.filter(ImageFilter.GaussianBlur(w*0.006))
    im=im.convert('RGBA'); im.alpha_composite(sh); im.alpha_composite(sh); im.alpha_composite(lg,(m,y0))
    d=ImageDraw.Draw(im)
    d.text((tx,ty-sb[1]),'Toko Listrik',font=fs,fill=(255,255,255))
    d.text((tx,ty+(sb[3]-sb[1])+gap-bb[1]),'ABADI JAYA',font=fb,fill=(254,200,20))
    im.convert('RGB').save(out,quality=92)
if __name__=='__main__': brand(sys.argv[1],sys.argv[2])
