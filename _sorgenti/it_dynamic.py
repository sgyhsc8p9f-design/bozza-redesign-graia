"""Pagine italiane generate dai dati: attività, news, team, ricerca, documenti, privacy, BLU, contatti, proposta."""
import json
import re
import html as H
from pathlib import Path
from layout import page, interna

HERE = Path(__file__).resolve().parent
ACT = json.load(open(HERE / "data" / "attivita.json", encoding="utf-8"))
NEWS = json.load(open(HERE / "data" / "news.json", encoding="utf-8"))
ACT_BY = {a["slug"]: a for a in ACT}
NEWS_BY = {n["slug"]: n for n in NEWS}

pages = {}
search_index = []


def strip(h):
    return H.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))).strip()


# ------------------------------------------------------------------ TEAM
TEAM = [
    dict(id="gentili", gruppo="soci", nome="Gaetano Gentili", ruolo="Presidente", foto="gentili.jpg",
         studio="Dottore in Medicina Veterinaria, iscritto all'Ordine dei Medici Veterinari della Provincia di Varese con il n. 232",
         attivita="Ecologia degli ambienti acquatici; professore a contratto del corso di Acquacoltura all'Università degli Studi di Milano",
         bio="Mi chiamo Gaetano Gentili, sono veterinario dal 1988 e insieme ad amici e colleghi ho fondato GRAIA nel 1991. Ho cominciato la mia professione occupandomi di animali in ambiente naturale, poi la mia attività si è sempre più indirizzata verso l'ecologia degli ambienti fluviali, con particolare riferimento all'ecoidraulica. Le responsabilità, anche amministrative, in GRAIA mi portano comunque a seguire progetti più diversi nell'ambito della tutela e della gestione degli ambienti e delle risorse naturali. Ho la fortuna di lavorare con colleghi ed amici dalle formazioni e professionalità più diverse e questo non solo mi ha arricchito culturalmente ma mi consente di fare un lavoro straordinariamente vario e diverso quasi ogni giorno.",
         motto="Mai fidarsi troppo!"),
    dict(id="puzzi", gruppo="soci", nome="Cesare Mario Puzzi", ruolo="Amministratore delegato", foto="puzzi.jpg",
         studio="Dottore in Medicina Veterinaria, iscritto all'Ordine dei Medici Veterinari della Provincia di Milano con il n. 1648",
         attivita="Ittiologia; professore a contratto del corso di Gestione della fauna ittica selvatica d'acqua dolce all'Università degli Studi di Milano",
         bio="Mi chiamo Cesare Mario Puzzi, sono veterinario dal 1989 e insieme ad amici e colleghi ho fondato GRAIA nel 1991. La mia professione è l'ittiologia, nata dalla mia naturale passione per i pesci e per la pesca. Con gli anni e con un po' di esperienza acquisita grazie al lavoro multidisciplinare e alla necessità di capire anche i punti di vista di ingegneri, paesaggisti, agronomi, forestali, naturalisti, geologi, biologi, zootecnici e di molti altri professionisti, oggi mi occupo di progetti ambientali, il cui filo conduttore è sempre l'acqua. I corridoi fluviali e i passaggi per pesci, con le riqualifiche fluvio-lacustri, sono i temi che mi coinvolgono maggiormente e che mi emozionano ogni giorno.",
         motto="Credi in quello che fai!"),
    dict(id="sartorelli", gruppo="soci", nome="Massimo Sartorelli", ruolo="Amministratore delegato", foto="sartorelli.jpg",
         studio="Dottore in ingegneria civile per la difesa del suolo e la pianificazione territoriale (indirizzo ambientale), iscritto all'Ordine degli Ingegneri della Provincia di Varese con il n. 2096 e all'Ordine degli Ingegneri e Architetti del Canton Ticino con il n. 4271",
         attivita="Ingegneria dell'ambiente e del territorio; professore a contratto del corso di Valutazione d'impatto ambientale all'Università dell'Insubria di Varese",
         bio="Mi chiamo Massimo Sartorelli, sono ingegnere ambientale dal 1995 e dallo stesso anno con i miei colleghi ed amici ho contribuito a far crescere Graia nell'ambito della progettazione ambientale e paesaggistica. Seguo con passione la realizzazione di importanti interventi di riqualificazione ambientale occupandomi del coordinamento di un team affiatato di bravi professionisti. Il continuo confronto con colleghi aventi competenze differenti, mi ha permesso in questi anni di crescere professionalmente con loro. Credo molto nel lavoro di squadra per affrontare le sfide che ci aspetteranno nei prossimi anni.",
         motto="L'unione… con la passione, fanno la forza!"),
    dict(id="trasforini", gruppo="graia", nome="Stefania Trasforini", ruolo="Dipendente", foto="trasforini.jpg",
         studio="Dottore in Scienze Biologiche, iscritta all'Ordine Nazionale dei Biologi al n. 51042, Sezione A",
         attivita="Ecologia applicata e conservazione della natura",
         bio="Mi chiamo Stefania Trasforini, ho una laurea in scienze biologiche e faccio parte del team dal 1998. Mi occupo di conservazione della biodiversità e riqualificazione ecologica, operando all'interno di progetti di conservazione e gestione della fauna e delle reti ecologiche ed anche nell'ambito della valutazione ambientale e della divulgazione. Le mie principali mansioni sono: la gestione ed il coordinamento interno di progetti, la redazione di rapporti tecnici, l'elaborazione ed interpretazione di dati biologici, territoriali e ambientali, la stesura di proposte di progetto in campo faunistico ed ecologico; la realizzazione di pacchetti informatici per la gestione di dati ambientali e territoriali, la redazione e progettazione grafica di prodotti stampati e digitali destinati alla divulgazione e sensibilizzazione.",
         motto="Impariamo dalla natura!"),
    dict(id="ippoliti", gruppo="graia", nome="Alessandra Ippoliti", ruolo="Dipendente", foto="ippoliti.jpg",
         studio="Dottore in Scienze Biologiche, iscritta all'Ordine Nazionale dei Biologi con il n. 53869, Sezione A",
         attivita="Ecologia dei corpi idrici",
         bio="Mi chiamo Alessandra Ippoliti, sono laureata in scienze biologiche e faccio parte del team dal 2002. Mi occupo di monitoraggio biologico degli ecosistemi acquatici, conservazione e gestione delle risorse ambientali e faunistiche, con particolare riferimento allo studio dei popolamenti ittici e del loro stato di conservazione. Le mie principali mansioni sono: redazione di rapporti tecnici in campo ittico ed ecologico; elaborazione e interpretazione di dati biologici, territoriali e ambientali; redazione di piani di gestione di aree protette; elaborazione di Studi di Incidenza e Studi di Impatto Ambientale; redazione e progettazione grafica di prodotti destinati alla divulgazione; attività di educazione ambientale e scientifica, dalle elementari alle scuole di specializzazione post-universitaria.",
         motto="Chi la dura la vince!"),
    dict(id="luvie", gruppo="graia", nome="Chiara Luviè", ruolo="Dipendente", foto="luvie.jpg",
         studio="Dottore in Scienze Naturali. Master in «Gestione e conservazione dell'ambiente e della fauna»",
         attivita="Valutazione e monitoraggio ambientale",
         bio="Mi chiamo Chiara Luviè, ho una laurea in scienze naturali e ho conseguito il master in gestione e conservazione dell'ambiente e della fauna. Faccio parte del team dal 2006. Mi occupo principalmente di valutazione e monitoraggio ambientale. Le mie mansioni principali sono la gestione e il coordinamento di progetti, la stesura di relazioni, la redazione di cartografia tematica mediante sistemi informativi territoriali, l'organizzazione di banche dati ambientali, la stesura di proposte di progetti in campo ecologico.",
         motto="Non una parola d'ordine ma tre: collaborazione, organizzazione, determinazione."),
    dict(id="ballerio", gruppo="graia", nome="Alessandra Ballerio", ruolo="Dipendente", foto="ballerio.jpg",
         studio="Dottore in Scienze Ambientali",
         attivita="Monitoraggio ambientale",
         bio="Mi chiamo Alessandra Ballerio, ho una laurea in scienze ambientali e faccio parte del team dal 2010. Mi occupo di monitoraggio delle acque nell'ambito di progetti di valutazione degli effetti di sbarramenti e derivazioni idriche, di sperimentazione del deflusso minimo vitale e di analisi degli effetti della gestione del sedimento negli invasi artificiali. Le mie principali mansioni sono: la predisposizione di piani di monitoraggio, la stesura di progetti di gestione di invasi e di aste fluviali, l'elaborazione ed interpretazione di dati chimici, biologici ed ecotossicologici e la redazione di rapporti tecnici.",
         motto="Organizzazione!"),
    dict(id="bonatto", gruppo="graia", nome="Sonia Bonatto", ruolo="Dipendente", foto="bonatto.jpg",
         studio="Dottore in Scienze Biologiche",
         attivita="Biomonitoraggio",
         bio="Mi chiamo Sonia Bonatto, sono laureata in biologia e biologia marina. Faccio parte del team GRAIA dal 2010. Gestisco e coordino progetti di monitoraggio ambientale e progetti di riqualificazione ecologica, oltre a operare nel campo della valutazione di impatto ambientale e di incidenza. Per GRAIA, oltre a svolgere attività di monitoraggio e campionamento delle matrici biologiche, mi occupo della gestione e interpretazione dei dati chimici e biologici e della redazione di rapporti tecnici. Collaboro inoltre con enti pubblici e privati nell'ambito della stesura e attuazione di progetti di conservazione e gestione delle reti ecologiche.",
         motto="La passione non è lavoro!"),
    dict(id="tresoldi", gruppo="blu", nome="Elisa Tresoldi", ruolo="Dipendente di BLU Progetti srl", foto="tresoldi.jpg",
         studio="Geometra",
         attivita="Progettazione e direzione lavori",
         bio="Mi chiamo Elisa Tresoldi, sono diplomata come geometra e sono dipendente della società BluProgetti dalla fine del 2013. Lavoro a stretto contatto con il gruppo di ingegneri consulenti della società, occupandomi con loro della progettazione e della Direzione Lavori nell'ambito di interventi di riqualificazione ambientale, sistemi di fitodepurazione, realizzazione di passaggi per la risalita per la fauna ittica e altri interventi nel campo dell'ingegneria ambientale e naturalistica.",
         motto=None),
]


