#!/usr/bin/env python3
"""Genera le pagine HTML della bozza GRAIA. Uso: python3 _sorgenti/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAV = [
    ("attivita.html", "Attività"),
    ("portfolio.html", "Portfolio"),
    ("blu-progetti.html", "BLU Progetti"),
    ("news.html", "News"),
    ("chi-siamo.html", "Chi siamo"),
    ("contatti.html", "Contatti"),
]


def page(fname, title, desc, body):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == fname else ""}>{t}</a></li>' for h, t in NAV
    )
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v=9">
</head>
<body>
<div class="bozza"><b>Bozza di proposta</b>: non è il sito ufficiale di GRAIA. Testi e immagini sono ripresi da graia.eu a solo scopo dimostrativo. <a href="proposta.html" style="color:#fff">Cosa cambia →</a></div>
<header class="site">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="GRAIA, home"><img src="img/logo.png" alt="GRAIA" width="145" height="58"></a>
    <button class="burger" aria-expanded="false" aria-controls="menu">Menu</button>
    <nav class="main" id="menu" aria-label="Principale"><ul>{nav}</ul></nav>
    <span class="lang"><b>IT</b> · EN</span>
  </div>
</header>
<main>
{body}
</main>
<footer class="site">
  <div class="wrap">
    <div class="griglia">
      <div>
        <a class="logo-footer" href="index.html"><img src="img/logo.png" alt="GRAIA"></a>
        <p><strong>G.R.A.I.A. srl</strong><br>Gestione e Ricerca Ambientale Ittica Acque<br>Viale Repubblica 1, 21020 Varano Borghi (VA)</p>
        <p>Tel. <a href="tel:+390332961097">+39 0332 961 097</a><br><a href="mailto:info@graia.eu">info@graia.eu</a> · PEC graia@pec.it</p>
        <p class="partner">Graia è partner di Life Natura<br><img src="img/life-natura.png" alt="Life Natura"></p>
      </div>
      <div>
        <h4>Il sito</h4>
        <ul>
          <li><a href="attivita.html">Le nostre attività</a></li>
          <li><a href="portfolio.html">Portfolio</a></li>
          <li><a href="blu-progetti.html">BLU Progetti</a></li>
          <li><a href="news.html">News</a></li>
          <li><a href="chi-siamo.html">Chi siamo</a></li>
          <li><a href="contatti.html">Contatti</a></li>
        </ul>
      </div>
      <div>
        <h4>Documenti</h4>
        <ul>
          <li><a href="https://www.graia.eu/wp-content/uploads/2017/07/Interventi-idraulici-ittiocompatibili.pdf">Interventi idraulici ittiocompatibili: linee guida (Regione Lombardia, 2011)</a></li>
          <li><a href="https://www.graia.eu/proteggiamo-la-zsc-lago-la-vota/">Proteggiamo la ZSC Lago la Vota</a></li>
          <li><a href="proposta.html">Cookie policy e privacy: da rifare</a></li>
        </ul>
      </div>
    </div>
    <p class="legale">P. IVA 10454870154. Gli aiuti di Stato e gli aiuti de minimis ricevuti dalla nostra impresa sono contenuti nel Registro nazionale degli aiuti di Stato di cui all'art. 52 della L. 234/2012 e consultabili sulla pagina del RNA, inserendo come chiave di ricerca il codice fiscale della società. Il CF di GRAIA è 10454870154 e quello di Blu Progetti è 02935220125.</p>
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


pages = {}

# ---------------------------------------------------------------- HOME
pages["index.html"] = page(
    "index.html",
    "GRAIA · Gestione Ricerca Ambientale Ittica Acque",
    "Dal 1991 a servizio dell'uomo e della natura: ittiologia, riqualificazione fluviale e ricerca ambientale a Varano Borghi (VA).",
    """
<section class="hero" style="padding:0">
  <div class="testo">
    <p class="eyebrow">Gestione Ricerca Ambientale Ittica Acque</p>
    <h1>Dal 1991 a servizio dell'uomo e della natura.</h1>
    <p>Conserviamo le risorse naturali e cerchiamo di rendere la presenza e le attività umane il più possibile compatibili con l'ambiente.</p>
    <div class="azioni">
      <a class="btn" href="attivita.html">Cosa facciamo</a>
      <a class="btn ghost" href="contatti.html">Scrivici</a>
    </div>
  </div>
  <figure class="foto" style="margin:0">
    <img src="img/luccio.jpg" alt="Un luccio in mezzo alla vegetazione acquatica" width="1800" height="1180">
    <figcaption>Foto: archivio GRAIA</figcaption>
  </figure>
</section>

