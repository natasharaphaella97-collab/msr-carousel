# Na Nihongo carousel templates

Copy this folder to /home/claude/nanihongo (keeps the same paths the scripts expect):
  mkdir -p /home/claude/nanihongo && cp -r _tools/nanihongo/* /home/claude/nanihongo/

- p01/render.py   : base CSS (navy #1B2340, cream #F6F1E7, red #C8102E, Inter + Noto Sans CJK JP)
- batch/gen.py    : helpers cover(), text(), rows(), big(), chips(), cta() + "Kerja di Jepang" posts (10:00 WIB slot)
- cs/gen2.py      : vocab() rows (JP / romaji / arti) + "Cheat Sheet" posts (21:00 WIB slot)

Output: 1080x1350 PNG -> JPG q92, pushed to nanihongo-<slug>/s1..sN.jpg
