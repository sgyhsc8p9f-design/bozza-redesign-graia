"""English version of the main pages (files in en/)."""
import html as H
from layout import page, interna
import it_dynamic as D

pages = {}


def P(fname, title, desc, body, og="img/luccio.jpg"):
    pages["en/" + fname] = page(fname, title, desc, body, lang="en", og_image=og)


EN_TITLES = {
    "ittiologia": "Ichthyology",
    "carte-ittiche-e-piani-ittici": "Fish maps and fisheries management plans",
    "acquacoltura-incubatoi-allevamento-ittico": "Aquaculture, hatcheries and fish farming",
    "gestione-della-pesca-sportiva-e-professionale": "Management of recreational and commercial fishing",
    "ecologia-applicata-e-biomonitoraggio": "Applied ecology and biomonitoring",
    "valutazioni-di-impatto-ambientale": "Environmental Impact Assessment (EIA)",
    "valutazione-di-incidenza-vi": "Appropriate assessment (Habitats Directive)",
    "valutazione-ambientale-strategica-vas": "Strategic Environmental Assessment (SEA)",
    "autorizzazione-integrata-ambientale-aia": "Integrated Environmental Authorisation (IEA)",
    "modellistica-ambientale": "Environmental modelling",
    "urban-runoff-management": "Urban runoff management",
    "studi-di-impatto-sulla-vegetazione": "Vegetation impact studies",
    "riqualificazione-fluviale": "River and lake restoration",
    "ingegneria-naturalistica": "Soil and water bioengineering",
    "fitodepurazione-e-lagunaggio": "Constructed wetlands and lagooning",
    "reti-ecologiche": "Ecological networks",
    "gestione-e-conservazione-di-ecosistemi-e-ambienti-di-alta-quota": "Management and conservation of high-altitude ecosystems",
    "progettazione-e-dl-di-interventi-di-riqualificazione-e-rimboschimento-forestale": "Design and works supervision for forest restoration and reforestation",
    "gestione-delle-risorse-forestali": "Forest resource management",
    "paesaggistica-e-progettazione-del-verde": "Landscape and green space design",
    "agricoltura": "Agriculture",
    "passaggi-per-pesci": "Fish passes",
    "video-monitoraggio-delle-migrazioni-ittiche-nei-passaggi-per-pesci": "Video monitoring of fish migration in fish passes",
    "gestione-del-sedimento-negli-invasi-artificiali": "Sediment management in reservoirs",
    "progetti-life": "LIFE Programme",
    "progetto-life-predator": "LIFE PREDATOR project",
    "programma-di-cooperazione-interreg": "Interreg cooperation programme (Sharesalmo)",
    "eco4ticino-unalleanza-per-difendere-la-biodiversita-tra-italia-e-svizzera": "ECO4TICINO",
    "prospittico-progetto-sperimentale-per-il-monitoraggio-della-biodiversita-ittica-nei-corridoi-fluviali": "ProSpIttiCo",
    "divulgazione-e-didattica-ambientale": "Environmental education and outreach",
}
assert set(EN_TITLES) == set(D.ACT_BY)

AMBITI_EN = {
    "ittiologia": ("Ichthyology and fish fauna management", "Where we started: knowing fish in order to protect and manage them."),
    "monitoraggio": ("Environmental monitoring and assessment", "Field data read with rigour, to understand the state of rivers and lakes and for assessment procedures."),
    "riqualificazione": ("Restoration, bioengineering and land management", "Works that give space and ecological function back to water and land, also with BLU Progetti."),
    "passaggi": ("Fish passes and hydropower", "Where water meets a dam or a weir, fish must be able to get through."),
    "life": ("LIFE programmes and European research", "Projects co-funded by the European Union for species and habitats, from LIFE to Interreg and the Italian recovery plan."),
    "didattica": ("Education and outreach", "Telling the story of water to those who live by it: schools, citizens, anglers."),
}
note_it = '<p class="meta" style="margin-top:.8rem">Detailed pages are in Italian.</p>'


