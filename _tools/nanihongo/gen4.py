import asyncio, os, base64
src = open("/home/claude/nanihongo/cs/gen2.py").read().split('CS = "CHEAT SHEET"')[0]
ns = {}; exec(src, ns)
CSS, cover, text, cta, vocab = ns['CSS'], ns['cover'], ns['text'], ns['cta'], ns['vocab']
g = {}; exec(open("/home/claude/nanihongo/batch/gen.py").read().split('T = "KERJA')[0], g)
rows, big, chips = g['rows'], g['big'], g['chips']
R = "<span class='red'>{}</span>"; PINK = "<span style='color:#FF4D5E'>{}</span>"; J = "<span class='jp'>{}</span>"
CS = "CHEAT SHEET"
CSS += """
.tier{display:flex;align-items:stretch;border-bottom:3px solid #1B2340;min-height:150px}
.tl{width:150px;flex:0 0 150px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:96px;color:#F6F1E7}
.tr{display:flex;flex-wrap:wrap;gap:14px;align-items:center;padding:20px 0 20px 26px}
.tr span{background:#1B2340;color:#F6F1E7;font-weight:800;font-size:36px;padding:12px 20px;border-radius:12px}
.full{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}
.ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(27,35,64,.55) 0%,rgba(27,35,64,.92) 55%,#1B2340 100%)}
"""
def tiers(tag, rs):
    cols = {'S':'#C8102E','A':'#E0573B','B':'#4A5A86','C':'#8A90A6'}
    r = "".join(f"<div class='tier'><div class='tl' style='background:{cols[k]}'>{k}</div><div class='tr'>{''.join(f'<span>{x}</span>' for x in xs)}</div></div>" for k, xs in rs)
    return f"<body><div class='pad' style='top:150px'><span class='tag'>{tag}</span><div style='margin-top:36px;border-top:3px solid #1B2340'>{r}</div></div></body>"
def img(n): return "data:image/jpeg;base64,"+base64.b64encode(open(f"/home/claude/msr-carousel/_tools/nanihongo/photos/p_{n}.jpg","rb").read()).decode()
def pcover(n, tag, head, sub):
    return f"<body class='cover'><img class='full' src='{img(n)}'><div class='ov'></div><div class='pad' style='top:250px'><span class='tag'>{tag}</span><div class='h1'>{head}</div><div class='p' style='color:#e3e7f2'>{sub}</div></div></body>"
def check(tag, head, items, dark=True):
    r = "".join(f"<div style='display:flex;gap:22px;align-items:center;font-size:44px;font-weight:800;padding:18px 0;border-bottom:3px solid {'#F6F1E7' if dark else '#1B2340'}'><span style='color:#FF4D5E;font-size:50px'>✓</span>{i}</div>" for i in items)
    return f"<body{' class=cover' if dark else ''}><div class='pad' style='top:150px'><span class='tag'>{tag}</span><div class='h2' style='margin-top:30px;font-size:70px'>{head}</div><div style='margin-top:20px'>{r}</div></div></body>"

