# Metrum. Formalizzazione

[Guida per iniziare](README.md) · [English](FORMALIZZAZIONE.en.md) · [Latine](FORMALIZZAZIONE.la.md)

Metrum formalizza la misura della ricerca come un ente del grafo dotato di provenienza. Il punto di partenza è una tesi della pagina «Chi siamo» della Cripta Semantica: non esistono misure neutrali della qualità della scienza, ma sistemi tecnici di misurazione che la alterano. Se è così, una misura non può entrare in un'ontologia come un numero: deve entrarvi come un'osservazione, con il protocollo che l'ha prodotta, il corpus su cui è stata presa, il periodo, la copertura, lo stato del risultato e la fonte. Questo documento descrive il modello, le tre regole che lo governano, i vincoli che le fanno rispettare e il raccordo con gli altri moduli.

## Il modello

| Classe | Allineamenti | Che cosa rappresenta |
| --- | --- | --- |
| `mtr:Observation` | `prov:Entity`, `schema:Observation` | Una sola applicazione di un protocollo a un soggetto. |
| `mtr:Protocol` | `skos:Concept`, `prov:Plan` | Il contratto di misura: che cosa si conta o si descrive, con quale unità, su quali soggetti, con quale metodo e fonte. |
| `mtr:Family` | `skos:Concept` | Il gruppo del protocollo: quattordici famiglie. |
| `mtr:Scope` | `skos:Concept` | Il tipo di soggetto ammesso: nove ambiti. |
| `mtr:ValueType` | `skos:Concept` | Il tipo del valore, con il tipo di dato XML Schema corrispondente. |
| `mtr:Coverage` | `skos:Concept` | Copertura completa, parziale o ignota del corpus. |
| `mtr:ResultState` | `skos:Concept` | Osservato, assente, soppresso, non applicabile. |
| `mtr:Discipline` | `skos:Concept` | Un campo FORD del Manuale di Frascati 2015: sei campi e quarantadue sottocampi. |
| `mtr:Principle` | `prov:Entity` | Un enunciato citabile di una dichiarazione pubblica sulla valutazione responsabile. |
| `mtr:Corpus` | `prov:Entity` | Un corpus dichiarato, quando ha un IRI proprio. |
| `mtr:Comparison` | `prov:Entity` | Un confronto dichiarato fra due osservazioni. |

Le undici classi sono fra loro disgiunte. Le proprietà di un'osservazione sono `protocol`, `about` (sottoproprietà di `schema:observationAbout`), `corpus` e `corpusLabel`, `periodStart`, `periodEnd`, `acquiredOn`, `coverage`, `state`, `discipline`, `source` ed `evidence` (entrambe sottoproprietà di `prov:wasDerivedFrom`), `value`, `numerator`, `denominator`, `appliedMethod`, `editorialReading`. Le proprietà di un protocollo sono `family`, `scope`, `valueType`, `unit`, `method`, `requiresReferenceSet`, `guidedBy`; un principio ha `cautions`. La [gerarchia](schema.html) le elenca con dominio e codominio.

## Tre regole

**Un dato assente non vale zero.** Lo stato del risultato è obbligatorio e distinto dal valore. Un risultato osservato deve avere un valore; un risultato assente, soppresso o non applicabile non può averne. Chi aggrega osservazioni non può trasformare un'assenza in uno zero senza violare le forme.

**Due misure si confrontano solo con lo stesso contratto.** Un `mtr:Comparison` è ammesso solo se le due osservazioni condividono soggetto, protocollo, corpus, periodo e discipline e se nessuna delle due ha copertura ignota. La data di acquisizione può cambiare: è proprio ciò che il confronto descrive. La variazione resta descrittiva; non è un giudizio.

**Un principio limita, non vieta.** `mtr:cautions` collega un principio ai protocolli di cui mette in guardia l'uso improprio: DORA ai sette indicatori di rivista, l'impegno 3 di CoARA al fattore d'impatto e agli indici h, g, i10 e m, il principio 8 di Leiden ai percentili e ai punteggi di attenzione. I protocolli restano nel catalogo, perché esistono e vengono usati; il grafo rende visibile il limite.

## Vincoli SHACL

