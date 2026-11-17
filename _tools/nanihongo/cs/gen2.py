import asyncio, os, json, sys
sys.path.insert(0, '/home/claude/nanihongo/batch')
import importlib.util
spec = importlib.util.spec_from_file_location("g", "/home/claude/nanihongo/batch/gen.py")
src = open("/home/claude/nanihongo/batch/gen.py").read().split("T = \"KERJA")[0]
ns = {}; exec(src, ns)
CSS, cover, text, cta = ns['CSS'], ns['cover'], ns['text'], ns['cta']
R = "<span class='red'>{}</span>"; PINK = "<span style='color:#FF4D5E'>{}</span>"
CSS += """
.vr{display:flex;justify-content:space-between;align-items:center;gap:30px;border-bottom:3px solid #1B2340;padding:26px 0}
.vr .j{font-family:'Noto Sans CJK JP';font-weight:900;font-size:50px;line-height:1.15}
.vr .ro{font-size:32px;font-weight:700;color:#C8102E;margin-top:4px}
.vr .m{font-size:36px;font-weight:700;text-align:right;max-width:36%;line-height:1.2}
.vr>div:first-child{flex:1 1 auto}
.num{font-weight:900;font-size:170px;line-height:1;color:#FF4D5E}
"""
def vocab(tag, items):
    fs = lambda j: 50 if len(j)<=8 else (42 if len(j)<=11 else 36)
    r = "".join(f"<div class='vr'><div><div class='j' style='font-size:{fs(j)}px;white-space:nowrap'>{j}</div><div class='ro'>{ro}</div></div><div class='m'>{m}</div></div>" for j, ro, m in items)
    return f"<body><div class='pad' style='top:150px'><span class='tag'>{tag}</span><div style='margin-top:20px'>{r}</div></div></body>"
def nums():
    return """<body class='cover'><div class='pad' style='top:200px'><span class='tag'>NOMOR DARURAT JEPANG</span>
<div style='display:flex;gap:80px;margin-top:60px'><div><div class='num'>110</div><div class='p' style='color:#fff;font-weight:800'>Polisi</div></div>
<div><div class='num'>119</div><div class='p' style='color:#fff;font-weight:800'>Ambulans &amp; pemadam</div></div></div>
<div class='p' style='color:#cfd5e6'>Gratis, bisa dari HP mana pun.</div></div></body>"""