def membro(m):
    motto = f'<p class="motto">«{H.escape(m["motto"])}»</p>' if m["motto"] else ""
    return f"""<article class="membro" id="{m['id']}" data-gruppo="{m['gruppo']}">
  <img src="img/team/{m['foto']}" alt="Ritratto di {m['nome']}" loading="lazy" width="350" height="360">
  <h3>{m['nome']}</h3>
  <p class="ruolo">{m['ruolo']}</p>
  <p class="attivita-prof">{H.escape(m['attivita'])}</p>
  {motto}
  <details><summary>Titolo di studio e biografia</summary>
    <p><strong>Titolo di studio.</strong> {H.escape(m['studio'])}.</p>
    <p>{H.escape(m['bio'])}</p>
  </details>
</article>"""


pages["chi-siamo.html"] = page(
    "chi-siamo.html",
    "Chi siamo · GRAIA",
    "Tre soci fondatori e più di 35 tra dipendenti e collaboratori: la storia e il team di GRAIA dal 1991.",
    interna(
        "Chi siamo",
        "Il nostro lavoro ci piace.",
        "Lo facciamo con passione perché ci crediamo. È la frase con cui il gruppo si presenta da sempre, ed è anche il metodo.",
    )
    + """<section style="padding-top:2rem"><div class="wrap due">
  <div class="testo-lungo">
    <p class="lead">GRAIA è nata nel 1991 da quattro professionisti dell'ecologia acquatica e dell'ittiologia, uniti dalla passione per la fauna ittica e la pesca.</p>
    <p>Nel tempo il nucleo iniziale si è allargato a collaboratori, ingegneri ambientali e naturalisti. Oggi tre soci fondatori coordinano e guidano più di 35 tra dipendenti e collaboratori, che per la gran parte si sono formati professionalmente dentro la società.</p>
    <p>Il rapporto di ascolto, collaborazione e trasparenza che si è creato nel gruppo favorisce un vero lavoro di squadra, in cui tutti condividono motivazione, obiettivi e metodi, nel rispetto di ruoli e regole definiti.</p>
    <p style="font-size:.88rem;color:var(--grigio)">La società è iscritta allo Schedario Anagrafe Nazionale Ricerche del Ministero dell'Università e della Ricerca, codice 302816CX.</p>
  </div>
  <figure class="fig" style="margin:0"><img src="img/lago-sede.jpg" alt="La sponda del lago di Comabbio a Varano Borghi" width="1600" height="880" style="object-position:72% 50%"><figcaption>Il lago di Comabbio: la sede è a pochi metri dall'acqua.</figcaption></figure>
</div></section>
<section class="pallida"><div class="wrap">
  <p class="eyebrow">Il team</p>
  <h2 style="margin-bottom:1.5rem">Tre soci e le persone con cui lavorano.</h2>
  <div class="filtri" role="group" aria-label="Filtra il team">
    <button type="button" class="attivo" data-f="tutti">Tutti</button>
    <button type="button" data-f="soci">Soci fondatori</button>
    <button type="button" data-f="graia">Team GRAIA</button>
    <button type="button" data-f="blu">BLU Progetti</button>
  </div>
  <div class="team-grid">"""
    + "".join(membro(m) for m in TEAM)
    + """</div>
  <p class="todo" style="margin-top:2.5rem">Il sito attuale presenta nove persone con scheda; la società ne conta più di 35 tra dipendenti e collaboratori. Le altre schede vanno aggiunte con il materiale di GRAIA (foto, ruolo, breve profilo). Le foto sono quelle già pubblicate.</p>
</div></section>
<script>
document.querySelectorAll('.filtri button').forEach(function(b){b.addEventListener('click',function(){
  document.querySelectorAll('.filtri button').forEach(function(x){x.classList.remove('attivo')});b.classList.add('attivo');
  var f=b.dataset.f;document.querySelectorAll('.membro').forEach(function(m){m.hidden=!(f==='tutti'||m.dataset.gruppo===f)});});});
if(location.hash){var t=document.querySelector(location.hash);if(t){var d=t.querySelector('details');if(d)d.open=true;}}
</script>""",
)
for m in TEAM:
    search_index.append(dict(t=m["nome"], k="Team", u=f"chi-siamo.html#{m['id']}", x=m["ruolo"] + ". " + m["attivita"] + ". " + m["bio"][:400]))

