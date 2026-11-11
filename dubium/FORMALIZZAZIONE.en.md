# Formalisation of the manifesto

The [manifesto](https://criptasemantica.it/) begins with perplexity about the word “being”. It connects the question of the sense of being to a history of philosophy, to hyperwriting and to the dependence of different modes of inquiry. The [beginner's guide](README.en.md) introduces the project through an example.

## How to read the formalisation

The OWL schema describes the structure of records. A question and a position are disjoint types of research entry. A position's inverse link to its assertions allows navigation in either direction under OWL entailment. [OWL 2](https://www.w3.org/TR/owl2-syntax/)

The discourse graph represents a relation as an assertion within a position. The notation `Arc(r,p,s,k,o)` says that arc `r` in position `p` connects source concept `s` to target concept `o` using relation kind `k`. Each position has a source passage, a reading mode, a status and a formula. “Paraphrase” attributes a restatement to the text, “interpretive choice” marks a decision in the model, and “contextual extension” points to another public page. An arc is an aid to retrieval. Its parent formula retains the scope and logical structure.

In the formulas, `∀x:D` and `∃x:D` restrict a variable to a domain. `¬`, `∧`, `∨`, `→` and `↔` mean negation, conjunction, disjunction, implication and equivalence. `:=` defines an abbreviation. `◇` marks possibility, `Oₘ` a task prescribed by the manifesto, and `⟦…⟧` a mention in the discourse. `OInf`, `OAn` and `OFen` abbreviate computational, analytic and phenomenological ontology. `D(T)` is a theory's domain and `Dᵣ` a domain opened with respect to a region. The Italian names in formulas identify the same concepts across all editions. These formulas are textual descriptions and do not specify a possible-world semantics.

## Passage map

| Passage | Content | Entries |
| --- | --- | --- |
| P0 | Title, epigraph, the word “being”, presumed understanding and perplexity. | F01, Q01 |
| P1 | The task of posing the question of being, the Greek beginnings, oral practice, dialogue, recollection and transformation of the psyche. | F02–F05, Q02 |
| P2 | Textual tradition, the turning point of 1936, abstract machines, hyperhistory, the infosphere and the turn towards hypertext. | F06–F09 |
| P3 | Writing and hyperwriting, elementary and conscious levels, content, computable meaning and semantic capital. | F10–F13 |
| P4 | Ontology as specification, shared conceptualisation, reflexivity and two scopes of conveyability. | F14–F16 |
| P5 | Analytic commitment, what is specified and how, statements, bound variables, values and two requirements for quantification. | F17–F20 |
| P6 | Phenomenological dependence, formal and regional inquiry, judgement, regional essences and the opening of a domain. | F21–F25, Q03 |
| P7 | Entity as thing, being of an entity, being as such, four tasks of inquiry, the limiting reference and nothing. | F26–F30, Q04 |
| P8 | The sense of ontologies of entities, unexpressed totality, inquiry into essence and sense, and production of the hypertext. | F31–F35, Q05–Q06 |

## Interpretive choices

**Genealogy as attributed discourse.** F01 distinguishes the addressees' familiar use from the speakers' former confidence. F03 and F07 attribute the chronology and the priority claim about an abstract machine to the manifesto. Turing's paper records receipt and presentation in 1936 and appears in volume 42 of the *Proceedings* (1936–37). The manifesto leaves his name implicit. [Turing's paper](https://fab.cba.mit.edu/classes/862.22/notes/computation/Turing-1936.pdf)

**Writing, conveyability and quantification.** F08 describes the quantification of writing as a historical and technical process. F19 relates theory, statement, bound variable and admissible value. In F16, `∀c∈D ◇Veicola(p,c)` gives the capacity for each content item, while `◇Veicola(p,c₀)` concerns one specified item. The first formula leaves simultaneous conveyability open. F21 ranges over analytic ontologies, including object-oriented and hyperobject-oriented variants, regardless of awareness. F25 makes the dependence of the quantification domain on the inquiry explicit.

**Two ontological treatments.** F26 records the ontological treatment of an entity as a thing. F27 records the ontic treatment of being in relation to an entity whenever being is thematised in an ontology of entities. F28 places inquiry into being as such and the absence of a selected thing within the scope of the manifesto's prescription. F29 treats the being-there of being as a dimension to indicate. F13 uses Dasein for the human pole of access to content.

**Nothing and grounding.** F30 uses mention brackets for the limiting reference in the passage. `dub:nulla` identifies that sense. In OWL, `owl:Nothing` denotes the empty class. F31 expresses the grounding of sense in one direction. X03 gives the ontic support of inquiry in the other direction. The two relations have separate names and carry no transitivity axiom. F32 leaves the inquiry's totality open. [Project](https://criptasemantica.it/progetto/)

The contextual entries X01–X03 concern projection, the four determinations of thrownness and the map of entities. X04 distinguishes the site, the notes and the recurring hypertext. X05 connects the article to the articulation of an opening. The entries remain separately attributable. [Project](https://criptasemantica.it/progetto/), [About](https://criptasemantica.it/chi-siamo/), [Articles](https://criptasemantica.it/articoli/)

## Example query

This query retrieves who receives sense from fundamental ontology according to the manifesto, along with the reading and source.

```sparql
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>

SELECT ?concept ?position ?reading ?passage ?source WHERE {
  ?arc a dub:RelationAssertion ;
    dub:subjectConcept ?concept ;
    dub:relationKind dub:rel-riceveSensoDa ;
    dub:objectConcept dub:ontologiaFondamentale ;
    dub:belongsTo ?position .
  ?position dub:derivedFrom ?passage ; dub:readingMode ?reading .
  ?passage dub:partOfSource ?source .
}
```

The expected row is `dub:ontologiaEnte`, `dub:F31`, `dub:Fondamentale`, `dub:P8` and the manifesto's URL. The [catalogue](en/index.html#F31) presents the same route for a reader.

## Extend and check the graph

Give a new passage a reproducible locator and a new position an identifier, a source, a status and a force. A competing interpretation gets a separate position. SHACL checks whether the records contain the required data. OWL entailment provides structural links. The validity of an interpretation and the historical claims require reading the sources. [OWL 2](https://www.w3.org/TR/owl2-syntax/), [SHACL](https://www.w3.org/TR/shacl/)

## Formula catalogue

| Entry | Passage | Formula |
| --- | --- | --- |
| **F01** · From familiarity to perplexity | P0 | `Cita(epigrafe,sofista244a) ∧ AutoreAttribuito(sofista244a,platone) ∧ TraduzioneAttribuita(epigrafe,pietroChiodi) ∧ Familiarità(voi, «essente», t₀) ∧ Crede(noi, Comprende(noi, «essente»), t₁) ∧ Perplessi(noi, «essente», t₂) ∧ t₁ < t₂` |
| **F02** · The need to pose the question | P1 | `Oₘ Porre(problemaEssere) ∧ Innesca(Oₘ Porre(problemaEssere), pensieroOccidentale)` |
| **F03** · Locating the beginning | P1 | `EsordioDi(esordioGreco, pensieroOccidentale) ∧ Luogo(esordioGreco, grecia) ∧ Collocato(esordioGreco, «VII sec. a.C.; I–II sec. AUC»)` |
| **F04** · Oral philosophy and written transmission | P1 | `CorpoTradizionale(filosofia, pensieroOccidentale) ∧ Orale(filosofia) ∧ ∀p:PraticaDialogica, t:Testo [Trasferisce(filosofia,p,t) → Registra(t,Risultati(p)) ∧ Registra(t,Ricordi(p))]` |
| **F05** · Aim and effect of dialogue | P1 | `Fine(praticaDialogica, Reminiscenza(essere)) ∧ ∀a [Partecipa(a,praticaDialogica) → Effetto(praticaDialogica, ScienzaTrasformazione(Psiche(a)))]` |
| **F06** · Tradition up to the turning point | P2 | `Tramanda(tradizioneTestuale,filosofia) ∧ Accresce(tradizioneTestuale,filosofia) ∧ Intervallo(tradizioneTestuale,esordioGreco,svolta1936) ∧ DataNelManifesto(svolta1936,1936,2689_AUC)` |
| **F07** · Abstract machine, hyperhistory and infosphere | P2 | `Individua(pubblicazioneMacchina,svolta1936) ∧ Pubblica(pubblicazioneMacchina,macchinaAstratta) ∧ PrimaSecondoIlTesto(macchinaAstratta) ∧ Inaugura(svolta1936,iperstoria) ∧ FaNascere(svolta1936,infosfera)` |
| **F08** · Quantification made manifest in hypertext | P2 | `Avvia(svolta1936,quantificazioneScrittura) ∧ ConLaGenesiDi(web, Ostende(ipertesto,quantificazioneScrittura))` |
| **F09** · The turn towards hypertext after the threshold | P2 | `∀p:ProduzioneFilosofica [Posteriore(p,svolta1936) → DestinataAllaTrasposizione(p,ipertesto)] ∧ IndipendenteDa(destinazioneIpertestuale,consapevolezza)` |
| **F10** · The analogy between history and hyperhistory | P3 | `InizioCon(storia,scrittura) ∧ Corrisponde(Inizio(iperstoria),Comparsa(iperscrittura))` |
| **F11** · Two levels of hyperwriting | P3 | `∀p [(IperScrittura(p) → Produce(p,ipertesti)) ∧ (Elem(p) → MetteInFunzione(p,testi,macchineAstratte)) ∧ (Consap(p) → MetteInCircuito(p,contenuti,codici,web))]` |
| **F12** · The orientation of the Web | P3 | `SviluppoDi(sviluppoWeb,web) ∧ Fine(sviluppoWeb,Accumulare(capitaleSemantico)) ∧ Fine(sviluppoWeb,Distribuire(capitaleSemantico))` |
| **F13** · How semantic capital is formed | P3 | `Costituisce(organizzazioneSemantica,capitaleSemantico) ∧ Media(ontologiaInformatica,organizzazioneSemantica) ∧ ∀c,m [Organizza(organizzazioneSemantica,c,m) → (AccessibileA(c,esserci) ∧ AccessibileA(m,macchinaConcreta))]` |
| **F14** · Formal, explicit and shared specification | P4 | `OInf(o) ↔ ∃s,c [Specifica(o,s,c) ∧ Formale(s) ∧ Esplicita(s) ∧ Concettualizzazione(c) ∧ Condivisa(c)]` |
| **F15** · Reflexivity about the capacity to convey | P4 | `∀p [Riflessiva(p) → (RifletteSu(p,Consapevolezza(p)) ∧ MiraA(p,PossibilitàDiVeicolare) ∧ ¬FinePrimario(p,VeicolareUnContenuto))]` |
| **F16** · General and determinate scope of conveyability | P4 | `Generale(p,D) := ∀c∈D ◇ Veicola(p,c); Determinata(p,c₀) := c₀∈D ∧ ◇ Veicola(p,c₀)` |
| **F17** · The dependence of computational ontology on analytic ontology | P5 | `∀o:OInf ∃a:OAn [Presuppone(o,a) ∧ ImplicaNelManifesto(o,a) ∧ Integra(Implementazione(o),a) ∧ (Esplicito(Implementazione(o),a) ∨ Implicito(Implementazione(o),a))]` |
| **F18** · What exists, what is specified and how | P5 | `∀a:OAn [Individua(a,Entità,Tipi) ∧ Fornisce(a,Contenuto(concettualizzazione)) ∧ Fornisce(a,Modo(specificazione))]` |
| **F19** · Quantification relative to a theory | P5 | `Q(T,φ,v,d) := EnunciatoDi(φ,T) ∧ Vincolata(v,φ) ∧ d∈D(T) ∧ ∃g [Ammissibile(g,T,φ) ∧ g(v)=d]` |
| **F20** · Two requirements for quantification | P5 | `∀o:OInf ∃T:Teoria [Richiede(o,ContenutoQuantificato(T)) ∧ ConsisteIn(o,iperscrittura) ∧ Richiede(iperscrittura,QuantificazioneOntologica(scritturaSovrastata))]` |
| **F21** · The phenomenological dependence of analytic ontology | P6 | `∀a:OAn ∃p:OFen [EffettoDi(a,p)]` |
| **F22** · Formal and regional articulation | P6 | `Articolazione(ontologiaFenomenologica; ontologiaFormale, ontologiaRegionale)` |
| **F23** · Object in general, statement structure and judgement | P6 | `ValidePerOgniOggetto(StruttureFormali) ∧ ∀x [IndividuatoDaAnalitica(x) → Specifica(ontologiaFormale,EssereEntità(x))] ∧ Inquadra(ontologiaFormale,StruttureEnunciative) ∧ Richiede(ontologiaFormale,NozioneGiudizio)` |
| **F24** · Regional essences and possibilities | P6 | `∀r:Regione [Fissa(Usiologia(r),EssenzeSpecifiche(r)) ∧ ∀x∈D(r) [IndividuatoDaAnalitica(x) → Specifica(ontologiaRegionale(r),ComePossibile(x,r))]]` |
| **F25** · Quantification ranges over a regionally opened domain | P6 | `Apre(aperturaFenomenologica,Dᵣ;usiologia(r)) ∧ Quantifica(T,Dᵣ) ∧ PerOgniOggetto_Dᵣ(φ) := ∀x∈Dᵣ φ(x)` |
| **F26** · Metaphysics treats the entity ontologically | P7 | `∀o [(OFen(o) ∨ OAn(o) ∨ OInf(o)) → (Segue(o,metafisicaOccidentale) ∧ Tema(o,ente,OntologicoComeCosa))]` |
| **F27** · Metaphysics treats being ontically | P7 | `∀o:OntologiaDellEnte ∀b [TematizzaEssere(o,b) → ∃x∈D(o) [b=EssereDi(x) ∧ Tratta(o,b,OnticoRelativo)]]` |
| **F28** · Taking up being independently of a thing | P7 | `Oₘ [Tratta(oFond,essereInQuantoTale,OntologicoTematico) ∧ ¬∃x [Cosa(x) ∧ OggettoPrescelto(oFond,x)]]` |
| **F29** · Four tasks for the inquiry into being | P7 | `Oₘ [SpecificaFormalmente(concettualizzazioneEssere) ∧ Indica(esserciDellEssere) ∧ Esprime(essenzaEssere) ∧ Esplicita(ModoPossibilità(essereInQuantoTale))]` |
| **F30** · Ontically understood entity and nothing as a limiting reference | P7 | `RiferimentoNelPasso(⟦essere in quanto tale⟧,⟦ente onticamente inteso⟧) ∧ FiguraLimite(⟦ente onticamente inteso⟧,⟦nulla⟧) ∧ ¬Presupposto(∃x [Cosa(x) ∧ ReferentePrescelto(x)])` |
| **F31** · Grounding the sense of ontologies of entities | P8 | `∀o:OntologiaDellEnte [RiceveSensoDa(o,ontologiaFondamentale)]` |
| **F32** · The totality left unexpressed | P8 | `Problematico(essereInQuantoTale) ∧ A_CausaDi(¬EspressaNellaSuaTotalità(ontologiaFondamentale), Problematico(essereInQuantoTale))` |
| **F33** · Inquiry that poses the question of essence | P8 | `Sviluppa(ricercaFondamentale,ontologiaFondamentale) ∧ RicercaPosizionale(ricercaFondamentale,problemaEssenzaEssere)` |
| **F34** · Hyperwriting and its guiding thread | P8 | `Oₘ Porre(problemaSensoEssere) ∧ Realizza(iperscritturaFondamentale,Porre(problemaSensoEssere)) ∧ ∀l,p [Pertinenti(l,p,ricercaOntologica) → PuòRaccordare(iperscritturaFondamentale,l,p;problemaSensoEssere)]` |
| **F35** · Cripta as the resulting hypertext | P8 | `Ipertesto(criptaIpertesto) ∧ Produce(iperscritturaFondamentale,criptaIpertesto)` |
| **X01** · Planning to investigate the ground of planning | XProgetto | `Realizza(criptaIpertesto,progettoCripta) ∧ Tematizza(progettoCripta,progettualita) ∧ Interroga(progettoCripta,FondamentoDelProgettare(progettoCripta))` |
| **X02** · The determinability of thrownness | XProgetto | `DeterminabileCome(gettatezza; oggetto, soggetto, progetto, rigetto) ∧ Riguarda(gettatezza,progettualita)` |
| **X03** · Directions of grounding | XProgetto | `SostegnoOntico(ontologiaInformatica,ricercaFondamentale) ∧ Obiettivo(progettoCripta,mappaEnte) ∧ FondazioneDiSenso(ontologiaFondamentale,ontologiaEnte)` |
| **X04** · Cripta as website, hypertext and notes | XChiSiamo | `Raccoglie(criptaSito,note) ∧ RicorreIn(criptaIpertesto,note) ∧ PuòComunicare(notaIpertestuale,notaIpertestuale′)` |
| **X05** · The article as an articulation of an opening | XArticoli | `Artefatto(articolo) ∧ Articola(articolo,senso) ∧ Raccordabile(articolo,ricercaOntologica)` |

## Alignments of version 0.2.0

The alignments are subclass and subproperty axioms: they assert no equivalence and do not change the meaning of the entries. `dub:Concept ⊑ skos:Concept` allows the conceptual references to be treated as concepts of a scheme (`dub:concetti`), with `skos:prefLabel` repeating `rdfs:label`. `dub:Source ⊑ prov:Entity, schema:CreativeWork`; `dub:Passage`, `dub:ResearchItem` and `dub:RelationAssertion ⊑ prov:Entity`; `dub:derivedFrom ⊑ prov:wasDerivedFrom`; `dub:partOfSource ⊑ dcterms:isPartOf`. Under OWL RL a position inherits the type `prov:Entity` and the chain position → passage → source reads as PROV derivation. The Dubium classes remain mutually disjoint: sharing an external superclass does not merge them. The SHACL constraints and the module test are unchanged and still pass; the network test additionally checks that the alignment is inferred and that no disjoint classes receive common individuals.