def blocco(a):
    t, d = AMBITI_EN[a["id"]]
    cls = "fig poster" if a["poster"] else "fig"
    li = "".join(f'<li><a href="../a-{s}.html" hreflang="it">{H.escape(EN_TITLES[s])}</a></li>' for s in a["slugs"])
    return f"""<div class="sezione-attivita" id="{a['id']}">
  <figure class="{cls}" style="margin:0"><img src="../img/{a['img']}" alt="" loading="lazy" style="object-position:{a['pos']}"></figure>
  <div><p class="eyebrow">{a['n']}</p><h2 style="font-size:2rem;margin-bottom:1rem">{t}</h2><p>{d}</p><ul class="elenco-att">{li}</ul></div>
</div>"""


# ----------------------------------------------------------------- HOME
P("index.html", "GRAIA · Fish, water and environmental research",
  "Since 1991 in the service of people and nature: ichthyology, river restoration and environmental research in Varano Borghi (Varese, Italy).",
  """
<section class="hero" style="padding:0">
  <div class="testo">
    <p class="eyebrow">Gestione Ricerca Ambientale Ittica Acque</p>
    <h1>Since 1991, in the service of people and nature.</h1>
    <p>We conserve natural resources and work to make human presence and activities as compatible as possible with the environment.</p>
    <div class="azioni"><a class="btn" href="attivita.html">What we do</a><a class="btn ghost" href="contatti.html">Write to us</a></div>
  </div>
  <figure class="foto" style="margin:0"><img src="../img/luccio.jpg" alt="A pike among aquatic plants" width="1800" height="1180"><figcaption>Photo: GRAIA archive</figcaption></figure>
</section>

<section><div class="wrap due">
  <div><p class="eyebrow">GRAIA in a few lines</p><h2>Four professionals, one passion: fish and water.</h2></div>
  <div>
    <p class="lead">The company was founded in 1991 by four professionals in aquatic ecology and ichthyology, united by a passion for fish fauna and fishing. We love our work, and we do it with passion because we believe in it.</p>
    <ul class="fatti">
      <li><span class="k">1991</span><span class="v">founded in Varano Borghi, on Lake Comabbio</span></li>
      <li><span class="k">3 + 35</span><span class="v">three founding partners leading more than thirty employees and collaborators, most of whom trained inside the company</span></li>
      <li><span class="k">2006</span><span class="v">BLU Progetti is born, the engineering company of the same partners</span></li>
    </ul>
    <p style="margin-top:1.6rem"><a class="link-freccia" href="chi-siamo.html">Meet the team</a></p>
  </div>
</div></section>

<section class="pallida"><div class="wrap due">
  <div class="sticky"><p class="eyebrow">What we do</p><h2>Six areas of work, one common thread: water.</h2>
    <p style="margin-top:1.2rem;color:var(--grigio)">A multidisciplinary team, built over more than thirty years, is our guarantee of competence.</p>
    <p><a class="link-freccia" href="attivita.html">All activities</a></p></div>
  <ol class="attivita">
    <li><span class="n">01</span><div><h3>Ichthyology and fish fauna management</h3></div><p>Fish maps and fisheries plans, species conservation, hatcheries, aquaculture, recreational and commercial fishing.</p></li>
    <li><span class="n">02</span><div><h3>Environmental monitoring and assessment</h3></div><p>Biomonitoring, limnology, statistical analysis, bathymetry, water quality.</p></li>
    <li><span class="n">03</span><div><h3>River and lake restoration</h3></div><p>River continuity, ecological restoration, reforestation, constructed wetlands.</p></li>
    <li><span class="n">04</span><div><h3>Fish passes and hydropower</h3></div><p>Design and monitoring of migrations, minimum environmental flow, reservoir flushing.</p></li>
    <li><span class="n">05</span><div><h3>LIFE programmes and European research</h3></div><p>Conservation of species and habitats, climate change, ecological networks.</p></li>
    <li><span class="n">06</span><div><h3>Education and outreach</h3></div><p>Schools, books and installations, events for the local community.</p></li>
  </ol>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Featured projects</p><h2 style="max-width:18ch;margin-bottom:2.5rem">From research to the territory.</h2>
  <div class="progetto-grande">
    <img src="../img/lifeel.jpg" alt="LIFEEL Days poster, Comacchio" loading="lazy" width="1800" height="963">
    <div><p class="meta">24–26 April 2026 · Comacchio, Manifattura dei Marinati</p><h3 style="font-size:2rem">LIFEEL Days</h3>
      <p style="margin-top:.8rem">More than the formal end of the project: a moment to give results back to the territory, where the conservation of the European eel becomes a shared responsibility and a dialogue between science, institutions and citizens.</p>
      <a class="link-freccia" href="../news-lifeel-days.html" hreflang="it">Read the news (in Italian)</a></div>
  </div>
  <div class="righe-progetti">
    <article class="riga-progetto"><img src="../img/prospittico.png?v=2" alt="ProSpIttiCo project logos" loading="lazy"><p class="meta">Italian recovery plan · National Biodiversity Future Center</p><h3>ProSpIttiCo</h3>
      <p>A system to monitor the fish species passing through fish passes. GRAIA is the sole beneficiary. The platform with the beta version is coming soon.</p></article>
    <article class="riga-progetto"><img src="../img/eco4ticino.png?v=2" alt="ECO4TICINO, Interreg Italy-Switzerland" loading="lazy"><p class="meta">Interreg Italy–Switzerland · 2025–2027</p><h3>ECO4TICINO</h3>
      <p>An ecological corridor to manage together, across the border, along the River Ticino. GRAIA is a beneficiary.</p></article>
  </div>
</div></section>

<section class="acqua"><div class="wrap blu">
  <div><p class="eyebrow" style="color:var(--abisso)">BLU Progetti</p><h2>From study to construction site.</h2></div>
  <div><p class="lead">Since 2006 the partners of GRAIA have also run BLU Progetti, an engineering company for ecological, ecosystem and environmental restoration.</p>
    <p>Design and works supervision for public and private clients. Partner of GE.RI.KO. MERA, Interreg V-A Italy–Switzerland 2014–2020.</p>
    <a class="link-freccia" href="blu-progetti.html">About BLU Progetti</a></div>
</div></section>

<section class="pallida"><div class="wrap">
  <p class="eyebrow">News from GRAIA</p>
  <ul class="news-lista" style="margin-top:1.5rem">
    <li><time>20 April 2026</time><div><h3><a href="../news-lifeel-days.html" hreflang="it">LIFEEL Days</a></h3><p>The project closes with an event to give results back to the territory.</p></div></li>
    <li><time>20 October 2025</time><div><h3><a href="../news-progetto-prospittico-manca-poco-al-lancio-della-piattaforma-per-utilizzare-il-sistema-in-fase-di-sviluppo.html" hreflang="it">ProSpIttiCo: the platform is about to launch</a></h3><p>The beta version of the monitoring system is online.</p></div></li>
    <li><time>1 September 2025</time><div><h3><a href="../news-progetto-prospittico-prosegue-la-raccolta-dei-dati.html" hreflang="it">ProSpIttiCo: data collection continues</a></h3><p>Monitoring of fish biodiversity in river corridors goes on.</p></div></li>
  </ul>
  <p style="margin-top:1.6rem"><a class="link-freccia" href="news.html">All news</a></p>
</div></section>
""")