# ------------------------------------------------------------------ ATTIVITA
AMBITI = [
    dict(id="ittiologia", n="01", titolo="Ittiologia e gestione della fauna ittica", img="luccio.jpg", pos="35% 50%", poster=False,
         testo="Il mestiere da cui siamo partiti: conoscere i pesci per proteggerli e gestirli.",
         slugs=["ittiologia", "carte-ittiche-e-piani-ittici", "acquacoltura-incubatoi-allevamento-ittico", "gestione-della-pesca-sportiva-e-professionale"]),
    dict(id="monitoraggio", n="02", titolo="Monitoraggio e valutazioni ambientali", img="lago-sede.jpg", pos="72% 50%", poster=False,
         testo="Dati raccolti sul campo e letti con rigore, per capire lo stato di fiumi e laghi e per le procedure di valutazione.",
         slugs=["ecologia-applicata-e-biomonitoraggio", "valutazioni-di-impatto-ambientale", "valutazione-di-incidenza-vi", "valutazione-ambientale-strategica-vas", "autorizzazione-integrata-ambientale-aia", "modellistica-ambientale", "urban-runoff-management", "studi-di-impatto-sulla-vegetazione"]),
    dict(id="riqualificazione", n="03", titolo="Riqualificazione, ingegneria naturalistica e territorio", img="riqualificazione.jpg", pos="30% 62%", poster=False,
         testo="Interventi che restituiscono spazio e funzioni ecologiche all'acqua e al territorio, anche con BLU Progetti.",
         slugs=["riqualificazione-fluviale", "ingegneria-naturalistica", "fitodepurazione-e-lagunaggio", "reti-ecologiche", "gestione-e-conservazione-di-ecosistemi-e-ambienti-di-alta-quota", "progettazione-e-dl-di-interventi-di-riqualificazione-e-rimboschimento-forestale", "gestione-delle-risorse-forestali", "paesaggistica-e-progettazione-del-verde", "agricoltura"]),
    dict(id="passaggi", n="04", titolo="Passaggi per pesci e idroelettrico", img="torrente.jpg", pos="50% 60%", poster=False,
         testo="Dove l'acqua incontra una diga o una traversa, i pesci devono poter passare.",
         slugs=["passaggi-per-pesci", "video-monitoraggio-delle-migrazioni-ittiche-nei-passaggi-per-pesci", "gestione-del-sedimento-negli-invasi-artificiali"]),
    dict(id="life", n="05", titolo="Programmi LIFE e ricerca europea", img="lifeel.jpg", pos="50% 50%", poster=True,
         testo="Progetti cofinanziati dall'Unione europea per specie e habitat, dal LIFE a Interreg e al PNRR.",
         slugs=["progetti-life", "progetto-life-predator", "programma-di-cooperazione-interreg", "eco4ticino-unalleanza-per-difendere-la-biodiversita-tra-italia-e-svizzera", "prospittico-progetto-sperimentale-per-il-monitoraggio-della-biodiversita-ittica-nei-corridoi-fluviali"]),
    dict(id="didattica", n="06", titolo="Didattica e divulgazione ambientale", img="didattica.jpg", pos="50% 55%", poster=False,
         testo="Raccontare l'acqua a chi la vive: scuole, cittadini, pescatori.",
         slugs=["divulgazione-e-didattica-ambientale"]),
]
assert sorted(s for a in AMBITI for s in a["slugs"]) == sorted(ACT_BY), set(ACT_BY) ^ {s for a in AMBITI for s in a["slugs"]}
AMBITO_OF = {s: a for a in AMBITI for s in a["slugs"]}

