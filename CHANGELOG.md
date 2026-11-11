# Registro delle versioni · Changelog · Index versionum

Le versioni dei moduli sono indipendenti. Gli IRI già pubblicati non cambiano mai; una versione precedente resta citabile attraverso il suo IRI di versione.
Module versions are independent. Published IRIs never change; a prior version remains citable through its version IRI.
Versiones partium sui iuris sunt. IRI iam edita numquam mutantur; versio prior per IRI versionis citabilis manet.

## Aenigma 0.2.0 — 11 novembre 2026

**Italiano.** Aenigma diventa una rete di moduli. Nasce la radice `aenigma.ttl`, che importa i documenti pubblicati dei moduli e li descrive con un registro (`aen:Modulo`), e il file `void.ttl`, che elenca distribuzioni e numero di triple. Ogni modulo è ora esportato anche in JSON-LD e RDF/XML con un contesto JSON-LD. Il sito di riferimento è generato per tutti i moduli dallo stesso programma, con una pagina per ogni termine in tre lingue, una gerarchia per modulo e una pagina «Documentazione» che collega sito, repository e Wiki. Il collaudo copre l'intera rete (`tests/verifica.py`) e i collegamenti del sito (`tools/check_site.py`).

- **Dubium 0.2.0.** Metadati completi (titolo, descrizione, licenza CC BY 4.0, autori, editore, date, prefisso preferito), versione precedente citabile. Allineamenti: i concetti sono `skos:Concept` raccolti nello schema `dub:concetti` con etichette preferite; posizioni, domande, passi e asserzioni sono `prov:Entity`; `derivedFrom` è una sottoproprietà di `prov:wasDerivedFrom`; le fonti sono `schema:CreativeWork`. Nessun IRI è cambiato; le 2.786 triple della 0.1.0 sono conservate e ne sono state aggiunte 554.
- **Trivium 0.1.0 (nuovo).** Le 202 categorie pubbliche del sito come schemi SKOS di discipline, generi, linee di programma e stanze, con etichette in tre lingue, descrizioni d'autore tradotte, 112 corrispondenze Wikidata verificate (`skos:closeMatch`), 75 ponti verso i campi FORD di Metrum (`skos:broadMatch`) e 32 letture verso i concetti di Dubium (`skos:related`). Collezioni Trivio e Quadrivio. Generato da `tools/trivium_from_taxonomy.py` a partire dall'istantanea in `trivium/fonti/`.
- **Metrum 0.1.0 (nuovo).** Il modello dell'osservazione qualificata (protocollo, soggetto, corpus, periodo, copertura, stato, fonte, prova), 58 protocolli in 14 famiglie, 9 ambiti, 6 tipi di valore, 3 coperture, 4 stati, i 48 campi FORD e 35 principi di valutazione responsabile (DORA, Leiden, CoARA, FAIR, FORCE11, citazione del software, CRediT, preregistrazione) con la relazione `mtr:cautions`. Vincoli SHACL con regole SPARQL per stato e valore, periodo, copertura e confrontabilità; esempi sintetici in `metrum/esempi.ttl`. Generato da `tools/metrum_from_dictionary.py`.
- **Sito.** Stile terminale condiviso (`style.css`, `reference.css`); navigazione fra moduli; pagine di documentazione in tre lingue; schede dei termini con esempio Turtle; collegamenti ai termini di altri moduli e alle pagine Wikidata.

**English.** Aenigma becomes a network of modules. The root `aenigma.ttl` imports the published module documents and describes them in a registry (`aen:Modulo`); `void.ttl` lists distributions and triple counts. Every module is also exported as JSON-LD and RDF/XML with a JSON-LD context. The reference site is generated for all modules by the same program, with a page per term in three languages, a hierarchy per module and a "Documentation" page linking site, repository and Wiki. Testing covers the whole network (`tests/verifica.py`) and the site links (`tools/check_site.py`).