<section>
  <div class="wrap due">
    <div>
      <p class="eyebrow">Graia in poche righe</p>
      <h2>Quattro professionisti, un'unica passione: i pesci e l'acqua.</h2>
    </div>
    <div>
      <p class="lead">La società è nata nel 1991 da un'iniziativa di quattro professionisti dell'ecologia acquatica e dell'ittiologia, uniti dalla passione per la fauna ittica e la pesca. Il lavoro ci piace, e lo facciamo con passione perché ci crediamo.</p>
      <ul class="fatti">
        <li><span class="k">1991</span><span class="v">anno di fondazione a Varano Borghi, sul lago di Comabbio</span></li>
        <li><span class="k">3 + 35</span><span class="v">tre soci fondatori che guidano più di trenta tra dipendenti e collaboratori, in gran parte cresciuti dentro la società</span></li>
        <li><span class="k">2006</span><span class="v">nasce BLU Progetti, la società di ingegneria degli stessi soci</span></li>
      </ul>
      <p style="margin-top:1.6rem"><a class="link-freccia" href="chi-siamo.html">Conosci il team</a></p>
    </div>
  </div>
</section>

<section class="pallida">
  <div class="wrap due">
    <div class="sticky">
      <p class="eyebrow">Cosa facciamo</p>
      <h2>Sei ambiti di lavoro, un filo conduttore: l'acqua.</h2>
      <p style="margin-top:1.2rem;color:var(--grigio)">Un assetto multidisciplinare, costruito in oltre trent'anni, è la nostra garanzia di competenza.</p>
      <p><a class="link-freccia" href="attivita.html">Tutte le attività</a></p>
    </div>
    <ol class="attivita">
      <li><span class="n">01</span><div><h3>Ittiologia e gestione della fauna ittica</h3></div><p>Carte e piani ittici, conservazione delle specie, incubatoi, acquacoltura, pesca sportiva e professionale.</p></li>
      <li><span class="n">02</span><div><h3>Monitoraggio e analisi ambientale</h3></div><p>Biomonitoraggio, limnologia, analisi statistica, batimetria, qualità delle acque.</p></li>
      <li><span class="n">03</span><div><h3>Riqualificazione fluviale e lacustre</h3></div><p>Ripristino della continuità fluviale, riqualificazione ecologica, rimboschimento, fitodepurazione.</p></li>
      <li><span class="n">04</span><div><h3>Passaggi per pesci e idroelettrico</h3></div><p>Progettazione e monitoraggio delle migrazioni, deflusso minimo vitale, svasi.</p></li>
      <li><span class="n">05</span><div><h3>Programmi LIFE e ricerca europea</h3></div><p>Progetti per la conservazione di specie e habitat, cambiamenti climatici, reti ecologiche.</p></li>
      <li><span class="n">06</span><div><h3>Didattica e divulgazione ambientale</h3></div><p>Percorsi nelle scuole, libri e allestimenti, eventi per il territorio.</p></li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Progetti in primo piano</p>
    <h2 style="max-width:18ch;margin-bottom:2.5rem">Dalla ricerca al territorio.</h2>
    <div class="progetto-grande">
      <img src="img/lifeel.jpg" alt="Locandina di LIFEEL Days a Comacchio" loading="lazy" width="1800" height="963">
      <div>
        <p class="meta">20 aprile 2026 · Comacchio, Manifattura dei Marinati</p>
        <h3 style="font-size:2rem">LIFEEL Days</h3>
        <p style="margin-top:.8rem">Non solo la conclusione formale del progetto: un momento di restituzione al territorio, in cui la conservazione dell'anguilla europea diventa responsabilità collettiva e occasione di dialogo tra scienza, istituzioni e cittadini.</p>
        <a class="link-freccia" href="news.html">Leggi la news</a>
      </div>
    </div>
    <div class="righe-progetti">
      <article class="riga-progetto">
        <img src="img/prospittico.png?v=2" alt="Loghi del progetto ProSpIttiCo: Unione europea, Ministero dell'Università e della Ricerca, Italia domani, NBFC" loading="lazy">
        <p class="meta">PNRR · National Biodiversity Future Center</p>
        <h3>ProSpIttiCo</h3>
        <p>Un sistema per monitorare le specie ittiche che transitano nei passaggi per pesci. GRAIA è l'unico soggetto beneficiario. La piattaforma con la versione beta è in arrivo.</p>
      </article>
      <article class="riga-progetto">
        <img src="img/eco4ticino.png?v=2" alt="ECO4TICINO, progetto Interreg Italia-Svizzera" loading="lazy">
        <p class="meta">Interreg Italia–Svizzera · 2025–2027</p>
        <h3>ECO4TICINO</h3>
        <p>Un corridoio ecologico da gestire insieme, oltre confine, lungo il fiume Ticino.</p>
      </article>
    </div>
  </div>
</section>