# ----------------------------------------------------------------- ATTIVITA
P("attivita.html", "Our activities · GRAIA",
  "Ichthyology, monitoring, river restoration, fish passes, LIFE projects and environmental education.",
  interna("Our activities", "Six areas, one common thread.",
          "Our team's experience and multidisciplinary set-up, together with the cohesion of the whole working group, are our best guarantee of competence and professionalism.")
  + '<section style="padding-top:2rem"><div class="wrap">' + "".join(blocco(a) for a in D.AMBITI)
  + '<p class="todo" style="margin-top:1rem">The thirty detailed pages are currently in Italian only. English texts would be written with GRAIA for the final version.</p></div></section>')

# ----------------------------------------------------------------- PORTFOLIO
def gruppo(t, voci):
    return f'<div class="gruppo"><h3>{t}</h3><ul class="committenti">' + "".join(f"<li>{v}</li>" for v in voci) + "</ul></div>"


CASI_EN = """<section style="padding-top:2rem" id="casi"><div class="wrap">
  <p class="eyebrow">Case studies</p><h2 style="max-width:20ch;margin-bottom:2.5rem">Projects, up close.</h2>
  <article class="caso-grande">
    <figure class="fig" style="margin:0"><img src="../img/storione.jpg" alt="A Adriatic sturgeon swimming over a gravel and algae bed" loading="lazy" style="object-position:30% 50%"><figcaption>Adriatic sturgeon. Photo: GRAIA archive.</figcaption></figure>
    <div>
      <p class="meta">LIFE CON.FLU.PO · LIFE11 NAT/IT/188 · ended 30 June 2018</p>
      <h3>Opening the Po to the Adriatic sturgeon</h3>
      <p>The project restored connectivity in the Po basin, reopening the migration route for the Adriatic sturgeon (<i>Acipenser naccarii</i>) and ten other fish species listed in Annex II of the Habitats Directive.</p>
      <p>On 3 April 2019 the first sturgeon, about 1.5 m long, went through the fish pass at Isola Serafini: the project's flagship species showed it uses the Po corridor thanks to that structure.</p>
      <dl class="scheda"><dt>Field</dt><dd>Fish passes, river continuity</dd><dt>Programme</dt><dd>LIFE, European Union</dd><dt>Role</dt><dd>Project partner</dd></dl>
      <a class="link-freccia" href="../news-isola-serafini-lo-storione-cobice-ce.html" hreflang="it">The video of the passage (Italian page)</a>
    </div>
  </article>
  <div class="casi">
    <article class="caso"><img src="../img/lifeel.jpg" alt="LIFEEL Days poster" loading="lazy" class="poster-caso">
      <p class="meta">LIFE19 NAT/IT/000851 · five years, closed with LIFEEL Days (24–26 April 2026)</p><h3>LIFEEL: saving the European eel</h3>
      <p>Urgent measures for the long-term conservation of the European eel (<i>Anguilla anguilla</i>), an endangered species, supporting the biodiversity of the Po basin. Three days in Comacchio, in a former eel-processing plant now an ecomuseum, to give results back to the territory.</p><p class="ruolo">Role: project partner</p></article>
    <article class="caso"><img src="../img/prospittico.png?v=2" alt="ProSpIttiCo logos" loading="lazy" class="logo-caso larga">
      <p class="meta">Italian recovery plan · NBFC · 1 December 2024 – 30 November 2025</p><h3>ProSpIttiCo: a system that recognises fish</h3>
      <p>Development and testing of a monitoring system that recognises fish species passing through fish passes. The team combines GRAIA staff, an IT development company and three professionals chosen for the project.</p><p class="ruolo">Role: sole beneficiary · <a href="../a-prospittico-progetto-sperimentale-per-il-monitoraggio-della-biodiversita-ittica-nei-corridoi-fluviali.html" hreflang="it">Full page (Italian)</a></p></article>
    <article class="caso"><img src="../img/eco4ticino.png?v=2" alt="ECO4TICINO" loading="lazy" class="logo-caso">
      <p class="meta">Interreg Italy–Switzerland · project 0200063 · 2025–2027</p><h3>ECO4TICINO: a corridor across the border</h3>
      <p>Joint management of the River Ticino ecological corridor between Italy and Switzerland, based on the 2021–2031 restoration plan built by a network of about thirty bodies, to protect nature, biodiversity and green infrastructure.</p><p class="ruolo">Role: beneficiary · <a href="../a-eco4ticino-unalleanza-per-difendere-la-biodiversita-tra-italia-e-svizzera.html" hreflang="it">Full page (Italian)</a></p></article>
    <article class="caso"><img src="../img/geriko.jpg" alt="Interreg Italy-Switzerland" loading="lazy" class="logo-caso">
      <p class="meta">Interreg V-A Italy–Switzerland 2014–2020</p><h3>GE.RI.KO. MERA: the waters of the Mera, on both sides</h3>
      <p>Italy and Switzerland share the Mera basin but have different rules. The project builds a common strategy, with attention to solid transport after the Val Bondasca landslide, ecological corridor restoration in Natura 2000 sites and guidelines for cross-border governance.</p><p class="ruolo">Role: BLU Progetti, partner</p></article>
    <article class="caso"><p class="meta">Interreg V-A Italy–Switzerland 2014–2020</p><h3>Sharesalmo: native salmonids, together</h3>
      <p>Integrated, shared fisheries management to conserve grayling, marble trout and lake trout and to counter invasive alien species such as the wels catfish, with cross-border governance measures.</p><p class="ruolo">Role: partner · <a href="../a-programma-di-cooperazione-interreg.html" hreflang="it">Full page (Italian)</a></p></article>
    <article class="caso doppio"><p class="meta">Other LIFE Programme projects</p><h3>Long experience with LIFE</h3>
      <ul>
        <li><strong>LIFE PREDATOR</strong> (ongoing): preventing, detecting and combating the spread of the wels catfish (<i>Silurus glanis</i>) in southern European lakes.</li>
        <li><strong>IdroLIFE</strong> (ended 15 July 2021): conservation of freshwater fauna in the ecological corridors of Verbano-Cusio-Ossola.</li>
        <li><strong>LifeTicinoBiosource</strong> (ended 31 July 2021): restoring source areas for biodiversity in the Ticino Park.</li>
      </ul></article>
  </div>
  <p class="todo" style="margin-top:2.5rem">Case texts draw on facts already published on GRAIA's website. The final version needs new photos, data and results supplied by GRAIA.</p>
</div></section>"""