- **Dubium 0.2.0.** Full metadata, citable prior version, alignments to SKOS (`dub:concetti` scheme with preferred labels), PROV-O and schema.org. No IRI changed; the 2,786 triples of 0.1.0 are kept and 554 were added.
- **Trivium 0.1.0 (new).** The 202 public categories of the site as SKOS schemes of disciplines, genres, programme lines and rooms, with three-language labels, translated author's descriptions, 112 verified Wikidata correspondences, 75 bridges to the FORD fields and 32 readings towards Dubium concepts; Trivium and Quadrivium collections.
- **Metrum 0.1.0 (new).** The qualified observation model, 58 protocols in 14 families, 9 scopes, 6 value types, 3 coverages, 4 states, the 48 FORD fields and 35 principles of responsible assessment with the `mtr:cautions` relation; SHACL constraints with SPARQL rules; synthetic examples.
- **Site.** Shared terminal style; cross-module navigation; trilingual documentation pages; term pages with a Turtle example; links to terms of other modules and to Wikidata pages.

**Latine.** Aenigma fit rete partium. Radix `aenigma.ttl` documenta partium edita importat et in indice (`aen:Modulo`) describit; `void.ttl` distributiones et numeros triplorum enumerat. Quaeque pars etiam ut JSON-LD et RDF/XML cum contextu JSON-LD exportatur. Situs indicis omnibus partibus eodem programmate gignitur, cum pagina cuiusque vocis tribus linguis, hierarchia cuiusque partis et pagina «Documenta» quae situm, repositorium et Vicipaginam conectit. Probatio totum rete (`tests/verifica.py`) et nexus situs (`tools/check_site.py`) complectitur.

- **Dubium 0.2.0.** Notae plenae, versio prior citabilis, consensiones cum SKOS (schema `dub:concetti` cum titulis praelatis), PROV-O et schema.org. Nullum IRI mutatum; 2.786 tripla versionis 0.1.0 servata et 554 addita.
- **Trivium 0.1.0 (novum).** 202 categoriae publicae situs ut schemata SKOS disciplinarum, generum, linearum consilii et cellarum, cum titulis trium linguarum, descriptionibus auctoris versis, 112 consensionibus Wikidata probatis, 75 pontibus ad campos FORD et 32 lectionibus ad notiones Dubii; collectiones Trivium et Quadrivium.
- **Metrum 0.1.0 (novum).** Forma observationis qualificatae, 58 protocolla in 14 familiis, 9 ambitus, 6 genera valorum, 3 ambitus corporis, 4 status, 48 campi FORD et 35 principia aestimationis responsabilis cum relatione `mtr:cautions`; regulae SHACL cum regulis SPARQL; exempla ficta.
- **Situs.** Stylus terminalis communis; navigatio inter partes; paginae documentorum trilingues; schedulae vocum cum exemplo Turtle; nexus ad voces aliarum partium et ad paginas Wikidata.

## Dubium 0.1.0-draft — 10 novembre 2026

Prima formalizzazione pubblica del manifesto della Cripta Semantica: 126 concetti, 40 posizioni, 161 asserzioni relazionali, 6 domande, 12 passi da quattro fonti pubbliche; vincoli SHACL; catalogo trilingue con 313 schede per lingua e stile terminale. Nella stessa giornata il sito ha ricevuto la gerarchia delle classi, le pagine dei termini e lo stile comune.
First public formalisation of the Cripta Semantica manifesto: 126 concepts, 40 positions, 161 relational assertions, 6 questions, 12 passages from four public sources; SHACL constraints; trilingual catalogue with 313 entries per language and terminal style.
Prima formalizatio publica prooemii Cryptae Semanticae: 126 notiones, 40 sententiae, 161 assertiones relationum, 6 quaestiones, 12 loci e quattuor fontibus publicis; regulae SHACL; index trilinguis cum 313 schedulis cuiusque linguae et stylo terminali.

## Prima di Dubium — giugno 2026

Homepage statica di Aenigma con RDFa e JSON-LD, politica di sicurezza dei contenuti con impronta del foglio di stile, dichiarazione dell'ontologia `dub:` senza classi.
Static Aenigma homepage with RDFa and JSON-LD, content security policy with stylesheet hash, declaration of the `dub:` ontology without classes.
Pagina prima statica Aenigmatis cum RDFa et JSON-LD, politica securitatis materiae cum vestigio styli, declaratio ontologiae `dub:` sine classibus.