<section class="acqua">
  <div class="wrap blu">
    <div>
      <p class="eyebrow" style="color:var(--abisso)">BLU Progetti</p>
      <h2>Dallo studio al cantiere.</h2>
    </div>
    <div>
      <p class="lead">Dal 2006 gli stessi soci di GRAIA hanno fondato BLU Progetti, società di ingegneria per la riqualificazione ecologica, ecosistemica e ambientale.</p>
      <p>Progettazione e direzione lavori per committenti pubblici e privati. Partner del progetto GE.RI.KO. MERA, Interreg V-A Italia–Svizzera 2014–2020.</p>
      <a class="link-freccia" href="blu-progetti.html">Conosci BLU Progetti</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Alcuni dei nostri clienti</p>
    <h2 style="max-width:22ch;margin-bottom:2rem">Scelti da enti e aziende che conoscono bene l'acqua.</h2>
    <ul class="committenti">
      <li>Ministero delle Politiche Agricole, Alimentari e Forestali</li>
      <li>ISPRA</li>
      <li>Autorità di Bacino del Fiume Po</li>
      <li>AIPO, Agenzia Interregionale per il fiume Po</li>
      <li>Regione Lombardia</li>
      <li>Repubblica e Cantone del Ticino</li>
      <li>Parco Nazionale del Gran Paradiso</li>
      <li>Parco Lombardo della Valle del Ticino</li>
      <li>Politecnico di Milano e di Torino</li>
      <li>Università dell'Insubria e di Milano</li>
      <li>CNR-IRSA</li>
      <li>ENEL, Edison, A2A, IREN</li>
    </ul>
    <p style="margin-top:1.6rem"><a class="link-freccia" href="portfolio.html#committenti">L'elenco completo</a> &nbsp; <a class="link-freccia" href="portfolio.html#casi">I casi</a></p>
  </div>
</section>

<section class="pallida">
  <div class="wrap">
    <p class="eyebrow">News dal mondo GRAIA</p>
    <ul class="news-lista" style="margin-top:1.5rem">
      <li><time>20 aprile 2026</time><div><h3><a href="news.html">LIFEEL Days</a></h3><p>Il progetto si chiude con un momento di restituzione al territorio.</p></div></li>
      <li><time>20 ottobre 2025</time><div><h3><a href="news.html">ProSpIttiCo: manca poco al lancio della piattaforma</a></h3><p>Online la versione beta del sistema di monitoraggio in sviluppo.</p></div></li>
      <li><time>1 settembre 2025</time><div><h3><a href="news.html">ProSpIttiCo: prosegue la raccolta dei dati</a></h3><p>Il monitoraggio della biodiversità ittica nei corridoi fluviali va avanti.</p></div></li>
    </ul>
    <p style="margin-top:1.6rem"><a class="link-freccia" href="news.html">Tutte le news</a></p>
  </div>
</section>
""",
)

# ---------------------------------------------------------------- ATTIVITA
def blocco(img, alt, n, titolo, testo, elenco, pos="50% 50%", poster=False):
    li = "".join(f"<li>{x}</li>" for x in elenco)
    return f"""<div class="sezione-attivita">
  <figure class="fig{' poster' if poster else ''}" style="margin:0"><img src="img/{img}" alt="{alt}" loading="lazy" style="object-position:{pos}"></figure>
  <div>
    <p class="eyebrow">{n}</p>
    <h2 style="font-size:2rem;margin-bottom:1rem">{titolo}</h2>
    <p>{testo}</p>
    <ul>{li}</ul>
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
    + blocco("luccio.jpg", "Un luccio tra le piante acquatiche", "01", "Ittiologia e gestione della fauna ittica",
             "Il mestiere da cui siamo partiti: conoscere i pesci per proteggerli e gestirli.",
             ["Carte ittiche e piani ittici", "Conservazione delle specie", "Incubatoi ittici e acquacoltura", "Pesca sportiva e professionale"], pos="35% 50%")
    + blocco("lago-sede.jpg", "Il lago di Comabbio visto dalla riva", "02", "Monitoraggio e analisi ambientale",
             "Dati raccolti sul campo, letti con rigore statistico, per capire lo stato di fiumi e laghi.",
             ["Biomonitoraggio e limnologia", "Analisi statistica", "Batimetria", "Inquinamento delle acque, salute umana"], pos="72% 50%")
    + blocco("riqualificazione.jpg", "Un intervento di ingegneria naturalistica con tronchi e massi sulla riva", "03", "Riqualificazione fluviale e lacustre",
             "Interventi che restituiscono spazio e funzioni ecologiche all'acqua, anche con BLU Progetti.",
             ["Ripristino della continuità fluviale", "Riqualificazione ecologica di rive e ambienti lacustri", "Rimboschimento e fitodepurazione", "Percorsi ciclopedonali e greenway"], pos="30% 62%")
    + blocco("torrente.jpg", "Un torrente di acqua turchese in una forra di roccia", "04", "Passaggi per pesci e idroelettrico",
             "Dove l'acqua incontra una diga o una traversa, i pesci devono poter passare.",
             ["Progettazione dei passaggi per pesci", "Monitoraggio delle migrazioni ittiche", "Deflusso minimo vitale (DMV)", "Svasi e valutazioni di impatto"], pos="50% 60%")
    + blocco("lifeel.jpg", "Locandina di LIFEEL Days", "05", "Programmi LIFE e ricerca europea",
             "Progetti cofinanziati dall'Unione europea per specie e habitat. Il più recente: LIFEEL, per l'anguilla europea.",
             ["Programma LIFE", "Cambiamenti climatici", "Reti ecologiche", "Ricerca: ProSpIttiCo, ECO4TICINO"], pos="50% 50%", poster=True)
    + blocco("didattica.jpg", "Un libro gigante illustrato sul ciclo dell'acqua, allestito su un molo", "06", "Didattica e divulgazione ambientale",
             "Raccontare l'acqua a chi la vive: scuole, cittadini, pescatori.",
             ["Didattica ambientale", "Allestimenti e libri illustrati", "Eventi e incontri sul territorio"], pos="50% 55%")
    + "</div></section>",
)