P("portfolio.html", "Portfolio · GRAIA", "Projects and clients of GRAIA srl.",
  interna("Portfolio", "What we have done, and for whom.",
          "A few projects up close, then the list of clients of the work carried out over the years, grouped by type.")
  + CASI_EN
  + '<section class="pallida" id="committenti"><div class="wrap"><p class="eyebrow">Clients</p><h2 style="margin-bottom:2.5rem">Our clients</h2>'
  + gruppo("Ministries, authorities and agencies", [
      "Ministry of Agriculture, Food and Forestry Policies, Directorate-General for Fisheries and Aquaculture", "Po River Basin Authority",
      "Basin Authority of Lakes Iseo, Endine and Moro", "AIPO, Interregional Agency for the River Po", "ISPRA", "Italian-Swiss Fisheries Commission",
      "Lombardy Region", "Republic and Canton of Ticino", "City of Lugano"])
  + gruppo("Universities and research", ["Politecnico di Milano", "Politecnico di Torino", "University of Insubria", "University of Milan", "Leibniz Institute (Berlin)", "CNR-IRSA (Brugherio)"])
  + gruppo("Parks", ["Gran Paradiso National Park", "Foreste Casentinesi, Monte Falterona and Campigna National Park", "Ticino Valley Lombard Park", "Adamello Park", "Adda Nord Park", "Adda Sud Park",
      "Orobie Valtellinesi Park", "Oglio Nord Park", "Oglio Sud Park", "Alpe Veglia and Alpe Devero Nature Park", "Alta Val Sesia Nature Park", "Campo dei Fiori Regional Park", "Lake Montorfano Park"])
  + gruppo("Provincial administrations", ["Arezzo", "Bergamo", "Biella", "Brescia", "Cagliari", "Catanzaro", "Como", "Cuneo", "Latina", "Mantova", "Milano", "Novara", "Olbia-Tempio", "Pavia", "Prato", "Rieti", "Sondrio", "Varese", "Verbano Cusio Ossola", "Torino", "Vercelli"])
  + gruppo("Energy, consortia and private clients", ["A2A", "Edison", "Edipower", "ENEL Produzione", "ENEL Green Power", "IREN", "Italgen", "Consorzio di Bonifica Est Ticino Villoresi",
      "Consorzio di Bonifica Muzza – Bassa Lodigiana", "Consorzio del Ticino", "Consorzio Venezia Nuova", "Navigli Lombardi", "Holcim", "Technital", "CIRF, Italian Centre for River Restoration", "FIPSAS", "LIPU", "Fondazione Lombardia per l'Ambiente"])
  + "</div></section>", og="img/storione.jpg")

