# Story IG 1080x1920 untuk SEMUA slide carousel (bukan cuma cover).
# Tiap s{i}.jpg (1080x1350) ditaruh di tengah kanvas 1080x1920, sisa atas/bawah diisi warna background slide.
# Tanpa label/teks tambahan. Pakai: python3 story.py <slug1> <slug2> ...
# Output: nanihongo-<slug>/st1.jpg, st2.jpg, ... (1 story per slide)
import sys, glob, re
from PIL import Image
REPO='/home/claude/msr-carousel'
for s in sys.argv[1:]:
    d=f"{REPO}/nanihongo-{s}"
    files=sorted(glob.glob(f"{d}/s[0-9]*.jpg"), key=lambda f:int(re.search(r's(\d+)\.jpg$',f).group(1)))
    for f in files:
        i=int(re.search(r's(\d+)\.jpg$',f).group(1))
        im=Image.open(f).convert('RGB')
        c=Image.new('RGB',(1080,1920),im.getpixel((10,10)))
        c.paste(im,(0,(1920-im.height)//2))
        c.save(f"{d}/st{i}.jpg",quality=92)
    print(s,len(files),'story')
