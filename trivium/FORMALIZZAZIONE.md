# Trivium. Formalizzazione e metodo

[Guida per iniziare](README.md) · [English](FORMALIZZAZIONE.en.md) · [Latine](FORMALIZZAZIONE.la.md)

Trivium formalizza un oggetto diverso da quello di Dubium. Dubium legge un testo; Trivium legge un ordinamento: la tassonomia con cui un sito distribuisce i suoi articoli. L'ordinamento è un fatto documentato (le categorie esistono, hanno un nome, una gerarchia, un numero), mentre le traduzioni, le corrispondenze e i ponti sono letture della redazione. Il modulo tiene distinte le due cose: ogni concetto conserva la fonte pubblica della categoria, e tutto ciò che è stato aggiunto è dichiarato in questo documento.

## Fonti

| Fonte | Che cosa fornisce | Data |
| --- | --- | --- |
| API pubblica delle categorie di criptasemantica.it | Nome, slug, identificativo, categoria madre, descrizione, collegamento | istantanea dell'11 novembre 2026, conservata in `fonti/` |
| Pagine Progetto, Chi siamo, Canali, Articoli, FINAI, Alessandro Sevardi | Le stanze, descritte nei testi alternativi delle immagini e nei testi delle pagine | 11 novembre 2026 |
| Wikidata | Elementi corrispondenti alle discipline, con numero di collegamenti a Wikipedia | 11 novembre 2026 |
| Manuale di Frascati 2015 (classificazione FORD), tramite Metrum | Campi di ricerca e sviluppo | edizione 2015 |
| Dubium | Concetti del manifesto a cui collegare le discipline | versione 0.2.0 |

I conteggi degli articoli per categoria non sono registrati: cambiano ogni giorno e non descrivono il concetto.

## Il modello

Quattro classi, tutte sottoclassi di `skos:Concept` e fra loro disgiunte: `trv:Disciplina`, `trv:Genere`, `trv:Programma`, `trv:Stanza`. Quattro schemi SKOS: `trv:discipline`, `trv:generi`, `trv:programmi`, `trv:stanze`. Due collezioni: `trv:trivio` e `trv:quadrivio`. Una sola proprietà propria, `trv:identificativoCategoria`, che conserva il numero della categoria su WordPress; tutto il resto usa SKOS e Dublin Core.

**Regola di assegnazione allo schema.** Si risale dalla categoria alla sua radice. Se la radice è una delle sezioni editoriali (notizie, recensioni, autori, profili, prodotti, sinergie, canali, senza categoria) il concetto è un genere; se è una delle linee di programma (comunismo digitale, grande rete semantica mondiale, motore di ricerca ermeneutico, programmazione filosofica, metafisica del gioco, studi accademici) è un programma; altrimenti è una disciplina. La gerarchia del sito è conservata con `skos:broader` all'interno dello stesso schema; le radici sono `skos:topConceptOf` del loro schema.

**Il caso «Logica».** Il sito ha due categorie con lo stesso slug: una di vertice e una dentro Dialettica. Un solo IRI confonderebbe due nodi del sito. La seconda riceve il suffisso `-dialettica`, lo stesso che il sito usa per distinguere le due «Antropologia», e le due voci sono dichiarate `skos:related`.