BLU_SLUGS = [
    "gestione-e-conservazione-di-ecosistemi-e-ambienti-di-alta-quota", "passaggi-per-pesci",
    "gestione-del-sedimento-negli-invasi-artificiali", "fitodepurazione-e-lagunaggio", "riqualificazione-fluviale",
    "ingegneria-naturalistica", "acquacoltura-incubatoi-allevamento-ittico", "urban-runoff-management",
    "modellistica-ambientale", "paesaggistica-e-progettazione-del-verde", "studi-di-impatto-sulla-vegetazione",
    "progettazione-e-dl-di-interventi-di-riqualificazione-e-rimboschimento-forestale", "gestione-delle-risorse-forestali",
]


def fix_links(h):
    def rep(m):
        u = m.group(1)
        mm = re.match(r"https?://www\.graia\.eu/chi-siamo/\?member=([A-Za-z]+)", u)
        if mm:
            key = mm.group(1).lower()
            ids = {t["id"]: t for t in TEAM}
            key = key if key in ids else next((i for i in ids if i.startswith(key[:5])), key)
            return f'href="chi-siamo.html#{key}"'
        mm = re.match(r"https?://www\.graia\.eu/le-nostre-attivita/([^/]+)/?$", u)
        if mm and mm.group(1) in ACT_BY:
            return f'href="a-{mm.group(1)}.html"'
        mm = re.match(r"https?://www\.graia\.eu/([^/]+)/?$", u)
        if mm and mm.group(1) in NEWS_BY:
            return f'href="news-{mm.group(1)}.html"'
        return m.group(0)
    h = re.sub(r'href="([^"]+)"', rep, h)
    h = re.sub(r"<a [^>]*>\s*(<br>)?\s*</a>", "", h)
    h = re.sub(r"<p>\s*(<br>)?\s*</p>", "", h)
    h = re.sub(r"(<br>\s*){3,}", "<br><br>", h)
    h = re.sub(r"<p>(.*?)</p>", lambda m: "<p>" + re.sub(r"(<br>\s*)+", "</p><p>", m.group(1)) + "</p>", h, flags=re.S)
    h = re.sub(r"<p>\s*</p>", "", h)
    return h.strip()