# ----------------------------------------------------------------- BLU
blu_li = "".join(f'<li><a href="../a-{s}.html" hreflang="it">{H.escape(EN_TITLES[s])}</a></li>' for s in D.BLU_SLUGS)
P("blu-progetti.html", "BLU Progetti · GRAIA", "Engineering company for ecological, ecosystem and environmental restoration.",
  interna("BLU Progetti", "The engineering company born from GRAIA.",
          "Since May 2006 the partners of GRAIA have also run BLU Progetti srl: design and works supervision for public and private clients, in ecological, ecosystem and environmental restoration.")
  + f"""<section style="padding-top:2rem"><div class="wrap due">
  <figure class="fig" style="margin:0"><img src="../img/riqualificazione.jpg" alt="Bioengineering works with logs and boulders on a shore" width="1600" height="1200" style="object-position:30% 62%"><figcaption>Shore restoration works.</figcaption></figure>
  <div><h2 style="margin-bottom:1rem">What BLU Progetti does</h2>
    <p>Where GRAIA studies and monitors, BLU Progetti designs and follows construction sites. The two companies share partners, skills and premises, and often work on the same projects.</p>
    <p>BLU Progetti is a partner of <strong>GE.RI.KO. MERA</strong>, funded by the Interreg V-A Italy–Switzerland 2014–2020 cooperation programme. <a href="portfolio.html#casi">Read the case</a>.</p>
    <p style="margin-top:1.5rem"><a class="btn" href="contatti.html">Talk to us</a></p></div>
</div></section>
<section class="pallida"><div class="wrap due"><div><p class="eyebrow">BLU Progetti activities</p><h2>Thirteen services, from study to site.</h2></div><ul class="elenco-att">{blu_li}</ul></div></section>""")

