# Metrum. Formalizatio

[Dux ad primam lectionem](README.la.md) · [Italiano](FORMALIZZAZIONE.md) · [English](FORMALIZZAZIONE.en.md)

Metrum mensuram investigationis ut ens graphi origine praeditum formalizat. Initium est sententia paginae «De nobis» Cryptae Semanticae: nullae mensurae neutrales qualitatis scientiae exstant, sed systemata technica mensurandi quae eam mutant. Si ita est, mensura in ontologiam ut numerus intrare non potest: ut observatio intret oportet, cum protocollo quod eam produxit, corpore in quo sumpta est, tempore, ambitu, statu exitus et fonte. Hoc documentum formam, tres regulas quae eam regunt, regulas quae eas servari faciunt et nexum cum ceteris partibus describit.

## Forma

| Classis | Consensiones | Quid repraesentet |
| --- | --- | --- |
| `mtr:Observation` | `prov:Entity`, `schema:Observation` | Una adhibitio protocolli ad subiectum. |
| `mtr:Protocol` | `skos:Concept`, `prov:Plan` | Pactum mensurae: quid numeretur vel describatur, qua unitate, de quibus subiectis, qua methodo et fonte. |
| `mtr:Family` | `skos:Concept` | Coetus protocolli: quattuordecim familiae. |
| `mtr:Scope` | `skos:Concept` | Genus subiecti admissum: novem ambitus. |
| `mtr:ValueType` | `skos:Concept` | Genus valoris, cum genere dati XML Schema. |
| `mtr:Coverage` | `skos:Concept` | Ambitus corporis integer, partialis vel ignotus. |
| `mtr:ResultState` | `skos:Concept` | Observatum, absens, suppressum, non applicabile. |
| `mtr:Discipline` | `skos:Concept` | Campus FORD Manualis Frascati 2015: sex campi et quadraginta duo subcampi. |
| `mtr:Principle` | `prov:Entity` | Enuntiatum citabile declarationis publicae de aestimatione responsabili. |
| `mtr:Corpus` | `prov:Entity` | Corpus declaratum, cum IRI proprium habet. |
| `mtr:Comparison` | `prov:Entity` | Comparatio declarata inter duas observationes. |

Undecim classes inter se disiunctae sunt. Proprietates observationis sunt `protocol`, `about` (subproprietas `schema:observationAbout`), `corpus` et `corpusLabel`, `periodStart`, `periodEnd`, `acquiredOn`, `coverage`, `state`, `discipline`, `source` et `evidence` (ambae subproprietates `prov:wasDerivedFrom`), `value`, `numerator`, `denominator`, `appliedMethod`, `editorialReading`. Proprietates protocolli sunt `family`, `scope`, `valueType`, `unit`, `method`, `requiresReferenceSet`, `guidedBy`; principium `cautions` habet. [Hierarchia](la/schema.html) eas cum ambitu subiectorum et valorum enumerat.

## Tres regulae

**Datum absens non est nihil.** Status exitus necessarius est et a valore distinctus. Exitus observatus valorem habere debet; exitus absens, suppressus vel non applicabilis nullum habere potest. Qui observationes colligit absentiam in nihil vertere non potest sine formis violatis.

**Duae mensurae tantum eodem pacto comparantur.** `mtr:Comparison` admittitur tantum si duae observationes subiectum, protocollum, corpus, tempus et disciplinas communicant et si neutra ambitum ignotum habet. Dies acquisitionis mutari potest: id ipsum comparatio describit. Variatio descriptiva manet; iudicium non est.

**Principium finit, non vetat.** `mtr:cautions` principium cum protocollis conectit de quorum usu improprio cavet: DORA cum septem indicibus sedium, pactum 3 CoARA cum indice impulsus et indicibus h, g, i10 et m, principium 8 Leidense cum centesimis partibus et punctis attentionis. Protocolla in indice manent, quia exstant et adhibentur; graphus finem visibilem reddit.

## Regulae SHACL