Le [forme](shapes.ttl) hanno quattro bersagli. `ObservationShape` richiede un protocollo, un soggetto, uno stato, una copertura, un periodo di date, una data di acquisizione, un'etichetta del corpus, una fonte e una prova in HTTPS, almeno una disciplina; tre vincoli SPARQL impongono la coerenza fra stato e valore, l'ordine del periodo e la lettura redazionale per le coperture non complete. `ProtocolShape` richiede tre etichette, notazione, famiglia, ambiti, tipo di valore, unità e metodo in tre lingue, la dichiarazione sull'insieme di riferimento e una fonte. `PrincipleShape` e `DisciplineShape` controllano fonti, etichette e notazioni FORD. `ComparisonShape` applica la regola del confronto con un vincolo SPARQL. Il programma di verifica prova sei alterazioni (osservazione senza protocollo, valore su un dato assente, copertura parziale senza lettura, periodo rovesciato, confronto fra protocolli diversi, protocollo senza fonte), tutte respinte.

## Famiglie

<!-- table:families -->
| Chiave | Famiglia | Protocolli |  |
| --- | --- | --- | --- |
| `agraria` | Agraria | 3 | Validazioni in campo e trasferimenti veterinari. |
| `apertura` | Apertura e accesso | 5 | Quote e controlli su accesso aperto, metadati, identificatori e materiali. |
| `arti` | Arti | 3 | Esposizioni, esecuzioni e valutazioni curatoriali documentate. |
| `clinica` | Ricerca clinica | 2 | Recepimento in linee guida e trasferimento clinico. |
| `dati` | Dati | 3 | Citazioni, riusi e contesto dei dati di ricerca. |
| `intervento` | Interventi | 2 | Esiti documentati di un intervento editoriale o bibliografico. |
| `metodo` | Metodo | 4 | Repliche, preregistrazioni e descrizione dei contributi. |
| `ricezione` | Ricezione | 13 | Citazioni e riusi che una fonte attribuisce a un'opera o a un soggetto. |
| `sedi` | Sedi di pubblicazione | 8 | Indicatori calcolati sulle riviste e sulle collane, non sui singoli lavori. |
| `sociale` | Ricerca sociale | 2 | Adozioni didattiche e riscontri territoriali. |
| `software` | Software | 3 | Citazioni, riusi e riproducibilità del software di ricerca. |
| `tecnica` | Tecnica | 2 | Verifiche in ambiente operativo e licenze d'uso. |
| `trasferimento` | Trasferimento | 4 | Riscontri dell'uso della ricerca fuori dall'accademia: policy, brevetti, adozioni. |
| `umanistica` | Saperi umanistici | 4 | Monografie, edizioni critiche, traduzioni e ricezione argomentativa. |
<!-- /table -->

## Protocolli

I protocolli hanno la stessa chiave usata dal servizio semantico della Cripta. La versione (`@1.0.0`) appartiene al servizio: l'IRI di Metrum identifica il contratto. Un protocollo locale aggiunto nel servizio non ha un IRI in Metrum finché non viene pubblicato qui.