def clean_news(h):
    """Toglie il piè di pagina di WordPress (data, categoria, tag) e rifà le gallerie."""
    tags = []
    m = re.search(r'<i></i>\s*<a href="https://www\.graia\.eu/[^"]*">\d{1,2} [a-z]+ \d{4}</a>', h)
    if m:
        tags = re.findall(r'href="https://www\.graia\.eu/tag/[^"]+">([^<]+)</a>', h[m.start():])
        h = h[: m.start()]
    h = re.sub(r"<h3>\s*<i></i>\s*Photo Gallery</h3>", "", h)
    h = re.sub(r"<i></i>", "", h)

    def gallery(mm):
        items = re.findall(r'<li>\s*<a href="[^"]+">\s*<img[^>]*>\s*</a>\s*(.*?)\s*<a href="([^"]+)">Full size</a>\s*</li>', mm.group(0), re.S)
        if not items:
            return mm.group(0)
        figs = "".join(
            f'<figure><a href="{u}"><img src="{u}" alt="" loading="lazy"></a>' + (f"<figcaption>{c.strip()}</figcaption>" if c.strip() else "") + "</figure>"
            for c, u in items
        )
        return f'<div class="galleria">{figs}</div>'

    h = re.sub(r"<ul>(?:(?!</ul>).)*Full size(?:(?!</ul>).)*</ul>", gallery, h, flags=re.S)
    if tags:
        h += '<p class="meta">Etichette: ' + " · ".join(tags) + "</p>"
    return h


def lista_att(slugs):
    return "".join(f'<li><a href="a-{s}.html">{H.escape(ACT_BY[s]["title"])}</a></li>' for s in slugs)


def blocco(a):
    cls = "fig poster" if a["poster"] else "fig"
    return f"""<div class="sezione-attivita" id="{a['id']}">
  <figure class="{cls}" style="margin:0"><img src="img/{a['img']}" alt="" loading="lazy" style="object-position:{a['pos']}"></figure>
  <div>
    <p class="eyebrow">{a['n']}</p>
    <h2 style="font-size:2rem;margin-bottom:1rem">{a['titolo']}</h2>
    <p>{a['testo']}</p>
    <ul class="elenco-att">{lista_att(a['slugs'])}</ul>
  </div>
</div>"""


pages["attivita.html"] = page(
    "attivita.html",
    "Le nostre attività · GRAIA",
    "Ittiologia, monitoraggio, riqualificazione fluviale, passaggi per pesci, progetti LIFE e didattica ambientale.",
    interna(
        "Le nostre attività",
        "Sei ambiti, un solo filo conduttore.",
        "L'esperienza del nostro team e il suo assetto multidisciplinare, insieme all'affiatamento di tutto il gruppo di lavoro, sono la migliore garanzia di competenza e professionalità.",
    )
    + '<section style="padding-top:2rem"><div class="wrap">'
    + "".join(blocco(a) for a in AMBITI)
    + '<p class="todo" style="margin-top:1rem">Le trenta schede riprendono i testi del sito attuale. Si possono cercare dalla pagina <a href="cerca.html">Cerca</a>.</p>'
    + "</div></section>",
)

for i, a in enumerate(ACT):
    amb = AMBITO_OF[a["slug"]]
    sibs = amb["slugs"]
    k = sibs.index(a["slug"])
    prev = f'<a href="a-{sibs[k-1]}.html">← {H.escape(ACT_BY[sibs[k-1]]["title"])}</a>' if k > 0 else "<span></span>"
    nxt = f'<a href="a-{sibs[k+1]}.html">{H.escape(ACT_BY[sibs[k+1]]["title"])} →</a>' if k < len(sibs) - 1 else "<span></span>"
    secs = ""
    for titolo, items in a["sections"]:
        lis = "".join(f"<li>{fix_links(x)}</li>" for x in items)
        secs += f"<h3>{H.escape(titolo)}</h3><ul>{lis}</ul>"
    intro = f'<p class="intro-serv">{fix_links(a["intro"])}</p>' if a["intro"] else ""
    gall = ""
    if a["imgs"]:
        gall = '<div class="galleria">' + "".join(f'<img src="{s}" alt="" loading="lazy">' for s in a["imgs"]) + "</div>"
    blu = a["slug"] in BLU_SLUGS
    badge = '<p class="meta" style="margin-top:1rem">Attività svolta anche da <a href="blu-progetti.html">BLU Progetti</a>.</p>' if blu else ""
    title = a["title"]
    pages[f"a-{a['slug']}.html"] = page(
        f"a-{a['slug']}.html",
        f"{title} · GRAIA",
        strip(a["intro"] or a["body"])[:155],
        f"""<section class="hero interna" style="padding:0"><div class="testo">
  <p class="eyebrow"><a href="attivita.html" style="color:inherit">Attività</a> · <a href="attivita.html#{amb['id']}" style="color:inherit">{amb['titolo']}</a></p>
  <h1>{H.escape(title)}</h1>
</div></section>
<section style="padding-top:3rem"><div class="wrap det">
  <div class="prosa">{fix_links(a['body'])}{gall}</div>
  <aside class="lato">{intro}{secs}{badge}</aside>
</div>
<div class="wrap nav-pagine">{prev}{nxt}</div></section>""",
        og_image=(a["imgs"][0] if a["imgs"] else "img/luccio.jpg"),
    )
    search_index.append(dict(t=title, k="Attività", u=f"a-{a['slug']}.html", x=strip(a["body"]) + " " + strip(a["intro"]) + " " + " ".join(strip(x) for _, its in a["sections"] for x in its)))