[Formae](shapes.ttl) quattuor scopos habent. `ObservationShape` protocollum, subiectum, statum, ambitum, tempus dierum, diem acquisitionis, titulum corporis, fontem et testimonium HTTPS, unam saltem disciplinam postulat; tres regulae SPARQL constantiam inter statum et valorem, ordinem temporis et lectionem editoriam pro ambitibus non integris imponunt. `ProtocolShape` tres titulos, notationem, familiam, ambitus, genus valoris, unitatem et methodum tribus linguis, declarationem de coetu comparando et fontem postulat. `PrincipleShape` et `DisciplineShape` fontes, titulos et notationes FORD probant. `ComparisonShape` regulam comparationis regula SPARQL applicat. Programma probationis sex mutationes temptat (observatio sine protocollo, valor in dato absenti, ambitus partialis sine lectione, tempus inversum, comparatio inter protocolla diversa, protocollum sine fonte), omnes recusatas.

## Familiae

<!-- table:families -->
| Clavis | Familia | Protocolla |  |
| --- | --- | --- | --- |
| `agraria` | Res agraria | 3 | Probationes in agro et translationes veterinariae. |
| `apertura` | Apertura et aditus | 5 | Partes et probationes de aditu aperto, notis datorum, indicibus et instrumentis. |
| `arti` | Artes | 3 | Exhibitiones, actiones et iudicia curatorialia documentata. |
| `clinica` | Investigatio clinica | 2 | Receptio in praeceptis clinicis et translatio clinica. |
| `dati` | Data | 3 | Citationes, usus iterati et contextus datorum investigationis. |
| `intervento` | Interventus | 2 | Exitus documentati interventus editorii vel bibliographici. |
| `metodo` | Methodus | 4 | Replicationes, praescriptiones et descriptio conlationum. |
| `ricezione` | Receptio | 13 | Citationes et usus iterati quos fons operi vel subiecto tribuit. |
| `sedi` | Sedes editionis | 8 | Indices de periodicis et seriebus computati, non de singulis operibus. |
| `sociale` | Investigatio socialis | 2 | Usus didactici et testimonia in communitate. |
| `software` | Programmata | 3 | Citationes, usus iterati et reproductio programmatum investigationis. |
| `tecnica` | Ars technica | 2 | Probationes in ambitu operandi et licentiae usus. |
| `trasferimento` | Translatio | 4 | Testimonia usus investigationis extra academiam: acta publica, diplomata, usus. |
| `umanistica` | Studia humanitatis | 4 | Monographiae, editiones criticae, versiones et receptio argumentorum. |
<!-- /table -->

## Protocolla

Protocolla eandem clavem habent qua ministerium semanticum Cryptae utitur. Versio (`@1.0.0`) ministerio pertinet: IRI partis Metrum pactum designat. Protocollum locale in ministerio additum IRI in Metrum non habet donec hic editum sit.