**Etichette.** L'italiano è il nome della categoria, carattere per carattere. L'inglese e il latino sono traduzioni editoriali. Per le discipline moderne il latino ricorre a neologismi trasparenti (`Informatica`, `Cybernetica`, `Data ingentia` per i big data) o a perifrasi (`Disciplina machinalis` per l'apprendimento automatico). Le note d'ambito riportano il testo dell'autore in italiano e, per le venti categorie che ne hanno una, la traduzione in inglese e latino.

## Corrispondenze con Wikidata

Il metodo è stato il seguente. Per ogni nome italiano si è interrogato il servizio SPARQL di Wikidata chiedendo gli elementi con quell'etichetta italiana, escludendo pagine di disambiguazione e articoli scientifici, ordinati per numero di collegamenti a Wikipedia. Si è scelto l'elemento più collegato solo quando la sua descrizione corrispondeva al senso della categoria; nei casi ambigui non si è scelto nulla. Alcuni esempi delle esclusioni: «Cosmologia» (la categoria sta sotto Epistemologia; l'elemento più collegato è la cosmologia fisica); «Cronaca» (l'elemento più collegato è il genere storiografico); «Teoria critica» (l'elemento trovato è la sociologia critica); «Scienze politiche» (elemento con cinque soli collegamenti); «Storia dell'Africa» (si trovava solo il continente); «Filosofia italiana», «Psicanalisi», «Filosofia prima», «Beni culturali» (nessun elemento con quell'etichetta). «Politica», «Heidegger» e «Nietzsche» sono stati verificati singolarmente.

La relazione è sempre `skos:closeMatch`. `skos:exactMatch` è vietato dai vincoli SHACL: una categoria editoriale non è identica a un concetto enciclopedico, anche quando porta lo stesso nome. La data della verifica è quella dell'istantanea.

<!-- table:wikidata -->
| Concetto | IRI | Elemento Wikidata |
| --- | --- | --- |
| Antropologia | `trv:antropologia` | [Q23404](https://www.wikidata.org/wiki/Q23404) |
| Antropologia | `trv:antropologia-dialettica` | [Q23404](https://www.wikidata.org/wiki/Q23404) |
| Antropologia Culturale | `trv:antropologia-culturale` | [Q28598](https://www.wikidata.org/wiki/Q28598) |
| Architettura dell'Informazione | `trv:architettura-dellinformazione` | [Q845921](https://www.wikidata.org/wiki/Q845921) |
| Arte | `trv:arte` | [Q735](https://www.wikidata.org/wiki/Q735) |
| Arte Contemporanea | `trv:arte-contemporanea` | [Q186030](https://www.wikidata.org/wiki/Q186030) |
| Arte Medievale | `trv:arte-medievale` | [Q3624153](https://www.wikidata.org/wiki/Q3624153) |
| Astronomia | `trv:astronomia` | [Q333](https://www.wikidata.org/wiki/Q333) |
| Big Data | `trv:big-data` | [Q858810](https://www.wikidata.org/wiki/Q858810) |
| Biologia | `trv:biologia` | [Q420](https://www.wikidata.org/wiki/Q420) |
| Buddismo | `trv:buddismo` | [Q748](https://www.wikidata.org/wiki/Q748) |
| Cibernetica | `trv:cibernetica` | [Q123637](https://www.wikidata.org/wiki/Q123637) |
| Costituzione | `trv:costituzione` | [Q7755](https://www.wikidata.org/wiki/Q7755) |
| Dialettica | `trv:dialettica` | [Q9453](https://www.wikidata.org/wiki/Q9453) |
| Diritti Umani | `trv:diritti-umani` | [Q8458](https://www.wikidata.org/wiki/Q8458) |
| Diritto | `trv:diritto` | [Q7748](https://www.wikidata.org/wiki/Q7748) |
| Ecologia | `trv:ecologia` | [Q7150](https://www.wikidata.org/wiki/Q7150) |
| Economia | `trv:economia` | [Q159810](https://www.wikidata.org/wiki/Q159810) |
| Economia Politica | `trv:economia-politica` | [Q47555](https://www.wikidata.org/wiki/Q47555) |
| Epistemologia | `trv:epistemologia` | [Q9471](https://www.wikidata.org/wiki/Q9471) |
| Ermeneutica | `trv:ermeneutica` | [Q102686](https://www.wikidata.org/wiki/Q102686) |
| Estetica | `trv:estetica` | [Q35986](https://www.wikidata.org/wiki/Q35986) |
| Etica | `trv:etica` | [Q9465](https://www.wikidata.org/wiki/Q9465) |
| Etnologia | `trv:etnologia` | [Q43455](https://www.wikidata.org/wiki/Q43455) |
| Evoluzione | `trv:evoluzione` | [Q1063](https://www.wikidata.org/wiki/Q1063) |
| Femminismo | `trv:femminismo` | [Q7252](https://www.wikidata.org/wiki/Q7252) |
| Fenomenologia | `trv:fenomenologia` | [Q179235](https://www.wikidata.org/wiki/Q179235) |
| Filologia | `trv:filologia` | [Q40634](https://www.wikidata.org/wiki/Q40634) |
| Filosofia Antica | `trv:filosofia-antica` | [Q204100](https://www.wikidata.org/wiki/Q204100) |
| Filosofia Contemporanea | `trv:filosofia-contemporanea` | [Q943303](https://www.wikidata.org/wiki/Q943303) |
| Filosofia Moderna | `trv:filosofia-moderna` | [Q860746](https://www.wikidata.org/wiki/Q860746) |
| Filosofia Politica | `trv:filosofia-politica` | [Q179805](https://www.wikidata.org/wiki/Q179805) |
| Filosofia Teoretica | `trv:filosofia-teoretica` | [Q2166096](https://www.wikidata.org/wiki/Q2166096) |
| Filosofia del Linguaggio | `trv:filosofia-del-linguaggio` | [Q484761](https://www.wikidata.org/wiki/Q484761) |
| Filosofia della Matematica | `trv:filosofia-della-matematica` | [Q180536](https://www.wikidata.org/wiki/Q180536) |
| Filosofia della Musica | `trv:filosofia-della-musica` | [Q2092865](https://www.wikidata.org/wiki/Q2092865) |
| Filosofia della Scienza | `trv:filosofia-della-scienza` | [Q59115](https://www.wikidata.org/wiki/Q59115) |
| Filosofia della Tecnica | `trv:filosofia-della-tecnica` | [Q5862034](https://www.wikidata.org/wiki/Q5862034) |
| Finanza | `trv:finanza` | [Q43015](https://www.wikidata.org/wiki/Q43015) |
| Fisica | `trv:fisica` | [Q413](https://www.wikidata.org/wiki/Q413) |
| Fondamenti della Matematica | `trv:fondamenti-della-matematica` | [Q833585](https://www.wikidata.org/wiki/Q833585) |
| Genetica | `trv:genetica` | [Q7162](https://www.wikidata.org/wiki/Q7162) |
| Geografia | `trv:geografia` | [Q1071](https://www.wikidata.org/wiki/Q1071) |
| Geopolitica | `trv:geopolitica` | [Q159385](https://www.wikidata.org/wiki/Q159385) |
| Giainismo | `trv:giainismo` | [Q9232](https://www.wikidata.org/wiki/Q9232) |
| Giurisprudenza | `trv:giurisprudenza` | [Q4932206](https://www.wikidata.org/wiki/Q4932206) |
| Globalizzazione | `trv:globalizzazione` | [Q7181](https://www.wikidata.org/wiki/Q7181) |
| Globalizzazione | `trv:globalizzazione-storia` | [Q7181](https://www.wikidata.org/wiki/Q7181) |
| Gnoseologia | `trv:gnoseologia` | [Q2560959](https://www.wikidata.org/wiki/Q2560959) |
| Grammatica | `trv:grammatica` | [Q8091](https://www.wikidata.org/wiki/Q8091) |
| Heidegger | `trv:heidegger` | [Q48301](https://www.wikidata.org/wiki/Q48301) |
| Imperialismo | `trv:imperialismo` | [Q7260](https://www.wikidata.org/wiki/Q7260) |
| Industria | `trv:industria` | [Q8148](https://www.wikidata.org/wiki/Q8148) |
| Informatica | `trv:informatica` | [Q21198](https://www.wikidata.org/wiki/Q21198) |
| Intelligenza Artificiale | `trv:intelligenza-artificiale` | [Q11660](https://www.wikidata.org/wiki/Q11660) |
| Lavoro | `trv:lavoro` | [Q268378](https://www.wikidata.org/wiki/Q268378) |
| Letteratura | `trv:letteratura` | [Q8242](https://www.wikidata.org/wiki/Q8242) |
| Linguistica | `trv:linguistica` | [Q8162](https://www.wikidata.org/wiki/Q8162) |
| Logica | `trv:logica` | [Q8078](https://www.wikidata.org/wiki/Q8078) |
| Logica | `trv:logica-dialettica` | [Q8078](https://www.wikidata.org/wiki/Q8078) |
| Logica Matematica | `trv:logica-matematica` | [Q1166618](https://www.wikidata.org/wiki/Q1166618) |
| Machine Learning | `trv:machine-learning` | [Q2539](https://www.wikidata.org/wiki/Q2539) |
| Macroeconomia | `trv:macroeconomia` | [Q39680](https://www.wikidata.org/wiki/Q39680) |
| Matematica | `trv:matematica` | [Q395](https://www.wikidata.org/wiki/Q395) |
| Materialismo Dialettico | `trv:materialismo-dialettico` | [Q181207](https://www.wikidata.org/wiki/Q181207) |
| Materialismo Storico | `trv:materialismo-storico` | [Q190004](https://www.wikidata.org/wiki/Q190004) |
| Metafisica | `trv:metafisica` | [Q35277](https://www.wikidata.org/wiki/Q35277) |
| Metafisica Generale | `trv:metafisica-generale` | [Q35277](https://www.wikidata.org/wiki/Q35277) |
| Metaversi | `trv:metaversi` | [Q2632041](https://www.wikidata.org/wiki/Q2632041) |
| Mito | `trv:mito` | [Q12827256](https://www.wikidata.org/wiki/Q12827256) |
| Mitologia | `trv:mitologia` | [Q9134](https://www.wikidata.org/wiki/Q9134) |
| Musica | `trv:musica` | [Q638](https://www.wikidata.org/wiki/Q638) |
| Neuroscienze | `trv:neuroscienze` | [Q207011](https://www.wikidata.org/wiki/Q207011) |
| Neuroscienze Cognitive | `trv:neuroscienze-cognitive` | [Q1138951](https://www.wikidata.org/wiki/Q1138951) |
| Nietzsche | `trv:nietzsche` | [Q9358](https://www.wikidata.org/wiki/Q9358) |
| Notizie | `trv:notizie` | [Q38926](https://www.wikidata.org/wiki/Q38926) |
| Ontologia | `trv:ontologia` | [Q44325](https://www.wikidata.org/wiki/Q44325) |
| Ontologia Formale | `trv:ontologia-formale` | [Q1437388](https://www.wikidata.org/wiki/Q1437388) |
| Polemologia | `trv:polemologia` | [Q1367522](https://www.wikidata.org/wiki/Q1367522) |
| Politica | `trv:politica` | [Q7163](https://www.wikidata.org/wiki/Q7163) |
| Politica Estera | `trv:politica-estera` | [Q181648](https://www.wikidata.org/wiki/Q181648) |
| Psicolinguistica | `trv:psicolinguistica` | [Q179488](https://www.wikidata.org/wiki/Q179488) |
| Psicolinguistica | `trv:psicolinguistica-linguistica` | [Q179488](https://www.wikidata.org/wiki/Q179488) |
| Psicologia | `trv:psicologia` | [Q9418](https://www.wikidata.org/wiki/Q9418) |
| Psicologia Sociale | `trv:psicologia-sociale` | [Q161272](https://www.wikidata.org/wiki/Q161272) |
| Psicologia dello Sviluppo | `trv:psicologia-dello-sviluppo` | [Q175002](https://www.wikidata.org/wiki/Q175002) |
| Quadrivio | `trv:quadrivio` | [Q273822](https://www.wikidata.org/wiki/Q273822) |
| Recensioni | `trv:recensioni` | [Q265158](https://www.wikidata.org/wiki/Q265158) |
| Relazioni Internazionali | `trv:relazioni-internazionali` | [Q166542](https://www.wikidata.org/wiki/Q166542) |
| Retorica | `trv:retorica` | [Q81009](https://www.wikidata.org/wiki/Q81009) |
| Saggistica | `trv:saggistica` | [Q27801](https://www.wikidata.org/wiki/Q27801) |
| Scienze Cognitive | `trv:scienze-cognitive` | [Q147638](https://www.wikidata.org/wiki/Q147638) |
| Semantica | `trv:semantica` | [Q39645](https://www.wikidata.org/wiki/Q39645) |
| Sindacato | `trv:sindacato` | [Q178790](https://www.wikidata.org/wiki/Q178790) |
| Sociologia | `trv:sociologia` | [Q21201](https://www.wikidata.org/wiki/Q21201) |
| Spiritualismo | `trv:spiritualismo` | [Q2636432](https://www.wikidata.org/wiki/Q2636432) |
| Storia | `trv:storia` | [Q309](https://www.wikidata.org/wiki/Q309) |
| Storia Contemporanea | `trv:storia-contemporanea` | [Q186075](https://www.wikidata.org/wiki/Q186075) |
| Storia dell'Arte | `trv:storia-dellarte` | [Q50637](https://www.wikidata.org/wiki/Q50637) |
| Storia della Filosofia | `trv:storia-della-filosofia` | [Q27654](https://www.wikidata.org/wiki/Q27654) |
| Storia della Matematica | `trv:storia-della-matematica` | [Q185264](https://www.wikidata.org/wiki/Q185264) |
| Storia della Sardegna | `trv:storia-della-sardegna` | [Q1516605](https://www.wikidata.org/wiki/Q1516605) |
| Storia delle Religioni | `trv:storia-delle-religioni` | [Q846742](https://www.wikidata.org/wiki/Q846742) |
| Storia delle Scienze | `trv:storia-delle-scienze` | [Q201486](https://www.wikidata.org/wiki/Q201486) |
| Studi Culturali | `trv:studi-culturali` | [Q1143546](https://www.wikidata.org/wiki/Q1143546) |
| Studi postcoloniali | `trv:studi-postcoloniali` | [Q265425](https://www.wikidata.org/wiki/Q265425) |
| Sviluppo | `trv:sviluppo` | [Q4530482](https://www.wikidata.org/wiki/Q4530482) |
| Teatro | `trv:teatro` | [Q11635](https://www.wikidata.org/wiki/Q11635) |
| Tecnologia | `trv:tecnologia` | [Q11016](https://www.wikidata.org/wiki/Q11016) |
| Teoria Marxista | `trv:teoria-marxista` | [Q7264](https://www.wikidata.org/wiki/Q7264) |
| Teoria dei Sistemi | `trv:teoria-dei-sistemi` | [Q269699](https://www.wikidata.org/wiki/Q269699) |
| Transumanesimo | `trv:transumanesimo` | [Q194100](https://www.wikidata.org/wiki/Q194100) |
| Trivio | `trv:trivio` | [Q205186](https://www.wikidata.org/wiki/Q205186) |
| Umbria | `trv:umbria` | [Q1280](https://www.wikidata.org/wiki/Q1280) |
| Web Semantico | `trv:web-semantico` | [Q54837](https://www.wikidata.org/wiki/Q54837) |
<!-- /table -->

## Ponti verso i campi FORD

Il ponte è `skos:broadMatch`: la categoria della Cripta è letta come più specifica di un campo FORD, oppure come interna a esso. La classificazione FORD descrive attività di ricerca, non pensieri: per questo alcuni ponti sorprendono. L'antropologia sta in «Sociologia» (5.4) perché il Manuale di Frascati vi include antropologia ed etnologia; la retorica e la grammatica stanno in «Lingue e letterature» (6.2); la logica ha due ponti, filosofia (6.3) e matematica (1.1); la geografia del sito, che raccoglie fisica e biologia, è letta come «Terra e ambiente» (1.5). I ponti sono dichiarati solo dove la collocazione è difendibile; le categorie di cronaca, politica interna o territorio non ne hanno.

<!-- table:ford -->
| Concetto | IRI | Campo FORD |
| --- | --- | --- |
| Antropologia | `trv:antropologia` | 5.4 · Sociologia |
| Antropologia | `trv:antropologia-dialettica` | 5.4 · Sociologia |
| Arte | `trv:arte` | 6.4 · Arti e pratiche performative |
| Astronomia | `trv:astronomia` | 1.3 · Fisica |
| Big Data | `trv:big-data` | 1.2 · Informatica e informazione |
| Biologia | `trv:biologia` | 1.6 · Biologia |
| Buddismo | `trv:buddismo` | 6.3 · Filosofia, etica e religione |
| Cibernetica | `trv:cibernetica` | 1.2 · Informatica e informazione |
| Cibernetica | `trv:cibernetica` | 2.2 · Elettronica, elettricità e informazione |
| Cosmologia | `trv:cosmologia` | 1.3 · Fisica |
| Dialettica | `trv:dialettica` | 6.3 · Filosofia, etica e religione |
| Diritto | `trv:diritto` | 5.5 · Diritto |
| Ecologia | `trv:ecologia` | 1.6 · Biologia |
| Economia | `trv:economia` | 5.2 · Economia e impresa |
| Epistemologia | `trv:epistemologia` | 6.3 · Filosofia, etica e religione |
| Epistemologia e Metafisica | `trv:epistemologia-e-metafisica` | 6.3 · Filosofia, etica e religione |
| Ermeneutica | `trv:ermeneutica` | 6.3 · Filosofia, etica e religione |
| Estetica | `trv:estetica` | 6.3 · Filosofia, etica e religione |
| Etica | `trv:etica` | 6.3 · Filosofia, etica e religione |
| Femminismo | `trv:femminismo` | 5.4 · Sociologia |
| Fenomenologia | `trv:fenomenologia` | 6.3 · Filosofia, etica e religione |
| Filologia | `trv:filologia` | 6.2 · Lingue e letterature |
| Filosofia Orientale | `trv:filosofia-orientale` | 6.3 · Filosofia, etica e religione |
| Filosofia Politica | `trv:filosofia-politica` | 6.3 · Filosofia, etica e religione |
| Filosofia del Linguaggio | `trv:filosofia-del-linguaggio` | 6.3 · Filosofia, etica e religione |
| Filosofia della Scienza | `trv:filosofia-della-scienza` | 6.3 · Filosofia, etica e religione |
| Finanza | `trv:finanza` | 5.2 · Economia e impresa |
| Fisica | `trv:fisica` | 1.3 · Fisica |
| Genetica | `trv:genetica` | 1.6 · Biologia |
| Geografia | `trv:geografia` | 1.5 · Terra e ambiente |
| Geopolitica | `trv:geopolitica` | 5.6 · Scienze politiche |
| Giainismo | `trv:giainismo` | 6.3 · Filosofia, etica e religione |
| Giurisprudenza | `trv:giurisprudenza` | 5.5 · Diritto |
| Grammatica | `trv:grammatica` | 6.2 · Lingue e letterature |
| Grande Rete Semantica Mondiale | `trv:www-semantico` | 1.2 · Informatica e informazione |
| Informatica | `trv:informatica` | 1.2 · Informatica e informazione |
| Intelligenza Artificiale | `trv:intelligenza-artificiale` | 1.2 · Informatica e informazione |
| Letteratura | `trv:letteratura` | 6.2 · Lingue e letterature |
| Linguistica | `trv:linguistica` | 6.2 · Lingue e letterature |
| Logica | `trv:logica` | 1.1 · Matematica |
| Logica | `trv:logica` | 6.3 · Filosofia, etica e religione |
| Logica | `trv:logica-dialettica` | 1.1 · Matematica |
| Logica | `trv:logica-dialettica` | 6.3 · Filosofia, etica e religione |
| Logica Matematica | `trv:logica-matematica` | 1.1 · Matematica |
| Machine Learning | `trv:machine-learning` | 1.2 · Informatica e informazione |
| Matematica | `trv:matematica` | 1.1 · Matematica |
| Metafisica | `trv:metafisica` | 6.3 · Filosofia, etica e religione |
| Metafisica Generale | `trv:metafisica-generale` | 6.3 · Filosofia, etica e religione |
| Metafisica del Gioco | `trv:metafisica-gioco` | 6.3 · Filosofia, etica e religione |
| Mitologia | `trv:mitologia` | 6.3 · Filosofia, etica e religione |
| Motore di ricerca ermeneutico | `trv:motore-ermeneutico` | 1.2 · Informatica e informazione |
| Musica | `trv:musica` | 6.4 · Arti e pratiche performative |
| Neuroscienze | `trv:neuroscienze` | 3.1 · Medicina di base |
| Ontologia | `trv:ontologia` | 6.3 · Filosofia, etica e religione |
| Ontologia Fondamentale | `trv:ontologia-fondamentale` | 6.3 · Filosofia, etica e religione |
| Politica | `trv:politica` | 5.6 · Scienze politiche |
| Programmazione filosofica | `trv:programmazione-filosofica` | 1.2 · Informatica e informazione |
| Programmazione filosofica | `trv:programmazione-filosofica` | 6.3 · Filosofia, etica e religione |
| Psicanalisi | `trv:psicanalisi` | 5.1 · Psicologia e cognizione |
| Psicolinguistica | `trv:psicolinguistica` | 5.1 · Psicologia e cognizione |
| Psicolinguistica | `trv:psicolinguistica-linguistica` | 5.1 · Psicologia e cognizione |
| Psicologia | `trv:psicologia` | 5.1 · Psicologia e cognizione |
| Retorica | `trv:retorica` | 6.2 · Lingue e letterature |
| Scienze Cognitive | `trv:scienze-cognitive` | 5.1 · Psicologia e cognizione |
| Scienze sociali | `trv:scienze-sociali` | 5.9 · Altre scienze sociali |
| Semantica | `trv:semantica` | 6.2 · Lingue e letterature |
| Sociologia | `trv:sociologia` | 5.4 · Sociologia |
| Storia | `trv:storia` | 6.1 · Storia e archeologia |
| Storia dell'Arte | `trv:storia-dellarte` | 6.4 · Arti e pratiche performative |
| Storia della Filosofia | `trv:storia-della-filosofia` | 6.3 · Filosofia, etica e religione |
| Storia delle Religioni | `trv:storia-delle-religioni` | 6.3 · Filosofia, etica e religione |
| Storia delle Scienze | `trv:storia-delle-scienze` | 6.1 · Storia e archeologia |
| Studi Classici | `trv:studi-classici` | 6.2 · Lingue e letterature |
| Teatro | `trv:teatro` | 6.4 · Arti e pratiche performative |
| Tecnologia | `trv:tecnologia` | 2.11 · Altre ingegnerie e tecnologie |
<!-- /table -->

## Legami con Dubium

Un legame `skos:related` fra una categoria e un concetto del manifesto è una lettura: propone con quale nozione di Dubium conviene leggere gli articoli di quella categoria. Non afferma che la categoria sia definita dal manifesto. Le letture più dirette sono quelle in cui il nome coincide: Ontologia Fondamentale e `dub:ontologiaFondamentale`, Ontologia Formale e `dub:ontologiaFormale`, Fenomenologia e `dub:ontologiaFenomenologica`. Altre esplicitano una funzione: la Grammatica rimanda a scrittura e testo, la Dialettica alla pratica dialogica e alla reminiscenza, la Retorica alla condivisione e all'esplicitezza, l'Informatica alla macchina concreta, l'Intelligenza Artificiale alla macchina astratta, la Grande Rete Semantica Mondiale al Web e al capitale semantico. La categoria Heidegger rimanda a `dub:problemaEssere` perché l'epigrafe di «Ontologia Fondamentale» nel sito è la prima pagina di *Essere e tempo*.

<!-- table:dubium -->
| Concetto | IRI | Concetto di Dubium |
| --- | --- | --- |
| Autori | `trv:autori` | `dub:esserci` · esserci |
| Canali | `trv:canali` | `dub:criptaSito` · Cripta Semantica come sito |
| Cibernetica | `trv:cibernetica` | `dub:macchinaAstratta` · macchina astratta |
| Dialettica | `trv:dialettica` | `dub:praticaDialogica` · pratica dialogica |
| Dialettica | `trv:dialettica` | `dub:reminiscenza` · reminiscenza |
| Epistemologia | `trv:epistemologia` | `dub:scienzaTrasformazione` · scienza come trasformazione |
| Epistemologia | `trv:epistemologia` | `dub:teoria` · teoria |
| Fenomenologia | `trv:fenomenologia` | `dub:ontologiaFenomenologica` · ontologia fenomenologica |
| Filosofia Antica | `trv:filosofia-antica` | `dub:esordioGreco` · esordio greco |
| Filosofia Prima | `trv:filosofia-prima` | `dub:ontologiaFondamentale` · ontologia fondamentale |
| Filosofia del Linguaggio | `trv:filosofia-del-linguaggio` | `dub:enunciato` · enunciato |
| Filosofia della Matematica | `trv:filosofia-della-matematica` | `dub:quantificazioneOntologica` · quantificazione ontologica |
| Gnoseologia | `trv:gnoseologia` | `dub:concettualizzazione` · concettualizzazione |
| Grammatica | `trv:grammatica` | `dub:scrittura` · scrittura |
| Grammatica | `trv:grammatica` | `dub:testo` · testo |
| Grande Rete Semantica Mondiale | `trv:www-semantico` | `dub:capitaleSemantico` · capitale semantico |
| Grande Rete Semantica Mondiale | `trv:www-semantico` | `dub:web` · Rete di Portata Mondiale |
| Heidegger | `trv:heidegger` | `dub:problemaEssere` · problema dell'essere |
| Informatica | `trv:informatica` | `dub:macchinaConcreta` · macchina concreta |
| Intelligenza Artificiale | `trv:intelligenza-artificiale` | `dub:macchinaAstratta` · macchina astratta |
| Logica | `trv:logica` | `dub:giudizio` · giudizio |
| Logica | `trv:logica` | `dub:strutturaLogica` · struttura logica |
| Logica | `trv:logica-dialettica` | `dub:giudizio` · giudizio |
| Logica | `trv:logica-dialettica` | `dub:strutturaLogica` · struttura logica |
| Matematica | `trv:matematica` | `dub:reminiscenza` · reminiscenza |
| Metafisica | `trv:metafisica` | `dub:metafisicaOccidentale` · metafisica occidentale |
| Metafisica Generale | `trv:metafisica-generale` | `dub:metafisicaOccidentale` · metafisica occidentale |
| Notizie | `trv:notizie` | `dub:articolo` · articolo come artefatto |
| Ontologia | `trv:ontologia` | `dub:ontologiaEnte` · ontologia dell'ente |
| Ontologia Fondamentale | `trv:ontologia-fondamentale` | `dub:ontologiaFondamentale` · ontologia fondamentale |
| Ontologia Fondamentale | `trv:ontologia-fondamentale` | `dub:problemaSensoEssere` · problema del senso dell'essere |
| Ontologia Formale | `trv:ontologia-formale` | `dub:ontologiaFormale` · ontologia formale fenomenologica |
| Ontologia e Semantica | `trv:ontologia-e-semantica` | `dub:ontologiaInformatica` · ontologia informatica |
| Ontologia e Semantica | `trv:ontologia-e-semantica` | `dub:significato` · significato computabile |
| Programmazione filosofica | `trv:programmazione-filosofica` | `dub:codiceSviluppo` · codice di sviluppo |
| Programmazione filosofica | `trv:programmazione-filosofica` | `dub:iperscritturaConsapevole` · iperscrittura consapevole |
| Recensioni | `trv:recensioni` | `dub:articolo` · articolo come artefatto |
| Retorica | `trv:retorica` | `dub:condivisione` · condivisione |
| Retorica | `trv:retorica` | `dub:esplicitezza` · esplicitezza |
| Semantica | `trv:semantica` | `dub:significato` · significato computabile |
| Stanza degli Articoli | `trv:stanza-degli-articoli` | `dub:articolo` · articolo come artefatto |
| Stanza del Laboratorio Algoritmico | `trv:stanza-del-laboratorio-algoritmico` | `dub:notaIpertestuale` · nota ipertestuale |
| Stanza del Progetto | `trv:stanza-del-progetto` | `dub:gettatezza` · gettatezza |
| Stanza del Progetto | `trv:stanza-del-progetto` | `dub:progettoCripta` · progetto della Cripta |
| Stanza della Rosa Blu | `trv:stanza-della-rosa-blu` | `dub:praticaDialogica` · pratica dialogica |
| Stanza di FINAI | `trv:stanza-di-finai` | `dub:criptaSito` · Cripta Semantica come sito |
| Storia dell'essere | `trv:storia-dellessere` | `dub:pensieroOccidentale` · pensiero occidentale |
| Storia dell'essere | `trv:storia-dellessere` | `dub:sensoEssere` · senso dell'essere |
| Storia della Filosofia | `trv:storia-della-filosofia` | `dub:filosofia` · filosofia |
| Storia della Filosofia | `trv:storia-della-filosofia` | `dub:tradizioneTestuale` · tradizione testuale |
| Web Semantico | `trv:web-semantico` | `dub:ontologiaInformatica` · ontologia informatica |
| Web Semantico | `trv:web-semantico` | `dub:organizzazioneSemantica` · organizzazione semantica |
<!-- /table -->

## Le stanze

Le nove stanze non sono categorie: sono i luoghi allegorici che il sito descrive nei testi alternativi delle sue immagini e nei testi delle pagine. Ogni stanza conserva come fonte la pagina in cui compare e una nota d'ambito che ne riassume l'iconografia. Due stanze, Interpretazione e Giustizia, sono soltanto nominate come portali: la nota lo dichiara. La stanza degli Articoli prende il nome dalla frase «dalla corrente stanza della Cripta Semantica» con cui la pagina presenta la rete degli articoli.

## Vincoli SHACL

Le [forme](shapes.ttl) controllano, per ogni concetto: tre etichette preferite con lingue distinte, uno schema, una notazione in minuscolo, una fonte sul dominio del sito, note d'ambito con lingue distinte, corrispondenze solo verso Wikidata, nessuna `skos:exactMatch`, ponti solo verso i campi FORD di Metrum, e la regola per cui un concetto è di vertice oppure ha un padre nello stesso schema (vincolo SPARQL). Per le categorie è richiesto l'identificativo WordPress. Il programma di verifica prova cinque alterazioni di Trivium (etichetta latina assente, corrispondenza non Wikidata, equivalenza vietata, concetto senza schema, padre in un altro schema), tutte respinte.

## Interrogazioni di esempio

Discipline che il sito colloca nel trivio, con la corrispondenza Wikidata:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?arte ?wikidata WHERE {
  trv:trivio skos:member ?arte .
  ?arte skos:closeMatch ?wikidata .
}
```

Discipline che hanno un ponte verso il campo FORD «Filosofia, etica e religione»:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?nome WHERE {
  ?disciplina skos:broadMatch mtr:ford-6-3 ; skos:prefLabel ?nome .
  FILTER ( lang(?nome) = "it" )
} ORDER BY ?nome
```

Categorie da leggere con il concetto di ontologia fondamentale:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?categoria WHERE { ?categoria skos:related dub:ontologiaFondamentale }
```

## Limiti

Le categorie di un sito cambiano: Trivium fotografa una data e la dichiara. Le traduzioni e le corrispondenze sono scelte editoriali rivedibili. Le descrizioni esistono solo dove l'autore le ha scritte. I ponti FORD servono alla scientometria di Metrum e non pretendono di classificare la filosofia. Il modulo non registra quanti articoli stanno in una categoria, né quali: questo lavoro spetta al servizio semantico del sito.