# ---------------------------------------------------------------- PORTFOLIO
def gruppo(titolo, voci):
    li = "".join(f"<li>{v}</li>" for v in voci)
    return f'<div class="gruppo"><h3>{titolo}</h3><ul class="committenti">{li}</ul></div>'



CASI = """<section style="padding-top:2rem" id="casi"><div class="wrap">
  <p class="eyebrow">Casi</p>
  <h2 style="max-width:20ch;margin-bottom:2.5rem">Progetti raccontati da vicino.</h2>

  <article class="caso-grande">
    <figure class="fig" style="margin:0"><img src="img/storione.jpg" alt="Uno storione cobice che nuota su un fondale di ghiaia e alghe" loading="lazy" style="object-position:30% 50%"><figcaption>Storione cobice. Foto: archivio GRAIA.</figcaption></figure>
    <div>
      <p class="meta">LIFE CON.FLU.PO · LIFE11 NAT/IT/188 · concluso il 30 giugno 2018</p>
      <h3>Aprire il Po allo storione cobice</h3>
      <p>Il progetto ha ripristinato la connettività nel bacino del Po, riaprendo la via migratoria allo storione cobice (<i>Acipenser naccarii</i>) e ad altre dieci specie ittiche dell'Allegato II della direttiva Habitat.</p>
      <p>Il 3 aprile 2019 il primo storione cobice, lungo circa un metro e mezzo, è transitato nel passaggio per pesci di Isola Serafini: la specie-bandiera del progetto ha dimostrato di usare il corridoio del Po grazie a quella struttura.</p>
      <dl class="scheda">
        <dt>Ambito</dt><dd>Passaggi per pesci, continuità fluviale</dd>
        <dt>Programma</dt><dd>LIFE, Unione europea</dd>
        <dt>Ruolo</dt><dd>Partner del progetto</dd>
      </dl>
      <a class="link-freccia" href="https://www.graia.eu/isola-serafini-lo-storione-cobice-ce/">Il video del passaggio</a>
    </div>
  </article>

  <div class="casi">
    <article class="caso">
      <img src="img/lifeel.jpg" alt="Locandina di LIFEEL Days" loading="lazy" class="poster-caso">
      <p class="meta">LIFE19 NAT/IT/000851 · chiuso con LIFEEL Days, 20 aprile 2026</p>
      <h3>LIFEEL: salvare l'anguilla europea</h3>
      <p>Misure urgenti nel Mediterraneo orientale per la conservazione a lungo termine dell'anguilla europea (<i>Anguilla anguilla</i>), specie in pericolo. La chiusura è stata un evento a Comacchio per restituire i risultati al territorio.</p>
      <p class="ruolo">Ruolo: partner del progetto</p>
    </article>
    <article class="caso">
      <img src="img/prospittico.png?v=2" alt="Loghi del progetto ProSpIttiCo" loading="lazy" class="logo-caso larga">
      <p class="meta">PNRR · NBFC · dal 1 dicembre 2024 al 30 novembre 2025</p>
      <h3>ProSpIttiCo: un sistema che riconosce i pesci</h3>
      <p>Sviluppo e prova di un sistema di monitoraggio che riconosce le specie ittiche in transito nei passaggi per pesci. Il gruppo di lavoro unisce il personale GRAIA, una società di sviluppo informatico e tre professionisti scelti per il progetto.</p>
      <p class="ruolo">Ruolo: unico soggetto beneficiario</p>
    </article>
    <article class="caso">
      <img src="img/eco4ticino.png?v=2" alt="ECO4TICINO, progetto Interreg Italia-Svizzera" loading="lazy" class="logo-caso">
      <p class="meta">Interreg Italia–Svizzera · progetto 0200063 · 2025–2027</p>
      <h3>ECO4TICINO: un corridoio oltre confine</h3>
      <p>Gestione comune del corridoio ecologico del fiume Ticino tra Italia e Svizzera, per proteggere la natura, la biodiversità e le infrastrutture verdi.</p>
      <p class="ruolo">Ruolo: da specificare</p>
    </article>
    <article class="caso">
      <img src="img/geriko.jpg" alt="Interreg Italia-Svizzera" loading="lazy" class="logo-caso">
      <p class="meta">Interreg V-A Italia–Svizzera 2014–2020</p>
      <h3>GE.RI.KO. MERA: l'acqua del Mera, di qua e di là</h3>
      <p>Italia e Svizzera condividono il bacino del Mera ma hanno regole diverse. Il progetto prepara una strategia comune, con attenzione al trasporto solido dopo la frana in Val Bondasca, il ripristino del corridoio ecologico nei siti Natura 2000 e linee guida per la governance transfrontaliera.</p>
      <p class="ruolo">Ruolo: BLU Progetti, partner</p>
    </article>
    <article class="caso doppio">
      <p class="meta">Altri progetti del Programma LIFE</p>
      <h3>Una lunga esperienza con LIFE</h3>
      <ul>
        <li><strong>LIFE PREDATOR</strong> (in corso): prevenire, individuare e contrastare la diffusione del siluro (<i>Silurus glanis</i>) nei laghi dell'Europa meridionale.</li>
        <li><strong>IdroLIFE</strong> (concluso il 15 luglio 2021): conservazione della fauna d'acqua dolce nei corridoi ecologici del Verbano-Cusio-Ossola.</li>
        <li><strong>LifeTicinoBiosource</strong> (concluso il 31 luglio 2021): ripristino delle aree sorgive per la biodiversità nel Parco del Ticino.</li>
      </ul>
    </article>
  </div>
  <p class="todo" style="margin-top:2.5rem">Le schede riprendono i fatti già pubblicati sul sito di GRAIA. Per la versione definitiva servono, per ogni caso, foto, dati e risultati forniti da GRAIA (ruolo esatto, lunghezza dei tratti riqualificati, specie monitorate, ecc.).</p>
</div></section>"""


