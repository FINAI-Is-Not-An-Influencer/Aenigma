# Trivium. Formalisation and method

[Beginner's guide](README.en.md) · [Italiano](FORMALIZZAZIONE.md) · [Latine](FORMALIZZAZIONE.la.md)

Trivium formalises a different object from Dubium. Dubium reads a text; Trivium reads an ordering: the taxonomy by which a site distributes its articles. The ordering is a documented fact (the categories exist, they have a name, a hierarchy, a number), while translations, correspondences and bridges are editorial readings. The module keeps the two apart: every concept keeps the public source of the category, and everything that was added is declared in this document.

## Sources

| Source | What it provides | Date |
| --- | --- | --- |
| Public categories API of criptasemantica.it | Name, slug, identifier, parent, description, link | snapshot of 11 November 2026, kept in `fonti/` |
| Project, About, Channels, Articles, FINAI and Alessandro Sevardi pages | The rooms, described in the alternative texts of the images and in the page texts | 11 November 2026 |
| Wikidata | Items matching the disciplines, with their number of Wikipedia links | 11 November 2026 |
| Frascati Manual 2015 (FORD classification), through Metrum | Fields of research and development | 2015 edition |
| Dubium | Concepts of the manifesto to which the disciplines are linked | version 0.2.0 |

Article counts per category are not recorded: they change daily and do not describe the concept.

## The model

Four classes, all subclasses of `skos:Concept` and mutually disjoint: `trv:Disciplina`, `trv:Genere`, `trv:Programma`, `trv:Stanza`. Four SKOS schemes: `trv:discipline`, `trv:generi`, `trv:programmi`, `trv:stanze`. Two collections: `trv:trivio` and `trv:quadrivio`. One property of its own, `trv:identificativoCategoria`, which keeps the WordPress number of the category; everything else uses SKOS and Dublin Core.

**Scheme assignment rule.** One climbs from the category to its root. If the root is one of the editorial sections (news, reviews, authors, profiles, products, synergies, channels, uncategorised) the concept is a genre; if it is one of the programme lines (digital communism, world-wide semantic web, hermeneutic search engine, philosophical programming, metaphysics of play, academic studies) it is a programme; otherwise it is a discipline. The hierarchy of the site is kept with `skos:broader` within the same scheme; the roots are `skos:topConceptOf` their scheme.

**The "Logica" case.** The site has two categories with the same slug: one at the top and one under Dialectic. A single IRI would merge two nodes of the site. The second receives the suffix `-dialettica`, the same the site uses to tell the two "Antropologia" apart, and the two entries are declared `skos:related`.

**Labels.** Italian is the category name, character for character. English and Latin are editorial translations. For modern disciplines Latin uses transparent neologisms (`Informatica`, `Cybernetica`, `Data ingentia` for big data) or periphrases (`Disciplina machinalis` for machine learning). Scope notes carry the author's Italian text and, for the twenty categories that have one, the English and Latin translation.

## Wikidata correspondences

The method was as follows. For each Italian name the Wikidata SPARQL service was asked for the items with that Italian label, excluding disambiguation pages and scholarly articles, ordered by number of Wikipedia links. The most linked item was chosen only when its description matched the sense of the category; in ambiguous cases nothing was chosen. Some of the exclusions: "Cosmologia" (the category sits under Epistemology; the most linked item is physical cosmology); "Cronaca" (the most linked item is the historiographic genre); "Teoria critica" (the item found is critical sociology); "Scienze politiche" (an item with only five links); "Storia dell'Africa" (only the continent was found); "Filosofia italiana", "Psicanalisi", "Filosofia prima", "Beni culturali" (no item with that label). "Politica", "Heidegger" and "Nietzsche" were verified individually.

The relation is always `skos:closeMatch`. `skos:exactMatch` is forbidden by the SHACL constraints: an editorial category is not identical to an encyclopaedic concept, even when it bears the same name. The verification date is that of the snapshot.

<!-- table:wikidata -->
| Concept | IRI | Wikidata item |
| --- | --- | --- |
| Aesthetics | `trv:estetica` | [Q35986](https://www.wikidata.org/wiki/Q35986) |
| Ancient philosophy | `trv:filosofia-antica` | [Q204100](https://www.wikidata.org/wiki/Q204100) |
| Anthropology | `trv:antropologia` | [Q23404](https://www.wikidata.org/wiki/Q23404) |
| Anthropology | `trv:antropologia-dialettica` | [Q23404](https://www.wikidata.org/wiki/Q23404) |
| Art | `trv:arte` | [Q735](https://www.wikidata.org/wiki/Q735) |
| Art history | `trv:storia-dellarte` | [Q50637](https://www.wikidata.org/wiki/Q50637) |
| Artificial intelligence | `trv:intelligenza-artificiale` | [Q11660](https://www.wikidata.org/wiki/Q11660) |
| Astronomy | `trv:astronomia` | [Q333](https://www.wikidata.org/wiki/Q333) |
| Big data | `trv:big-data` | [Q858810](https://www.wikidata.org/wiki/Q858810) |
| Biology | `trv:biologia` | [Q420](https://www.wikidata.org/wiki/Q420) |
| Buddhism | `trv:buddismo` | [Q748](https://www.wikidata.org/wiki/Q748) |
| Cognitive neuroscience | `trv:neuroscienze-cognitive` | [Q1138951](https://www.wikidata.org/wiki/Q1138951) |
| Cognitive science | `trv:scienze-cognitive` | [Q147638](https://www.wikidata.org/wiki/Q147638) |
| Computer science | `trv:informatica` | [Q21198](https://www.wikidata.org/wiki/Q21198) |
| Constitution | `trv:costituzione` | [Q7755](https://www.wikidata.org/wiki/Q7755) |
| Contemporary art | `trv:arte-contemporanea` | [Q186030](https://www.wikidata.org/wiki/Q186030) |
| Contemporary history | `trv:storia-contemporanea` | [Q186075](https://www.wikidata.org/wiki/Q186075) |
| Contemporary philosophy | `trv:filosofia-contemporanea` | [Q943303](https://www.wikidata.org/wiki/Q943303) |
| Cultural anthropology | `trv:antropologia-culturale` | [Q28598](https://www.wikidata.org/wiki/Q28598) |
| Cultural studies | `trv:studi-culturali` | [Q1143546](https://www.wikidata.org/wiki/Q1143546) |
| Cybernetics | `trv:cibernetica` | [Q123637](https://www.wikidata.org/wiki/Q123637) |
| Development | `trv:sviluppo` | [Q4530482](https://www.wikidata.org/wiki/Q4530482) |
| Developmental psychology | `trv:psicologia-dello-sviluppo` | [Q175002](https://www.wikidata.org/wiki/Q175002) |
| Dialectic | `trv:dialettica` | [Q9453](https://www.wikidata.org/wiki/Q9453) |
| Dialectical materialism | `trv:materialismo-dialettico` | [Q181207](https://www.wikidata.org/wiki/Q181207) |
| Ecology | `trv:ecologia` | [Q7150](https://www.wikidata.org/wiki/Q7150) |
| Economics | `trv:economia` | [Q159810](https://www.wikidata.org/wiki/Q159810) |
| Epistemology | `trv:epistemologia` | [Q9471](https://www.wikidata.org/wiki/Q9471) |
| Essay writing | `trv:saggistica` | [Q27801](https://www.wikidata.org/wiki/Q27801) |
| Ethics | `trv:etica` | [Q9465](https://www.wikidata.org/wiki/Q9465) |
| Ethnology | `trv:etnologia` | [Q43455](https://www.wikidata.org/wiki/Q43455) |
| Evolution | `trv:evoluzione` | [Q1063](https://www.wikidata.org/wiki/Q1063) |
| Feminism | `trv:femminismo` | [Q7252](https://www.wikidata.org/wiki/Q7252) |
| Finance | `trv:finanza` | [Q43015](https://www.wikidata.org/wiki/Q43015) |
| Foreign policy | `trv:politica-estera` | [Q181648](https://www.wikidata.org/wiki/Q181648) |
| Formal ontology | `trv:ontologia-formale` | [Q1437388](https://www.wikidata.org/wiki/Q1437388) |
| Foundations of mathematics | `trv:fondamenti-della-matematica` | [Q833585](https://www.wikidata.org/wiki/Q833585) |
| General metaphysics | `trv:metafisica-generale` | [Q35277](https://www.wikidata.org/wiki/Q35277) |
| Genetics | `trv:genetica` | [Q7162](https://www.wikidata.org/wiki/Q7162) |
| Geography | `trv:geografia` | [Q1071](https://www.wikidata.org/wiki/Q1071) |
| Geopolitics | `trv:geopolitica` | [Q159385](https://www.wikidata.org/wiki/Q159385) |
| Globalisation | `trv:globalizzazione` | [Q7181](https://www.wikidata.org/wiki/Q7181) |
| Globalisation | `trv:globalizzazione-storia` | [Q7181](https://www.wikidata.org/wiki/Q7181) |
| Gnoseology | `trv:gnoseologia` | [Q2560959](https://www.wikidata.org/wiki/Q2560959) |
| Grammar | `trv:grammatica` | [Q8091](https://www.wikidata.org/wiki/Q8091) |
| Heidegger | `trv:heidegger` | [Q48301](https://www.wikidata.org/wiki/Q48301) |
| Hermeneutics | `trv:ermeneutica` | [Q102686](https://www.wikidata.org/wiki/Q102686) |
| Historical materialism | `trv:materialismo-storico` | [Q190004](https://www.wikidata.org/wiki/Q190004) |
| History | `trv:storia` | [Q309](https://www.wikidata.org/wiki/Q309) |
| History of Sardinia | `trv:storia-della-sardegna` | [Q1516605](https://www.wikidata.org/wiki/Q1516605) |
| History of mathematics | `trv:storia-della-matematica` | [Q185264](https://www.wikidata.org/wiki/Q185264) |
| History of philosophy | `trv:storia-della-filosofia` | [Q27654](https://www.wikidata.org/wiki/Q27654) |
| History of religions | `trv:storia-delle-religioni` | [Q846742](https://www.wikidata.org/wiki/Q846742) |
| History of science | `trv:storia-delle-scienze` | [Q201486](https://www.wikidata.org/wiki/Q201486) |
| Human rights | `trv:diritti-umani` | [Q8458](https://www.wikidata.org/wiki/Q8458) |
| Imperialism | `trv:imperialismo` | [Q7260](https://www.wikidata.org/wiki/Q7260) |
| Industry | `trv:industria` | [Q8148](https://www.wikidata.org/wiki/Q8148) |
| Information architecture | `trv:architettura-dellinformazione` | [Q845921](https://www.wikidata.org/wiki/Q845921) |
| International relations | `trv:relazioni-internazionali` | [Q166542](https://www.wikidata.org/wiki/Q166542) |
| Jainism | `trv:giainismo` | [Q9232](https://www.wikidata.org/wiki/Q9232) |
| Jurisprudence | `trv:giurisprudenza` | [Q4932206](https://www.wikidata.org/wiki/Q4932206) |
| Labour | `trv:lavoro` | [Q268378](https://www.wikidata.org/wiki/Q268378) |
| Law | `trv:diritto` | [Q7748](https://www.wikidata.org/wiki/Q7748) |
| Linguistics | `trv:linguistica` | [Q8162](https://www.wikidata.org/wiki/Q8162) |
| Literature | `trv:letteratura` | [Q8242](https://www.wikidata.org/wiki/Q8242) |
| Logic | `trv:logica` | [Q8078](https://www.wikidata.org/wiki/Q8078) |
| Logic | `trv:logica-dialettica` | [Q8078](https://www.wikidata.org/wiki/Q8078) |
| Machine learning | `trv:machine-learning` | [Q2539](https://www.wikidata.org/wiki/Q2539) |
| Macroeconomics | `trv:macroeconomia` | [Q39680](https://www.wikidata.org/wiki/Q39680) |
| Marxist theory | `trv:teoria-marxista` | [Q7264](https://www.wikidata.org/wiki/Q7264) |
| Mathematical logic | `trv:logica-matematica` | [Q1166618](https://www.wikidata.org/wiki/Q1166618) |
| Mathematics | `trv:matematica` | [Q395](https://www.wikidata.org/wiki/Q395) |
| Medieval art | `trv:arte-medievale` | [Q3624153](https://www.wikidata.org/wiki/Q3624153) |
| Metaphysics | `trv:metafisica` | [Q35277](https://www.wikidata.org/wiki/Q35277) |
| Metaverses | `trv:metaversi` | [Q2632041](https://www.wikidata.org/wiki/Q2632041) |
| Modern philosophy | `trv:filosofia-moderna` | [Q860746](https://www.wikidata.org/wiki/Q860746) |
| Music | `trv:musica` | [Q638](https://www.wikidata.org/wiki/Q638) |
| Myth | `trv:mito` | [Q12827256](https://www.wikidata.org/wiki/Q12827256) |
| Mythology | `trv:mitologia` | [Q9134](https://www.wikidata.org/wiki/Q9134) |
| Neuroscience | `trv:neuroscienze` | [Q207011](https://www.wikidata.org/wiki/Q207011) |
| News | `trv:notizie` | [Q38926](https://www.wikidata.org/wiki/Q38926) |
| Nietzsche | `trv:nietzsche` | [Q9358](https://www.wikidata.org/wiki/Q9358) |
| Ontology | `trv:ontologia` | [Q44325](https://www.wikidata.org/wiki/Q44325) |
| Phenomenology | `trv:fenomenologia` | [Q179235](https://www.wikidata.org/wiki/Q179235) |
| Philology | `trv:filologia` | [Q40634](https://www.wikidata.org/wiki/Q40634) |
| Philosophy of language | `trv:filosofia-del-linguaggio` | [Q484761](https://www.wikidata.org/wiki/Q484761) |
| Philosophy of mathematics | `trv:filosofia-della-matematica` | [Q180536](https://www.wikidata.org/wiki/Q180536) |
| Philosophy of music | `trv:filosofia-della-musica` | [Q2092865](https://www.wikidata.org/wiki/Q2092865) |
| Philosophy of science | `trv:filosofia-della-scienza` | [Q59115](https://www.wikidata.org/wiki/Q59115) |
| Philosophy of technics | `trv:filosofia-della-tecnica` | [Q5862034](https://www.wikidata.org/wiki/Q5862034) |
| Physics | `trv:fisica` | [Q413](https://www.wikidata.org/wiki/Q413) |
| Polemology | `trv:polemologia` | [Q1367522](https://www.wikidata.org/wiki/Q1367522) |
| Political economy | `trv:economia-politica` | [Q47555](https://www.wikidata.org/wiki/Q47555) |
| Political philosophy | `trv:filosofia-politica` | [Q179805](https://www.wikidata.org/wiki/Q179805) |
| Politics | `trv:politica` | [Q7163](https://www.wikidata.org/wiki/Q7163) |
| Postcolonial studies | `trv:studi-postcoloniali` | [Q265425](https://www.wikidata.org/wiki/Q265425) |
| Psycholinguistics | `trv:psicolinguistica` | [Q179488](https://www.wikidata.org/wiki/Q179488) |
| Psycholinguistics | `trv:psicolinguistica-linguistica` | [Q179488](https://www.wikidata.org/wiki/Q179488) |
| Psychology | `trv:psicologia` | [Q9418](https://www.wikidata.org/wiki/Q9418) |
| Quadrivium | `trv:quadrivio` | [Q273822](https://www.wikidata.org/wiki/Q273822) |
| Reviews | `trv:recensioni` | [Q265158](https://www.wikidata.org/wiki/Q265158) |
| Rhetoric | `trv:retorica` | [Q81009](https://www.wikidata.org/wiki/Q81009) |
| Semantic web | `trv:web-semantico` | [Q54837](https://www.wikidata.org/wiki/Q54837) |
| Semantics | `trv:semantica` | [Q39645](https://www.wikidata.org/wiki/Q39645) |
| Social psychology | `trv:psicologia-sociale` | [Q161272](https://www.wikidata.org/wiki/Q161272) |
| Sociology | `trv:sociologia` | [Q21201](https://www.wikidata.org/wiki/Q21201) |
| Spiritualism | `trv:spiritualismo` | [Q2636432](https://www.wikidata.org/wiki/Q2636432) |
| Systems theory | `trv:teoria-dei-sistemi` | [Q269699](https://www.wikidata.org/wiki/Q269699) |
| Technology | `trv:tecnologia` | [Q11016](https://www.wikidata.org/wiki/Q11016) |
| Theatre | `trv:teatro` | [Q11635](https://www.wikidata.org/wiki/Q11635) |
| Theoretical philosophy | `trv:filosofia-teoretica` | [Q2166096](https://www.wikidata.org/wiki/Q2166096) |
| Trade union | `trv:sindacato` | [Q178790](https://www.wikidata.org/wiki/Q178790) |
| Transhumanism | `trv:transumanesimo` | [Q194100](https://www.wikidata.org/wiki/Q194100) |
| Trivium | `trv:trivio` | [Q205186](https://www.wikidata.org/wiki/Q205186) |
| Umbria | `trv:umbria` | [Q1280](https://www.wikidata.org/wiki/Q1280) |
<!-- /table -->

## Bridges to the FORD fields

The bridge is `skos:broadMatch`: the Cripta category is read as narrower than a FORD field, or as internal to it. The FORD classification describes research activities, not thoughts: this is why some bridges surprise. Anthropology sits in "Sociology" (5.4) because the Frascati Manual includes anthropology and ethnology there; rhetoric and grammar sit in "Languages and literature" (6.2); logic has two bridges, philosophy (6.3) and mathematics (1.1); the site's geography, which gathers physics and biology, is read as "Earth and related environmental sciences" (1.5). Bridges are declared only where the placement is defensible; the categories of local news, domestic politics or territory have none.

<!-- table:ford -->
| Concept | IRI | FORD field |
| --- | --- | --- |
| Aesthetics | `trv:estetica` | 6.3 · Philosophical, ethical and religious studies |
| Anthropology | `trv:antropologia` | 5.4 · Sociological research |
| Anthropology | `trv:antropologia-dialettica` | 5.4 · Sociological research |
| Art | `trv:arte` | 6.4 · Art, performance and music studies |
| Art history | `trv:storia-dellarte` | 6.4 · Art, performance and music studies |
| Artificial intelligence | `trv:intelligenza-artificiale` | 1.2 · Computing and information studies |
| Astronomy | `trv:astronomia` | 1.3 · Physical research |
| Big data | `trv:big-data` | 1.2 · Computing and information studies |
| Biology | `trv:biologia` | 1.6 · Biological research |
| Buddhism | `trv:buddismo` | 6.3 · Philosophical, ethical and religious studies |
| Classical studies | `trv:studi-classici` | 6.2 · Language and literary studies |
| Cognitive science | `trv:scienze-cognitive` | 5.1 · Psychology and cognition |
| Computer science | `trv:informatica` | 1.2 · Computing and information studies |
| Cosmology | `trv:cosmologia` | 1.3 · Physical research |
| Cybernetics | `trv:cibernetica` | 1.2 · Computing and information studies |
| Cybernetics | `trv:cibernetica` | 2.2 · Electrical, electronic and information engineering |
| Dialectic | `trv:dialettica` | 6.3 · Philosophical, ethical and religious studies |
| Eastern philosophy | `trv:filosofia-orientale` | 6.3 · Philosophical, ethical and religious studies |
| Ecology | `trv:ecologia` | 1.6 · Biological research |
| Economics | `trv:economia` | 5.2 · Economics and enterprise |
| Epistemology | `trv:epistemologia` | 6.3 · Philosophical, ethical and religious studies |
| Epistemology and metaphysics | `trv:epistemologia-e-metafisica` | 6.3 · Philosophical, ethical and religious studies |
| Ethics | `trv:etica` | 6.3 · Philosophical, ethical and religious studies |
| Feminism | `trv:femminismo` | 5.4 · Sociological research |
| Finance | `trv:finanza` | 5.2 · Economics and enterprise |
| Fundamental ontology | `trv:ontologia-fondamentale` | 6.3 · Philosophical, ethical and religious studies |
| General metaphysics | `trv:metafisica-generale` | 6.3 · Philosophical, ethical and religious studies |
| Genetics | `trv:genetica` | 1.6 · Biological research |
| Geography | `trv:geografia` | 1.5 · Earth and environmental research |
| Geopolitics | `trv:geopolitica` | 5.6 · Political research |
| Grammar | `trv:grammatica` | 6.2 · Language and literary studies |
| Hermeneutic search engine | `trv:motore-ermeneutico` | 1.2 · Computing and information studies |
| Hermeneutics | `trv:ermeneutica` | 6.3 · Philosophical, ethical and religious studies |
| History | `trv:storia` | 6.1 · Historical and archaeological research |
| History of philosophy | `trv:storia-della-filosofia` | 6.3 · Philosophical, ethical and religious studies |
| History of religions | `trv:storia-delle-religioni` | 6.3 · Philosophical, ethical and religious studies |
| History of science | `trv:storia-delle-scienze` | 6.1 · Historical and archaeological research |
| Jainism | `trv:giainismo` | 6.3 · Philosophical, ethical and religious studies |
| Jurisprudence | `trv:giurisprudenza` | 5.5 · Legal research |
| Law | `trv:diritto` | 5.5 · Legal research |
| Linguistics | `trv:linguistica` | 6.2 · Language and literary studies |
| Literature | `trv:letteratura` | 6.2 · Language and literary studies |
| Logic | `trv:logica` | 1.1 · Mathematical research |
| Logic | `trv:logica` | 6.3 · Philosophical, ethical and religious studies |
| Logic | `trv:logica-dialettica` | 1.1 · Mathematical research |
| Logic | `trv:logica-dialettica` | 6.3 · Philosophical, ethical and religious studies |
| Machine learning | `trv:machine-learning` | 1.2 · Computing and information studies |
| Mathematical logic | `trv:logica-matematica` | 1.1 · Mathematical research |
| Mathematics | `trv:matematica` | 1.1 · Mathematical research |
| Metaphysics | `trv:metafisica` | 6.3 · Philosophical, ethical and religious studies |
| Metaphysics of play | `trv:metafisica-gioco` | 6.3 · Philosophical, ethical and religious studies |
| Music | `trv:musica` | 6.4 · Art, performance and music studies |
| Mythology | `trv:mitologia` | 6.3 · Philosophical, ethical and religious studies |
| Neuroscience | `trv:neuroscienze` | 3.1 · Foundations of medicine |
| Ontology | `trv:ontologia` | 6.3 · Philosophical, ethical and religious studies |
| Phenomenology | `trv:fenomenologia` | 6.3 · Philosophical, ethical and religious studies |
| Philology | `trv:filologia` | 6.2 · Language and literary studies |
| Philosophical programming | `trv:programmazione-filosofica` | 1.2 · Computing and information studies |
| Philosophical programming | `trv:programmazione-filosofica` | 6.3 · Philosophical, ethical and religious studies |
| Philosophy of language | `trv:filosofia-del-linguaggio` | 6.3 · Philosophical, ethical and religious studies |
| Philosophy of science | `trv:filosofia-della-scienza` | 6.3 · Philosophical, ethical and religious studies |
| Physics | `trv:fisica` | 1.3 · Physical research |
| Political philosophy | `trv:filosofia-politica` | 6.3 · Philosophical, ethical and religious studies |
| Politics | `trv:politica` | 5.6 · Political research |
| Psychoanalysis | `trv:psicanalisi` | 5.1 · Psychology and cognition |
| Psycholinguistics | `trv:psicolinguistica` | 5.1 · Psychology and cognition |
| Psycholinguistics | `trv:psicolinguistica-linguistica` | 5.1 · Psychology and cognition |
| Psychology | `trv:psicologia` | 5.1 · Psychology and cognition |
| Rhetoric | `trv:retorica` | 6.2 · Language and literary studies |
| Semantics | `trv:semantica` | 6.2 · Language and literary studies |
| Social sciences | `trv:scienze-sociali` | 5.9 · Other social research |
| Sociology | `trv:sociologia` | 5.4 · Sociological research |
| Technology | `trv:tecnologia` | 2.11 · Other engineering and technology research |
| Theatre | `trv:teatro` | 6.4 · Art, performance and music studies |
| World-wide semantic web | `trv:www-semantico` | 1.2 · Computing and information studies |
<!-- /table -->

## Links to Dubium

A `skos:related` link between a category and a concept of the manifesto is a reading: it proposes with which notion of Dubium the articles of that category are best read. It does not claim that the category is defined by the manifesto. The most direct readings are those where the name coincides: Fundamental Ontology and `dub:ontologiaFondamentale`, Formal Ontology and `dub:ontologiaFormale`, Phenomenology and `dub:ontologiaFenomenologica`. Others make a function explicit: Grammar points to writing and text, Dialectic to dialogical practice and recollection, Rhetoric to sharing and explicitness, Computer Science to the concrete machine, Artificial Intelligence to the abstract machine, the World-wide Semantic Web to the Web and to semantic capital. The Heidegger category points to `dub:problemaEssere` because the epigraph of "Fundamental Ontology" on the site is the first page of *Being and Time*.

<!-- table:dubium -->
| Concept | IRI | Dubium concept |
| --- | --- | --- |
| Ancient philosophy | `trv:filosofia-antica` | `dub:esordioGreco` · Greek beginnings |
| Artificial intelligence | `trv:intelligenza-artificiale` | `dub:macchinaAstratta` · abstract machine |
| Authors | `trv:autori` | `dub:esserci` · Dasein |
| Channels | `trv:canali` | `dub:criptaSito` · Cripta Semantica as website |
| Computer science | `trv:informatica` | `dub:macchinaConcreta` · concrete machine |
| Cybernetics | `trv:cibernetica` | `dub:macchinaAstratta` · abstract machine |
| Dialectic | `trv:dialettica` | `dub:praticaDialogica` · dialogical practice |
| Dialectic | `trv:dialettica` | `dub:reminiscenza` · recollection |
| Epistemology | `trv:epistemologia` | `dub:scienzaTrasformazione` · science as transformation |
| Epistemology | `trv:epistemologia` | `dub:teoria` · theory |
| First philosophy | `trv:filosofia-prima` | `dub:ontologiaFondamentale` · fundamental ontology |
| Formal ontology | `trv:ontologia-formale` | `dub:ontologiaFormale` · formal phenomenological ontology |
| Fundamental ontology | `trv:ontologia-fondamentale` | `dub:ontologiaFondamentale` · fundamental ontology |
| Fundamental ontology | `trv:ontologia-fondamentale` | `dub:problemaSensoEssere` · question of the sense of being |
| General metaphysics | `trv:metafisica-generale` | `dub:metafisicaOccidentale` · Western metaphysics |
| Gnoseology | `trv:gnoseologia` | `dub:concettualizzazione` · conceptualisation |
| Grammar | `trv:grammatica` | `dub:scrittura` · writing |
| Grammar | `trv:grammatica` | `dub:testo` · text |
| Heidegger | `trv:heidegger` | `dub:problemaEssere` · question of being |
| History of being | `trv:storia-dellessere` | `dub:pensieroOccidentale` · Western thought |
| History of being | `trv:storia-dellessere` | `dub:sensoEssere` · sense of being |
| History of philosophy | `trv:storia-della-filosofia` | `dub:filosofia` · philosophy |
| History of philosophy | `trv:storia-della-filosofia` | `dub:tradizioneTestuale` · textual tradition |
| Logic | `trv:logica` | `dub:giudizio` · judgement |
| Logic | `trv:logica` | `dub:strutturaLogica` · logical structure |
| Logic | `trv:logica-dialettica` | `dub:giudizio` · judgement |
| Logic | `trv:logica-dialettica` | `dub:strutturaLogica` · logical structure |
| Mathematics | `trv:matematica` | `dub:reminiscenza` · recollection |
| Metaphysics | `trv:metafisica` | `dub:metafisicaOccidentale` · Western metaphysics |
| News | `trv:notizie` | `dub:articolo` · article as an artefact |
| Ontology | `trv:ontologia` | `dub:ontologiaEnte` · ontology of entities |
| Ontology and semantics | `trv:ontologia-e-semantica` | `dub:ontologiaInformatica` · computational ontology |
| Ontology and semantics | `trv:ontologia-e-semantica` | `dub:significato` · computable meaning |
| Phenomenology | `trv:fenomenologia` | `dub:ontologiaFenomenologica` · phenomenological ontology |
| Philosophical programming | `trv:programmazione-filosofica` | `dub:codiceSviluppo` · development code |
| Philosophical programming | `trv:programmazione-filosofica` | `dub:iperscritturaConsapevole` · conscious hyperwriting |
| Philosophy of language | `trv:filosofia-del-linguaggio` | `dub:enunciato` · statement |
| Philosophy of mathematics | `trv:filosofia-della-matematica` | `dub:quantificazioneOntologica` · ontological quantification |
| Reviews | `trv:recensioni` | `dub:articolo` · article as an artefact |
| Rhetoric | `trv:retorica` | `dub:condivisione` · shared character |
| Rhetoric | `trv:retorica` | `dub:esplicitezza` · explicitness |
| Room of Articles | `trv:stanza-degli-articoli` | `dub:articolo` · article as an artefact |
| Room of FINAI | `trv:stanza-di-finai` | `dub:criptaSito` · Cripta Semantica as website |
| Room of the Algorithmic Laboratory | `trv:stanza-del-laboratorio-algoritmico` | `dub:notaIpertestuale` · hypertextual note |
| Room of the Blue Rose | `trv:stanza-della-rosa-blu` | `dub:praticaDialogica` · dialogical practice |
| Room of the Project | `trv:stanza-del-progetto` | `dub:gettatezza` · thrownness |
| Room of the Project | `trv:stanza-del-progetto` | `dub:progettoCripta` · the Cripta project |
| Semantic web | `trv:web-semantico` | `dub:ontologiaInformatica` · computational ontology |
| Semantic web | `trv:web-semantico` | `dub:organizzazioneSemantica` · semantic organisation |
| Semantics | `trv:semantica` | `dub:significato` · computable meaning |
| World-wide semantic web | `trv:www-semantico` | `dub:capitaleSemantico` · semantic capital |
| World-wide semantic web | `trv:www-semantico` | `dub:web` · World Wide Web |
<!-- /table -->

## The rooms

The nine rooms are not categories: they are the allegorical places the site describes in the alternative texts of its images and in its page texts. Each room keeps as source the page where it appears and a scope note summarising its iconography. Two rooms, Interpretation and Justice, are only named as portals: the note says so. The Room of Articles takes its name from the sentence "from the current room of the Cripta Semantica" with which the page introduces the network of articles.

## SHACL constraints

The [shapes](shapes.ttl) check, for every concept: three preferred labels with distinct languages, a scheme, a lowercase notation, a source on the site's domain, scope notes with distinct languages, correspondences only towards Wikidata, no `skos:exactMatch`, bridges only towards the FORD fields of Metrum, and the rule that a concept is a top concept or has a parent in the same scheme (SPARQL constraint). Categories must carry the WordPress identifier. The verification program tries five alterations of Trivium (missing Latin label, non-Wikidata correspondence, forbidden equivalence, concept without scheme, parent in another scheme), all rejected.

## Example queries

Disciplines the site places in the trivium, with their Wikidata correspondence:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?art ?wikidata WHERE {
  trv:trivio skos:member ?art .
  ?art skos:closeMatch ?wikidata .
}
```

Disciplines bridged to the FORD field "Philosophy, ethics and religion":

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?name WHERE {
  ?discipline skos:broadMatch mtr:ford-6-3 ; skos:prefLabel ?name .
  FILTER ( lang(?name) = "en" )
} ORDER BY ?name
```

Categories to be read with the concept of fundamental ontology:

```sparql
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?category WHERE { ?category skos:related dub:ontologiaFondamentale }
```

## Limits

The categories of a site change: Trivium photographs a date and declares it. Translations and correspondences are revisable editorial choices. Descriptions exist only where the author wrote them. The FORD bridges serve the scientometrics of Metrum and do not claim to classify philosophy. The module does not record how many articles sit in a category, nor which: that work belongs to the semantic service of the site.