POSTS = {
"cs15-ketuker": [
 cover(CS, "Salah 1 huruf, " + PINK.format("tante jadi nenek."), "6 pasang kata Jepang yang sering ketuker."),
 text("Di bahasa Jepang, " + R.format("vokal panjang") + " ngubah arti.", "Beda 1 huruf aja, artinya bisa beda jauh. Ini yang paling sering bikin malu."),
 vocab("VOKAL PANJANG", [("おばさん", "obasan", "Tante / ibu-ibu"), ("おばあさん", "obaasan", "Nenek"), ("おじさん", "ojisan", "Om / bapak-bapak"), ("おじいさん", "ojiisan", "Kakek")]),
 vocab("DI JALAN", [("ビル", "biru", "Gedung"), ("ビール", "biiru", "Bir"), ("病院", "byouin", "Rumah sakit"), ("美容院", "biyouin", "Salon")]),
 vocab("SEHARI-HARI", [("かわいい", "kawaii", "Imut"), ("こわい", "kowai", "Takut / serem"), ("地図", "chizu", "Peta"), ("チーズ", "chiizu", "Keju")]),
 text("Tips: tahan vokal panjang " + PINK.format("2 ketukan."), "おばあさん = o-ba-<b style='color:#fff'>a</b>-san. Kalau kependekan, nenek jadi tante.", dark=True),
 cta("Di izakaya mau pesan bir, bilang apa?", "A. ビル  B. ビール. Jawab A/B di komen."),
],
"tl02-konbini-halal": [
 pcover("cash", "TIER LIST KONBINI", "Jajan konbini tapi " + PINK.format("nggak makan babi?"), "Tier list dari yang paling aman sampai yang harus dihindari."),
 text("Babi sering " + R.format("ngumpet") + " di kaldu, roti, dan bumbu.", "Labelnya tulisan Jepang semua. Jadi hafalin urutan aman ini dulu."),
 tiers("TIER LIST JAJAN KONBINI", [('S', ['Telur rebus', 'Buah', 'Onigiri garam']), ('A', ['Onigiri salmon', 'Onigiri tuna mayo']), ('B', ['Mi cup', 'Roti', 'Puding / jelly']), ('C', ['Nikuman', 'Sandwich katsu', 'Ramen tonkotsu'])]),
 text("Tier S & A: " + R.format("biasanya aman."), J.format("ゆで卵") + " (telur rebus), " + J.format("鮭") + " (salmon), " + J.format("ツナマヨ") + " (tuna mayo).", "Tetap cek label, resep tiap konbini bisa beda."),
 text("Tier B: " + R.format("wajib cek label."), "Mi cup sering pakai ekstrak babi. Puding & jelly bisa pakai gelatin babi."),
 text("Tier C: " + PINK.format("hindari."), J.format("肉まん") + " (nikuman) isinya babi. Katsu di sandwich biasanya babi. Tonkotsu = kaldu tulang babi.", dark=True),
 vocab("KATA DI LABEL", [("原材料", "genzairyou", "Komposisi"), ("豚肉・ポーク", "butaniku / pooku", "Daging babi"), ("ポークエキス", "pooku ekisu", "Ekstrak babi"), ("ゼラチン", "zerachin", "Gelatin"), ("酒精", "shusei", "Alkohol (pengawet)")]),
 cta("Kamu cek label dulu atau langsung beli?", "Jawab CEK atau LANGSUNG di komen."),
],
"cs16-maaf": [
 cover(CS, "Minta maaf di Jepang " + PINK.format("ada levelnya."), "Salah pilih, bisa kedengeran nggak sopan."),
 text("Ke temen, ke orang asing, ke atasan: " + R.format("kata maafnya beda."), "Plus cara jawab kalau orang lain yang minta maaf ke kamu."),
 vocab("MINTA MAAF", [("ごめん", "gomen", "Sori (ke temen)"), ("ごめんなさい", "gomen nasai", "Maaf ya (temen, keluarga)"), ("失礼しました", "shitsurei shimashita", "Maaf, permisi (sopan)"), ("申し訳ありません", "moushiwake arimasen", "Mohon maaf (kerja, formal)")]),
 vocab("JAWABANNYA", [("大丈夫です", "daijoubu desu", "Nggak apa-apa"), ("気にしないで", "ki ni shinaide", "Jangan dipikirin"), ("こちらこそ", "kochira koso", "Aku juga minta maaf"), ("全然大丈夫です", "zenzen daijoubu desu", "Santai, nggak masalah")]),
 text("Salah di tempat kerja? Pakai " + PINK.format(J.format("申し訳ありません")), "Jangan " + J.format("ごめん") + " ke atasan. Kesannya kayak ngomong ke temen.", dark=True),
 cta("Kata maaf yang paling sering kamu pakai?", "A. ごめん  B. すみません. Jawab A/B."),
],
"kj01-hari-pertama": [
 cover("KERJA DI JEPANG", "Hari pertama kerja, " + PINK.format("8 kalimat ini") + " wajib bisa.", "Biar kesan pertama ke senpai & atasan langsung aman."),
 text("Hari pertama yang dinilai " + R.format("bukan skill.") , "Tapi sikap: salam duluan, jawab dengan jelas, dan berani nanya kalau nggak ngerti."),
 vocab("PAS DATANG", [("〇〇と申します", "... to moushimasu", "Saya ... (sopan)"), ("本日からお世話になります", "honjitsu kara osewa ni narimasu", "Mulai hari ini mohon bimbingannya"), ("よろしくお願いします", "yoroshiku onegai shimasu", "Mohon kerja samanya"), ("おはようございます", "ohayou gozaimasu", "Salam pertama tiap shift")]),
 vocab("PAS KERJA", [("分かりました", "wakarimashita", "Baik, saya ngerti"), ("もう一度お願いします", "mou ichido onegai shimasu", "Tolong ulangi"), ("終わりました", "owarimashita", "Sudah selesai"), ("次は何をすればいいですか？", "tsugi wa nani o sureba ii desu ka", "Selanjutnya ngapain?")]),
 text("Nggak ngerti? " + PINK.format("Jangan bilang " + J.format("分かりました") + "."), "Bilang もう一度お願いします. Salah karena pura-pura ngerti jauh lebih fatal.", dark=True),
 check("SCREENSHOT INI", "Checklist hari pertama:", ["Datang 10 menit lebih awal", "Salam おはようございます duluan", "Bawa memo & pulpen", "Nggak ngerti → minta ulang", "Selesai → lapor 終わりました"]),
 cta("Dari 8 kalimat tadi, kamu udah hafal berapa?", "Jawab angkanya di komen. Kirim ke temen yang lagi di LPK."),
],
"cs17-indonesia": [
 cover(CS, "Ditanya orang Jepang " + PINK.format("“dari mana?”") + ", jawab gini.", "8 kalimat buat cerita soal Indonesia."),
 text("Orang Jepang paling sering kenal " + R.format("Bali.") , "Mulai dari situ, terus ceritain kotamu. Obrolan langsung jalan."),
 vocab("DITANYA ASAL", [("どこから来ましたか？", "doko kara kimashita ka", "Dari mana?"), ("インドネシアから来ました", "indoneshia kara kimashita", "Dari Indonesia"), ("ジャカルタ出身です", "jakaruta shusshin desu", "Asal Jakarta"), ("バリ島、知っていますか？", "baritou, shitte imasu ka", "Tahu Bali?")]),
 vocab("CERITA INDONESIA", [("インドネシアは暑いです", "indoneshia wa atsui desu", "Indonesia panas"), ("島がたくさんあります", "shima ga takusan arimasu", "Pulaunya banyak banget"), ("ナシゴレンがおいしいです", "nashigoren ga oishii desu", "Nasi goreng enak"), ("日本に来るのが夢でした", "nihon ni kuru no ga yume deshita", "Ke Jepang itu mimpiku")]),
 text("Ganti " + PINK.format("ジャカルタ") + " pakai kotamu.", "スラバヤ (Surabaya), バンドン (Bandung), メダン (Medan), ジョグジャカルタ (Yogyakarta).", dark=True),
 cta("Kamu dari kota mana?", "Jawab 1 kata di komen."),
],
"ck01-winter": [
 cover("CHECKLIST", "Winter pertama di Jepang? " + PINK.format("Bawa 8 barang ini."), "Plus nama Jepangnya, biar gampang nyari di toko."),
 text("Buat orang tropis, dingin Jepang " + R.format("kerasa banget."), "Kuncinya pakai baju berlapis, bukan cuma 1 jaket tebal."),
 vocab("PAKAIAN", [("肌着", "hadagi", "Baju dalam (lapisan 1)"), ("ダウン", "daun", "Jaket puffer"), ("手袋", "tebukuro", "Sarung tangan"), ("マフラー", "mafuraa", "Syal")]),
 vocab("PERLENGKAPAN", [("カイロ", "kairo", "Penghangat tempel"), ("リップクリーム", "rippu kuriimu", "Lip balm"), ("加湿器", "kashitsuki", "Pelembap udara"), ("滑り止め", "suberidome", "Anti-licin (sepatu)")]),
 text("Kairo murah di konbini & drugstore. " + PINK.format("Jangan tempel langsung ke kulit."), "Tempel di luar baju dalam. Kalau kelamaan nempel di kulit bisa melepuh.", dark=True),
 check("SCREENSHOT INI", "Checklist winter:", ["Baju dalam + jaket puffer", "Sarung tangan + syal", "Kairo + lip balm", "Pelembap udara", "Sepatu anti-licin"], dark=False),
 cta("Kamu lebih tahan yang mana?", "A. Panas  B. Dingin. Jawab A/B di komen."),
],
"cs18-minta-tolong": [
 cover(CS, "Mau minta " + PINK.format("difotoin") + " orang Jepang? Pakai kalimat ini.", "8 kalimat buat minta tolong dengan sopan."),
 text("Orang Jepang umumnya mau bantu, asal " + R.format("dimulai dengan sopan."), "Buka pakai すみません (sumimasen) dulu, baru minta tolong."),
 vocab("MINTA TOLONG", [("写真を撮ってもらえますか？", "shashin o totte moraemasu ka", "Bisa tolong fotoin?"), ("一緒に写真いいですか？", "issho ni shashin ii desu ka", "Boleh foto bareng?"), ("ちょっと手伝ってもらえますか？", "chotto tetsudatte moraemasu ka", "Bisa bantu sebentar?"), ("駅への行き方を教えてください", "eki e no ikikata o oshiete kudasai", "Tolong kasih tahu jalan ke stasiun")]),
 vocab("SESUDAHNYA", [("もう一回いいですか？", "mou ikkai ii desu ka", "Sekali lagi boleh?"), ("これでいいですか？", "kore de ii desu ka", "Gini udah bener?"), ("助かりました", "tasukarimashita", "Ngebantu banget"), ("本当にありがとうございます", "hontou ni arigatou gozaimasu", "Makasih banyak")]),
 text("Ganti " + PINK.format("駅") + " (eki) pakai tujuanmu.", "ホテル (hoteru) = hotel, トイレ (toire) = toilet, コンビニ (konbini).", dark=True),
 cta("Kamu lebih sering yang mana?", "A. Minta difotoin  B. Nanya jalan. Jawab A/B."),
],
}
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':1080,'height':1350})
        for name, slides in POSTS.items():
            d = f"/home/claude/msr-carousel/nanihongo-{name}"; os.makedirs(d, exist_ok=True)
            for i, body in enumerate(slides, 1):
                await pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head>{body}</html>")
                await pg.wait_for_timeout(150)
                await pg.screenshot(path=f"{d}/s{i}.jpg", type='jpeg', quality=92)
        await b.close()
asyncio.run(main())
from PIL import Image
os.makedirs("/tmp/claude-0/sheets", exist_ok=True)
for name, slides in POSTS.items():
    n=len(slides); ims=[Image.open(f"/home/claude/msr-carousel/nanihongo-{name}/s{i}.jpg").resize((360,450)) for i in range(1,n+1)]
    c=Image.new('RGB',(360*4,900),'white')
    for k,im in enumerate(ims): c.paste(im,((k%4)*360,(k//4)*450))
    c.save(f"/tmp/claude-0/sheets/{name}.jpg")
print("ok")