pages["portfolio.html"] = page(
    "portfolio.html",
    "Portfolio · GRAIA",
    "Progetti e committenti di GRAIA srl.",
    interna(
        "Portfolio",
        "Cosa abbiamo fatto, e per chi.",
        "Alcuni progetti raccontati da vicino, poi l'elenco dei committenti dei lavori realizzati in questi anni, raggruppati per tipo.",
    )
    + CASI
    + '<section class="pallida" id="committenti"><div class="wrap"><p class="eyebrow">Committenti</p><h2 style="margin-bottom:2.5rem">I nostri clienti</h2>'
    + gruppo("Ministeri, autorità e agenzie", [
        "Ministero delle Politiche Agricole, Alimentari e Forestali, Direzione Generale della Pesca e dell'Acquacoltura",
        "Autorità di Bacino del Fiume Po",
        "Autorità di Bacino Lacuale dei Laghi d'Iseo, Endine e Moro",
        "AIPO, Agenzia Interregionale per il fiume Po",
        "ISPRA",
        "Commissariato Italo-Elvetico sulla Pesca",
        "Regione Lombardia",
        "Repubblica e Cantone del Ticino",
        "Città di Lugano",
    ])
    + gruppo("Università e ricerca", [
        "Politecnico di Milano", "Politecnico di Torino", "Università degli Studi dell'Insubria",
        "Università degli Studi di Milano", "Leibniz Institut (Berlino)", "CNR-IRSA (Brugherio)",
    ])
    + gruppo("Parchi", [
        "Parco Nazionale del Gran Paradiso", "Parco Nazionale Foreste Casentinesi, Monte Falterona e Campigna",
        "Parco Lombardo della Valle del Ticino", "Parco Adamello", "Parco Adda Nord", "Parco Adda Sud",
        "Parco delle Orobie Valtellinesi", "Parco Oglio Nord", "Parco Oglio Sud",
        "Parco Naturale Alpe Veglia e Alpe Devero", "Parco Naturale Alta Val Sesia",
        "Parco Regionale del Campo dei Fiori", "Ente Parco Lago Montorfano",
    ])
    + gruppo("Amministrazioni provinciali", [
        "Arezzo", "Bergamo", "Biella", "Brescia", "Cagliari", "Catanzaro", "Como", "Cuneo", "Latina",
        "Mantova", "Milano", "Novara", "Olbia-Tempio", "Pavia", "Prato", "Rieti", "Sondrio", "Varese",
        "Verbano Cusio Ossola", "Torino", "Vercelli",
    ])
    + gruppo("Energia, consorzi e privati", [
        "A2A", "Edison", "Edipower", "ENEL Produzione", "ENEL Green Power", "IREN", "Italgen",
        "Consorzio di Bonifica Est Ticino Villoresi", "Consorzio di Bonifica Muzza – Bassa Lodigiana",
        "Consorzio del Ticino", "Consorzio Venezia Nuova", "Navigli Lombardi", "Holcim", "Technital",
        "CIRF, Centro Italiano di Riqualificazione Fluviale", "FIPSAS", "LIPU", "Fondazione Lombardia per l'Ambiente",
    ])
    + '<p class="todo" style="margin-top:3rem">Il sito attuale mostra solo i nomi. Nella versione definitiva ogni committente potrebbe rimandare ai casi in cui ha lavorato con GRAIA.</p>'
    + "</div></section>",
)

