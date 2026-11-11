# Trivium. Formalizatio et methodus

[Dux ad primam lectionem](README.la.md) · [Italiano](FORMALIZZAZIONE.md) · [English](FORMALIZZAZIONE.en.md)

Trivium rem aliam ac Dubium formalizat. Dubium textum legit; Trivium ordinem legit: taxonomiam qua situs articulos suos distribuit. Ordo factum documentatum est (categoriae exstant, nomen, hierarchiam, numerum habent), versiones autem, consensiones et pontes lectiones editoriae sunt. Pars utrumque distinguit: quaeque notio fontem publicum categoriae servat, et quidquid additum est in hoc documento declaratur.

## Fontes

| Fons | Quid praebeat | Dies |
| --- | --- | --- |
| API publica categoriarum situs criptasemantica.it | Nomen, clavem, indicem, parentem, descriptionem, nexum | exemplar diei 11 Novembris 2026, in `fonti/` servatum |
| Paginae Consilii, De nobis, Canalium, Articulorum, FINAI, Alexandri Sevardi | Cellae, in textibus imaginum alternis et in textibus paginarum descriptae | 11 Novembris 2026 |
| Wikidata | Res disciplinis congruentes, cum numero nexuum ad Vicipaediam | 11 Novembris 2026 |
| Manuale Frascati 2015 (classificatio FORD), per Metrum | Campi investigationis | editio 2015 |
| Dubium | Notiones prooemii quibus disciplinae conectuntur | versio 0.2.0 |

Numeri articulorum cuiusque categoriae non scribuntur: cotidie mutantur nec notionem describunt.

## Forma

Quattuor classes, omnes subclasses `skos:Concept` et inter se disiunctae: `trv:Disciplina`, `trv:Genere`, `trv:Programma`, `trv:Stanza`. Quattuor schemata SKOS: `trv:discipline`, `trv:generi`, `trv:programmi`, `trv:stanze`. Duae collectiones: `trv:trivio` et `trv:quadrivio`. Una proprietas propria, `trv:identificativoCategoria`, quae numerum categoriae in WordPress servat; cetera SKOS et Dublin Core adhibent.

**Regula schematis assignandi.** A categoria ad radicem ascenditur. Si radix una est e partibus editoriis (nuntii, recensiones, auctores, vitae, merces, synergiae, canales, sine categoria), notio genus est; si una e lineis consilii (communismus digitalis, rete semantica universalis, machina quaerendi hermeneutica, programmatio philosophica, metaphysica ludi, studia academica), consilium est; aliter disciplina. Hierarchia situs per `skos:broader` intra idem schema servatur; radices sunt `skos:topConceptOf` sui schematis.

**Casus «Logica».** Situs duas categorias eadem clave habet: unam summam, alteram sub Dialectica. Unum IRI duos nodos situs confunderet. Altera suffixum `-dialettica` accipit, idem quo situs duas «Antropologia» distinguit, et ambae voces `skos:related` declarantur.

**Tituli.** Italicus est nomen categoriae, littera ad litteram. Anglicus et Latinus versiones editoriae sunt. Pro disciplinis recentioribus Latinus neologismis perspicuis (`Informatica`, `Cybernetica`, `Data ingentia`) vel circumlocutionibus (`Disciplina machinalis`) utitur. Notae ambitus textum auctoris Italicum ferunt et, pro viginti categoriis quae eam habent, versionem Anglicam et Latinam.

## Consensiones cum Wikidata

Methodus haec fuit. Pro quoque nomine Italico ministerium SPARQL Wikidata rogatum est de rebus illo titulo Italico insignitis, paginis distinctionis et articulis scientificis exclusis, ordine numeri nexuum ad Vicipaediam. Res maxime conexa electa est tantum cum descriptio eius sensui categoriae congruebat; in casibus ambiguis nihil electum est. Exempla exclusionum: «Cosmologia» (categoria sub Epistemologia iacet; res maxime conexa est cosmologia physica); «Cronaca» (res maxime conexa est genus historiographicum); «Teoria critica» (res inventa est sociologia critica); «Scienze politiche» (res quinque tantum nexibus); «Storia dell'Africa» (solus continens inventus est); «Filosofia italiana», «Psicanalisi», «Filosofia prima», «Beni culturali» (nulla res illo titulo). «Politica», «Heidegger» et «Nietzsche» singillatim probata sunt.