<!-- table:protocols -->
| Clavis | Notio | Familia | Ambitus | Unitas |
| --- | --- | --- | --- | --- |
| `accessibilita-editoriale` | Probationes accessibilitatis superatae | Apertura et aditus | Fructus investigationis | pars centesima |
| `adozioni-cliniche` | Receptio in praeceptis clinicis | Investigatio clinica | Fructus investigationis | documenta |
| `adozioni-documentate` | Usus independentes probati | Translatio | Fructus investigationis | usus |
| `altmetric` | Puncta attentionis Altmetric | Receptio | Opus vel editio | puncta |
| `article-influence` | Puncta auctoritatis articulorum | Sedes editionis | Sedes editionis | index |
| `citazioni` | Citationes receptae | Receptio | Opus vel editio | citationes |
| `citazioni-brevetti` | Citationes in diplomatibus inventorum | Translatio | Opus vel editio | documenta |
| `citazioni-dati` | Citationes datorum | Data | Data investigationis | citationes |
| `citazioni-politiche` | Citationes in actis publicis | Translatio | Opus vel editio | documenta |
| `citazioni-senza-auto` | Citationes sine autocitationibus | Receptio | Opus vel editio | citationes |
| `citazioni-software` | Citationes programmatis | Programmata | Programmata investigationis | citationes |
| `citescore` | Puncta CiteScore | Sedes editionis | Sedes editionis | ratio |
| `completezza-metadati` | Plenitudo notarum datorum | Apertura et aditus | Fructus investigationis | pars centesima |
| `contributi-credit` | Conlationes secundum CRediT | Methodus | Fructus investigationis | textus |
| `copertura-identificatori` | Ambitus indicum persistentium | Apertura et aditus | Persona vel institutio | pars centesima |
| `correzioni-metadati` | Monumenta emendata et probata | Interventus | Interventus documentabilis | schedulae |
| `diffusione-didattica` | Usus didactici documentati | Investigatio socialis | Fructus investigationis | usus |
| `edizioni-critiche` | Conlatio editionis criticae | Studia humanitatis | Opus vel editio | textus |
| `eigenfactor` | Puncta Eigenfactor | Sedes editionis | Sedes editionis | index |
| `emivita-citazioni` | Dimidia aetas citationum receptarum | Sedes editionis | Sedes editionis | anni |
| `esito-intervento` | Exitus interventus documentatus | Interventus | Interventus documentabilis | textus |
| `esito-replica` | Exitus replicationis argumentis munitus | Methodus | Fructus investigationis | textus |
| `esposizioni-curate` | Exhibitiones curatae documentatae | Artes | Artefactum vel actio | eventus |
| `fwci` | Vis citationum ad disciplinam relata | Receptio | Opus vel editio | ratio |
| `g-index` | Index g | Receptio | Persona vel institutio | index |
| `h-index` | Index h | Receptio | Persona vel institutio | index |
| `i10-index` | Index i10 | Receptio | Persona vel institutio | opera |
| `impatto-territoriale` | Testimonium effectus in communitate | Investigatio socialis | Fructus investigationis | textus |
| `jci` | Index citationum periodici | Sedes editionis | Sedes editionis | index |
| `jif` | Index impulsus periodici | Sedes editionis | Sedes editionis | ratio |
| `licenze-applicate` | Licentiae usus documentatae | Ars technica | Fructus investigationis | licentiae |
| `m-index` | Index m | Receptio | Investigator | ratio |
| `materiali-disponibili` | Copia instrumentorum investigationis | Apertura et aditus | Fructus investigationis | pars centesima |
| `monografie-recepite` | Testimonia receptionis monographiarum | Studia humanitatis | Opus vel editio | testimonia |
| `opere-citanti` | Opera citantia distincta | Receptio | Opus vel editio | opera |
| `opere-indicizzate` | Opera indicata | Receptio | Persona vel institutio | opera |
| `percentile` | Centilesima citationum | Receptio | Opus vel editio | centesima pars |
| `performance-documentate` | Actiones publicae documentatae | Artes | Artefactum vel actio | eventus |
| `protocolli-preregistrati` | Praescriptiones ante investigationem documentatae | Methodus | Fructus investigationis | protocolla |
| `qualita-dati` | Contextus et fines datorum | Data | Data investigationis | textus |
| `quota-accesso-aperto` | Pars operum aperte patentium | Apertura et aditus | Persona vel institutio | pars centesima |
| `rcr` | Ratio relativa citationum | Receptio | Opus vel editio | ratio |
| `recepimento-policy` | Receptio in actis vel usu publico | Translatio | Fructus investigationis | textus |
| `repliche-indipendenti` | Replicationes independentes documentatae | Methodus | Fructus investigationis | replicationes |
| `ricezione-argomentativa` | Receptio argumentorum | Studia humanitatis | Fructus investigationis | textus |
| `riferimenti-bibliografici` | Relationes bibliographicae exeuntes | Receptio | Opus vel editio | relationes |
| `riproducibilita-software` | Testimonium reproductionis programmatis | Programmata | Programmata investigationis | textus |
| `riusi-dati` | Usus iterati datorum probati | Data | Data investigationis | usus iterati |
| `riusi-software` | Usus iterati programmatis documentati | Programmata | Programmata investigationis | usus iterati |
| `siti-agrari-indipendenti` | Loci agrarii probationis independentes | Res agraria | Fructus investigationis | loci |
| `sjr` | Index SJR | Sedes editionis | Sedes editionis | index |
| `snip` | Index SNIP | Sedes editionis | Sedes editionis | index |
| `traduzioni-verificate` | Versiones probabiles | Studia humanitatis | Opus vel editio | versiones |
| `trasferimento-clinico` | Testimonium translationis clinicae | Investigatio clinica | Fructus investigationis | textus |
| `trasferimento-ingegneristico` | Probatio in ambitu operandi | Ars technica | Fructus investigationis | textus |
| `trasferimento-veterinario` | Testimonium usus veterinarii | Res agraria | Fructus investigationis | textus |
| `validazione-agronomica` | Probatio in agro | Res agraria | Fructus investigationis | textus |
| `valutazione-artistica` | Iudicium curatoriale vel artisticum | Artes | Artefactum vel actio | textus |
<!-- /table -->

