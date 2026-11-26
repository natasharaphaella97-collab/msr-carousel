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
def img(n): return "data:image/jpeg;base64,"+base64.b64encode(open(f"/home/claude/nanihongo/photos/p_{n}.jpg","rb").read()).decode()
def pcover(n, tag, head, sub):
    return f"<body class='cover'><img class='full' src='{img(n)}'><div class='ov'></div><div class='pad' style='top:250px'><span class='tag'>{tag}</span><div class='h1'>{head}</div><div class='p' style='color:#e3e7f2'>{sub}</div></div></body>"
def check(tag, head, items, dark=True):
    r = "".join(f"<div style='display:flex;gap:22px;align-items:center;font-size:44px;font-weight:800;padding:18px 0;border-bottom:3px solid {'#F6F1E7' if dark else '#1B2340'}'><span style='color:#FF4D5E;font-size:50px'>✓</span>{i}</div>" for i in items)
    return f"<body{' class=cover' if dark else ''}><div class='pad' style='top:150px'><span class='tag'>{tag}</span><div class='h2' style='margin-top:30px;font-size:70px'>{head}</div><div style='margin-top:20px'>{r}</div></div></body>"

POSTS = {
"kj02-kanji-bahaya": [
 cover("KERJA DI JEPANG", "8 kanji ini " + PINK.format("nempel di tembok") + " tempat kerjamu.", "Nggak bisa baca = bisa celaka. Hafalin sebelum berangkat."),
 text("Instruksi bisa ditanya. Tapi " + R.format("papan peringatan") + " nggak nunggu kamu ngerti.", "Pabrik, gudang, dapur, proyek: kanji ini muncul di mana-mana."),
 vocab("BAHAYA & LARANGAN", [("危険", "kiken", "Bahaya"), ("注意", "chuui", "Hati-hati"), ("禁止", "kinshi", "Dilarang"), ("立入禁止", "tachiiri kinshi", "Dilarang masuk")]),
 vocab("API & DARURAT", [("火気厳禁", "kaki genkin", "Dilarang ada api"), ("非常口", "hijouguchi", "Pintu darurat"), ("消火器", "shoukaki", "Alat pemadam (APAR)"), ("安全第一", "anzen daiichi", "Utamakan keselamatan")]),
 text("Lihat " + PINK.format(J.format("禁止")) + "? Itu kuncinya.", "Kata apa pun + 禁止 = dilarang. 撮影禁止 (satsuei kinshi) = dilarang foto.", dark=True),
 check("SCREENSHOT INI", "Checklist minggu pertama:", ["Cari letak 非常口 & 消火器", "Ingat area 立入禁止", "Foto papan yang belum paham", "Nggak yakin → tanya senpai", "Lihat 危険 → jangan dekat-dekat"], dark=False),
 cta("Tebak: " + J.format("禁煙") + " artinya apa?", "Petunjuk: 煙 = asap. Jawab 1 kata di komen."),
],
"cs19-kereta": [
 cover(CS, "Naik kereta di Jepang " + PINK.format("tanpa nyasar.") , "8 kalimat & kata yang wajib ada di HP-mu."),
 text("Salah naik kereta " + R.format("cepat") + " bisa kelewat stasiunmu.", "Jadi tanya dulu, dan pahami tulisan di papan peron."),
 vocab("NANYA DI STASIUN", [("〇〇に行きますか？", "... ni ikimasu ka", "Ini ke ...?"), ("何番線ですか？", "nanbansen desu ka", "Jalur berapa?"), ("乗り換えはどこですか？", "norikae wa doko desu ka", "Pindah kereta di mana?"), ("〇〇までいくらですか？", "... made ikura desu ka", "Sampai ... berapa?")]),
 vocab("DI PAPAN PERON", [("各駅停車", "kakueki teisha", "Berhenti tiap stasiun"), ("快速", "kaisoku", "Cepat, skip stasiun"), ("終電", "shuuden", "Kereta terakhir"), ("女性専用車", "josei senyousha", "Gerbong khusus wanita")]),
 text("Turun di stasiun kecil? Naik " + PINK.format(J.format("各駅停車") + "."), "快速 & 急行 (kyuukou) nggak berhenti di semua stasiun. Cek dulu sebelum naik.", dark=True),
 cta("Kereta yang berhenti di tiap stasiun?", "A. 快速  B. 各駅停車. Jawab A/B di komen."),
],
"ck02-14-hari": [
 cover("CHECKLIST", "Baru sampai Jepang? " + PINK.format("5 urusan") + " 14 hari pertama.", "Biar gaji bisa masuk & asuransi aktif."),
 text("Batas lapor alamat: " + R.format("14 hari") + " sejak tinggal di alamat baru.", "Bawa 在留カード (kartu izin tinggal) ke kantor kota. Telat lapor bisa kena denda."),
 vocab("DI KANTOR KOTA", [("市役所", "shiyakusho", "Kantor kota"), ("在留カード", "zairyuu kaado", "Kartu izin tinggal"), ("住所", "juusho", "Alamat"), ("転入届", "tennyuu todoke", "Lapor pindah masuk")]),
 vocab("SETELAH ITU", [("マイナンバー", "mai nanbaa", "Nomor identitas (dikirim ke alamat)"), ("健康保険", "kenkou hoken", "Asuransi kesehatan"), ("銀行口座", "ginkou kouza", "Rekening bank"), ("携帯電話", "keitai denwa", "Nomor HP")]),
 text("Asuransi lewat " + PINK.format("perusahaan") + " atau kantor kota.", "Karyawan biasanya ikut 健康保険 perusahaan. Kalau nggak, daftar 国民健康保険 (kokumin kenkou hoken) di kantor kota.", dark=True),
 check("SCREENSHOT INI", "Checklist 14 hari pertama:", ["Lapor alamat di 市役所", "Tunggu kartu マイナンバー", "Pastikan 健康保険 aktif", "Buka 銀行口座 buat gaji", "Aktifin nomor HP Jepang"], dark=False),
 cta("Dari 5 ini, mana yang paling bikin bingung?", "Jawab angkanya 1–5 di komen. Kirim ke temen yang mau berangkat."),
],
"cs20-line": [
 cover(CS, "Udah tukeran LINE sama orang Jepang? " + PINK.format("Bales pakai ini."), "8 kata & kalimat biar chat nggak kaku."),
 text("Orang Jepang chat pakai " + R.format("LINE") + ", bukan WA.", "Minta kontaknya: LINE交換しませんか？(LINE koukan shimasen ka) = Tukeran LINE yuk?"),
 vocab("KATA DI CHAT", [("了解", "ryoukai", "Oke, siap"), ("おつかれ", "otsukare", "Makasih, capek ya hari ini"), ("既読", "kidoku", "Udah dibaca"), ("スタンプ", "sutanpu", "Stiker LINE")]),
 vocab("KALIMAT CHAT", [("今、大丈夫？", "ima, daijoubu?", "Lagi senggang?"), ("返信遅れてごめん", "henshin okurete gomen", "Maaf telat bales"), ("また連絡するね", "mata renraku suru ne", "Nanti kukabarin ya"), ("おやすみ", "oyasumi", "Selamat tidur")]),
 text("Awas " + PINK.format(J.format("既読スルー") + "."), "kidoku suruu = di-read doang, nggak dibales. Bales singkat aja, misalnya 了解！ atau 1 stiker.", dark=True),
 cta("Kamu lebih sering yang mana?", "A. Telat bales  B. Read doang. Jawab A/B di komen."),
],
"tl03-aplikasi": [
 pcover("qr", "TIER LIST APLIKASI", "Ke Jepang, " + PINK.format("aplikasi apa") + " yang wajib di HP?", "Dari yang paling kepake sampai yang cuma pelengkap."),
 text("Di Jepang, HP itu " + R.format("peta, kamus, dan dompet.") , "Install dari Indonesia, biar sampai sana langsung siap pakai."),
 tiers("TIER LIST APLIKASI JEPANG", [('S', ['Google Maps', 'LINE']), ('A', ['Google Translate', 'Japan Transit']), ('B', ['Suica (Wallet)', 'Tabelog']), ('C', ['GO (taksi)'])]),
 text("Tier S: " + R.format("Google Maps & LINE."), "Maps buat rute kereta & jalan kaki. LINE buat chat sama orang Jepang, temen kerja, sampai perusahaan."),
 text("Tier A–C: " + PINK.format("pelengkap."), "Translate pakai mode kamera buat baca menu. Japan Transit buat jadwal kereta. Tabelog cari makan. GO kalau terpaksa naik taksi.", dark=True),
 vocab("KATA DI APLIKASI PETA", [("現在地", "genzaichi", "Lokasimu sekarang"), ("徒歩", "toho", "Jalan kaki"), ("乗換", "norikae", "Pindah kereta"), ("番線", "bansen", "Nomor jalur peron")]),
 cta("Aplikasi pertama yang kamu install?", "Jawab 1 kata di komen. Kirim ke temen yang mau ke Jepang."),
],
"cs21-apotek": [
 cover(CS, "Sakit pas di Jepang? " + PINK.format("Bilang ini") + " di apotek.", "8 kalimat & kata biar nggak cuma nunjuk-nunjuk."),
 text("Flu atau sakit kepala ringan? " + R.format("Drugstore") + " ada di mana-mana.", "ドラッグストア (doraggusutoa) jual obat bebas. Tinggal jelasin keluhanmu."),
 vocab("BILANG KELUHAN", [("頭が痛いです", "atama ga itai desu", "Kepala sakit"), ("お腹が痛いです", "onaka ga itai desu", "Perut sakit"), ("熱があります", "netsu ga arimasu", "Aku demam"), ("風邪をひきました", "kaze o hikimashita", "Aku kena flu")]),
 vocab("DI APOTEK", [("薬局", "yakkyoku", "Apotek"), ("風邪薬", "kazegusuri", "Obat flu"), ("痛み止め", "itamidome", "Obat pereda nyeri"), ("アレルギーがあります", "arerugii ga arimasu", "Aku punya alergi")]),
 text("Bingung pilih obat? Tanya " + PINK.format(J.format("どれがいいですか？")), "dore ga ii desu ka = Yang mana yang cocok? Parah atau darurat, langsung telepon 119.", dark=True),
 cta("Tebak: " + J.format("目が痛い") + " artinya apa?", "Petunjuk: 目 = mata. Jawab di komen."),
],
"kj03-cuti": [
 cover("KERJA DI JEPANG", "Kerja 6 bulan di Jepang = " + PINK.format("10 hari cuti dibayar."), "Hak ini juga berlaku buat pekerja asing."),
 text("Namanya " + R.format(J.format("有給休暇")) + " (yuukyuu kyuuka).", "Syaratnya: kerja terus 6 bulan dan masuk minimal 80% hari kerja. Gaji tetap dibayar saat cuti."),
 rows("JATAH CUTI (KARYAWAN PENUH WAKTU)", [("Setelah 6 bulan", "", "10 hari"), ("1,5 tahun", "", "11 hari"), ("2,5 tahun", "", "12 hari"), ("3,5 tahun", "", "14 hari"), ("6,5 tahun+", "", "20 hari")]),
 text("Jatah 10 hari ke atas? " + PINK.format("Minimal 5 hari") + " wajib diambil tiap tahun.", "Perusahaan wajib memastikan kamu ambil. Jadi jangan takut minta cuti.", dark=True),
 vocab("MINTA CUTI & IZIN", [("有給を取りたいです", "yuukyuu o toritai desu", "Mau ambil cuti"), ("休みをいただけますか", "yasumi o itadakemasu ka", "Boleh minta libur?"), ("体調不良です", "taichou furyou desu", "Lagi nggak enak badan"), ("早退してもいいですか", "soutai shite mo ii desu ka", "Boleh pulang duluan?")]),
 check("SCREENSHOT INI", "Checklist cuti:", ["6 bulan kerja = 10 hari", "Masuk minimal 80%", "Minimal 5 hari diambil/tahun", "Bilang jauh hari ke atasan", "Pakai 有給を取りたいです"], dark=False),
 cta("Kalau dapat 10 hari cuti, kamu pakai buat?", "A. Pulang ke Indonesia  B. Jalan-jalan di Jepang. Jawab A/B."),
],
"cs22-belanja": [
 cover(CS, "Belanja baju di Jepang? " + PINK.format("8 kalimat ini") + " cukup.", "Dari nyoba baju sampai baca label diskon."),
 text("Pelayan toko Jepang ramah, tapi " + R.format("nggak semua bisa bahasa Inggris."), "Hafalin kalimat pendek ini, belanja jadi santai."),
 vocab("DI TOKO", [("見ているだけです", "mite iru dake desu", "Cuma lihat-lihat"), ("試着してもいいですか？", "shichaku shite mo ii desu ka", "Boleh dicoba?"), ("他の色はありますか？", "hoka no iro wa arimasu ka", "Ada warna lain?"), ("大きいサイズはありますか？", "ookii saizu wa arimasu ka", "Ada ukuran lebih besar?")]),
 vocab("DI LABEL HARGA", [("税込", "zeikomi", "Udah termasuk pajak"), ("税抜", "zeinuki", "Belum termasuk pajak"), ("割引", "waribiki", "Diskon"), ("半額", "hangaku", "Setengah harga")]),
 text("Lihat " + PINK.format(J.format("税抜") + "?") + " Siapin uang lebih.", "Di kasir ditambah pajak ±10%. Harga ¥1.000 税抜 jadi ±¥1.100.", dark=True),
 cta("半額 = diskon berapa persen?", "Jawab angkanya di komen."),
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
                ov = await pg.evaluate("()=>{const o=[];document.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&(r.right>1062||r.bottom>1340))o.push(e.className+':'+Math.round(r.right)+','+Math.round(r.bottom))});return o.slice(0,3)}")
                if ov: print(name, i, ov)
                await pg.screenshot(path=f"{d}/s{i}.jpg", type='jpeg', quality=92)
        await b.close()
asyncio.run(main())
from PIL import Image
S="/tmp/claude-0/-home-claude-msr-carousel/11bf9338-a3a1-56d0-b8e9-bffa752c7ff8/scratchpad"
for name, slides in POSTS.items():
    n=len(slides); ims=[Image.open(f"/home/claude/msr-carousel/nanihongo-{name}/s{i}.jpg").resize((360,450)) for i in range(1,n+1)]
    c=Image.new('RGB',(360*4,900),'white')
    for k,im in enumerate(ims): c.paste(im,((k%4)*360,(k//4)*450))
    c.save(f"{S}/{name}.jpg")
print("ok")
