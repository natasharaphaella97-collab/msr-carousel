# Story IG 1080x1920: cover carousel (s1.jpg) full-bleed di atas, sisa bawah diisi warna background cover.
# Tanpa label/teks tambahan. Pakai: python3 story.py <slug1> <slug2> ...  -> nanihongo-<slug>/story.jpg
import sys
from PIL import Image
REPO='/home/claude/msr-carousel'
for s in sys.argv[1:]:
    im=Image.open(f"{REPO}/nanihongo-{s}/s1.jpg").convert('RGB')
    c=Image.new('RGB',(1080,1920),im.getpixel((20,1340))); c.paste(im,(0,0))
    c.save(f"{REPO}/nanihongo-{s}/story.jpg",quality=92)