Relatio semper est `skos:closeMatch`. `skos:exactMatch` regulis SHACL vetatur: categoria editoria notioni encyclopaedicae non est eadem, etiam cum idem nomen fert. Dies probationis est dies exemplaris.

<!-- table:wikidata -->
| Notio | IRI | Res Wikidata |
| --- | --- | --- |
| Aesthetica | `trv:estetica` | [Q35986](https://www.wikidata.org/wiki/Q35986) |
| Anthropologia | `trv:antropologia` | [Q23404](https://www.wikidata.org/wiki/Q23404) |
| Anthropologia | `trv:antropologia-dialettica` | [Q23404](https://www.wikidata.org/wiki/Q23404) |
| Anthropologia culturalis | `trv:antropologia-culturale` | [Q28598](https://www.wikidata.org/wiki/Q28598) |
| Architectura informationis | `trv:architettura-dellinformazione` | [Q845921](https://www.wikidata.org/wiki/Q845921) |
| Ars | `trv:arte` | [Q735](https://www.wikidata.org/wiki/Q735) |
| Ars hodierna | `trv:arte-contemporanea` | [Q186030](https://www.wikidata.org/wiki/Q186030) |
| Ars mediaevalis | `trv:arte-medievale` | [Q3624153](https://www.wikidata.org/wiki/Q3624153) |
| Astronomia | `trv:astronomia` | [Q333](https://www.wikidata.org/wiki/Q333) |
| Biologia | `trv:biologia` | [Q420](https://www.wikidata.org/wiki/Q420) |
| Buddhismus | `trv:buddismo` | [Q748](https://www.wikidata.org/wiki/Q748) |
| Collegium opificum | `trv:sindacato` | [Q178790](https://www.wikidata.org/wiki/Q178790) |
| Constitutio | `trv:costituzione` | [Q7755](https://www.wikidata.org/wiki/Q7755) |
| Cybernetica | `trv:cibernetica` | [Q123637](https://www.wikidata.org/wiki/Q123637) |
| Data ingentia | `trv:big-data` | [Q858810](https://www.wikidata.org/wiki/Q858810) |
| Dialectica | `trv:dialettica` | [Q9453](https://www.wikidata.org/wiki/Q9453) |
| Disciplina machinalis | `trv:machine-learning` | [Q2539](https://www.wikidata.org/wiki/Q2539) |
| Epistemologia | `trv:epistemologia` | [Q9471](https://www.wikidata.org/wiki/Q9471) |
| Ethica | `trv:etica` | [Q9465](https://www.wikidata.org/wiki/Q9465) |
| Ethnologia | `trv:etnologia` | [Q43455](https://www.wikidata.org/wiki/Q43455) |
| Evolutio | `trv:evoluzione` | [Q1063](https://www.wikidata.org/wiki/Q1063) |
| Feminismus | `trv:femminismo` | [Q7252](https://www.wikidata.org/wiki/Q7252) |
| Fundamenta mathematicae | `trv:fondamenti-della-matematica` | [Q833585](https://www.wikidata.org/wiki/Q833585) |
| Genetica | `trv:genetica` | [Q7162](https://www.wikidata.org/wiki/Q7162) |
| Geographia | `trv:geografia` | [Q1071](https://www.wikidata.org/wiki/Q1071) |
| Geopolitica | `trv:geopolitica` | [Q159385](https://www.wikidata.org/wiki/Q159385) |
| Globalizatio | `trv:globalizzazione` | [Q7181](https://www.wikidata.org/wiki/Q7181) |
| Globalizatio | `trv:globalizzazione-storia` | [Q7181](https://www.wikidata.org/wiki/Q7181) |
| Gnoseologia | `trv:gnoseologia` | [Q2560959](https://www.wikidata.org/wiki/Q2560959) |
| Grammatica | `trv:grammatica` | [Q8091](https://www.wikidata.org/wiki/Q8091) |
| Heidegger | `trv:heidegger` | [Q48301](https://www.wikidata.org/wiki/Q48301) |
| Hermeneutica | `trv:ermeneutica` | [Q102686](https://www.wikidata.org/wiki/Q102686) |
| Historia | `trv:storia` | [Q309](https://www.wikidata.org/wiki/Q309) |
| Historia Sardiniae | `trv:storia-della-sardegna` | [Q1516605](https://www.wikidata.org/wiki/Q1516605) |
| Historia aetatis nostrae | `trv:storia-contemporanea` | [Q186075](https://www.wikidata.org/wiki/Q186075) |
| Historia artis | `trv:storia-dellarte` | [Q50637](https://www.wikidata.org/wiki/Q50637) |
| Historia mathematicae | `trv:storia-della-matematica` | [Q185264](https://www.wikidata.org/wiki/Q185264) |
| Historia philosophiae | `trv:storia-della-filosofia` | [Q27654](https://www.wikidata.org/wiki/Q27654) |
| Historia religionum | `trv:storia-delle-religioni` | [Q846742](https://www.wikidata.org/wiki/Q846742) |
| Historia scientiarum | `trv:storia-delle-scienze` | [Q201486](https://www.wikidata.org/wiki/Q201486) |
| Iainismus | `trv:giainismo` | [Q9232](https://www.wikidata.org/wiki/Q9232) |
| Imperialismus | `trv:imperialismo` | [Q7260](https://www.wikidata.org/wiki/Q7260) |
| Industria | `trv:industria` | [Q8148](https://www.wikidata.org/wiki/Q8148) |
| Informatica | `trv:informatica` | [Q21198](https://www.wikidata.org/wiki/Q21198) |
| Intellegentia artificialis | `trv:intelligenza-artificiale` | [Q11660](https://www.wikidata.org/wiki/Q11660) |
| Iura humana | `trv:diritti-umani` | [Q8458](https://www.wikidata.org/wiki/Q8458) |
| Iurisprudentia | `trv:giurisprudenza` | [Q4932206](https://www.wikidata.org/wiki/Q4932206) |
| Ius | `trv:diritto` | [Q7748](https://www.wikidata.org/wiki/Q7748) |
| Labor | `trv:lavoro` | [Q268378](https://www.wikidata.org/wiki/Q268378) |
| Linguistica | `trv:linguistica` | [Q8162](https://www.wikidata.org/wiki/Q8162) |
| Litterae | `trv:letteratura` | [Q8242](https://www.wikidata.org/wiki/Q8242) |
| Logica | `trv:logica` | [Q8078](https://www.wikidata.org/wiki/Q8078) |
| Logica | `trv:logica-dialettica` | [Q8078](https://www.wikidata.org/wiki/Q8078) |
| Logica mathematica | `trv:logica-matematica` | [Q1166618](https://www.wikidata.org/wiki/Q1166618) |
| Macrooeconomia | `trv:macroeconomia` | [Q39680](https://www.wikidata.org/wiki/Q39680) |
| Materialismus dialecticus | `trv:materialismo-dialettico` | [Q181207](https://www.wikidata.org/wiki/Q181207) |
| Materialismus historicus | `trv:materialismo-storico` | [Q190004](https://www.wikidata.org/wiki/Q190004) |
| Mathematica | `trv:matematica` | [Q395](https://www.wikidata.org/wiki/Q395) |
| Metaphysica | `trv:metafisica` | [Q35277](https://www.wikidata.org/wiki/Q35277) |
| Metaphysica generalis | `trv:metafisica-generale` | [Q35277](https://www.wikidata.org/wiki/Q35277) |
| Metaversa | `trv:metaversi` | [Q2632041](https://www.wikidata.org/wiki/Q2632041) |
| Musica | `trv:musica` | [Q638](https://www.wikidata.org/wiki/Q638) |
| Mythologia | `trv:mitologia` | [Q9134](https://www.wikidata.org/wiki/Q9134) |
| Mythus | `trv:mito` | [Q12827256](https://www.wikidata.org/wiki/Q12827256) |
| Neuroscientiae | `trv:neuroscienze` | [Q207011](https://www.wikidata.org/wiki/Q207011) |
| Neuroscientiae cognitivae | `trv:neuroscienze-cognitive` | [Q1138951](https://www.wikidata.org/wiki/Q1138951) |
| Nietzsche | `trv:nietzsche` | [Q9358](https://www.wikidata.org/wiki/Q9358) |
| Nuntii | `trv:notizie` | [Q38926](https://www.wikidata.org/wiki/Q38926) |
| Oecologia | `trv:ecologia` | [Q7150](https://www.wikidata.org/wiki/Q7150) |
| Oeconomia | `trv:economia` | [Q159810](https://www.wikidata.org/wiki/Q159810) |
| Oeconomia politica | `trv:economia-politica` | [Q47555](https://www.wikidata.org/wiki/Q47555) |
| Ontologia | `trv:ontologia` | [Q44325](https://www.wikidata.org/wiki/Q44325) |
| Ontologia formalis | `trv:ontologia-formale` | [Q1437388](https://www.wikidata.org/wiki/Q1437388) |
| Phaenomenologia | `trv:fenomenologia` | [Q179235](https://www.wikidata.org/wiki/Q179235) |
| Philologia | `trv:filologia` | [Q40634](https://www.wikidata.org/wiki/Q40634) |
| Philosophia aetatis nostrae | `trv:filosofia-contemporanea` | [Q943303](https://www.wikidata.org/wiki/Q943303) |
| Philosophia antiqua | `trv:filosofia-antica` | [Q204100](https://www.wikidata.org/wiki/Q204100) |
| Philosophia linguae | `trv:filosofia-del-linguaggio` | [Q484761](https://www.wikidata.org/wiki/Q484761) |
| Philosophia mathematicae | `trv:filosofia-della-matematica` | [Q180536](https://www.wikidata.org/wiki/Q180536) |
| Philosophia musicae | `trv:filosofia-della-musica` | [Q2092865](https://www.wikidata.org/wiki/Q2092865) |
| Philosophia politica | `trv:filosofia-politica` | [Q179805](https://www.wikidata.org/wiki/Q179805) |
| Philosophia recentior | `trv:filosofia-moderna` | [Q860746](https://www.wikidata.org/wiki/Q860746) |
| Philosophia scientiae | `trv:filosofia-della-scienza` | [Q59115](https://www.wikidata.org/wiki/Q59115) |
| Philosophia technicae | `trv:filosofia-della-tecnica` | [Q5862034](https://www.wikidata.org/wiki/Q5862034) |
| Philosophia theoretica | `trv:filosofia-teoretica` | [Q2166096](https://www.wikidata.org/wiki/Q2166096) |
| Physica | `trv:fisica` | [Q413](https://www.wikidata.org/wiki/Q413) |
| Polemologia | `trv:polemologia` | [Q1367522](https://www.wikidata.org/wiki/Q1367522) |
| Politica | `trv:politica` | [Q7163](https://www.wikidata.org/wiki/Q7163) |
| Politica externa | `trv:politica-estera` | [Q181648](https://www.wikidata.org/wiki/Q181648) |
| Progressus oeconomicus | `trv:sviluppo` | [Q4530482](https://www.wikidata.org/wiki/Q4530482) |
| Psycholinguistica | `trv:psicolinguistica` | [Q179488](https://www.wikidata.org/wiki/Q179488) |
| Psycholinguistica | `trv:psicolinguistica-linguistica` | [Q179488](https://www.wikidata.org/wiki/Q179488) |
| Psychologia | `trv:psicologia` | [Q9418](https://www.wikidata.org/wiki/Q9418) |
| Psychologia evolutionis | `trv:psicologia-dello-sviluppo` | [Q175002](https://www.wikidata.org/wiki/Q175002) |
| Psychologia socialis | `trv:psicologia-sociale` | [Q161272](https://www.wikidata.org/wiki/Q161272) |
| Quadrivium | `trv:quadrivio` | [Q273822](https://www.wikidata.org/wiki/Q273822) |
| Recensiones | `trv:recensioni` | [Q265158](https://www.wikidata.org/wiki/Q265158) |
| Relationes internationales | `trv:relazioni-internazionali` | [Q166542](https://www.wikidata.org/wiki/Q166542) |
| Res nummaria | `trv:finanza` | [Q43015](https://www.wikidata.org/wiki/Q43015) |
| Rete semantica | `trv:web-semantico` | [Q54837](https://www.wikidata.org/wiki/Q54837) |
| Rhetorica | `trv:retorica` | [Q81009](https://www.wikidata.org/wiki/Q81009) |
| Scientiae cognitivae | `trv:scienze-cognitive` | [Q147638](https://www.wikidata.org/wiki/Q147638) |
| Scripta disputatoria | `trv:saggistica` | [Q27801](https://www.wikidata.org/wiki/Q27801) |
| Semantica | `trv:semantica` | [Q39645](https://www.wikidata.org/wiki/Q39645) |
| Sociologia | `trv:sociologia` | [Q21201](https://www.wikidata.org/wiki/Q21201) |
| Spiritualismus | `trv:spiritualismo` | [Q2636432](https://www.wikidata.org/wiki/Q2636432) |
| Studia culturalia | `trv:studi-culturali` | [Q1143546](https://www.wikidata.org/wiki/Q1143546) |
| Studia postcolonialia | `trv:studi-postcoloniali` | [Q265425](https://www.wikidata.org/wiki/Q265425) |
| Technologia | `trv:tecnologia` | [Q11016](https://www.wikidata.org/wiki/Q11016) |
| Theatrum | `trv:teatro` | [Q11635](https://www.wikidata.org/wiki/Q11635) |
| Theoria Marxiana | `trv:teoria-marxista` | [Q7264](https://www.wikidata.org/wiki/Q7264) |
| Theoria systematum | `trv:teoria-dei-sistemi` | [Q269699](https://www.wikidata.org/wiki/Q269699) |
| Transhumanismus | `trv:transumanesimo` | [Q194100](https://www.wikidata.org/wiki/Q194100) |
| Trivium | `trv:trivio` | [Q205186](https://www.wikidata.org/wiki/Q205186) |
| Umbria | `trv:umbria` | [Q1280](https://www.wikidata.org/wiki/Q1280) |
<!-- /table -->

## Pontes ad campos FORD

Pons est `skos:broadMatch`: categoria Cryptae ut angustior campo FORD, vel intra eum, legitur. Classificatio FORD actiones investigationis describit, non cogitationes: ideo nonnulli pontes mirantur. Anthropologia in «Sociologia» (5.4) iacet quia Manuale Frascati anthropologiam et ethnologiam ibi includit; rhetorica et grammatica in «Linguae et litterae» (6.2); logica duos pontes habet, philosophiam (6.3) et mathematicam (1.1); geographia situs, quae physicam et biologiam colligit, ut «Tellus et ambitus» (1.5) legitur. Pontes tantum declarantur ubi collocatio defendi potest; categoriae chronicae, politicae internae vel territorii nullum habent.

<!-- table:ford -->
| Notio | IRI | Campus FORD |
| --- | --- | --- |
| Aesthetica | `trv:estetica` | 6.3 · Philosophia, ethica et religio |
| Anthropologia | `trv:antropologia` | 5.4 · Sociologia |
| Anthropologia | `trv:antropologia-dialettica` | 5.4 · Sociologia |
| Ars | `trv:arte` | 6.4 · Artes, spectacula et musica |
| Astronomia | `trv:astronomia` | 1.3 · Physica |
| Biologia | `trv:biologia` | 1.6 · Biologia |
| Buddhismus | `trv:buddismo` | 6.3 · Philosophia, ethica et religio |
| Cosmologia | `trv:cosmologia` | 1.3 · Physica |
| Cybernetica | `trv:cibernetica` | 1.2 · Informatica et notitia |
| Cybernetica | `trv:cibernetica` | 2.2 · Ingeniaria electrica, electronica et informatica |
| Data ingentia | `trv:big-data` | 1.2 · Informatica et notitia |
| Dialectica | `trv:dialettica` | 6.3 · Philosophia, ethica et religio |
| Disciplina machinalis | `trv:machine-learning` | 1.2 · Informatica et notitia |
| Epistemologia | `trv:epistemologia` | 6.3 · Philosophia, ethica et religio |
| Epistemologia et metaphysica | `trv:epistemologia-e-metafisica` | 6.3 · Philosophia, ethica et religio |
| Ethica | `trv:etica` | 6.3 · Philosophia, ethica et religio |
| Feminismus | `trv:femminismo` | 5.4 · Sociologia |
| Genetica | `trv:genetica` | 1.6 · Biologia |
| Geographia | `trv:geografia` | 1.5 · Tellus et ambitus |
| Geopolitica | `trv:geopolitica` | 5.6 · Scientiae politicae |
| Grammatica | `trv:grammatica` | 6.2 · Linguae et litterae |
| Hermeneutica | `trv:ermeneutica` | 6.3 · Philosophia, ethica et religio |
| Historia | `trv:storia` | 6.1 · Historia et archaeologia |
| Historia artis | `trv:storia-dellarte` | 6.4 · Artes, spectacula et musica |
| Historia philosophiae | `trv:storia-della-filosofia` | 6.3 · Philosophia, ethica et religio |
| Historia religionum | `trv:storia-delle-religioni` | 6.3 · Philosophia, ethica et religio |
| Historia scientiarum | `trv:storia-delle-scienze` | 6.1 · Historia et archaeologia |
| Iainismus | `trv:giainismo` | 6.3 · Philosophia, ethica et religio |
| Informatica | `trv:informatica` | 1.2 · Informatica et notitia |
| Intellegentia artificialis | `trv:intelligenza-artificiale` | 1.2 · Informatica et notitia |
| Iurisprudentia | `trv:giurisprudenza` | 5.5 · Ius |
| Ius | `trv:diritto` | 5.5 · Ius |
| Linguistica | `trv:linguistica` | 6.2 · Linguae et litterae |
| Litterae | `trv:letteratura` | 6.2 · Linguae et litterae |
| Logica | `trv:logica` | 1.1 · Mathematica |
| Logica | `trv:logica` | 6.3 · Philosophia, ethica et religio |
| Logica | `trv:logica-dialettica` | 1.1 · Mathematica |
| Logica | `trv:logica-dialettica` | 6.3 · Philosophia, ethica et religio |
| Logica mathematica | `trv:logica-matematica` | 1.1 · Mathematica |
| Machina quaerendi hermeneutica | `trv:motore-ermeneutico` | 1.2 · Informatica et notitia |
| Mathematica | `trv:matematica` | 1.1 · Mathematica |
| Metaphysica | `trv:metafisica` | 6.3 · Philosophia, ethica et religio |
| Metaphysica generalis | `trv:metafisica-generale` | 6.3 · Philosophia, ethica et religio |
| Metaphysica ludi | `trv:metafisica-gioco` | 6.3 · Philosophia, ethica et religio |
| Musica | `trv:musica` | 6.4 · Artes, spectacula et musica |
| Mythologia | `trv:mitologia` | 6.3 · Philosophia, ethica et religio |
| Neuroscientiae | `trv:neuroscienze` | 3.1 · Medicina fundamentalis |
| Oecologia | `trv:ecologia` | 1.6 · Biologia |
| Oeconomia | `trv:economia` | 5.2 · Oeconomia et negotia |
| Ontologia | `trv:ontologia` | 6.3 · Philosophia, ethica et religio |
| Ontologia fundamentalis | `trv:ontologia-fondamentale` | 6.3 · Philosophia, ethica et religio |
| Phaenomenologia | `trv:fenomenologia` | 6.3 · Philosophia, ethica et religio |
| Philologia | `trv:filologia` | 6.2 · Linguae et litterae |
| Philosophia linguae | `trv:filosofia-del-linguaggio` | 6.3 · Philosophia, ethica et religio |
| Philosophia orientalis | `trv:filosofia-orientale` | 6.3 · Philosophia, ethica et religio |
| Philosophia politica | `trv:filosofia-politica` | 6.3 · Philosophia, ethica et religio |
| Philosophia scientiae | `trv:filosofia-della-scienza` | 6.3 · Philosophia, ethica et religio |
| Physica | `trv:fisica` | 1.3 · Physica |
| Politica | `trv:politica` | 5.6 · Scientiae politicae |
| Programmatio philosophica | `trv:programmazione-filosofica` | 1.2 · Informatica et notitia |
| Programmatio philosophica | `trv:programmazione-filosofica` | 6.3 · Philosophia, ethica et religio |
| Psychoanalysis | `trv:psicanalisi` | 5.1 · Psychologia et cognitio |
| Psycholinguistica | `trv:psicolinguistica` | 5.1 · Psychologia et cognitio |
| Psycholinguistica | `trv:psicolinguistica-linguistica` | 5.1 · Psychologia et cognitio |
| Psychologia | `trv:psicologia` | 5.1 · Psychologia et cognitio |
| Res nummaria | `trv:finanza` | 5.2 · Oeconomia et negotia |
| Rete semantica universalis | `trv:www-semantico` | 1.2 · Informatica et notitia |
| Rhetorica | `trv:retorica` | 6.2 · Linguae et litterae |
| Scientiae cognitivae | `trv:scienze-cognitive` | 5.1 · Psychologia et cognitio |
| Scientiae sociales | `trv:scienze-sociali` | 5.9 · Aliae scientiae sociales |
| Semantica | `trv:semantica` | 6.2 · Linguae et litterae |
| Sociologia | `trv:sociologia` | 5.4 · Sociologia |
| Studia classica | `trv:studi-classici` | 6.2 · Linguae et litterae |
| Technologia | `trv:tecnologia` | 2.11 · Aliae disciplinae ingeniariae et technologiae |
| Theatrum | `trv:teatro` | 6.4 · Artes, spectacula et musica |
<!-- /table -->

## Nexus cum Dubio

Nexus `skos:related` inter categoriam et notionem prooemii lectio est: proponit qua notione Dubii articuli illius categoriae legendi sint. Non affirmat categoriam a prooemio definiri. Lectiones directissimae sunt ubi nomen congruit: Ontologia Fundamentalis et `dub:ontologiaFondamentale`, Ontologia Formalis et `dub:ontologiaFormale`, Phaenomenologia et `dub:ontologiaFenomenologica`. Aliae munus explicant: Grammatica ad scripturam et textum remittit, Dialectica ad usum dialogicum et reminiscentiam, Rhetorica ad communicationem et explicitatem, Informatica ad machinam concretam, Intellegentia artificialis ad machinam abstractam, Rete semantica universalis ad Rete et capitale semanticum. Categoria Heidegger ad `dub:problemaEssere` remittit quia epigraphe «Ontologiae Fundamentalis» in situ prima pagina libri *Sein und Zeit* est.

<!-- table:dubium -->
| Notio | IRI | Notio Dubii |
| --- | --- | --- |
| Auctores | `trv:autori` | `dub:esserci` · adesse (Dasein) |
| Canales | `trv:canali` | `dub:criptaSito` · Crypta Semantica ut situs retialis |
| Cella Articulorum | `trv:stanza-degli-articoli` | `dub:articolo` · articulus ut artefactum |
| Cella Consilii | `trv:stanza-del-progetto` | `dub:gettatezza` · iectitas |
| Cella Consilii | `trv:stanza-del-progetto` | `dub:progettoCripta` · propositum Cryptae |
| Cella FINAI | `trv:stanza-di-finai` | `dub:criptaSito` · Crypta Semantica ut situs retialis |
| Cella Laboratorii Algorithmici | `trv:stanza-del-laboratorio-algoritmico` | `dub:notaIpertestuale` · nota hypertextualis |
| Cella Rosae Caeruleae | `trv:stanza-della-rosa-blu` | `dub:praticaDialogica` · exercitatio dialogica |
| Cybernetica | `trv:cibernetica` | `dub:macchinaAstratta` · machina abstracta |
| Dialectica | `trv:dialettica` | `dub:praticaDialogica` · exercitatio dialogica |
| Dialectica | `trv:dialettica` | `dub:reminiscenza` · reminiscentia |
| Epistemologia | `trv:epistemologia` | `dub:scienzaTrasformazione` · scientia ut transformatio |
| Epistemologia | `trv:epistemologia` | `dub:teoria` · theoria |
| Gnoseologia | `trv:gnoseologia` | `dub:concettualizzazione` · conceptuum ordinatio |
| Grammatica | `trv:grammatica` | `dub:scrittura` · scriptura |
| Grammatica | `trv:grammatica` | `dub:testo` · textus |
| Heidegger | `trv:heidegger` | `dub:problemaEssere` · quaestio de esse |
| Historia essendi | `trv:storia-dellessere` | `dub:pensieroOccidentale` · cogitatio occidentalis |
| Historia essendi | `trv:storia-dellessere` | `dub:sensoEssere` · sensus essendi |
| Historia philosophiae | `trv:storia-della-filosofia` | `dub:filosofia` · philosophia |
| Historia philosophiae | `trv:storia-della-filosofia` | `dub:tradizioneTestuale` · traditio textualis |
| Informatica | `trv:informatica` | `dub:macchinaConcreta` · machina concreta |
| Intellegentia artificialis | `trv:intelligenza-artificiale` | `dub:macchinaAstratta` · machina abstracta |
| Logica | `trv:logica` | `dub:giudizio` · iudicium |
| Logica | `trv:logica` | `dub:strutturaLogica` · structura logica |
| Logica | `trv:logica-dialettica` | `dub:giudizio` · iudicium |
| Logica | `trv:logica-dialettica` | `dub:strutturaLogica` · structura logica |
| Mathematica | `trv:matematica` | `dub:reminiscenza` · reminiscentia |
| Metaphysica | `trv:metafisica` | `dub:metafisicaOccidentale` · metaphysica occidentalis |
| Metaphysica generalis | `trv:metafisica-generale` | `dub:metafisicaOccidentale` · metaphysica occidentalis |
| Nuntii | `trv:notizie` | `dub:articolo` · articulus ut artefactum |
| Ontologia | `trv:ontologia` | `dub:ontologiaEnte` · ontologia entium |
| Ontologia et semantica | `trv:ontologia-e-semantica` | `dub:ontologiaInformatica` · ontologia informatica |
| Ontologia et semantica | `trv:ontologia-e-semantica` | `dub:significato` · significatio computabilis |
| Ontologia formalis | `trv:ontologia-formale` | `dub:ontologiaFormale` · ontologia phaenomenologica formalis |
| Ontologia fundamentalis | `trv:ontologia-fondamentale` | `dub:ontologiaFondamentale` · ontologia fundamentalis |
| Ontologia fundamentalis | `trv:ontologia-fondamentale` | `dub:problemaSensoEssere` · quaestio de sensu essendi |
| Phaenomenologia | `trv:fenomenologia` | `dub:ontologiaFenomenologica` · ontologia phaenomenologica |
| Philosophia antiqua | `trv:filosofia-antica` | `dub:esordioGreco` · exordium Graecum |
| Philosophia linguae | `trv:filosofia-del-linguaggio` | `dub:enunciato` · enuntiatum |
| Philosophia mathematicae | `trv:filosofia-della-matematica` | `dub:quantificazioneOntologica` · quantificatio ontologica |
| Philosophia prima | `trv:filosofia-prima` | `dub:ontologiaFondamentale` · ontologia fundamentalis |
| Programmatio philosophica | `trv:programmazione-filosofica` | `dub:codiceSviluppo` · praecepta ad Rete exstruendum |
| Programmatio philosophica | `trv:programmazione-filosofica` | `dub:iperscritturaConsapevole` · hyperscriptura conscia |
| Recensiones | `trv:recensioni` | `dub:articolo` · articulus ut artefactum |
| Rete semantica | `trv:web-semantico` | `dub:ontologiaInformatica` · ontologia informatica |
| Rete semantica | `trv:web-semantico` | `dub:organizzazioneSemantica` · ordinatio semantica |
| Rete semantica universalis | `trv:www-semantico` | `dub:capitaleSemantico` · capitale semanticum |
| Rete semantica universalis | `trv:www-semantico` | `dub:web` · Rete Totum Orbem Complectens |
| Rhetorica | `trv:retorica` | `dub:condivisione` · communicatio |
| Rhetorica | `trv:retorica` | `dub:esplicitezza` · ratio explicita |
| Semantica | `trv:semantica` | `dub:significato` · significatio computabilis |
<!-- /table -->

## Cellae

Novem cellae categoriae non sunt: loca allegorica sunt quae situs in textibus imaginum alternis et in textibus paginarum describit. Quaeque cella ut fontem paginam in qua apparet et notam ambitus iconographiam breviter exponentem servat. Duae cellae, Interpretationis et Iustitiae, tantum ut portae nominantur: nota id declarat. Cella Articulorum nomen e sententia «e praesenti cella Cryptae Semanticae» ducit, qua pagina rete articulorum introducit.

## Regulae SHACL

[Formae](shapes.ttl) pro quaque notione probant: tres titulos praelatos linguis distinctis, schema, notationem minusculis litteris, fontem in dominio situs, notas ambitus linguis distinctis, consensiones ad solam Wikidata, nullam `skos:exactMatch`, pontes ad solos campos FORD partis Metrum, et regulam qua notio summa est vel parentem in eodem schemate habet (regula SPARQL). Categoriis index WordPress requiritur. Programma probationis quinque mutationes Trivii temptat (titulus Latinus absens, consensio non Wikidata, aequivalentia vetita, notio sine schemate, parens in alio schemate), omnes recusatas.

## Interrogationes exemplares

Disciplinae quas situs in trivio collocat, cum consensione Wikidata:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?ars ?wikidata WHERE {
  trv:trivio skos:member ?ars .
  ?ars skos:closeMatch ?wikidata .
}
```

Disciplinae ponte ad campum FORD «Philosophia, ethica et religio» coniunctae:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?nomen WHERE {
  ?disciplina skos:broadMatch mtr:ford-6-3 ; skos:prefLabel ?nomen .
  FILTER ( lang(?nomen) = "la" )
} ORDER BY ?nomen
```

Categoriae notione ontologiae fundamentalis legendae:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?categoria WHERE { ?categoria skos:related dub:ontologiaFondamentale }
```

## Fines

Categoriae situs mutantur: Trivium diem effingit eumque declarat. Versiones et consensiones electiones editoriae retractabiles sunt. Descriptiones tantum exstant ubi auctor eas scripsit. Pontes FORD scientometriae partis Metrum serviunt neque philosophiam classificare praesumunt. Pars non scribit quot articuli in categoria sint, neque qui: hoc opus ministerio semantico situs pertinet.
