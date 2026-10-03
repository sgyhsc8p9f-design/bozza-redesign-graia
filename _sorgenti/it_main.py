"""Pagine italiane statiche: home e portfolio."""
from layout import page, interna

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
      <li><span class="n">01</span><div><h3><a href="attivita.html#ittiologia" style="color:inherit;text-decoration:none">Ittiologia e gestione della fauna ittica</a></h3></div><p>Carte e piani ittici, conservazione delle specie, incubatoi, acquacoltura, pesca sportiva e professionale.</p></li>
      <li><span class="n">02</span><div><h3><a href="attivita.html#monitoraggio" style="color:inherit;text-decoration:none">Monitoraggio e analisi ambientale</a></h3></div><p>Biomonitoraggio, limnologia, analisi statistica, batimetria, qualità delle acque.</p></li>
      <li><span class="n">03</span><div><h3><a href="attivita.html#riqualificazione" style="color:inherit;text-decoration:none">Riqualificazione fluviale e lacustre</a></h3></div><p>Ripristino della continuità fluviale, riqualificazione ecologica, rimboschimento, fitodepurazione.</p></li>
      <li><span class="n">04</span><div><h3><a href="attivita.html#passaggi" style="color:inherit;text-decoration:none">Passaggi per pesci e idroelettrico</a></h3></div><p>Progettazione e monitoraggio delle migrazioni, deflusso minimo vitale, svasi.</p></li>
      <li><span class="n">05</span><div><h3><a href="attivita.html#life" style="color:inherit;text-decoration:none">Programmi LIFE e ricerca europea</a></h3></div><p>Progetti per la conservazione di specie e habitat, cambiamenti climatici, reti ecologiche.</p></li>
      <li><span class="n">06</span><div><h3><a href="attivita.html#didattica" style="color:inherit;text-decoration:none">Didattica e divulgazione ambientale</a></h3></div><p>Percorsi nelle scuole, libri e allestimenti, eventi per il territorio.</p></li>
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
        <p class="meta">24–26 aprile 2026 · Comacchio, Manifattura dei Marinati</p>
        <h3 style="font-size:2rem">LIFEEL Days</h3>
        <p style="margin-top:.8rem">Non solo la conclusione formale del progetto: un momento di restituzione al territorio, in cui la conservazione dell'anguilla europea diventa responsabilità collettiva e occasione di dialogo tra scienza, istituzioni e cittadini.</p>
        <a class="link-freccia" href="news-lifeel-days.html">Leggi la news</a>
      </div>
    </div>
    <div class="righe-progetti">
      <article class="riga-progetto">
        <img src="img/prospittico.png?v=2" alt="Loghi del progetto ProSpIttiCo: Unione europea, Ministero dell'Università e della Ricerca, Italia domani, NBFC" loading="lazy">
        <p class="meta">PNRR · National Biodiversity Future Center</p>
        <h3><a href="a-prospittico-progetto-sperimentale-per-il-monitoraggio-della-biodiversita-ittica-nei-corridoi-fluviali.html" style="color:inherit;text-decoration:none">ProSpIttiCo</a></h3>
        <p>Un sistema per monitorare le specie ittiche che transitano nei passaggi per pesci. GRAIA è l'unico soggetto beneficiario. La piattaforma con la versione beta è in arrivo.</p>
      </article>
      <article class="riga-progetto">
        <img src="img/eco4ticino.png?v=2" alt="ECO4TICINO, progetto Interreg Italia-Svizzera" loading="lazy">
        <p class="meta">Interreg Italia–Svizzera · 2025–2027</p>
        <h3><a href="a-eco4ticino-unalleanza-per-difendere-la-biodiversita-tra-italia-e-svizzera.html" style="color:inherit;text-decoration:none">ECO4TICINO</a></h3>
        <p>Un corridoio ecologico da gestire insieme, oltre confine, lungo il fiume Ticino. GRAIA è soggetto beneficiario.</p>
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
      <li><time>20 aprile 2026</time><div><h3><a href="news-lifeel-days.html">LIFEEL Days</a></h3><p>Il progetto si chiude con un momento di restituzione al territorio.</p></div></li>
      <li><time>20 ottobre 2025</time><div><h3><a href="news-progetto-prospittico-manca-poco-al-lancio-della-piattaforma-per-utilizzare-il-sistema-in-fase-di-sviluppo.html">ProSpIttiCo: manca poco al lancio della piattaforma</a></h3><p>Online la versione beta del sistema di monitoraggio in sviluppo.</p></div></li>
      <li><time>1 settembre 2025</time><div><h3><a href="news-progetto-prospittico-prosegue-la-raccolta-dei-dati.html">ProSpIttiCo: prosegue la raccolta dei dati</a></h3><p>Il monitoraggio della biodiversità ittica nei corridoi fluviali va avanti.</p></div></li>
    </ul>
    <p style="margin-top:1.6rem"><a class="link-freccia" href="news.html">Tutte le news</a></p>
  </div>
