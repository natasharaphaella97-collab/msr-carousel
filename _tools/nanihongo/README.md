# Na Nihongo carousel templates

Copy this folder to /home/claude/nanihongo (keeps the same paths the scripts expect):
  mkdir -p /home/claude/nanihongo && cp -r _tools/nanihongo/* /home/claude/nanihongo/

- p01/render.py   : base CSS (navy #1B2340, cream #F6F1E7, red #C8102E, Inter + Noto Sans CJK JP)
- batch/gen.py    : helpers cover(), text(), rows(), big(), chips(), cta() + "Kerja di Jepang" posts (10:00 WIB slot)
- cs/gen2.py      : vocab() rows (JP / romaji / arti) + "Cheat Sheet" posts (21:00 WIB slot)

Output: 1080x1350 PNG -> JPG q92, pushed to nanihongo-<slug>/s1..sN.jpg

- story.py       : bikin story 1080x1920 untuk SEMUA slide. Jalankan: python3 story.py <slug1> <slug2> ... Output: nanihongo-<slug>/st1.jpg..stN.jpg. Jadwalkan 1 STORY post per slide: st1 di +15 menit setelah carousel, lalu st2, st3... tiap +1 menit.

- photos/: foto stok yang sudah dibayar (pakai ulang, JANGAN generate baru): p_cash.jpg (bayar cash di kasir), p_ic.jpg (tap kartu IC di gate stasiun), p_qr.jpg (HP scan QR di kasir), p_card.jpg (kartu debit di mesin). Contoh pakai: pay01_gen.py (photo(), pcover()).
