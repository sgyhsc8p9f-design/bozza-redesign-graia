"""Struttura comune delle pagine (header, footer, lingua)."""
import html as _h

EN_PAGES = {
    "index.html", "attivita.html", "portfolio.html", "blu-progetti.html",
    "news.html", "chi-siamo.html", "contatti.html", "privacy.html", "documenti.html",
}

T = {
    "it": {
        "lang": "it",
        "skip": "Vai al contenuto",
        "banner": '<b>Bozza di proposta</b>: non è il sito ufficiale di GRAIA. Testi e immagini sono ripresi da graia.eu a solo scopo dimostrativo.',
        "banner_link": "Cosa cambia →",
        "nav": [
            ("attivita.html", "Attività"),
            ("portfolio.html", "Portfolio"),
            ("blu-progetti.html", "BLU Progetti"),
            ("news.html", "News"),
            ("chi-siamo.html", "Chi siamo"),
            ("contatti.html", "Contatti"),
        ],
        "search": "Cerca",
        "menu": "Menu",
        "main_nav": "Principale",
        "home_aria": "GRAIA, home",
        "addr": "Gestione e Ricerca Ambientale Ittica Acque<br>Viale Repubblica 1, 21020 Varano Borghi (VA)",
        "partner": "Graia è partner di Life Natura",
        "site": "Il sito",
        "site_links": [
            ("attivita.html", "Le nostre attività"),
            ("portfolio.html", "Portfolio"),
            ("blu-progetti.html", "BLU Progetti"),
            ("news.html", "News"),
            ("chi-siamo.html", "Chi siamo"),
            ("contatti.html", "Contatti"),
        ],
        "docs": "Documenti",
        "docs_links": [
            ("documenti.html", "Download"),
            ("privacy.html", "Privacy e cookie"),
            ("cerca.html", "Cerca nel sito"),
        ],
        "legal": "P. IVA 10454870154. Gli aiuti di Stato e gli aiuti de minimis ricevuti dalla nostra impresa sono contenuti nel Registro nazionale degli aiuti di Stato di cui all'art. 52 della L. 234/2012 e consultabili sulla pagina del RNA, inserendo come chiave di ricerca il codice fiscale della società. Il CF di GRAIA è 10454870154 e quello di Blu Progetti è 02935220125.",
    },
    "en": {
        "lang": "en",
        "skip": "Skip to content",
        "banner": '<b>Draft proposal</b>: this is not the official GRAIA website. Text and images are taken from graia.eu for demonstration only.',
        "banner_link": "What changes →",
        "nav": [
            ("attivita.html", "Activities"),
            ("portfolio.html", "Portfolio"),
            ("blu-progetti.html", "BLU Progetti"),
            ("news.html", "News"),
            ("chi-siamo.html", "About us"),
            ("contatti.html", "Contact"),
        ],
        "search": "Search",
        "menu": "Menu",
        "main_nav": "Main",
        "home_aria": "GRAIA, home",
        "addr": "Gestione e Ricerca Ambientale Ittica Acque<br>Viale Repubblica 1, 21020 Varano Borghi (VA), Italy",
        "partner": "Graia is a Life Natura partner",
        "site": "Site",
        "site_links": [
            ("attivita.html", "Our activities"),
            ("portfolio.html", "Portfolio"),
            ("blu-progetti.html", "BLU Progetti"),
            ("news.html", "News"),
            ("chi-siamo.html", "About us"),
            ("contatti.html", "Contact"),
        ],
        "docs": "Documents",
        "docs_links": [
            ("documenti.html", "Downloads"),
            ("privacy.html", "Privacy and cookies"),
        ],
        "legal": "VAT no. 10454870154. State aid and de minimis aid received by our company are recorded in the National State Aid Register (art. 52, law 234/2012) and can be consulted on the RNA website using the company's tax code as search key. GRAIA's tax code is 10454870154; Blu Progetti's is 02935220125.",
    },
}


def page(fname, title, desc, body, lang="it", og_image="img/luccio.jpg"):
    t = T[lang]
    p = "" if lang == "it" else "../"
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == fname else ""}>{lbl}</a></li>' for h, lbl in t["nav"]
    )
    if lang == "it":
        other = f"en/{fname}" if fname in EN_PAGES else "en/index.html"
        sw = f'<a href="cerca.html">Cerca</a> &nbsp;·&nbsp; <b>IT</b> · <a href="{other}" hreflang="en" lang="en">EN</a>'
        prop = "proposta.html"
    else:
        sw = f'<a href="../{fname}" hreflang="it" lang="it">IT</a> · <b>EN</b>'
        prop = "../proposta.html"
    fl = "".join(f'<li><a href="{h}">{lbl}</a></li>' for h, lbl in t["site_links"])
    dl = "".join(f'<li><a href="{h}">{lbl}</a></li>' for h, lbl in t["docs_links"])
    t_ = _h.escape(title)
    d_ = _h.escape(desc, quote=True)
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{t_}</title>
<meta name="description" content="{d_}">
<meta property="og:title" content="{t_}">
<meta property="og:description" content="{d_}">
<meta property="og:image" content="{p}{og_image}">
<link rel="icon" href="{p}img/logo.png">
<link rel="stylesheet" href="{p}fonts/fonts.css">
<link rel="stylesheet" href="{p}style.css?v=11">
</head>
<body>
<a class="skip" href="#contenuto">{t['skip']}</a>
<div class="bozza">{t['banner']} <a href="{prop}" style="color:#fff">{t['banner_link']}</a></div>
<header class="site">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="{t['home_aria']}"><img src="{p}img/logo.png" alt="GRAIA" width="145" height="58"></a>
    <button class="burger" aria-expanded="false" aria-controls="menu">{t['menu']}</button>
    <nav class="main" id="menu" aria-label="{t['main_nav']}"><ul>{nav}</ul></nav>
    <span class="lang">{sw}</span>
  </div>
</header>
<main id="contenuto">
{body}
</main>
<footer class="site">
  <div class="wrap">
    <div class="griglia">
      <div>
        <a class="logo-footer" href="index.html"><img src="{p}img/logo.png" alt="GRAIA"></a>
        <p><strong>G.R.A.I.A. srl</strong><br>{t['addr']}</p>
        <p>Tel. <a href="tel:+390332961097">+39 0332 961 097</a><br><a href="mailto:info@graia.eu">info@graia.eu</a> · PEC graia@pec.it</p>
        <p class="partner">{t['partner']}<br><img src="{p}img/life-natura.png" alt="Life Natura"></p>
      </div>
      <div><h4>{t['site']}</h4><ul>{fl}</ul></div>
      <div><h4>{t['docs']}</h4><ul>{dl}</ul></div>
    </div>
    <p class="legale">{t['legal']}</p>
  </div>
</footer>
<script>
const b=document.querySelector('.burger'),n=document.getElementById('menu');
b.addEventListener('click',()=>{{const o=n.classList.toggle('aperto');b.setAttribute('aria-expanded',o)}});
</script>
</body>
</html>
"""


def interna(eyebrow, h1, lead):
    return f"""<section class="hero interna" style="padding:0">
  <div class="testo">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p>{lead}</p>
  </div>
</section>"""