# ----------------------------------------------------------------- NEWS
righe = ""
last = None
for n in D.NEWS:
    y = D.anno(n)
    if y != last:
        righe += f'<h2 class="anno">{"Undated" if y == "Senza data" else y}</h2>'
        last = y
    righe += f'<article class="news-riga"><time>{n["date"] or "—"}</time><div><h3><a href="../news-{n["slug"]}.html" hreflang="it">{H.escape(n["title"])}</a></h3></div></article>'
P("news.html", "News · GRAIA", "News from GRAIA: projects, research, findings and events.",
  interna("News", "From the world of GRAIA.", "Projects, research, findings and events, from 2013 to today. Articles are currently in Italian.")
  + f'<section style="padding-top:2rem"><div class="wrap news-elenco">{righe}</div></section>')

# ----------------------------------------------------------------- CHI SIAMO
MOTTI = {"gentili": "Never trust too much!", "puzzi": "Believe in what you do!", "sartorelli": "Unity… with passion, makes strength!",
         "trasforini": "Let's learn from nature!", "ippoliti": "Slow and steady wins the race!", "luvie": "Not one watchword but three: collaboration, organisation, determination.",
         "ballerio": "Organisation!", "bonatto": "Passion is not work!"}
ROLES = {"Presidente": "Chairman", "Amministratore delegato": "Managing director", "Dipendente": "Employee", "Dipendente di BLU Progetti srl": "Employee of BLU Progetti srl"}
FIELDS = {"gentili": "Ecology of aquatic environments", "puzzi": "Ichthyology", "sartorelli": "Environmental and land engineering", "trasforini": "Applied ecology and nature conservation",
          "ippoliti": "Ecology of water bodies", "luvie": "Environmental assessment and monitoring", "ballerio": "Environmental monitoring", "bonatto": "Biomonitoring", "tresoldi": "Design and works supervision"}


def membro(m):
    mt = f'<p class="motto">“{MOTTI[m["id"]]}”</p>' if m["id"] in MOTTI else ""
    return f"""<article class="membro" id="{m['id']}" data-gruppo="{m['gruppo']}">
  <img src="../img/team/{m['foto']}" alt="Portrait of {m['nome']}" loading="lazy" width="350" height="360">
  <h3>{m['nome']}</h3><p class="ruolo">{ROLES[m['ruolo']]}</p><p class="attivita-prof">{FIELDS[m['id']]}</p>{mt}
  <p style="margin-top:1rem"><a href="../chi-siamo.html#{m['id']}" hreflang="it">Full biography (Italian)</a></p>
</article>"""