<!-- table:protocols -->
| Chiave | Concetto | Famiglia | Ambito | Unità |
| --- | --- | --- | --- | --- |
| `accessibilita-editoriale` | Controlli editoriali di accessibilità superati | Apertura e accesso | Prodotto della ricerca | percento |
| `adozioni-cliniche` | Recepimenti in linee guida | Ricerca clinica | Prodotto della ricerca | documenti |
| `adozioni-documentate` | Adozioni indipendenti verificate | Trasferimento | Prodotto della ricerca | adozioni |
| `altmetric` | Punteggio di attenzione Altmetric | Ricezione | Opera o edizione | punteggio |
| `article-influence` | Article Influence Score | Sedi di pubblicazione | Sede di pubblicazione | indice |
| `citazioni` | Citazioni ricevute | Ricezione | Opera o edizione | citazioni |
| `citazioni-brevetti` | Citazioni in brevetti | Trasferimento | Opera o edizione | documenti |
| `citazioni-dati` | Citazioni di dati | Dati | Dati di ricerca | citazioni |
| `citazioni-politiche` | Citazioni in documenti di policy | Trasferimento | Opera o edizione | documenti |
| `citazioni-senza-auto` | Citazioni esclusa l’autocitazione | Ricezione | Opera o edizione | citazioni |
| `citazioni-software` | Citazioni del software | Software | Software di ricerca | citazioni |
| `citescore` | CiteScore | Sedi di pubblicazione | Sede di pubblicazione | rapporto |
| `completezza-metadati` | Completezza dei metadati | Apertura e accesso | Prodotto della ricerca | percento |
| `contributi-credit` | Contributi descritti con CRediT | Metodo | Prodotto della ricerca | testo |
| `copertura-identificatori` | Copertura degli identificatori persistenti | Apertura e accesso | Persona o organizzazione | percento |
| `correzioni-metadati` | Schede corrette con verifica | Interventi | Intervento documentabile | schede |
| `diffusione-didattica` | Adozioni didattiche documentate | Ricerca sociale | Prodotto della ricerca | adozioni |
| `edizioni-critiche` | Contributo dell’edizione critica | Saperi umanistici | Opera o edizione | testo |
| `eigenfactor` | Eigenfactor Score | Sedi di pubblicazione | Sede di pubblicazione | indice |
| `emivita-citazioni` | Emivita delle citazioni ricevute | Sedi di pubblicazione | Sede di pubblicazione | anni |
| `esito-intervento` | Esito documentato di un intervento | Interventi | Intervento documentabile | testo |
| `esito-replica` | Esito argomentato di replica | Metodo | Prodotto della ricerca | testo |
| `esposizioni-curate` | Esposizioni curate documentate | Arti | Artefatto o esecuzione | eventi |
| `fwci` | Impatto citazionale normalizzato per campo | Ricezione | Opera o edizione | rapporto |
| `g-index` | Indice g | Ricezione | Persona o organizzazione | indice |
| `h-index` | Indice h | Ricezione | Persona o organizzazione | indice |
| `i10-index` | Indice i10 | Ricezione | Persona o organizzazione | opere |
| `impatto-territoriale` | Riscontro di impatto territoriale | Ricerca sociale | Prodotto della ricerca | testo |
| `jci` | Journal Citation Indicator | Sedi di pubblicazione | Sede di pubblicazione | indice |
| `jif` | Journal Impact Factor | Sedi di pubblicazione | Sede di pubblicazione | rapporto |
| `licenze-applicate` | Licenze d’uso documentate | Tecnica | Prodotto della ricerca | licenze |
| `m-index` | Indice m | Ricezione | Ricercatrice o ricercatore | rapporto |
| `materiali-disponibili` | Disponibilità di materiali di ricerca | Apertura e accesso | Prodotto della ricerca | percento |
| `monografie-recepite` | Riscontri su monografie | Saperi umanistici | Opera o edizione | riscontri |
| `opere-citanti` | Opere citanti distinte | Ricezione | Opera o edizione | opere |
| `opere-indicizzate` | Opere indicizzate | Ricezione | Persona o organizzazione | opere |
| `percentile` | Percentile citazionale | Ricezione | Opera o edizione | percentile |
| `performance-documentate` | Esecuzioni pubbliche documentate | Arti | Artefatto o esecuzione | eventi |
| `protocolli-preregistrati` | Preregistrazioni documentate | Metodo | Prodotto della ricerca | protocolli |
| `qualita-dati` | Contesto e limiti dei dati | Dati | Dati di ricerca | testo |
| `quota-accesso-aperto` | Quota di opere ad accesso aperto | Apertura e accesso | Persona o organizzazione | percento |
| `rcr` | Relative Citation Ratio | Ricezione | Opera o edizione | rapporto |
| `recepimento-policy` | Recepimento in atti o pratiche pubbliche | Trasferimento | Prodotto della ricerca | testo |
| `repliche-indipendenti` | Repliche indipendenti documentate | Metodo | Prodotto della ricerca | repliche |
| `ricezione-argomentativa` | Ricezione argomentativa | Saperi umanistici | Prodotto della ricerca | testo |
| `riferimenti-bibliografici` | Riferimenti in uscita | Ricezione | Opera o edizione | riferimenti |
| `riproducibilita-software` | Riscontro di riproducibilità software | Software | Software di ricerca | testo |
| `riusi-dati` | Riusi verificati di dati | Dati | Dati di ricerca | riusi |
| `riusi-software` | Riusi documentati del software | Software | Software di ricerca | riusi |
| `siti-agrari-indipendenti` | Siti indipendenti di validazione agraria | Agraria | Prodotto della ricerca | siti |
| `sjr` | SJR | Sedi di pubblicazione | Sede di pubblicazione | indice |
| `snip` | SNIP | Sedi di pubblicazione | Sede di pubblicazione | indice |
| `traduzioni-verificate` | Traduzioni verificabili | Saperi umanistici | Opera o edizione | traduzioni |
| `trasferimento-clinico` | Riscontro di trasferimento clinico | Ricerca clinica | Prodotto della ricerca | testo |
| `trasferimento-ingegneristico` | Verifica in ambiente operativo | Tecnica | Prodotto della ricerca | testo |
| `trasferimento-veterinario` | Riscontro di trasferimento veterinario | Agraria | Prodotto della ricerca | testo |
| `validazione-agronomica` | Validazione in campo | Agraria | Prodotto della ricerca | testo |
| `valutazione-artistica` | Valutazione curatoriale o artistica | Arti | Artefatto o esecuzione | testo |
<!-- /table -->