## Principia

Principia paraphrases sunt; fons verba auctoritate praedita servat. Declarationes citatae sunt Declaratio Sancti Francisci de aestimatione investigationis (DORA), Manifestum Leidense (decem principia), Pactum de aestimatione investigationis reformanda (CoARA, quattuor pacta praecipua), principia FAIR, Declaratio communis de principiis citationis datorum (FORCE11, octo principia), principia citationis programmatum (sex), taxonomia CRediT et praescriptio.

<!-- table:principles -->
| Clavis | Principium | Fons | Cavet de |
| --- | --- | --- | --- |
| CRediT | Conlationes quattuordecim muneribus describe, ab ordine auctorum distinctis | [Fons](https://credit.niso.org/) | — |
| Citazione del software 1 | Momentum: programma est fructus investigationis citabilis | [Fons](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 2 | Laus et attributio iis qui programma fecerunt | [Fons](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 3 | Designatio singularis et machinis legibilis | [Fons](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 4 | Persistentia indicum et notarum | [Fons](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 5 | Aditus ad programma et notas | [Fons](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 6 | Proprietas versionis citatae | [Fons](https://doi.org/10.7717/peerj-cs.86) | — |
| CoARA, impegno 1 | Varietatem conlationum et cursuum in investigatione agnosce | [Fons](https://coara.eu/agreement/the-agreement-full-text/) | — |
| CoARA, impegno 2 | Aestimationem in iudicio qualitativo et recensione parium funda, indicibus responsabiliter adhibitis | [Fons](https://coara.eu/agreement/the-agreement-full-text/) | — |
| CoARA, impegno 3 | Usus improprios indicum periodicorum et editionum, velut JIF et index h, relinque | [Fons](https://coara.eu/agreement/the-agreement-full-text/) | `g-index`, `h-index`, `i10-index`, `jif`, `m-index` |
| CoARA, impegno 4 | Ordines institutionum investigationis in aestimatione ne adhibeas | [Fons](https://coara.eu/agreement/the-agreement-full-text/) | — |
| DORA | Ne indicibus periodicorum ad singulos articulos vel personas aestimandas utaris | [Fons](https://sfdora.org/read/) | `article-influence`, `citescore`, `eigenfactor`, `jci`, `jif`, `sjr`, `snip` |
| FAIR A | Accessibile: protocolla aperta et notae quae data superstant | [Fons](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR F | Reperibile: indices persistentes et notae copiosae | [Fons](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR I | Interoperabile: lexica formalia et communia | [Fons](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR R | Iterum usurpabile: licentia perspicua, origo accurata, normae communitatis | [Fons](https://doi.org/10.1038/sdata.2016.18) | — |
| FORCE11 1 | Momentum: data sunt fructus investigationis legitimi et citabiles | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 2 | Laus et attributio omnibus qui data contulerunt | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 3 | Testimonium: data cita quibus affirmatio nititur | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 4 | Designatio singularis et persistens | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 5 | Aditus ad data et notas citata | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 6 | Persistentia indicum et notarum ultra vitam datorum | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 7 | Proprietas et probabilitas partis citatae | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 8 | Interoperabilitas et flexibilitas inter communitates | [Fons](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| Manifesto di Leiden 1 | Aestimatio quantitativa iudicium qualitativum peritorum sustineat | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 10 | Indices identidem examina et renova | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 2 | Opus ad missiones investigationis institutionis, coetus vel personae metire | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 3 | Excellentiam investigationis localiter pertinentis tuere | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 4 | Collectionem datorum et analysin apertas, perspicuas et simplices serva | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 5 | Aestimatis data et analysin probare sine | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 6 | Varietatem disciplinarum in usu edendi et citandi respice | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 7 | Singulos investigatores iudicio qualitativo operum suorum aestima | [Fons](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 8 | Concretionem alienam et falsam subtilitatem vita | [Fons](https://www.nature.com/articles/520429a) | `altmetric`, `percentile` |
| Manifesto di Leiden 9 | Effectus systematicos aestimationis et indicum agnosce | [Fons](https://www.nature.com/articles/520429a) | — |
| Preregistrazione | Hypotheses et methodum ante data collecta declara | [Fons](https://www.cos.io/initiatives/prereg) | — |
<!-- /table -->

## Campi FORD

Manuale Frascati 2015 OCSE investigationem in sex campos (scientiae naturales; ingeniaria et technologia; medicina et salus; agricultura et medicina veterinaria; scientiae sociales; studia humanitatis et artes) et quadraginta duo subcampos dividit. Metrum eos ut schema SKOS cum titulis trium linguarum a Crypta adhibitis edit; codices opus editorium ordinant et meritum non aestimant. Trivium ad eos per `skos:broadMatch` pontem facit.

## Nexus philosophicus

Prooemium Cryptae in secundo loco discrimen describit: cum machina abstracta anni 1936 «processus quantificationis scripturae» incipit, qui in hypertextu ostensionem ultimam invenit ([F08](../dubium/la/term/F08.html)). In quinto loco quantificatio ontologica est relatio inter valores variabilium vinctarum theoriae et enuntiata eius ([F19](../dubium/la/term/F19.html)). Scientometria est quantificatio secundi gradus: non esse quantificat, sed scripturam quae de eo tractat, numerans quomodo textus inter se citent, iterum usurpent, distribuant. Metrum hoc discrimen firmum tenet. Observationes eius opera, editiones, sedes, personas ut subiecta ontica spectant; quaestio de sensu eorum quae metiuntur in Dubio manet. Ideo caput partis ad F08, ad F19 et ad capitale semanticum ([F13](../dubium/la/term/F13.html)) remittit, nullamque aequivalentiam declarat.

Altera sententia est de non neutralitate. Mensura mutat quod metitur: qui se numerari scit, ut numeretur scribit. Manifestum Leidense id effectum systematicum vocat (principium 9); pagina «De nobis» Cryptae id lexico materialismi dialectici dicit. Metrum problema non solvit, sed visibile reddit: quaeque observatio pactum suum declarat, et quodque pactum principia secum fert quae usum eius finiunt.

## Interrogationes exemplares

Protocolla quorum usum DORA finit, cum familia:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?protocollum ?familia WHERE {
  mtr:principle-dora mtr:cautions ?p .
  ?p skos:prefLabel ?protocollum ; mtr:family/skos:prefLabel ?familia .
  FILTER ( lang(?protocollum) = "la" && lang(?familia) = "la" )
}
```

Protocolla ad data investigationis applicabilia:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
SELECT ?p WHERE { ?p mtr:scope mtr:scope-data }
```

Disciplinae Trivii ad campum FORD studiorum humanitatis ponte coniunctae:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?disciplina ?campus WHERE {
  ?campus skos:broader mtr:ford-6 .
  ?disciplina skos:broadMatch ?campus .
}
```

## Fines

Metrum protocolla edit quae ministerium Cryptae hodie novit; scientometriam exhaurire non praesumit. Methodi una sententia describuntur: reproductio vera indicis a fonte eiusque corpore pendet. Tituli Anglici et Latini camporum FORD sunt ii quibus Crypta utitur, non versiones officiales OCSE. Pars observationes veras non continet: eae in ministerio semantico situs vivunt, quod tantum edit quod editores emiserunt.
