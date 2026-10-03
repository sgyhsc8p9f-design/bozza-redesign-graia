"""Pagina 'La proposta': cosa cambia, cosa resta, cosa manca, prossimi passi."""
from layout import page, interna

pages = {}

pages["proposta.html"] = page(
    "proposta.html",
    "La proposta · bozza di redesign GRAIA",
    "Cosa cambia rispetto al sito attuale di GRAIA, cosa resta uguale e come si arriva alla versione definitiva.",
    interna(
        "La proposta",
        "Stesso carattere, sito più chiaro.",
        "Questa è una bozza per discutere la direzione. Qui sotto: cosa abbiamo tenuto, cosa cambia, cosa è già fatto e cosa serve da GRAIA per arrivare alla versione definitiva.",
    )
    + """<section style="padding-top:2rem"><div class="wrap">
  <h2 style="font-size:2rem;margin-bottom:1.5rem">Cosa cambia</h2>
  <table class="confronto">
    <thead><tr><th>Aspetto</th><th>Oggi su graia.eu</th><th>In questa bozza</th></tr></thead>
    <tbody>
      <tr><td>Prima impressione</td><td>Slider con la locandina del progetto in corso; chi arriva non capisce subito cosa fa GRAIA.</td><td>Un'unica frase e una foto vera (il luccio), poi i progetti. I progetti in corso restano visibili, più in basso.</td></tr>
      <tr><td>Le attività</td><td>Una nuvola di cinquanta etichette da filtrare e trenta pagine in un elenco piatto.</td><td>Sei ambiti con una frase ciascuno; le trenta schede, con testi e servizi originali, si aprono da lì. Resta la ricerca.</td></tr>
      <tr><td>Portfolio</td><td>Muro di testo con i nomi dei committenti.</td><td>Sei casi raccontati da vicino (storione nel Po, anguilla, ProSpIttiCo…), poi i committenti raggruppati per tipo.</td></tr>
      <tr><td>Team</td><td>Schede lunghe in una pagina unica.</td><td>Nove persone con foto e motto in evidenza, biografia che si apre a richiesta, filtro per gruppo.</td></tr>
      <tr><td>News</td><td>Elenco a blocchi, senza distinzione tra novità e archivio.</td><td>Archivio per anno con tutti i 20 articoli migrati, ciascuno con la sua pagina.</td></tr>
      <tr><td>Lettura</td><td>Testo piccolo (10 px di base), grigio chiaro, menu azzurro con testo bianco poco leggibile.</td><td>Testo da 17 px, contrasto verificato, menu su una riga con voce attiva sottolineata, link «Vai al contenuto».</td></tr>
      <tr><td>Telefono</td><td>Layout adattato in modo parziale.</td><td>Pensato prima per il telefono: menu a scomparsa, colonne che si impilano.</td></tr>
      <tr><td>Cookie e privacy</td><td>Banner fisso in basso che non si chiude da solo; i caratteri vengono caricati da servizi esterni.</td><td>Nessun cookie né servizio di terzi: i font sono ospitati sul sito, quindi non serve banner. Informativa breve da validare.</td></tr>
      <tr><td>Lingue</td><td>Italiano e inglese, con l'inglese parziale.</td><td>Versione inglese delle pagine principali (home, attività, portfolio, BLU, team, contatti); le schede di dettaglio per ora solo in italiano.</td></tr>
    </tbody>
  </table>
</div></section>

<section class="pallida"><div class="wrap due">
  <div>
    <h2 style="font-size:2rem;margin-bottom:1rem">Cosa resta uguale</h2>
    <p>I colori sono quelli del sito attuale, ricavati dal suo foglio di stile: il verde del logo e dei link, l'azzurro del menu. Ho solo aggiunto un blu profondo, della stessa tinta dell'azzurro, per le sezioni scure, e scurito il verde per il testo, perché quello del logo su bianco non ha abbastanza contrasto.</p>
    <p>Restano anche i contenuti: i testi sono quelli del sito, riordinati. Non ho inventato numeri né frasi; dove manca un'informazione, la pagina lo dice.</p>
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

<section><div class="wrap due">
  <div>
    <h2 style="font-size:2rem;margin-bottom:1rem">Cosa serve da GRAIA</h2>
    <p>La bozza usa solo materiale già pubblico. Per la versione definitiva servono cose che possono dare solo loro.</p>
  </div>
  <ul class="check">
    <li><strong>Foto nuove.</strong> Quelle attuali sono di qualità e risoluzione diverse, alcune molto piccole. Servono scatti recenti di campo, sede, persone, e l'ok sui diritti di quelle da tenere.</li>
    <li><strong>Il resto del team.</strong> Il sito attuale mostra nove persone; la società ne conta più di 35. Per ciascuna: foto, ruolo, due righe di profilo.</li>
    <li><strong>Dati per i casi.</strong> Ruolo esatto, risultati e cifre dei progetti da raccontare (tratti riqualificati, specie monitorate, periodi).</li>
    <li><strong>Testi in inglese.</strong> Le schede di dettaglio e le news per ora sono solo in italiano.</li>
    <li><strong>Revisione legale.</strong> L'informativa privacy è una bozza; va validata da chi segue gli aspetti legali di GRAIA.</li>
    <li><strong>Un modo per ricevere i messaggi.</strong> Il modulo contatti prepara un'e-mail; per l'invio diretto va scelto un servizio di ricezione.</li>
  </ul>
</div></section>

<section class="pallida"><div class="wrap">
  <h2 style="font-size:2rem;margin-bottom:2rem">Come ci si arriva</h2>
  <ol class="passi">
    <li><strong>Direzione.</strong> Si guarda questa bozza insieme e si decide cosa tenere, cambiare o togliere.</li>
    <li><strong>Materiale.</strong> GRAIA raccoglie foto, schede del team e dati dei casi (elenco qui sopra).</li>
    <li><strong>Piattaforma.</strong> Si sceglie dove far vivere il sito. Oggi è su WordPress; le strade sono restare lì con un tema nuovo o passare a un sito statico come questo, con gli aggiornamenti curati da una persona di GRAIA. Dipende da chi aggiorna i contenuti e con che frequenza.</li>
    <li><strong>Migrazione.</strong> Si portano i contenuti, si mantengono gli indirizzi esistenti con reindirizzamenti, si controllano i link e le pagine inglesi.</li>
    <li><strong>Lancio e cura.</strong> Pubblicazione, controllo dopo i primi giorni, indicazioni su come aggiungere news e progetti.</li>
  </ol>
</div></section>""",
)