## Principi

I principi sono parafrasi; la fonte conserva il testo autorevole. Le dichiarazioni citate sono la Dichiarazione di San Francisco sulla valutazione della ricerca (DORA), il Manifesto di Leiden (dieci principi), l'Accordo per la riforma della valutazione della ricerca (CoARA, quattro impegni fondamentali), i principi FAIR, la Dichiarazione congiunta sui principi di citazione dei dati (FORCE11, otto principi), i principi di citazione del software (sei), la tassonomia CRediT e la preregistrazione.

<!-- table:principles -->
| Chiave | Principio | Fonte | Mette in guardia su |
| --- | --- | --- | --- |
| CRediT | Descrivere i contributi con quattordici ruoli, distinti dall'ordine degli autori | [Fonte](https://credit.niso.org/) | — |
| Citazione del software 1 | Importanza: il software è un prodotto di ricerca citabile | [Fonte](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 2 | Credito e attribuzione a chi lo ha sviluppato | [Fonte](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 3 | Identificazione univoca e leggibile dalle macchine | [Fonte](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 4 | Persistenza di identificatori e metadati | [Fonte](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 5 | Accessibilità del software e dei metadati | [Fonte](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 6 | Specificità della versione citata | [Fonte](https://doi.org/10.7717/peerj-cs.86) | — |
| CoARA, impegno 1 | Riconoscere la diversità dei contributi e delle carriere nella ricerca | [Fonte](https://coara.eu/agreement/the-agreement-full-text/) | — |
| CoARA, impegno 2 | Fondare la valutazione sul giudizio qualitativo e sulla revisione fra pari, con indicatori usati responsabilmente | [Fonte](https://coara.eu/agreement/the-agreement-full-text/) | — |
| CoARA, impegno 3 | Abbandonare gli usi impropri delle metriche di rivista e di pubblicazione, come fattore d'impatto e indice h | [Fonte](https://coara.eu/agreement/the-agreement-full-text/) | `g-index`, `h-index`, `i10-index`, `jif`, `m-index` |
| CoARA, impegno 4 | Evitare l'uso delle classifiche delle organizzazioni di ricerca nella valutazione | [Fonte](https://coara.eu/agreement/the-agreement-full-text/) | — |
| DORA | Non usare metriche di rivista per valutare singoli articoli o persone | [Fonte](https://sfdora.org/read/) | `article-influence`, `citescore`, `eigenfactor`, `jci`, `jif`, `sjr`, `snip` |
| FAIR A | Accessibile: protocolli aperti e metadati che restano anche senza i dati | [Fonte](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR F | Reperibile: identificatori persistenti e metadati ricchi | [Fonte](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR I | Interoperabile: vocabolari formali e condivisi | [Fonte](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR R | Riusabile: licenza chiara, provenienza dettagliata, standard di comunità | [Fonte](https://doi.org/10.1038/sdata.2016.18) | — |
| FORCE11 1 | Importanza: i dati sono prodotti di ricerca legittimi e citabili | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 2 | Credito e attribuzione a chi ha contribuito ai dati | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 3 | Evidenza: citare i dati su cui si fonda un'affermazione | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 4 | Identificazione univoca e persistente | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 5 | Accesso ai dati e ai metadati citati | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 6 | Persistenza degli identificatori e dei metadati oltre la vita dei dati | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 7 | Specificità e verificabilità della porzione citata | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 8 | Interoperabilità e flessibilità fra comunità | [Fonte](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| Manifesto di Leiden 1 | La valutazione quantitativa sostiene il giudizio qualitativo degli esperti | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 10 | Esaminare regolarmente gli indicatori e aggiornarli | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 2 | Misurare rispetto alle missioni di ricerca dell'istituzione, del gruppo o della persona | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 3 | Proteggere l'eccellenza nella ricerca di rilevanza locale | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 4 | Tenere aperti, trasparenti e semplici raccolta dei dati e analisi | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 5 | Permettere a chi è valutato di verificare dati e analisi | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 6 | Tenere conto delle differenze fra campi nelle pratiche di pubblicazione e citazione | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 7 | Valutare le singole persone con un giudizio qualitativo del loro portafoglio | [Fonte](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 8 | Evitare la concretezza fuori luogo e la falsa precisione | [Fonte](https://www.nature.com/articles/520429a) | `altmetric`, `percentile` |
| Manifesto di Leiden 9 | Riconoscere gli effetti sistemici della valutazione e degli indicatori | [Fonte](https://www.nature.com/articles/520429a) | — |
| Preregistrazione | Dichiarare ipotesi e metodo prima di raccogliere i dati | [Fonte](https://www.cos.io/initiatives/prereg) | — |
<!-- /table -->

## Campi FORD

Il Manuale di Frascati 2015 dell'OCSE classifica la ricerca e sviluppo in sei campi (scienze naturali; ingegneria e tecnologia; medicina e salute; agraria e veterinaria; scienze sociali; scienze umane e arti) e quarantadue sottocampi. Metrum li pubblica come schema SKOS con le etichette in tre lingue usate dalla Cripta; i codici organizzano il lavoro editoriale e non misurano il merito. Trivium vi fa ponte con `skos:broadMatch`.

## Il raccordo filosofico

Il manifesto della Cripta descrive, nel secondo capoverso, una svolta: con la macchina astratta del 1936 si avvia «il processo di quantificazione della scrittura», che trova nell'ipertesto la sua ostensione finale ([F08](../dubium/term/F08.html)). Nel quinto capoverso la quantificazione ontologica è il rapporto fra i valori delle variabili vincolate di una teoria e i suoi enunciati ([F19](../dubium/term/F19.html)). La scientometria è una quantificazione di secondo grado: non quantifica l'essere, ma la scrittura che ne tratta, contando come i testi si citano, si riusano, si distribuiscono. Metrum tiene fermo questo scarto. Le sue osservazioni riguardano opere, edizioni, sedi, persone come soggetti ontici; la domanda sul senso di ciò che misurano resta in Dubium. Per questo l'intestazione del modulo rimanda a F08, a F19 e al capitale semantico ([F13](../dubium/term/F13.html)), e non dichiara alcuna equivalenza.

La seconda tesi è quella della non neutralità. Una misura altera ciò che misura: chi sa di essere contato scrive per essere contato. Il Manifesto di Leiden lo chiama effetto sistemico (principio 9); la pagina «Chi siamo» della Cripta lo dice con il lessico del materialismo dialettico. Metrum non risolve il problema, ma lo rende visibile: ogni osservazione dichiara il suo contratto, e ogni contratto porta con sé i principi che ne limitano l'uso.

## Interrogazioni di esempio

I protocolli di cui DORA limita l'uso, con la famiglia:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?protocollo ?famiglia WHERE {
  mtr:principle-dora mtr:cautions ?p .
  ?p skos:prefLabel ?protocollo ; mtr:family/skos:prefLabel ?famiglia .
  FILTER ( lang(?protocollo) = "it" && lang(?famiglia) = "it" )
}
```

I protocolli applicabili ai dati di ricerca:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
SELECT ?p WHERE { ?p mtr:scope mtr:scope-data }
```

Le discipline di Trivium che fanno ponte a un campo FORD delle scienze umane:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?disciplina ?campo WHERE {
  ?campo skos:broader mtr:ford-6 .
  ?disciplina skos:broadMatch ?campo .
}
```

## Limiti

Metrum pubblica i protocolli che il servizio della Cripta conosce oggi; non pretende di esaurire la scientometria. I metodi sono descritti in una frase: la riproduzione effettiva di un indicatore dipende dalla fonte e dal suo corpus. Le etichette inglesi e latine dei campi FORD sono quelle usate dalla Cripta, non traduzioni ufficiali dell'OCSE. Il modulo non contiene osservazioni reali: quelle vivono nel servizio semantico del sito, che pubblica solo ciò che la redazione ha rilasciato.