# ------------------------------------------------------------------ NEWS
def anno(n):
    m = re.search(r"(\d{4})$", n["date"] or "")
    return m.group(1) if m else "Senza data"


for i, n in enumerate(NEWS):
    prev = f'<a href="news-{NEWS[i+1]["slug"]}.html">← {H.escape(NEWS[i+1]["title"])}</a>' if i + 1 < len(NEWS) else "<span></span>"
    nxt = f'<a href="news-{NEWS[i-1]["slug"]}.html">{H.escape(NEWS[i-1]["title"])} →</a>' if i > 0 else "<span></span>"
    hero = f'<figure class="fig-news"><img src="{n["hero"]}" alt=""></figure>' if n["hero"] else ""
    date = f'<time>{n["date"]}</time>' if n["date"] else "<time>Data non indicata sul sito attuale</time>"
    pages[f"news-{n['slug']}.html"] = page(
        f"news-{n['slug']}.html",
        f"{n['title']} · GRAIA",
        strip(clean_news(n["html"]))[:155],
        f"""<section class="hero interna" style="padding:0"><div class="testo">
  <p class="eyebrow"><a href="news.html" style="color:inherit">News</a> · {date}</p>
  <h1>{H.escape(n['title'])}</h1>
</div></section>
<section style="padding-top:3rem"><div class="wrap">
  {hero}
  <div class="prosa solo">{fix_links(clean_news(n['html']))}</div>
</div>
<div class="wrap nav-pagine">{prev}{nxt}</div></section>""",
        og_image=n["hero"] or "img/luccio.jpg",
    )
    search_index.append(dict(t=n["title"], k="News", u=f"news-{n['slug']}.html", x=strip(clean_news(n["html"]))))

righe = ""
last = None
for n in NEWS:
    y = anno(n)
    if y != last:
        righe += f'<h2 class="anno">{y}</h2>' if last is not None else f'<h2 class="anno">{y}</h2>'
        last = y
    righe += f"""<article class="news-riga"><time>{n['date'] or '—'}</time><div><h3><a href="news-{n['slug']}.html">{H.escape(n['title'])}</a></h3><p>{H.escape(strip(clean_news(n['html']))[:190])}…</p></div></article>"""

pages["news.html"] = page(
    "news.html",
    "News · GRAIA",
    "Le news dal mondo GRAIA: progetti, ricerche, ritrovamenti e appuntamenti.",
    interna("News", "Dal mondo GRAIA.", "Progetti, ricerche, ritrovamenti e appuntamenti, dal 2013 a oggi.")
    + f'<section style="padding-top:2rem"><div class="wrap news-elenco">{righe}</div></section>',
)

# ------------------------------------------------------------------ BLU
blu_li = "".join(f'<li><a href="a-{s}.html">{H.escape(ACT_BY[s]["title"])}</a></li>' for s in BLU_SLUGS)
pages["blu-progetti.html"] = page(
    "blu-progetti.html",
    "BLU Progetti · GRAIA",
    "Società di ingegneria per la riqualificazione ecologica, ecosistemica e ambientale.",
    interna(
        "BLU Progetti",
        "La società di ingegneria nata da GRAIA.",
        "Dal maggio 2006 gli stessi soci di GRAIA hanno costituito BLU Progetti srl: progettazione e direzione lavori per soggetti pubblici e privati, nel campo della riqualificazione ecologica, ecosistemica e ambientale.",
    )
    + f"""<section style="padding-top:2rem"><div class="wrap due">
  <figure class="fig" style="margin:0"><img src="img/riqualificazione.jpg" alt="Intervento di ingegneria naturalistica con tronchi e massi" width="1600" height="1200" style="object-position:30% 62%"><figcaption>Intervento di riqualificazione di una riva.</figcaption></figure>
  <div>
    <h2 style="margin-bottom:1rem">Cosa fa BLU Progetti</h2>
    <p>Dove GRAIA studia e monitora, BLU Progetti progetta e segue i cantieri. Le due società condividono soci, competenze e sede, e lavorano spesso sugli stessi progetti.</p>
    <p>BLU Progetti è partner del progetto <strong>GE.RI.KO. MERA</strong>, finanziato dal Programma di cooperazione Interreg V-A Italia–Svizzera 2014–2020: una strategia comune tra i due Paesi per la gestione delle acque del bacino del Mera. <a href="portfolio.html#casi">Leggi il caso</a>.</p>
    <p style="margin-top:1.5rem"><a class="btn" href="contatti.html">Parla con noi</a></p>
  </div>
</div></section>
<section class="pallida"><div class="wrap due">
  <div><p class="eyebrow">Le attività di BLU Progetti</p><h2>Tredici servizi, dallo studio al cantiere.</h2></div>
  <ul class="elenco-att">{blu_li}</ul>
</div></section>""",
)