# ---------------------------------------------------------------- BLU
pages["blu-progetti.html"] = page(
    "blu-progetti.html",
    "BLU Progetti · GRAIA",
    "Società di ingegneria per la riqualificazione ecologica, ecosistemica e ambientale.",
    interna(
        "BLU Progetti",
        "La società di ingegneria nata da GRAIA.",
        "Dal maggio 2006 gli stessi soci di GRAIA hanno costituito BLU Progetti srl: progettazione e direzione lavori per soggetti pubblici e privati, nel campo della riqualificazione ecologica, ecosistemica e ambientale.",
    )
    + """<section style="padding-top:2rem"><div class="wrap due">
  <figure class="fig" style="margin:0"><img src="img/riqualificazione.jpg" alt="Intervento di ingegneria naturalistica con tronchi e massi" width="1600" height="1200" style="object-position:30% 62%"><figcaption>Intervento di riqualificazione di una riva.</figcaption></figure>
  <div>
    <h2 style="margin-bottom:1rem">Cosa fa BLU Progetti</h2>
    <p>Dove GRAIA studia e monitora, BLU Progetti progetta e segue i cantieri. Le due società condividono soci, competenze e sede, e lavorano spesso sugli stessi progetti.</p>
    <p>BLU Progetti è partner del progetto <strong>GE.RI.KO. MERA</strong>, Programma di cooperazione Interreg V-A Italia–Svizzera 2014–2020.</p>
    <p class="todo">Da completare con il materiale di BLU Progetti: elenco dei servizi, progetti realizzati, referenze. Il sito attuale rimanda a una pagina separata.</p>
    <p style="margin-top:1.5rem"><a class="btn" href="contatti.html">Parla con noi</a></p>
  </div>
</div></section>""",
)

# ---------------------------------------------------------------- NEWS
pages["news.html"] = page(
    "news.html",
    "News · GRAIA",
    "Le ultime news dal mondo GRAIA.",
    interna("News", "Dal mondo GRAIA.", "Progetti, ricerche, ritrovamenti e appuntamenti.")
    + """<section style="padding-top:2rem"><div class="wrap">
<ul class="news-lista">
  <li><time>20 aprile 2026</time><div><h3><a href="https://www.graia.eu/news/">LIFEEL Days</a></h3><p>Non solo la conclusione formale del progetto, ma un momento di restituzione al territorio e di apertura al futuro: la conservazione dell'anguilla europea diventa patrimonio condiviso.</p></div></li>
  <li><time>20 ottobre 2025</time><div><h3><a href="https://www.graia.eu/progetto-prospittico-manca-poco-al-lancio-della-piattaforma-per-utilizzare-il-sistema-in-fase-di-sviluppo/">Progetto ProSpIttiCo – Manca poco al lancio della piattaforma</a></h3><p>Uno degli obiettivi è stato progettare e mettere a disposizione una piattaforma con la versione beta del sistema in via di sviluppo.</p></div></li>
  <li><time>1 settembre 2025</time><div><h3><a href="https://www.graia.eu/progetto-prospittico-prosegue-la-raccolta-dei-dati/">Progetto ProSpIttiCo – Prosegue la raccolta dei dati!</a></h3><p>Il progetto sperimentale per il monitoraggio della biodiversità ittica nei corridoi fluviali ha come unico soggetto beneficiario G.R.A.I.A. srl.</p></div></li>
  <li><time>10 gennaio 2025</time><div><h3><a href="https://www.graia.eu/iniziato-il-progetto-prospittico/">Iniziato il Progetto ProSpIttiCo!</a></h3><p>Finanziato dall'Unione europea (NextGenerationEU), nell'ambito del PNRR e del National Biodiversity Future Center.</p></div></li>
  <li><time>28 gennaio 2021</time><div><h3><a href="https://www.graia.eu/sono-aperte-le-selezioni-per-la-posizione-di-project-manager-del-progetto-lifeel/">Selezioni aperte per Project Manager del progetto LIFEEL</a></h3></div></li>
  <li><time>8 ottobre 2019</time><div><h3><a href="https://www.graia.eu/progetto-erasmus-wow-written-on-water-seminario-del-14-novembre-2019/">Progetto Erasmus+ “WOW – Written On Water”: seminario del 14 novembre 2019</a></h3></div></li>
  <li><time>18 aprile 2019</time><div><h3><a href="https://www.graia.eu/isola-serafini-lo-storione-cobice-ce/">Isola Serafini, lo storione cobice c'è!</a></h3></div></li>
</ul>
<p class="todo" style="margin-top:2rem">I link portano al sito attuale. Nella versione definitiva ogni articolo avrebbe una pagina nel nuovo sito, con foto in testa e filtri per progetto.</p>
</div></section>""",
)