P("chi-siamo.html", "About us · GRAIA", "Three founding partners and more than 35 employees and collaborators: GRAIA's story and team since 1991.",
  interna("About us", "We love our work.", "We do it with passion because we believe in it. It is how the group has always introduced itself, and it is also the method.")
  + """<section style="padding-top:2rem"><div class="wrap due">
  <div class="testo-lungo">
    <p class="lead">GRAIA was founded in 1991 by four professionals in aquatic ecology and ichthyology, united by a passion for fish fauna and fishing.</p>
    <p>Over time the original core grew to include collaborators, environmental engineers and naturalists. Today three founding partners coordinate and lead more than 35 employees and collaborators, most of whom trained professionally inside the company.</p>
    <p>The relationship of listening, collaboration and transparency built within the group favours real teamwork, in which everyone shares motivation, goals and methods, respecting defined roles and rules.</p>
    <p style="font-size:.88rem;color:var(--grigio)">The company is registered in the National Research Register of the Ministry of University and Research, code 302816CX.</p>
  </div>
  <figure class="fig" style="margin:0"><img src="../img/lago-sede.jpg" alt="The shore of Lake Comabbio at Varano Borghi" width="1600" height="880" style="object-position:72% 50%"><figcaption>Lake Comabbio: the office is a few metres from the water.</figcaption></figure>
</div></section>
<section class="pallida"><div class="wrap"><p class="eyebrow">The team</p><h2 style="margin-bottom:2.5rem">Three partners and the people they work with.</h2>
  <div class="team-grid">""" + "".join(membro(m) for m in D.TEAM) + """</div></div></section>""")

# ----------------------------------------------------------------- CONTATTI
campo = 'style="width:100%;padding:.7rem;border:1px solid var(--linea);font:inherit"'
P("contatti.html", "Contact · GRAIA", "How to reach GRAIA in Varano Borghi (Varese, Italy) and how to contact us.",
  interna("Contact", "Write to us or come and visit.", "Our office is in Varano Borghi, a few metres from Lake Comabbio.")
  + f"""<section style="padding-top:2rem"><div class="wrap due">
  <div>
    <dl class="dati"><dt>Company</dt><dd>GRAIA srl, Gestione e Ricerca Ambientale Ittica Acque</dd><dt>Address</dt><dd>Viale Repubblica 1<br>21020 Varano Borghi (VA), Italy</dd>
      <dt>Phone</dt><dd><a href="tel:+390332961097">+39 0332 961 097</a></dd><dt>Fax</dt><dd>+39 0332 961 162</dd><dt>E-mail</dt><dd><a href="mailto:info@graia.eu">info@graia.eu</a></dd><dt>PEC</dt><dd>graia@pec.it</dd></dl>
    <h2 style="font-size:1.6rem;margin:3rem 0 1rem">Getting here</h2>
    <p><strong>By car.</strong> From Milan, take the A8 towards Varese. After the Lainate toll gate follow signs for Varese/Gravellona Toce (A26), exit at Vergiate/Sesto Calende and take the SS-629 towards Laveno-Luino. At the first traffic light turn right into via San Rocco in Corgeno di Vergiate, then left onto the SP-18 along Lake Comabbio. The office is on the left, about 200 m after the entrance to Varano Borghi.</p>
    <p><strong>By train.</strong> Nearest FS stations: Ternate (walking distance), Vergiate and Sesto Calende.</p>
    <p><a class="link-freccia" href="https://www.openstreetmap.org/search?query=Viale%20Repubblica%201%20Varano%20Borghi">Open the map</a></p>
  </div>
  <div>
    <form id="form-contatti" novalidate>
      <p class="eyebrow">Write to us</p>
      <p style="margin-bottom:.8rem"><label for="n">Name</label><br><input id="n" name="nome" autocomplete="name" required {campo}></p>
      <p style="margin-bottom:.8rem"><label for="e">E-mail</label><br><input id="e" name="email" type="email" autocomplete="email" required {campo}></p>
      <p style="margin-bottom:.8rem"><label for="o">Subject</label><br><select id="o" name="oggetto" {campo}><option>Information request</option><option>Quote or collaboration</option><option>Education and schools</option><option>Press</option><option>Other</option></select></p>
      <p><label for="m">Message</label><br><textarea id="m" name="messaggio" rows="6" required {campo}></textarea></p>
      <p style="font-size:.88rem;color:var(--grigio)"><label><input type="checkbox" id="c" required> I have read the <a href="privacy.html">privacy notice</a>.</label></p>
      <button class="btn" type="submit">Prepare the e-mail</button>
      <p id="esito" role="status" style="margin-top:1rem;color:var(--verde-scuro);font-weight:600"></p>
    </form>
    <p class="todo" style="margin-top:1.5rem">The form prepares an e-mail to <strong>info@graia.eu</strong> in the sender's mail program: no server stores messages, so no data passes through this site.</p>
  </div>
</div></section>
<script>
document.getElementById('form-contatti').addEventListener('submit',function(ev){{
  ev.preventDefault();var f=ev.target,esito=document.getElementById('esito');
  if(!f.nome.value.trim()||!f.email.value||!f.email.checkValidity()||!f.messaggio.value.trim()||!document.getElementById('c').checked){{esito.style.color='#a33';esito.textContent='Please fill in name, e-mail and message, and confirm you have read the notice.';return;}}
  var corpo=f.messaggio.value+'\\n\\n—\\n'+f.nome.value+' ('+f.email.value+')';
  location.href='mailto:info@graia.eu?subject='+encodeURIComponent(f.oggetto.value)+'&body='+encodeURIComponent(corpo);
  esito.style.color='';esito.textContent='Your mail program opens with the message ready to send.';
}});
</script>""")

