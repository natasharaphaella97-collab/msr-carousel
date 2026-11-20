import asyncio, os
from playwright.async_api import async_playwright
src = open('/home/claude/nanihongo/cs/gen2.py').read().split('async def main')[0]
ns = {}; exec(src, ns)
CSS, cover, text, cta, vocab = ns['CSS'], ns['cover'], ns['text'], ns['cta'], ns['vocab']
big = None
g = {}; exec(open('/home/claude/nanihongo/batch/gen.py').read().split('T = "KERJA')[0], g); big = g['big']
R = "<span class='red'>{}</span>"; PINK = "<span style='color:#FF4D5E'>{}</span>"
CSS += """
.tier{display:flex;align-items:stretch;border-bottom:3px solid #1B2340;min-height:150px}
.tl{width:150px;flex:0 0 150px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:96px;color:#F6F1E7}
.tr{display:flex;flex-wrap:wrap;gap:14px;align-items:center;padding:20px 0 20px 26px}
.tr span{background:#1B2340;color:#F6F1E7;font-weight:800;font-size:38px;padding:12px 22px;border-radius:12px}
"""
def tiers(tag, rows):
    cols = {'S':'#C8102E','A':'#E0573B','B':'#4A5A86','C':'#8A90A6'}
    r = "".join(f"<div class='tier'><div class='tl' style='background:{cols[k]}'>{k}</div><div class='tr'>{''.join(f'<span>{x}</span>' for x in xs)}</div></div>" for k, xs in rows)
    return f"<body><div class='pad' style='top:170px'><span class='tag'>{tag}</span><div style='margin-top:40px;border-top:3px solid #1B2340'>{r}</div></div></body>"
import base64
def img(n): return "data:image/jpeg;base64,"+base64.b64encode(open(f"/home/claude/nanihongo/pay01/p_{n}.jpg","rb").read()).decode()
CSS += """
.ph{position:absolute;left:0;top:0;width:1080px;height:540px;object-fit:cover}
.phb{position:absolute;left:0;top:560px;width:1080px;height:40px;background:linear-gradient(transparent,rgba(0,0,0,.0))}
.full{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}
.ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(27,35,64,.55) 0%,rgba(27,35,64,.92) 55%,#1B2340 100%)}
"""
def photo(n, tag, head, *ps, dark=False):
    pp = "".join(f"<div class='p'{' style=color:#cfd5e6' if dark else ''}>{p}</div>" for p in ps)
    return f"<body{' class=cover' if dark else ''}><img class='ph' src='{img(n)}'><div class='pad' style='top:590px'><span class='tag'>{tag}</span><div class='h2' style='margin-top:30px;font-size:76px'>{head}</div>{pp}</div></body>"
def pcover(n, tag, head, sub):
    return f"<body class='cover'><img class='full' src='{img(n)}'><div class='ov'></div><div class='pad' style='top:250px'><span class='tag'>{tag}</span><div class='h1'>{head}</div><div class='p' style='color:#e3e7f2'>{sub}</div></div></body>"
slides = [
 pcover("ic", "TIER LIST 2026", "Di Jepang bayar pakai apa? " + PINK.format("Tier list") + " versi 2026.", "Biar nggak panik di depan kasir."),
 photo("cash", "JEPANG BELUM FULL CASHLESS", R.format("58%") + " transaksi udah cashless.", "Data 2025. Artinya ±4 dari 10 yen masih dibayar tunai. Tetap bawa cash."),
 tiers("TIER LIST BAYAR DI JEPANG", [('S', ['Suica / PASMO / ICOCA', 'Cash']), ('A', ['PayPay']), ('B', ['Debit Visa', 'Mastercard']), ('C', ['QRIS'])]),
 photo("ic", "TIER S", "Kartu IC " + R.format("+ cash."), "Suica, PASMO, ICOCA: 1 kartu buat kereta, bus, konbini, vending machine.", "Pakai iPhone? Suica bisa langsung ditambah di Apple Wallet."),
 photo("qr", "TIER A", R.format("PayPay."), "Dipakai 75 juta+ orang di Jepang.", "Cocok buat yang udah kerja di sana. Daftarnya umumnya butuh nomor HP Jepang."),
 photo("card", "TIER B &amp; C", "Cadangan: " + PINK.format("kartu &amp; QRIS."), "Debit Visa/Mastercard: aman di toko besar &amp; konbini. Warung kecil sering cash only.", "QRIS: bisa sejak Agustus 2025, tapi tokonya masih terbatas.", dark=True),
 vocab("KALIMAT DI KASIR", [("カードで払えますか？", "kaado de haraemasu ka?", "Bisa bayar pakai kartu?"), ("現金のみ", "genkin nomi", "Cash only"), ("現金で払います", "genkin de haraimasu", "Bayar cash ya"), ("チャージ", "chaaji", "Isi saldo kartu IC"), ("残高不足", "zandaka busoku", "Saldo kurang")]),
 cta("Kamu tim cash atau tim kartu?", "Jawab 1 kata di komen."),
]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':1080,'height':1350})
        for i, body in enumerate(slides, 1):
            await pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head>{body}</html>")
            await pg.wait_for_timeout(150); await pg.screenshot(path=f"s{i}.png")
        await b.close()
asyncio.run(main())