# ------------------------------------------------------------------ CONTATTI
campo = 'style="width:100%;padding:.7rem;border:1px solid var(--linea);font:inherit"'
pages["contatti.html"] = page(
    "contatti.html",
    "Contatti · GRAIA",
    "Come raggiungere GRAIA a Varano Borghi (VA) e come contattarci.",
    interna("Contatti", "Scrivici o vieni a trovarci.", "La sede è a Varano Borghi, a pochi metri dal lago di Comabbio.")
    + f"""<section style="padding-top:2rem"><div class="wrap due">
  <div>
    <dl class="dati">
      <dt>Società</dt><dd>GRAIA srl, Gestione e Ricerca Ambientale Ittica Acque</dd>
      <dt>Indirizzo</dt><dd>Viale Repubblica 1<br>21020 Varano Borghi (VA)</dd>
      <dt>Telefono</dt><dd><a href="tel:+390332961097">+39 0332 961 097</a></dd>
      <dt>Fax</dt><dd>+39 0332 961 162</dd>
      <dt>E-mail</dt><dd><a href="mailto:info@graia.eu">info@graia.eu</a></dd>
      <dt>PEC</dt><dd>graia@pec.it</dd>
    </dl>
    <h2 style="font-size:1.6rem;margin:3rem 0 1rem">Come arrivare</h2>
    <p><strong>In auto.</strong> Da Milano, A8 verso Varese. Dopo la barriera di Lainate seguire Varese/Gravellona Toce (A26), uscire a Vergiate/Sesto Calende e imboccare la SS-629 verso Laveno-Luino. Al primo semaforo a destra in via San Rocco a Corgeno di Vergiate, poi a sinistra sulla SP-18 lungo il lago di Comabbio. La sede è sulla sinistra, circa 200 m dopo l'ingresso a Varano Borghi.</p>
    <p><strong>In treno.</strong> Stazioni FS più vicine: Ternate (si raggiunge a piedi), Vergiate e Sesto Calende.</p>
    <p><a class="link-freccia" href="https://www.openstreetmap.org/search?query=Viale%20Repubblica%201%20Varano%20Borghi">Apri la mappa</a></p>
  </div>
  <div>
    <form id="form-contatti" novalidate>
      <p class="eyebrow">Scrivici</p>
      <p style="margin-bottom:.8rem"><label for="n">Nome</label><br><input id="n" name="nome" autocomplete="name" required {campo}></p>
      <p style="margin-bottom:.8rem"><label for="e">E-mail</label><br><input id="e" name="email" type="email" autocomplete="email" required {campo}></p>
      <p style="margin-bottom:.8rem"><label for="o">Argomento</label><br>
        <select id="o" name="oggetto" {campo}><option>Richiesta di informazioni</option><option>Preventivo o collaborazione</option><option>Didattica e scuole</option><option>Stampa e comunicazione</option><option>Altro</option></select></p>
      <p><label for="m">Messaggio</label><br><textarea id="m" name="messaggio" rows="6" required {campo}></textarea></p>
      <p style="font-size:.88rem;color:var(--grigio)"><label><input type="checkbox" id="c" required> Ho letto l'<a href="privacy.html">informativa privacy</a>.</label></p>
      <button class="btn" type="submit">Prepara l'e-mail</button>
      <p id="esito" role="status" style="margin-top:1rem;color:var(--verde-scuro);font-weight:600"></p>
    </form>
    <p class="todo" style="margin-top:1.5rem">Il modulo compila un'e-mail per <strong>info@graia.eu</strong> nel programma di posta di chi scrive: non c'è un server che conservi i messaggi, quindi nessun dato passa da questo sito. Per un invio diretto servirà un servizio di ricezione, da scegliere con GRAIA.</p>
  </div>
</div></section>
<script>
document.getElementById('form-contatti').addEventListener('submit',function(ev){{
  ev.preventDefault();var f=ev.target,esito=document.getElementById('esito');
  if(!f.nome.value.trim()||!f.email.checkValidity()||!f.email.value||!f.messaggio.value.trim()||!document.getElementById('c').checked){{esito.style.color='#a33';esito.textContent='Compila nome, e-mail e messaggio e conferma di aver letto l\\'informativa.';return;}}
  var corpo=f.messaggio.value+'\\n\\n—\\n'+f.nome.value+' ('+f.email.value+')';
  location.href='mailto:info@graia.eu?subject='+encodeURIComponent(f.oggetto.value)+'&body='+encodeURIComponent(corpo);
  esito.style.color='';esito.textContent='Si apre il tuo programma di posta con il messaggio pronto da inviare.';
}});
</script>""".replace("{{", "{").replace("}}", "}"),
)

# ------------------------------------------------------------------ DOCUMENTI
pages["documenti.html"] = page(
    "documenti.html",
    "Download · GRAIA",
    "Documenti scaricabili: linee guida per interventi idraulici ittiocompatibili e materiali di progetto.",
    interna("Download", "Documenti e materiali.", "Pubblicazioni e materiali di progetto, ospitati sul sito attuale di GRAIA.")
    + """<section style="padding-top:2rem"><div class="wrap">
  <ul class="news-lista">
    <li><time>PDF · Regione Lombardia, 2011</time><div><h3><a href="https://www.graia.eu/wp-content/uploads/2017/07/Interventi-idraulici-ittiocompatibili.pdf">Interventi idraulici ittiocompatibili: linee guida</a></h3><p>Quaderni della Ricerca n. 125, gennaio 2011.</p></div></li>
    <li><time>Progetto</time><div><h3><a href="https://www.graia.eu/proteggiamo-la-zsc-lago-la-vota/">Proteggiamo la ZSC Lago la Vota</a></h3><p>Materiali del progetto, sul sito attuale.</p></div></li>
  </ul>
  <p class="todo" style="margin-top:2rem">I file restano sul sito attuale: nella versione definitiva andrebbero migrati qui, con titolo, anno e dimensione del file per ciascuno.</p>
</div></section>""",
)