# ----------------------------------------------------------------- DOCS / PRIVACY
P("documenti.html", "Downloads · GRAIA", "Downloadable documents.",
  interna("Downloads", "Documents and materials.", "Publications and project materials, hosted on GRAIA's current website.")
  + """<section style="padding-top:2rem"><div class="wrap"><ul class="news-lista">
    <li><time>PDF · Lombardy Region, 2011</time><div><h3><a href="https://www.graia.eu/wp-content/uploads/2017/07/Interventi-idraulici-ittiocompatibili.pdf">Fish-friendly hydraulic works: guidelines</a></h3><p>Quaderni della Ricerca no. 125, January 2011 (Italian).</p></div></li>
    <li><time>Project</time><div><h3><a href="https://www.graia.eu/proteggiamo-la-zsc-lago-la-vota/">Protecting the Lago la Vota SAC</a></h3><p>Project materials on the current website (Italian).</p></div></li>
  </ul></div></section>""")

P("privacy.html", "Privacy and cookies · GRAIA", "Short privacy notice for this draft site.",
  interna("Privacy and cookies", "No cookies, no tracking.", "Short-form notice for this draft. To be completed and validated by GRAIA's legal advisers before publication.")
  + """<section style="padding-top:2rem"><div class="wrap"><div class="prosa solo">
  <h2>Cookies</h2>
  <p>This draft sets no cookies and uses no analytics or third-party services that track browsing. Typefaces are hosted on the site itself, so visiting it sends no data to Google Fonts. That is why no consent banner is needed.</p>
  <p>If statistics, embedded maps or third-party videos are added later, a compliant consent banner will be required.</p>
  <h2>Personal data</h2>
  <p>The contact form does not send anything to a server: it prepares an e-mail in the sender's mail program. The data entered reaches GRAIA only if the user sends that message. Some links lead to graia.eu or project sites, which have their own notices.</p>
  <h2>Controller</h2>
  <p>G.R.A.I.A. srl, Viale Repubblica 1, 21020 Varano Borghi (VA), Italy. VAT no. 10454870154. <a href="mailto:info@graia.eu">info@graia.eu</a>.</p>
  <p class="todo">Text to be validated by GRAIA's adviser: purposes and legal bases, retention periods, data subject rights.</p>
</div></div></section>""")