</section>
""",
)


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
      <a class="link-freccia" href="news-isola-serafini-lo-storione-cobice-ce.html">Il video del passaggio</a>
    </div>
  </article>

  <div class="casi">
    <article class="caso">
      <img src="img/lifeel.jpg" alt="Locandina di LIFEEL Days" loading="lazy" class="poster-caso">
      <p class="meta">LIFE19 NAT/IT/000851 · cinque anni, chiusi con LIFEEL Days (24–26 aprile 2026)</p>
      <h3>LIFEEL: salvare l'anguilla europea</h3>
      <p>Misure urgenti per la conservazione a lungo termine dell'anguilla europea (<i>Anguilla anguilla</i>), specie in pericolo, a sostegno della biodiversità del bacino del Po. Tre giornate a Comacchio, nell'ex stabilimento di lavorazione dell'anguilla oggi ecomuseo, per restituire i risultati al territorio.</p>
      <p class="ruolo">Ruolo: partner del progetto · <a href="news-lifeel-days.html">La news</a></p>
    </article>
    <article class="caso">
      <img src="img/prospittico.png?v=2" alt="Loghi del progetto ProSpIttiCo" loading="lazy" class="logo-caso larga">
      <p class="meta">PNRR · NBFC · dal 1 dicembre 2024 al 30 novembre 2025</p>
      <h3>ProSpIttiCo: un sistema che riconosce i pesci</h3>
      <p>Sviluppo e prova di un sistema di monitoraggio che riconosce le specie ittiche in transito nei passaggi per pesci. Il gruppo di lavoro unisce il personale GRAIA, una società di sviluppo informatico e tre professionisti scelti per il progetto.</p>
      <p class="ruolo">Ruolo: unico soggetto beneficiario · <a href="a-prospittico-progetto-sperimentale-per-il-monitoraggio-della-biodiversita-ittica-nei-corridoi-fluviali.html">Scheda completa</a></p>
    </article>
    <article class="caso">
      <img src="img/eco4ticino.png?v=2" alt="ECO4TICINO, progetto Interreg Italia-Svizzera" loading="lazy" class="logo-caso">
      <p class="meta">Interreg Italia–Svizzera · progetto 0200063 · 2025–2027</p>
      <h3>ECO4TICINO: un corridoio oltre confine</h3>
      <p>Gestione comune del corridoio ecologico del fiume Ticino tra Italia e Svizzera, sul Piano di riqualificazione 2021–2031 costruito da una rete di circa trenta enti, per proteggere natura, biodiversità e infrastrutture verdi.</p>
      <p class="ruolo">Ruolo: soggetto beneficiario · <a href="a-eco4ticino-unalleanza-per-difendere-la-biodiversita-tra-italia-e-svizzera.html">Scheda completa</a></p>
    </article>
    <article class="caso">
      <img src="img/geriko.jpg" alt="Interreg Italia-Svizzera" loading="lazy" class="logo-caso">
      <p class="meta">Interreg V-A Italia–Svizzera 2014–2020</p>
      <h3>GE.RI.KO. MERA: l'acqua del Mera, di qua e di là</h3>
      <p>Italia e Svizzera condividono il bacino del Mera ma hanno regole diverse. Il progetto prepara una strategia comune, con attenzione al trasporto solido dopo la frana in Val Bondasca, il ripristino del corridoio ecologico nei siti Natura 2000 e linee guida per la governance transfrontaliera.</p>
      <p class="ruolo">Ruolo: BLU Progetti, partner</p>
    </article>
    <article class="caso">
      <p class="meta">Interreg V-A Italia–Svizzera 2014–2020</p>
      <h3>Sharesalmo: i salmonidi nativi, insieme</h3>
      <p>Gestione ittica integrata e condivisa per conservare temolo, trota marmorata e trota lacustre e contrastare le specie aliene invasive come il siluro, con misure di governance transfrontaliera.</p>
      <p class="ruolo">Ruolo: partner · <a href="a-programma-di-cooperazione-interreg.html">Scheda completa</a></p>
    </article>
    <article class="caso doppio">
      <p class="meta">Altri progetti del Programma LIFE</p>
      <h3><a href="a-progetti-life.html" style="color:inherit;text-decoration:none">Una lunga esperienza con LIFE</a></h3>
      <ul>
        <li><strong><a href="a-progetto-life-predator.html">LIFE PREDATOR</a></strong> (in corso): prevenire, individuare e contrastare la diffusione del siluro (<i>Silurus glanis</i>) nei laghi dell'Europa meridionale.</li>
        <li><strong>IdroLIFE</strong> (concluso il 15 luglio 2021): conservazione della fauna d'acqua dolce nei corridoi ecologici del Verbano-Cusio-Ossola.</li>
        <li><strong>LifeTicinoBiosource</strong> (concluso il 31 luglio 2021): ripristino delle aree sorgive per la biodiversità nel Parco del Ticino.</li>
      </ul>
    </article>
  </div>
  <p class="todo" style="margin-top:2.5rem">Le schede riprendono i fatti già pubblicati sul sito di GRAIA. Per la versione definitiva servono, per ogni caso, foto nuove, dati e risultati forniti da GRAIA (lunghezza dei tratti riqualificati, specie monitorate, ecc.).</p>
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

