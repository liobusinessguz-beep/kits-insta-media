import base64, subprocess, os, html
D = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(D, "tempo_fonts.css")).read()
OUT = os.path.join(D, "pins"); os.makedirs(OUT, exist_ok=True)

def img(name):
    return "data:image/png;base64," + base64.b64encode(open(os.path.join(D, "cov2", f"Couverture {name}.png"), "rb").read()).decode()

TH = {
 "roi":   dict(bg1="#0e1738", bg2="#1d2b53", halo="#2f4fd6", acc="#a9bbff", mono="#9fb0e6", txt="#d6dcf0"),
 "bord":  dict(bg1="#1e0f16", bg2="#3a1f20", halo="#8a1c3c", acc="#f2b8c6", mono="#e7a9b8", txt="#e3d6da"),
 "terra": dict(bg1="#29150e", bg2="#422a19", halo="#b4532a", acc="#f0a98a", mono="#e8b49a", txt="#ecdcd2"),
 "sapin": dict(bg1="#142018", bg2="#2c3322", halo="#2f7a50", acc="#8fd1a8", mono="#a6d6b6", txt="#d9e6dc"),
}

PINS = [
 ("01-photographe-5-legendes-offertes", "roi", "Cadeau 5 legendes", "Pour les photographes",
  "5 légendes Instagram", "offertes", "Copie, colle, publie. Pour poster plus souvent sans passer tes soirées à chercher les mots.",
  "Gratuit · PDF à télécharger"),
 ("02-photographe-quoi-ecrire", "roi", "Cadeau 5 legendes", "Photographe · Instagram",
  "Quoi écrire sous", "tes photos ?", "5 légendes prêtes à copier pour présenter ton travail, raconter une séance et donner envie de réserver.",
  "Gratuit · PDF à télécharger"),
 ("03-pack-30-legendes", "bord", "Pack Insta Photographe", "Pack · pour les photographes",
  "30 légendes Instagram", "prêtes à poster", "Un mois de contenu écrit d'avance : légendes, idées de reels sans visage et réponses aux messages.",
  "Pack PDF · 17 €"),
 ("04-pack-planning-4-semaines", "bord", "Pack Insta Photographe", "Planning Instagram",
  "Un mois de posts", "déjà planifié", "3 posts par semaine pendant 4 semaines, prêts en 10 minutes. Pensé pour les photographes.",
  "Pack PDF · 17 €"),
 ("05-janvier-2027-offert", "terra", "Cadeau janvier", "Pour les indépendants",
  "Ton janvier 2027", "en avance", "Ton calendrier Instagram rempli, les dates clés du mois et 2 posts prêts à copier : vœux et soldes.",
  "Gratuit · PDF à télécharger"),
 ("06-kit-du-mois-janvier", "sapin", "Kit du Mois", "Indépendants · Instagram",
  "Quoi poster", "en janvier ?", "12 posts avec légende, 2 idées de reels et ton calendrier : ton mois de contenu prêt en 30 minutes.",
  "Abonnement · 9 € / mois"),
]

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1000px;height:1500px;overflow:hidden}
body{font-family:TI,sans-serif;color:#fff;position:relative;background:linear-gradient(165deg,{bg2} 0%,{bg1} 55%)}
.halo{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,{halo}88 0%,transparent 65%);right:-380px;top:-380px}
.halo2{position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,{halo}55 0%,transparent 65%);left:-320px;bottom:-200px}
.wrap{position:relative;padding:88px 80px 0}
.mono{font:700 21px JBM,monospace;letter-spacing:.2em;text-transform:uppercase;color:{mono}}
h1{font:700 96px/1.0 TID,serif;letter-spacing:-.02em;margin:30px 0 30px}
h1 i{font-style:italic;color:{acc}}
p.lead{font-size:31px;line-height:1.42;color:{txt};max-width:820px}
.mock{position:absolute;left:50%;bottom:150px;width:520px;transform:translateX(-50%) rotate(-3deg);border-radius:14px;box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.12)}
.mock2{position:absolute;left:50%;bottom:170px;width:500px;transform:translateX(-38%) rotate(5deg);border-radius:14px;opacity:.55;filter:blur(1px);box-shadow:0 30px 70px rgba(0,0,0,.5)}
.cta{position:absolute;left:80px;right:80px;bottom:54px;display:flex;justify-content:space-between;align-items:center}
.pill{background:{acc};color:{bg1};font:800 27px TI;padding:20px 34px;border-radius:999px}
.shop{font:700 20px JBM;letter-spacing:.14em;text-transform:uppercase;color:{mono}}
"""

def build(slug, th, cover, kick, a, b, lead, cta):
    t = TH[th]; css = CSS
    for k, v in t.items(): css = css.replace("{" + k + "}", v)
    src = img(cover)
    doc = f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}{css}</style></head><body>
<div class=halo></div><div class=halo2></div>
<div class=wrap><div class=mono>{html.escape(kick)}</div><h1>{html.escape(a)}<br><i>{html.escape(b)}</i></h1><p class=lead>{html.escape(lead)}</p></div>
<img class=mock2 src="{src}"><img class=mock src="{src}">
<div class=cta><span class=pill>{html.escape(cta)}</span><span class=shop>Les Kits Insta</span></div>
</body></html>"""
    hp = os.path.join(OUT, slug + ".html"); open(hp, "w").write(doc)
    png = os.path.join(OUT, slug + ".png")
    subprocess.run(["google-chrome", "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=1000,1500", f"--screenshot={png}", "file://" + hp], capture_output=True, timeout=90)
    return png

if __name__ == "__main__":
    for p in PINS: print(build(*p))