# ------------------------------------------------------------------ PRIVACY
pages["privacy.html"] = page(
    "privacy.html",
    "Privacy e cookie · GRAIA",
    "Informativa breve su cookie e dati personali di questa bozza di sito.",
    interna("Privacy e cookie", "Nessun cookie, nessun tracciamento.", "Informativa in forma breve per questa bozza. Va completata e validata da chi cura gli aspetti legali di GRAIA prima della pubblicazione.")
    + """<section style="padding-top:2rem"><div class="wrap"><div class="prosa solo">
  <h2>Cookie</h2>
  <p>Questa bozza non imposta cookie, non usa strumenti di analisi né servizi di terze parti che tracciano la navigazione. I caratteri tipografici sono ospitati sul sito stesso, quindi la visita non invia dati a Google Fonts. Per questo non serve un banner di consenso.</p>
  <p>Se in futuro si aggiungessero statistiche, mappe incorporate o video di terzi, servirà un banner di consenso conforme: il rifiuto dovrà essere semplice quanto l'accettazione e i servizi non essenziali non dovranno partire prima della scelta.</p>
  <h2>Dati personali</h2>
  <p>Il modulo nella pagina Contatti non invia nulla a un server: prepara un'e-mail nel programma di posta di chi scrive. I dati che vi si inseriscono arrivano a GRAIA solo se l'utente invia quel messaggio.</p>
  <p>Alcuni link (documenti, video, articoli completi) portano al sito attuale graia.eu o a siti di progetto, che hanno le proprie informative.</p>
  <h2>Titolare</h2>
  <p>G.R.A.I.A. srl, Viale Repubblica 1, 21020 Varano Borghi (VA). P. IVA 10454870154. <a href="mailto:info@graia.eu">info@graia.eu</a>.</p>
  <p class="todo">Testo da validare con il consulente di GRAIA: finalità e basi giuridiche, tempi di conservazione, diritti dell'interessato e riferimento al Garante.</p>
</div></div></section>""",
)

# ------------------------------------------------------------------ CERCA
pages["cerca.html"] = page(
    "cerca.html",
    "Cerca · GRAIA",
    "Cerca tra attività, news e team di GRAIA.",
    interna("Cerca", "Cerca nel sito.", "Attività, news e persone: scrivi una parola e premi invio.")
    + """<section style="padding-top:2rem"><div class="wrap"><div class="prosa solo">
  <form id="fc" role="search"><label for="q" class="eyebrow" style="display:block">Cerca</label>
    <input id="q" type="search" autocomplete="off" placeholder="ad esempio: anguilla, passaggi per pesci, VIA" style="width:100%;padding:.9rem;border:1px solid var(--inchiostro);font:inherit;font-size:1.1rem"></form>
  <p id="n-ris" style="margin:1rem 0;color:var(--grigio)"></p>
  <ol id="ris" class="risultati"></ol>
</div></div></section>
<script src="cerca-indice.js"></script>
<script>
(function(){
  var N=function(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')};
  var q=document.getElementById('q'),ol=document.getElementById('ris'),nr=document.getElementById('n-ris');
  function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function run(){
    var v=N(q.value).trim();ol.innerHTML='';
    if(v.length<2){nr.textContent='';return;}
    var terms=v.split(/\\s+/),out=[];
    INDICE.forEach(function(d){
      var t=N(d.t),x=N(d.x),s=0,ok=true;
      terms.forEach(function(w){var a=t.indexOf(w)>-1,b=x.split(w).length-1;if(!a&&!b)ok=false;s+=(a?10:0)+Math.min(b,5);});
      if(ok)out.push([s,d]);
    });
    out.sort(function(a,b){return b[0]-a[0]});
    nr.textContent=out.length?out.length+' risultati':'Nessun risultato.';
    out.slice(0,40).forEach(function(r){
      var d=r[1],x=N(d.x),i=x.indexOf(terms[0]);if(i<0)i=0;
      var sn=d.x.substr(Math.max(0,i-60),170);
      var li=document.createElement('li');
      li.innerHTML='<span class="tipo">'+esc(d.k)+'</span> <a href="'+d.u+'">'+esc(d.t)+'</a><p>…'+esc(sn)+'…</p>';
      ol.appendChild(li);
    });
  }
  q.addEventListener('input',run);document.getElementById('fc').addEventListener('submit',function(e){e.preventDefault();run()});
  var m=location.search.match(/[?&]q=([^&]+)/);if(m){q.value=decodeURIComponent(m[1].replace(/\\+/g,' '));run();}
})();
</script>""",
)