CS = "CHEAT SHEET"
POSTS = {
"cs01-halal": ("2026-11-18", [
 cover(CS, "Nggak makan babi? Hafalin " + PINK.format("8 kata ini") + " di Jepang.", "Babi sering ngumpet di kaldu & bumbu."),
 text("Babi di Jepang nggak selalu kelihatan.", "Sering ada di " + R.format("kaldu, bumbu, dan topping.") + " Cek kata-kata ini di menu dan label."),
 vocab("CEK DI MENU", [("豚肉", "butaniku", "daging babi"), ("豚骨", "tonkotsu", "kaldu tulang babi"), ("チャーシュー", "chaashuu", "babi panggang (topping ramen)"), ("ラード", "raado", "lemak babi")]),
 vocab("CEK DI LABEL", [("ハム・ベーコン", "hamu, beekon", "ham, bacon"), ("ゼラチン", "zerachin", "gelatin, sering dari babi"), ("みりん", "mirin", "bumbu manis, ada alkohol"), ("料理酒", "ryourishu", "sake untuk masak")]),
 text("Paling aman: cari tulisan " + PINK.format("ハラール") + " (haraaru).", "Atau tanya langsung: <span class='jp' style='color:#fff'>豚肉は入っていますか？</span> (Ada babinya?)", dark=True),
 cta("Kata mana yang baru kamu tahu?"),
], "Nggak makan babi atau alkohol? Hafalin 8 kata ini sebelum ke Jepang, karena babi sering ngumpet di kaldu dan bumbu.\n\nDi menu:\n豚肉 (butaniku) = daging babi\n豚骨 (tonkotsu) = kaldu tulang babi\nチャーシュー (chaashuu) = babi panggang, topping ramen\nラード (raado) = lemak babi\n\nDi label:\nハム・ベーコン (hamu, beekon) = ham, bacon\nゼラチン (zerachin) = gelatin, sering dari babi\nみりん (mirin) = bumbu manis, ada alkoholnya\n料理酒 (ryourishu) = sake untuk masak\n\nPaling aman cari tulisan ハラール (haraaru), atau tanya: 豚肉は入っていますか？\n\nSave buat liburan nanti. Kata mana yang baru kamu tahu?\n\n#belajarbahasajepang #nihongo #halaljapan"),
"cs02-kenalan": ("2026-11-19", [
 cover(CS, "Udah bilang hajimemashite. " + PINK.format("Terus ngomong apa?"), "8 kalimat biar obrolan nggak mati."),
 text("Kenalan itu gampang. " + R.format("Lanjutin obrolannya") + " yang susah.", "Ini kalimat buat nanya balik, cerita soal kamu, dan minta diulang."),
 vocab("NANYA BALIK", [("お仕事は何ですか？", "oshigoto wa nan desu ka", "Kerjanya apa?"), ("趣味は何ですか？", "shumi wa nan desu ka", "Hobinya apa?"), ("日本は初めてです。", "nihon wa hajimete desu", "Pertama kali ke Jepang."), ("日本語を勉強しています。", "nihongo o benkyou shite imasu", "Lagi belajar bahasa Jepang.")]),
 vocab("KALAU BINGUNG", [("日本語が少しできます。", "nihongo ga sukoshi dekimasu", "Bisa sedikit."), ("もう一度お願いします。", "mou ichido onegai shimasu", "Tolong ulangi."), ("ゆっくり話してください。", "yukkuri hanashite kudasai", "Tolong pelan-pelan."), ("インスタ、交換しませんか？", "insuta, koukan shimasen ka", "Tukeran IG yuk?")]),
 text("Kalimat paling penting: " + PINK.format("もう一度お願いします"), "Minta diulang itu sopan. Lebih baik daripada pura-pura ngerti.", dark=True),
 cta("趣味は何ですか？ Jawab pakai hobimu di komen."),
], "Udah bilang hajimemashite, terus apa? Ini 8 kalimat biar obrolan nggak mati.\n\nNanya balik:\nお仕事は何ですか？(oshigoto wa nan desu ka) = Kerjanya apa?\n趣味は何ですか？(shumi wa nan desu ka) = Hobinya apa?\n日本は初めてです。(nihon wa hajimete desu) = Ini pertama kali ke Jepang.\n日本語を勉強しています。(nihongo o benkyou shite imasu) = Lagi belajar bahasa Jepang.\n\nKalau bingung:\n日本語が少しできます。(nihongo ga sukoshi dekimasu) = Bisa sedikit.\nもう一度お願いします。(mou ichido onegai shimasu) = Tolong ulangi.\nゆっくり話してください。(yukkuri hanashite kudasai) = Tolong pelan-pelan.\nインスタ、交換しませんか？(insuta, koukan shimasen ka) = Tukeran IG yuk?\n\nSave dulu. 趣味は何ですか？ Jawab pakai hobimu di komen.\n\n#belajarbahasajepang #nihongo #bahasajepang"),
"cs03-konbini": ("2026-11-20", [
 cover(CS, "Kosakata konbini biar " + PINK.format("nggak bengong") + " di kasir.", "8 kata yang pasti keluar."),
 text("Kasir konbini ngomongnya " + R.format("cepet banget."), "Tapi yang ditanya itu-itu aja. Hafalin ini, pasti nyambung."),
 vocab("YANG DITANYA KASIR", [("温めますか？", "atatamemasu ka", "Mau dipanasin?"), ("袋", "fukuro", "kantong plastik"), ("お箸", "ohashi", "sumpit"), ("スプーン", "supuun", "sendok")]),
 vocab("PAS BAYAR", [("ポイントカード", "pointo kaado", "kartu poin"), ("レシート", "reshiito", "struk"), ("現金", "genkin", "tunai"), ("電子マネー", "denshi manee", "e-money / kartu IC")]),
 text("Ditanya kartu poin? Jawab aja " + PINK.format("ないです") + " (nai desu).", "Artinya: nggak punya. Selesai.", dark=True),
 cta("Konbini favoritmu: 7-Eleven, Lawson, atau FamilyMart?"),
], "Kasir konbini ngomongnya cepet, tapi yang ditanya itu-itu aja. Hafalin 8 kata ini:\n\nYang ditanya kasir:\n温めますか？(atatamemasu ka) = Mau dipanasin?\n袋 (fukuro) = kantong plastik\nお箸 (ohashi) = sumpit\nスプーン (supuun) = sendok\n\nPas bayar:\nポイントカード (pointo kaado) = kartu poin\nレシート (reshiito) = struk\n現金 (genkin) = tunai\n電子マネー (denshi manee) = e-money / kartu IC\n\nDitanya kartu poin? Jawab aja ないです (nai desu) = nggak punya.\n\nSave buat liburan nanti. Konbini favoritmu yang mana?\n\n#belajarbahasajepang #nihongo #japantravel"),
"cs04-angka": ("2026-11-21", [
 cover(CS, "Kasir bilang “happyaku en”. " + PINK.format("Itu berapa?"), "Angka Jepang yang sering bikin salah."),
 text("Angka Jepang sebenarnya gampang.", "Tapi ada beberapa yang " + R.format("bunyinya berubah.") + " Ini yang paling sering keluar di kasir."),
 vocab("RATUSAN", [("百", "hyaku", "100"), ("三百", "sanbyaku", "300"), ("六百", "roppyaku", "600"), ("八百", "happyaku", "800")]),
 vocab("RIBUAN", [("千", "sen", "1.000"), ("三千", "sanzen", "3.000"), ("八千", "hassen", "8.000"), ("一万", "ichiman", "10.000")]),
 text("Jepang ngitung per " + PINK.format("万") + " (10.000), bukan per 1.000.", "20.000 yen = 二万 (niman). Bukan “nijuu sen”.", dark=True),
 cta("Coba tebak: 五千円 itu berapa? Jawab di komen."),
], "Kasir bilang \"happyaku en\", itu berapa? Ini angka Jepang yang bunyinya suka berubah:\n\n百 (hyaku) = 100\n三百 (sanbyaku) = 300\n六百 (roppyaku) = 600\n八百 (happyaku) = 800\n千 (sen) = 1.000\n三千 (sanzen) = 3.000\n八千 (hassen) = 8.000\n一万 (ichiman) = 10.000\n\nJepang ngitung per 万 (10.000), bukan per 1.000. Jadi 20.000 yen = 二万 (niman).\n\nSave dulu. Coba tebak: 五千円 itu berapa? Jawab di komen.\n\n#belajarbahasajepang #nihongo #bahasajepang"),
"cs05-tanda": ("2026-11-22", [
 cover(CS, "Nggak bisa baca kanji? Hafalin " + PINK.format("8 tanda ini."), "Biar nggak nyasar di stasiun & toko."),
 text("Kamu nggak perlu hafal ribuan kanji.", "Cukup " + R.format("tanda yang muncul tiap hari") + " di stasiun, pintu, dan restoran."),
 vocab("DI STASIUN", [("入口", "iriguchi", "pintu masuk"), ("出口", "deguchi", "pintu keluar"), ("改札", "kaisatsu", "gerbang tiket"), ("乗換", "norikae", "pindah kereta")]),
 vocab("DI PINTU & TOKO", [("押", "osu", "dorong"), ("引", "hiku", "tarik"), ("営業中", "eigyouchuu", "buka"), ("準備中", "junbichuu", "lagi persiapan (tutup)")]),
 text(PINK.format("準備中") + " di depan restoran = belum buka.", "Bukan “lagi masak”. Datang lagi nanti ya.", dark=True),
 cta("Kanji mana yang paling sering kamu lihat di anime?"),
], "Nggak perlu hafal ribuan kanji. Cukup 8 tanda yang muncul tiap hari:\n\nDi stasiun:\n入口 (iriguchi) = pintu masuk\n出口 (deguchi) = pintu keluar\n改札 (kaisatsu) = gerbang tiket\n乗換 (norikae) = pindah kereta\n\nDi pintu & toko:\n押 (osu) = dorong\n引 (hiku) = tarik\n営業中 (eigyouchuu) = buka\n準備中 (junbichuu) = lagi persiapan, belum buka\n\nSave buat liburan nanti. Kanji mana yang paling sering kamu lihat?\n\n#belajarbahasajepang #nihongo #japantravel"),
"cs06-darurat": ("2026-11-23", [
 cover(CS, "Simpan ini sebelum ke Jepang. " + PINK.format("Semoga nggak kepake."), "Kalimat darurat paling penting."),
 text("Pas panik, bahasa Jepangmu " + R.format("bakal hilang semua."), "Makanya simpan sekarang, bukan nanti."),
 vocab("MINTA TOLONG", [("助けて！", "tasukete", "Tolong!"), ("道に迷いました。", "michi ni mayoimashita", "Aku nyasar."), ("財布をなくしました。", "saifu o nakushimashita", "Dompetku hilang."), ("気分が悪いです。", "kibun ga warui desu", "Aku nggak enak badan.")]),
 vocab("CARI BANTUAN", [("病院はどこですか？", "byouin wa doko desu ka", "Rumah sakit di mana?"), ("救急車を呼んでください。", "kyuukyuusha o yonde kudasai", "Tolong panggil ambulans."), ("警察", "keisatsu", "polisi"), ("交番", "kouban", "pos polisi kecil")]),
 nums(),
 cta("Share ke temen yang mau ke Jepang.", "Atau tulis di komen: kamu berangkat kapan?"),
], "Simpan ini sebelum ke Jepang. Semoga nggak kepake.\n\nMinta tolong:\n助けて！(tasukete) = Tolong!\n道に迷いました。(michi ni mayoimashita) = Aku nyasar.\n財布をなくしました。(saifu o nakushimashita) = Dompetku hilang.\n気分が悪いです。(kibun ga warui desu) = Aku nggak enak badan.\n\nCari bantuan:\n病院はどこですか？(byouin wa doko desu ka) = Rumah sakit di mana?\n救急車を呼んでください。(kyuukyuusha o yonde kudasai) = Tolong panggil ambulans.\n警察 (keisatsu) = polisi\n交番 (kouban) = pos polisi kecil\n\nNomor darurat Jepang: 110 polisi, 119 ambulans & pemadam.\n\nShare ke temen yang mau ke Jepang.\n\n#belajarbahasajepang #nihongo #japantravel"),
"cs07-sumimasen": ("2026-11-24", [
 cover(CS, "1 kata, 3 arti: " + PINK.format("<span class='jp'>すみません</span>"), "Kata paling kepake di Jepang."),
 text("Orang Jepang bisa bilang " + R.format("sumimasen") + " puluhan kali sehari.", "Artinya tergantung situasi. Ini 3 yang paling sering."),
 vocab("3 ARTI SUMIMASEN", [("すみません！", "manggil pelayan", "Permisi!"), ("あ、すみません。", "nyenggol orang", "Maaf."), ("わざわざすみません。", "wazawaza sumimasen", "Makasih udah repot-repot.")]),
 vocab("TEMAN-TEMANNYA", [("どうも", "doumo", "makasih (santai)"), ("お願いします", "onegai shimasu", "tolong / mohon"), ("大丈夫です", "daijoubu desu", "nggak apa-apa / nggak usah")]),
 text("Bingung mau ngomong apa? " + PINK.format("Sumimasen") + " hampir selalu aman.", "Buat manggil, minta maaf, atau bilang makasih.", dark=True),
 cta("Kata Jepang apa yang paling sering kamu pakai?"),
], "1 kata, 3 arti: すみません (sumimasen).\n\nすみません！= Permisi! (manggil pelayan)\nあ、すみません。= Maaf. (nyenggol orang)\nわざわざすみません。(wazawaza sumimasen) = Makasih udah repot-repot.\n\nTeman-temannya:\nどうも (doumo) = makasih, santai\nお願いします (onegai shimasu) = tolong / mohon\n大丈夫です (daijoubu desu) = nggak apa-apa / nggak usah\n\nBingung mau ngomong apa? Sumimasen hampir selalu aman.\n\nSave dulu. Kata Jepang apa yang paling sering kamu pakai?\n\n#belajarbahasajepang #nihongo #bahasajepang"),
"cs08-restoran": ("2026-11-25", [
 cover(CS, "Udah bisa pesan ramen. " + PINK.format("Ini level berikutnya."), "8 kalimat restoran yang jarang diajarin."),
 text("Pesan makanan itu level 1.", "Level 2: " + R.format("tanya rekomendasi, minta air, minta dibungkus.")),
 vocab("SEBELUM PESAN", [("おすすめは何ですか？", "osusume wa nan desu ka", "Rekomendasinya apa?"), ("英語のメニューはありますか？", "eigo no menyuu wa arimasu ka", "Ada menu Inggris?"), ("これは辛いですか？", "kore wa karai desu ka", "Ini pedas nggak?"), ("大盛り", "oomori", "porsi besar")]),
 vocab("PAS MAKAN", [("お水をください。", "omizu o kudasai", "Minta air putih."), ("取り皿をください。", "torizara o kudasai", "Minta piring kecil."), ("持ち帰りできますか？", "mochikaeri dekimasu ka", "Bisa dibungkus?"), ("食券", "shokken", "tiket makan")]),
 text("Banyak kedai ramen pakai " + PINK.format("食券機") + " (shokkenki).", "Bayar di mesin dulu, kasih tiketnya ke koki.", dark=True),
 cta("Kamu lebih suka ramen atau sushi?"),
], "Udah bisa pesan ramen? Ini level berikutnya.\n\nSebelum pesan:\nおすすめは何ですか？(osusume wa nan desu ka) = Rekomendasinya apa?\n英語のメニューはありますか？(eigo no menyuu wa arimasu ka) = Ada menu bahasa Inggris?\nこれは辛いですか？(kore wa karai desu ka) = Ini pedas nggak?\n大盛り (oomori) = porsi besar\n\nPas makan:\nお水をください。(omizu o kudasai) = Minta air putih.\n取り皿をください。(torizara o kudasai) = Minta piring kecil buat sharing.\n持ち帰りできますか？(mochikaeri dekimasu ka) = Bisa dibungkus?\n食券 (shokken) = tiket makan\n\nBanyak kedai ramen pakai 食券機 (shokkenki): bayar di mesin dulu, kasih tiketnya ke koki.\n\nSave buat liburan nanti. Ramen atau sushi?\n\n#belajarbahasajepang #nihongo #japantravel"),
}

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        meta = {}
        for name, (date, slides, cap) in POSTS.items():
            d = f"/home/claude/nanihongo/cs/{name}"; os.makedirs(d, exist_ok=True)
            for i, body in enumerate(slides, 1):
                await pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head>{body}</html>")
                await pg.wait_for_timeout(150)
                await pg.screenshot(path=f"{d}/s{i}.png")
            meta[name] = {"date": date, "n": len(slides), "caption": cap}
        await b.close()
        json.dump(meta, open('/home/claude/nanihongo/cs/meta.json', 'w'), ensure_ascii=False)
asyncio.run(main())