# ---------------------------------------------------------------- CHI SIAMO
pages["chi-siamo.html"] = page(
    "chi-siamo.html",
    "Chi siamo · GRAIA",
    "Tre soci fondatori e più di 35 tra dipendenti e collaboratori: la storia di GRAIA dal 1991.",
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
  <p class="eyebrow">I soci fondatori</p>
  <h2 style="margin-bottom:2.5rem">Tre mestieri diversi, la stessa acqua.</h2>
  <div class="soci">
    <article class="socio">
      <h3>Gaetano Gentili</h3>
      <p class="ruolo">Presidente · Medico veterinario</p>
      <p>Veterinario dal 1988, ha cominciato occupandosi di animali in ambiente naturale. Oggi si dedica all'ecologia degli ambienti fluviali, in particolare all'ecoidraulica. Professore a contratto di Acquacoltura all'Università degli Studi di Milano.</p>
      <p class="motto">«Mai fidarsi troppo!»</p>
    </article>
    <article class="socio">
      <h3>Cesare Mario Puzzi</h3>
      <p class="ruolo">Amministratore delegato · Medico veterinario</p>
      <p>La sua professione è l'ittiologia, nata dalla passione per i pesci e per la pesca. Si occupa di corridoi fluviali, passaggi per pesci e riqualificazioni fluvio-lacustri. Professore a contratto di Gestione della fauna ittica d'acqua dolce a Milano.</p>
      <p class="motto">«Credi in quello che fai!»</p>
    </article>
    <article class="socio">
      <h3>Massimo Sartorelli</h3>
      <p class="ruolo">Amministratore delegato · Ingegnere civile</p>
      <p>Ingegnere per la difesa del suolo e la pianificazione territoriale, indirizzo ambientale. Iscritto agli Ordini degli Ingegneri di Varese e del Canton Ticino.</p>
      <p class="todo" style="margin-top:1.2rem;font-size:.85rem">Biografia e motto da completare.</p>
    </article>
  </div>
  <p class="todo" style="margin-top:3rem">Nel sito attuale tutto il team ha una scheda con foto e biografia (più di 35 persone). Nella versione definitiva: un elenco filtrabile per area, con la stessa scheda.</p>
</div></section>""",
)

# ---------------------------------------------------------------- CONTATTI
pages["contatti.html"] = page(
    "contatti.html",
    "Contatti · GRAIA",
    "Come raggiungere GRAIA a Varano Borghi (VA) e come contattarci.",
    interna("Contatti", "Scrivici o vieni a trovarci.", "La sede è a Varano Borghi, a pochi metri dal lago di Comabbio.")
    + """<section style="padding-top:2rem"><div class="wrap due">
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
  </div>
  <div>
    <form class="todo" onsubmit="return false" style="border:0;padding:0">
      <p class="eyebrow">Scrivici (modulo di esempio)</p>
      <p style="margin-bottom:.4rem"><label for="n">Nome</label><br><input id="n" style="width:100%;padding:.7rem;border:1px solid var(--linea);font:inherit"></p>
      <p style="margin-bottom:.4rem"><label for="e">E-mail</label><br><input id="e" type="email" style="width:100%;padding:.7rem;border:1px solid var(--linea);font:inherit"></p>
      <p><label for="m">Messaggio</label><br><textarea id="m" rows="5" style="width:100%;padding:.7rem;border:1px solid var(--linea);font:inherit"></textarea></p>
      <button class="btn" type="button">Invia (non attivo)</button>
    </form>
    <p class="todo" style="margin-top:1.5rem">In questa bozza il modulo non invia nulla. Il sito attuale ha solo gli indirizzi e-mail.</p>
  </div>
</div></section>""",
)

# ---------------------------------------------------------------- PROPOSTA
pages["proposta.html"] = page(
    "proposta.html",
    "La proposta · bozza di redesign GRAIA",
    "Cosa cambia rispetto al sito attuale di GRAIA e cosa resta uguale.",
    interna(
        "La proposta",
        "Stesso carattere, sito più chiaro.",
        "Questa è una bozza per discutere la direzione, non un sito finito. Qui sotto: cosa abbiamo tenuto, cosa cambia e cosa manca.",
    )
    + """<section style="padding-top:2rem"><div class="wrap">
  <h2 style="font-size:2rem;margin-bottom:1.5rem">Cosa cambia</h2>
  <table class="confronto">
    <thead><tr><th>Aspetto</th><th>Oggi su graia.eu</th><th>In questa bozza</th></tr></thead>
    <tbody>
      <tr><td>Prima impressione</td><td>Slider con la locandina del progetto in corso; chi arriva non capisce subito cosa fa GRAIA.</td><td>Un'unica frase e una foto vera (il luccio), poi i progetti. I progetti in corso restano visibili, più in basso.</td></tr>
      <tr><td>Le attività</td><td>Nuvola di una cinquantina di tag da filtrare (da «Acquacoltura» a «VIA»).</td><td>Sei ambiti con una frase ciascuno, i tag restano come dettaglio dentro ogni ambito.</td></tr>
      <tr><td>Portfolio</td><td>Muro di testo con i nomi dei committenti.</td><td>Sei casi raccontati da vicino (storione nel Po, anguilla, ProSpIttiCo…), poi i committenti raggruppati per tipo.</td></tr>
      <tr><td>Team</td><td>Schede lunghe in una pagina unica.</td><td>I tre soci con ruolo e motto in evidenza; il resto del team in una lista filtrabile (da fare).</td></tr>
      <tr><td>Lettura</td><td>Testo piccolo (10 px di base), grigio chiaro, menu azzurro con testo bianco poco leggibile.</td><td>Testo da 17 px, contrasto verificato, menu su una riga con voce attiva sottolineata.</td></tr>
      <tr><td>Telefono</td><td>Layout adattato in modo parziale.</td><td>Pensato prima per il telefono: menu a scomparsa, colonne che si impilano.</td></tr>
      <tr><td>Cookie</td><td>Banner fisso in basso che non si chiude da solo.</td><td>Da rifare con un gestore conforme (non incluso in questa bozza).</td></tr>
    </tbody>
  </table>
</div></section>

<section class="pallida"><div class="wrap due">
  <div>
    <h2 style="font-size:2rem;margin-bottom:1rem">Cosa resta uguale</h2>
    <p>I colori sono quelli del sito attuale, ricavati dal suo foglio di stile: il verde del logo e dei link, l'azzurro del menu. Ho solo aggiunto un blu profondo, della stessa tinta dell'azzurro, per le sezioni scure, e scurito il verde per il testo, perché quello del logo su bianco non ha abbastanza contrasto.</p>
    <p>Restano anche i contenuti: i testi sono quelli del sito, riordinati. Non ho inventato numeri né frasi.</p>
  </div>
  <div>
    <ul class="palette">
      <li><i style="background:#799E50"></i><b>Verde</b><br>#799E50<br>accenti, link</li>
      <li><i style="background:#648242"></i><b>Verde scuro</b><br>#648242<br>testo, bottoni</li>
      <li><i style="background:#9FBB7F"></i><b>Verde logo</b><br>#9FBB7F</li>
      <li><i style="background:#6BA1B9"></i><b>Acqua</b><br>#6BA1B9</li>
      <li><i style="background:#C9E5F1"></i><b>Azzurro menu</b><br>#C9E5F1<br>fasce</li>
      <li><i style="background:#F0F9FD"></i><b>Azzurro pallido</b><br>#F0F9FD<br>sfondi</li>
      <li><i style="background:#1F3B47"></i><b>Abisso</b><br>#1F3B47<br>nuovo, derivato</li>
    </ul>
  </div>
</div></section>

<section><div class="wrap">
  <h2 style="font-size:2rem;margin-bottom:1rem">Cosa manca in questa bozza</h2>
  <div class="testo-lungo">
    <ul>
      <li>Le pagine singole di progetto e di news, il team completo, le schede dei casi.</li>
      <li>La versione inglese (oggi il sito ha IT/EN: andrà mantenuta).</li>
      <li>Il modulo contatti funzionante e la gestione dei cookie.</li>
      <li>Foto nuove: qui ci sono solo quelle già pubblicate sul sito, alcune a bassa risoluzione. I diritti sono di GRAIA o dei rispettivi autori.</li>
      <li>La scelta della piattaforma (oggi WordPress) e il piano di migrazione, che vanno discussi dopo aver concordato la direzione.</li>
    </ul>
  </div>
</div></section>""",
)

for name, html in pages.items():
    (ROOT / name).write_text(html, encoding="utf-8")
    print("scritto", name)
