# Formalizatio prooemii

[Prooemium](https://criptasemantica.it/) a perplexitate de voce «ens» incipit. Quaestionem de sensu essendi cum historia philosophiae, hyperscriptura et dependentia diversarum inquirendi rationum conectit. [Dux incipientium](README.la.md) consilium per exemplum aperit.

## Quomodo formalizatio legatur

Forma OWL structuram schedularum describit. Quaestio et sententia genera disiuncta schedulae inquisitionis sunt. Nexus inversus a sententia ad eius assertiones ducit, ita ut ex consequentia OWL utraque via pateat. [OWL 2](https://www.w3.org/TR/owl2-syntax/)

Graphus sermonis relationem ut assertionem intra sententiam exhibet. Signis `Arc(r,p,s,k,o)` indicatur arcum `r` in sententia `p` notionem subiectam `s` cum notione obiecta `o` per genus relationis `k` conectere. Quaeque sententia locum fontis, rationem legendi, statum et formulam habet. Paraphrasis reformulationem textui attribuit, electio interpretativa iudicium in exemplo factum indicat, extensio autem ad aliam paginam publicam refertur. Arcus investigationem adiuvat. Ambitus et structura logica in formula servantur.

In formulis `∀x:D` et `∃x:D` variabile ad certum ambitum restringunt. `¬`, `∧`, `∨`, `→` et `↔` negationem, coniunctionem, disiunctionem, implicationem et aequivalentiam significant. `:=` breviationem definit. `◇` possibilitatem notat, `Oₘ` munus a prooemio praescriptum, `⟦…⟧` mentionem in sermone. `OInf`, `OAn` et `OFen` ontologias informaticam, analyticam et phaenomenologicam breviter significant. `D(T)` est ambitus theoriae, `Dᵣ` ambitus secundum regionem apertus. Nomina Italica in formulis easdem notiones in omnibus editionibus designant. Formulae sunt descriptiones textuales. Semantica mundorum possibilium hic non definitur.

## Loci prooemii

| Locus | Materia | Schedulae |
| --- | --- | --- |
| P0 | Titulus, epigraphe, vox «ens», intellectus praesumptus et perplexitas. | F01, Q01 |
| P1 | Necessitas quaestionem de esse ponendi, exordium Graecum, oralis exercitatio, dialogus, reminiscentia et transformatio animi. | F02–F05, Q02 |
| P2 | Traditio textualis, discrimen anni 1936, machina abstracta, hyperhistoria, sphaera informationis et destinatio ad hypertextum. | F06–F09 |
| P3 | Scriptura et hyperscriptura, gradus elementaris et conscius, materia, significatio computabilis et capitale semanticum. | F10–F13 |
| P4 | Ontologia ut specificatio, ordinatio conceptuum communis, reflexivitas et duo ambitus facultatis tradendi. | F14–F16 |
| P5 | Obligatio analytica, quid et quomodo specificetur, enuntiata, variabilia ligata, valores et duplex postulatio quantificationis. | F17–F20 |
| P6 | Dependentia phaenomenologica, inquisitio formalis et regionalis, iudicium, essentiae regionales et apertio ambitus. | F21–F25, Q03 |
| P7 | Ens ut res, esse entis, esse ipsum, quattuor munera inquisitionis, relatio ad limen et nihil. | F26–F30, Q04 |
| P8 | Sensus ontologiarum entium, totalitas non expressa, inquisitio essentiae et sensus, productio hypertextus. | F31–F35, Q05–Q06 |

## Electiones interpretativae

**Genealogia fonti attributa.** F01 usum familiarem auditorum a pristina loquentium fiducia distinguit. F03 et F07 ordinem temporum et assertionem de prima machina abstracta prooemio attribuunt. Commentarius Turingi se anno 1936 receptum et lectum esse indicat et in volumine 42 *Proceedings* (1936–37) editus est. Prooemium nomen Turingi tacet. [Commentarius Turingi](https://fab.cba.mit.edu/classes/862.22/notes/computation/Turing-1936.pdf)

**Scriptura, facultas tradendi et quantificatio.** F08 quantificationem scripturae ut processum historicum et technicum describit. F19 theoriam, enuntiatum, variabile ligatum et valorem admissibilem conectit. In F16 `∀c∈D ◇Veicola(p,c)` facultatem cuiusque materiae tradendae significat; `◇Veicola(p,c₀)` ad materiam certam spectat. Prima formula quaestionem de omnibus simul tradendis apertam relinquit. F21 de ontologiis analyticis agit, iis etiam quae ad obiecta aut hyperobiecta diriguntur, sive conscie sive inscie. F25 ostendit ambitum quantificationis ab inquisitione pendere.

**Duae tractationes ontologicae.** F26 tractationem ontologicam entis ut rei consignat. F27 tractationem onticam essendi ad ens refert, quotiens esse in ontologia entium tractatur. F28 inquisitionem de esse ipso et absentiam rei praeelectae intra praeceptum prooemii ponit. F29 adesse ipsius esse ut rationem indicandam tractat. In F13 adesse partem humanam accessus ad materiam designat.

**Nihil et fundatio.** F30 signa mentionis adhibet ut relationem ad limen indicet. `dub:nulla` sensum illius loci designat. In OWL `owl:Nothing` classem vacuam significat. F31 fundationem sensus una via exprimit. X03 sustentationem onticam inquisitionis altera via exprimit. Duae relationes nomina distincta habent et nullum axioma transitivitatis accipiunt. F32 totalitatem inquisitionis apertam servat. [Propositum](https://criptasemantica.it/progetto/)

X01–X03 rationem proiciendi, quattuor determinationes iectitatis et tabulam entium attingunt. X04 situm, notas atque hypertextum recurrentem distinguit. X05 articulum cum articulatione aperturae conectit. Singulis schedulis fons proprius assignatur. [Propositum](https://criptasemantica.it/progetto/), [De Crypta](https://criptasemantica.it/chi-siamo/), [Articuli](https://criptasemantica.it/articoli/)

## Exemplum interrogationis

Interrogatio invenit quid secundum prooemium sensum ab ontologia fundamentali accipiat, una cum ratione legendi et fonte.

```sparql
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>

SELECT ?notio ?sententia ?lectio ?locus ?fons WHERE {
  ?arcus a dub:RelationAssertion ;
    dub:subjectConcept ?notio ;
    dub:relationKind dub:rel-riceveSensoDa ;
    dub:objectConcept dub:ontologiaFondamentale ;
    dub:belongsTo ?sententia .
  ?sententia dub:derivedFrom ?locus ; dub:readingMode ?lectio .
  ?locus dub:partOfSource ?fons .
}
```

Exspectantur `dub:ontologiaEnte`, `dub:F31`, `dub:Fondamentale`, `dub:P8` et inscriptio prooemii. [Index](la/index.html#F31) eandem viam lectori praebet.

## Graphum amplificare et probare

Novo loco indicium iterum inveniendum tribue. Novae sententiae signum, fontem, statum et vim assigna. Interpretatio diversa schedulam propriam accipiat. SHACL probat num adsint data requisita; consequentia OWL nexus structurae praebet. Ut interpretatio et assertiones historicae aestimentur, fontes legendi sunt. [OWL 2](https://www.w3.org/TR/owl2-syntax/), [SHACL](https://www.w3.org/TR/shacl/)

## Index formularum

| Schedula | Locus | Formula |
| --- | --- | --- |
| **F01** · A familiaritate ad perplexitatem | P0 | `Cita(epigrafe,sofista244a) ∧ AutoreAttribuito(sofista244a,platone) ∧ TraduzioneAttribuita(epigrafe,pietroChiodi) ∧ Familiarità(voi, «essente», t₀) ∧ Crede(noi, Comprende(noi, «essente»), t₁) ∧ Perplessi(noi, «essente», t₂) ∧ t₁ < t₂` |
| **F02** · Necessitas quaestionem ponendi | P1 | `Oₘ Porre(problemaEssere) ∧ Innesca(Oₘ Porre(problemaEssere), pensieroOccidentale)` |
| **F03** · Locus et tempus exordii | P1 | `EsordioDi(esordioGreco, pensieroOccidentale) ∧ Luogo(esordioGreco, grecia) ∧ Collocato(esordioGreco, «VII sec. a.C.; I–II sec. AUC»)` |
| **F04** · Philosophia oralis et traditio scripta | P1 | `CorpoTradizionale(filosofia, pensieroOccidentale) ∧ Orale(filosofia) ∧ ∀p:PraticaDialogica, t:Testo [Trasferisce(filosofia,p,t) → Registra(t,Risultati(p)) ∧ Registra(t,Ricordi(p))]` |
| **F05** · Finis et effectus dialogi | P1 | `Fine(praticaDialogica, Reminiscenza(essere)) ∧ ∀a [Partecipa(a,praticaDialogica) → Effetto(praticaDialogica, ScienzaTrasformazione(Psiche(a)))]` |
| **F06** · Traditio usque ad discrimen | P2 | `Tramanda(tradizioneTestuale,filosofia) ∧ Accresce(tradizioneTestuale,filosofia) ∧ Intervallo(tradizioneTestuale,esordioGreco,svolta1936) ∧ DataNelManifesto(svolta1936,1936,2689_AUC)` |
| **F07** · Machina abstracta, hyperhistoria et sphaera informationis | P2 | `Individua(pubblicazioneMacchina,svolta1936) ∧ Pubblica(pubblicazioneMacchina,macchinaAstratta) ∧ PrimaSecondoIlTesto(macchinaAstratta) ∧ Inaugura(svolta1936,iperstoria) ∧ FaNascere(svolta1936,infosfera)` |
| **F08** · Quantificatio in hypertextu manifesta | P2 | `Avvia(svolta1936,quantificazioneScrittura) ∧ ConLaGenesiDi(web, Ostende(ipertesto,quantificazioneScrittura))` |
| **F09** · Destinatio ad hypertextum post discrimen | P2 | `∀p:ProduzioneFilosofica [Posteriore(p,svolta1936) → DestinataAllaTrasposizione(p,ipertesto)] ∧ IndipendenteDa(destinazioneIpertestuale,consapevolezza)` |
| **F10** · Analogia historiae et hyperhistoriae | P3 | `InizioCon(storia,scrittura) ∧ Corrisponde(Inizio(iperstoria),Comparsa(iperscrittura))` |
| **F11** · Duo gradus hyperscripturae | P3 | `∀p [(IperScrittura(p) → Produce(p,ipertesti)) ∧ (Elem(p) → MetteInFunzione(p,testi,macchineAstratte)) ∧ (Consap(p) → MetteInCircuito(p,contenuti,codici,web))]` |
| **F12** · Directio Retis | P3 | `SviluppoDi(sviluppoWeb,web) ∧ Fine(sviluppoWeb,Accumulare(capitaleSemantico)) ∧ Fine(sviluppoWeb,Distribuire(capitaleSemantico))` |
| **F13** · Quomodo capitale semanticum constituatur | P3 | `Costituisce(organizzazioneSemantica,capitaleSemantico) ∧ Media(ontologiaInformatica,organizzazioneSemantica) ∧ ∀c,m [Organizza(organizzazioneSemantica,c,m) → (AccessibileA(c,esserci) ∧ AccessibileA(m,macchinaConcreta))]` |
| **F14** · Specificatio formalis, explicita et communis | P4 | `OInf(o) ↔ ∃s,c [Specifica(o,s,c) ∧ Formale(s) ∧ Esplicita(s) ∧ Concettualizzazione(c) ∧ Condivisa(c)]` |
| **F15** · Reflexio de facultate tradendi | P4 | `∀p [Riflessiva(p) → (RifletteSu(p,Consapevolezza(p)) ∧ MiraA(p,PossibilitàDiVeicolare) ∧ ¬FinePrimario(p,VeicolareUnContenuto))]` |
| **F16** · Ambitus generalis et determinatus facultatis tradendi | P4 | `Generale(p,D) := ∀c∈D ◇ Veicola(p,c); Determinata(p,c₀) := c₀∈D ∧ ◇ Veicola(p,c₀)` |
| **F17** · Dependentia ontologiae informaticae ab analytica | P5 | `∀o:OInf ∃a:OAn [Presuppone(o,a) ∧ ImplicaNelManifesto(o,a) ∧ Integra(Implementazione(o),a) ∧ (Esplicito(Implementazione(o),a) ∨ Implicito(Implementazione(o),a))]` |
| **F18** · Quid sit, quid et quomodo specificetur | P5 | `∀a:OAn [Individua(a,Entità,Tipi) ∧ Fornisce(a,Contenuto(concettualizzazione)) ∧ Fornisce(a,Modo(specificazione))]` |
| **F19** · Quantificatio ad theoriam relata | P5 | `Q(T,φ,v,d) := EnunciatoDi(φ,T) ∧ Vincolata(v,φ) ∧ d∈D(T) ∧ ∃g [Ammissibile(g,T,φ) ∧ g(v)=d]` |
| **F20** · Duplex postulatio quantificationis | P5 | `∀o:OInf ∃T:Teoria [Richiede(o,ContenutoQuantificato(T)) ∧ ConsisteIn(o,iperscrittura) ∧ Richiede(iperscrittura,QuantificazioneOntologica(scritturaSovrastata))]` |
| **F21** · Dependentia ontologiae analyticae a phaenomenologica | P6 | `∀a:OAn ∃p:OFen [EffettoDi(a,p)]` |
| **F22** · Articulatio formalis et regionalis | P6 | `Articolazione(ontologiaFenomenologica; ontologiaFormale, ontologiaRegionale)` |
| **F23** · Obiectum in genere, structura enuntiativa et iudicium | P6 | `ValidePerOgniOggetto(StruttureFormali) ∧ ∀x [IndividuatoDaAnalitica(x) → Specifica(ontologiaFormale,EssereEntità(x))] ∧ Inquadra(ontologiaFormale,StruttureEnunciative) ∧ Richiede(ontologiaFormale,NozioneGiudizio)` |
| **F24** · Essentiae et possibilitates regionales | P6 | `∀r:Regione [Fissa(Usiologia(r),EssenzeSpecifiche(r)) ∧ ∀x∈D(r) [IndividuatoDaAnalitica(x) → Specifica(ontologiaRegionale(r),ComePossibile(x,r))]]` |
| **F25** · Quantificatio per ambitum regionaliter apertum | P6 | `Apre(aperturaFenomenologica,Dᵣ;usiologia(r)) ∧ Quantifica(T,Dᵣ) ∧ PerOgniOggetto_Dᵣ(φ) := ∀x∈Dᵣ φ(x)` |
| **F26** · Metaphysica ens ontologice tractat | P7 | `∀o [(OFen(o) ∨ OAn(o) ∨ OInf(o)) → (Segue(o,metafisicaOccidentale) ∧ Tema(o,ente,OntologicoComeCosa))]` |
| **F27** · Metaphysica esse ontice tractat | P7 | `∀o:OntologiaDellEnte ∀b [TematizzaEssere(o,b) → ∃x∈D(o) [b=EssereDi(x) ∧ Tratta(o,b,OnticoRelativo)]]` |
| **F28** · Esse sine re praeelecta tractandum | P7 | `Oₘ [Tratta(oFond,essereInQuantoTale,OntologicoTematico) ∧ ¬∃x [Cosa(x) ∧ OggettoPrescelto(oFond,x)]]` |
| **F29** · Quattuor munera inquisitionis de esse | P7 | `Oₘ [SpecificaFormalmente(concettualizzazioneEssere) ∧ Indica(esserciDellEssere) ∧ Esprime(essenzaEssere) ∧ Esplicita(ModoPossibilità(essereInQuantoTale))]` |
| **F30** · Ens ontice intellectum et nihil ut relatio ad limen | P7 | `RiferimentoNelPasso(⟦essere in quanto tale⟧,⟦ente onticamente inteso⟧) ∧ FiguraLimite(⟦ente onticamente inteso⟧,⟦nulla⟧) ∧ ¬Presupposto(∃x [Cosa(x) ∧ ReferentePrescelto(x)])` |
| **F31** · Fundatio sensus ontologiarum entium | P8 | `∀o:OntologiaDellEnte [RiceveSensoDa(o,ontologiaFondamentale)]` |
| **F32** · Totalitas non expressa | P8 | `Problematico(essereInQuantoTale) ∧ A_CausaDi(¬EspressaNellaSuaTotalità(ontologiaFondamentale), Problematico(essereInQuantoTale))` |
| **F33** · Inquisitio qua quaestio essentiae ponitur | P8 | `Sviluppa(ricercaFondamentale,ontologiaFondamentale) ∧ RicercaPosizionale(ricercaFondamentale,problemaEssenzaEssere)` |
| **F34** · Hyperscriptura et filum dux | P8 | `Oₘ Porre(problemaSensoEssere) ∧ Realizza(iperscritturaFondamentale,Porre(problemaSensoEssere)) ∧ ∀l,p [Pertinenti(l,p,ricercaOntologica) → PuòRaccordare(iperscritturaFondamentale,l,p;problemaSensoEssere)]` |
| **F35** · Crypta ut hypertextus productus | P8 | `Ipertesto(criptaIpertesto) ∧ Produce(iperscritturaFondamentale,criptaIpertesto)` |
| **X01** · Propositum fundamenti proiciendi investigandi | XProgetto | `Realizza(criptaIpertesto,progettoCripta) ∧ Tematizza(progettoCripta,progettualita) ∧ Interroga(progettoCripta,FondamentoDelProgettare(progettoCripta))` |
| **X02** · Iectitas determinabilis | XProgetto | `DeterminabileCome(gettatezza; oggetto, soggetto, progetto, rigetto) ∧ Riguarda(gettatezza,progettualita)` |
| **X03** · Directiones fundationis | XProgetto | `SostegnoOntico(ontologiaInformatica,ricercaFondamentale) ∧ Obiettivo(progettoCripta,mappaEnte) ∧ FondazioneDiSenso(ontologiaFondamentale,ontologiaEnte)` |
| **X04** · Crypta ut situs, hypertextus et notae | XChiSiamo | `Raccoglie(criptaSito,note) ∧ RicorreIn(criptaIpertesto,note) ∧ PuòComunicare(notaIpertestuale,notaIpertestuale′)` |
| **X05** · Articulus ut articulatio aperturae | XArticoli | `Artefatto(articolo) ∧ Articola(articolo,senso) ∧ Raccordabile(articolo,ricercaOntologica)` |

## Consensiones versionis 0.2.0

Consensiones axiomata subclassium et subproprietatum sunt: nullam aequivalentiam asserunt neque sensum schedularum mutant. `dub:Concept ⊑ skos:Concept` sinit relationes ad notiones ut notiones schematis (`dub:concetti`) tractari, `skos:prefLabel` `rdfs:label` repetente. `dub:Source ⊑ prov:Entity, schema:CreativeWork`; `dub:Passage`, `dub:ResearchItem` et `dub:RelationAssertion ⊑ prov:Entity`; `dub:derivedFrom ⊑ prov:wasDerivedFrom`; `dub:partOfSource ⊑ dcterms:isPartOf`. Sub OWL RL sententia genus `prov:Entity` heredat et catena sententia → locus → fons ut derivatio PROV legitur. Classes Dubii inter se disiunctae manent: superclassis externa communis eas non confundit. Regulae SHACL et probatio partis immutatae manent et adhuc transeunt; probatio retis praeterea consensionem inferri et nullam classem disiunctam individua communia accipere probat.
