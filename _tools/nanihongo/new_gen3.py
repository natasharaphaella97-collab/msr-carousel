import asyncio, os, json
src = open("/home/claude/nanihongo/cs/gen2.py").read().split('CS = "CHEAT SHEET"')[0]
ns = {}; exec(src, ns)
CSS, cover, text, cta, vocab = ns['CSS'], ns['cover'], ns['text'], ns['cta'], ns['vocab']
g = {}; exec(open("/home/claude/nanihongo/batch/gen.py").read().split('T = "KERJA')[0], g)
rows, big = g['rows'], g['big']
R = "<span class='red'>{}</span>"; PINK = "<span style='color:#FF4D5E'>{}</span>"; J = "<span class='jp'>{}</span>"
CS = "CHEAT SHEET"
POSTS = {
"cs10-basabasi": [
 cover(CS, "Kenalan udah. Sekarang " + PINK.format("basa-basi ala Jepang."), "8 kalimat pembuka obrolan yang aman."),
 text("Orang Jepang jarang langsung nanya hal pribadi.", "Obrolan biasanya dibuka pakai " + R.format("cuaca dan hal ringan.")),
 vocab("SOAL CUACA", [("今日は暑いですね", "kyou wa atsui desu ne", "Hari ini panas ya"), ("寒いですね", "samui desu ne", "Dingin ya"), ("いい天気ですね", "ii tenki desu ne", "Cuacanya cerah ya"), ("雨が多いですね", "ame ga ooi desu ne", "Sering hujan ya")]),
 vocab("HAL RINGAN", [("日本はどうですか？", "nihon wa dou desu ka", "Gimana Jepang? (sering ditanya)"), ("楽しいです！", "tanoshii desu", "Seru!"), ("週末は何をしますか？", "shuumatsu wa nani o shimasu ka", "Weekend ngapain?"), ("おすすめの場所は？", "osusume no basho wa", "Ada tempat rekomendasi?")]),
 text("Kuncinya di akhiran " + PINK.format("〜ね") + " (ne).", "Artinya “ya kan?”. Ngajak lawan bicara setuju, obrolan jadi jalan.", dark=True),
 cta("Cuaca di kotamu sekarang: 暑い atau 寒い?", "Jawab 1 kata di komen."),
],
"cs11-aizuchi": [
 cover(CS, "Biar kedengeran " + PINK.format("nyambung") + " pas ngobrol sama orang Jepang.", "8 respon pendek yang wajib hafal."),
 text("Orang Jepang kasih respon " + R.format("tiap beberapa detik."), "Namanya " + J.format("相づち") + " (aizuchi). Diam aja bisa dikira nggak dengerin."),
 vocab("SETUJU & NGERTI", [("そうですね", "sou desu ne", "Iya ya / betul"), ("なるほど", "naruhodo", "Oh gitu (paham)"), ("たしかに", "tashika ni", "Bener juga"), ("そうそう", "sou sou", "Iya iya! (santai)")]),
 vocab("KAGET & KAGUM", [("そうなんですか？", "sou nan desu ka", "Oh ya? Masa?"), ("本当ですか？", "hontou desu ka", "Beneran?"), ("すごい！", "sugoi", "Keren!"), ("いいですね！", "ii desu ne", "Asik tuh!")]),
 text("Ngobrol sama atasan? Lebih aman pakai " + PINK.format(J.format("そうなんですね")), "(sou nan desu ne) = Oh, begitu ya. Sopan dan tetap nyambung.", dark=True),
 cta("Kamu paling sering bilang yang mana?", "A. なるほど  B. すごい. Jawab A/B di komen."),
],
"cs12-pujian": [
 cover(CS, "Dibilang " + PINK.format("“nihongo jouzu”") + ", jawab apa?", "8 kalimat buat muji & balas pujian."),
 text("Orang Jepang suka muji, tapi " + R.format("jarang terima pujian mentah-mentah."), "Biasanya dibalas merendah. Ini cara muji dan cara balasnya."),
 vocab("MUJI ORANG", [("日本語が上手ですね", "nihongo ga jouzu desu ne", "Bahasa Jepangmu bagus ya"), ("おしゃれですね", "oshare desu ne", "Stylish ya"), ("優しいですね", "yasashii desu ne", "Baik banget ya"), ("写真が上手ですね", "shashin ga jouzu desu ne", "Jago foto ya")]),
 vocab("BALAS PUJIAN", [("いえいえ、まだまだです", "ie ie, madamada desu", "Ah nggak, masih belajar"), ("そんなことないです", "sonna koto nai desu", "Ah nggak juga kok"), ("ありがとうございます", "arigatou gozaimasu", "Makasih!"), ("うれしいです", "ureshii desu", "Seneng dengernya")]),
 text("Jawaban paling aman: " + PINK.format(J.format("まだまだです")), "Sambil senyum. Merendah itu sopan di Jepang, tapi bilang makasih juga nggak salah.", dark=True),
 cta("Pernah dipuji orang Jepang?", "Jawab YA atau BELUM di komen."),
],
"cs13-ngajak": [
 cover(CS, "Mau ngajak " + PINK.format("jalan bareng") + " temen Jepang?", "8 kalimat buat ngajak & bikin janji."),
 text("Orang Jepang jarang nolak langsung.", "Kalau jawabnya " + R.format("“chotto…”") + ", biasanya artinya nggak bisa."),
 vocab("NGAJAK", [("一緒に行きませんか？", "issho ni ikimasen ka", "Mau pergi bareng?"), ("ご飯に行きませんか？", "gohan ni ikimasen ka", "Makan bareng yuk?"), ("いつが空いていますか？", "itsu ga aite imasu ka", "Kapan kosong?"), ("どこで会いますか？", "doko de aimasu ka", "Ketemu di mana?")]),
 vocab("JAWABAN", [("いいですね！行きましょう", "ii desu ne! ikimashou", "Asik! Ayo"), ("土曜日は大丈夫です", "doyoubi wa daijoubu desu", "Sabtu bisa"), ("その日はちょっと…", "sono hi wa chotto", "Hari itu agak… (nggak bisa)"), ("また今度", "mata kondo", "Lain kali ya")]),
 text("Dapat jawaban " + PINK.format(J.format("ちょっと…")) + "? Jangan dipaksa.", "Bilang aja また今度 (mata kondo). Obrolan tetap enak.", dark=True),
 cta("Diajak makan bareng orang Jepang, kamu jawab apa?", "A. 行きましょう  B. ちょっと… Jawab A/B."),
],
"cs14-pamitan": [
 cover(CS, "Jangan cuma bilang " + PINK.format("“sayonara”."), "8 kalimat pamitan yang lebih natural."),
 text("Sayonara kesannya " + R.format("kayak pisah lama."), "Ke temen atau orang yang bakal ketemu lagi, pakai ini."),
 vocab("KE TEMEN", [("じゃあね", "jaa ne", "Dah ya"), ("またね", "mata ne", "Sampai nanti"), ("また明日", "mata ashita", "Sampai besok"), ("気をつけて", "ki o tsukete", "Hati-hati ya")]),
 vocab("LEBIH SOPAN", [("今日は楽しかったです", "kyou wa tanoshikatta desu", "Hari ini seru banget"), ("ありがとうございました", "arigatou gozaimashita", "Makasih buat tadi"), ("また会いましょう", "mata aimashou", "Ketemu lagi ya"), ("お先に失礼します", "osaki ni shitsurei shimasu", "Aku pulang duluan")]),
 text("Pulang kerja duluan? Wajib bilang " + PINK.format(J.format("お先に失礼します")), "Balasan rekan kerja: <span class='jp' style='font-weight:700'>お疲れさまでした</span> (otsukaresama deshita).", dark=True),
 cta("Kata pamitan favoritmu?", "A. じゃあね  B. またね. Jawab A/B di komen."),
],
"bp02-kaigo": [
 cover("PERAWAT LANSIA 介護", "Jepang butuh " + PINK.format("±570 ribu") + " perawat lansia lagi.", "Siapa yang bakal ngisi?"),
 text("Lansia di Jepang makin banyak, yang ngerawat " + R.format("nggak cukup."), "Kementerian Kesehatan Jepang (MHLW) sudah hitung berapa perawat lansia (" + J.format("介護職員") + ") yang dibutuhkan."),
 big("TAHUN 2022", "±2,15 jt", "perawat lansia di Jepang", "Itu jumlah yang sudah kerja sekarang."),
 big("TAHUN 2040", "±2,72 jt", "yang dibutuhkan", "Kurang ±570 ribu orang. Rata-rata harus nambah ±32 ribu per tahun."),
 big("SSW BIDANG KAIGO", "74.745", "pekerja SSW perawat lansia", "Bidang SSW terbanyak ke-2 (Maret 2026, data sementara)."),
 text("Kaigo bukan cuma kuat fisik. Kuncinya " + PINK.format("bahasa Jepang."), "Kamu harus bisa ngobrol sama lansia setiap hari. Makanya syarat bahasanya lebih tinggi dari bidang lain.", dark=True),
 cta("Kalau kerja di Jepang, kamu pilih yang mana?", "A. Perawat lansia  B. Pabrik. Jawab A/B di komen."),
],
"rm02-jlpt-n4": [
 cover("ROADMAP BELAJAR", "Shortcut lulus " + PINK.format("JLPT N4") + " dari nol.", "Salah satu syarat bahasa buat SSW (Tokutei Ginou)."),
 rows("KENALAN DULU SAMA TESNYA", [("Format", "", "tes kertas"), ("Jadwal di Indonesia", "", "Juli & Des"), ("Skor total", "", "0–180"), ("Lulus", "", "min. 90")]),
 text("Ada " + R.format("nilai minimum") + " tiap bagian.", "Kosakata, tata bahasa & membaca: min. 38 dari 120.", "Listening: min. 19 dari 60. Total tinggi tapi listening jeblok = tetap gagal."),
 rows("SHORTCUT 4 LANGKAH", [("Beresin materi N5 dulu", "N5の復習", "1"), ("Kanji & kosakata tiap hari", "漢字・語彙", "2"), ("Tata bahasa + listening", "文法・聴解", "3"), ("Latihan soal resmi berwaktu", "公式問題集", "4")]),
 text("N4 atau <span style='white-space:nowrap'>JFT-Basic?</span> " + PINK.format("<span style='white-space:nowrap'>Dua-duanya</span> diterima") + " buat syarat bahasa SSW.", "JLPT cuma 2x setahun. Jangan sampai ketinggalan pendaftarannya.", dark=True),
 cta("Kamu sekarang di level mana?", "Jawab: NOL, N5, atau N4 di komen."),
],
"jb01-harga-makan": [
 cover("HARGA DI JEPANG 2026", "Kerja 1 jam di Jepang = " + PINK.format("2 mangkok gyudon."), "Harga makan sehari-hari, buat traveler & calon pekerja."),
 text("Upah minimum rata-rata Jepang sekarang " + R.format("¥1.177/jam."), "Biar kebayang, kita bandingin sama makanan yang paling sering dibeli."),
 big("GYUDON SUKIYA", "¥480", "porsi biasa (namimori)", "Naik ¥30 sejak Juli 2026. Masih salah satu makan kenyang termurah."),
 rows("HARGA MAKAN (KIRA-KIRA)", [("Onigiri konbini", "おにぎり", "±¥150–200"), ("Bento konbini", "弁当", "±¥500–700"), ("Gyudon", "牛丼", "¥480"), ("Ramen di kedai", "ラーメン", "±¥900–1.200")]),
 text("Makan 3x sehari di luar ≈ " + R.format("<span style='white-space:nowrap'>±¥2.000/hari.</span>"), "Liburan 7 hari: ±¥14rb ≈ Rp1,6 juta, cuma buat makan."),
 text("Buat pekerja: " + PINK.format("masak sendiri") + " jauh lebih hemat.", "Makan sebulan bisa ±¥30–40rb kalau rajin masak.", dark=True),
 cta("Tebak: 1 mangkok ramen = kerja berapa menit?", "Jawab angkanya di komen."),
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
for name, slides in POSTS.items():
    n=len(slides); ims=[Image.open(f"/home/claude/msr-carousel/nanihongo-{name}/s{i}.jpg").resize((360,450)) for i in range(1,n+1)]
    c=Image.new('RGB',(360*4,900),'white')
    for k,im in enumerate(ims): c.paste(im,((k%4)*360,(k//4)*450))
    c.save(f"/tmp/claude-0/cs_{name}.jpg")
