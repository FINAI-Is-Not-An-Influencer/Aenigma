#!/usr/bin/env python3
"""EN: Generate the Trivium module from the public taxonomy of criptasemantica.it.
LA: Partem Trivium e taxonomia publica situs criptasemantica.it gigne.

EN: The snapshot in trivium/fonti/ is the source of names, hierarchy and author's descriptions.
    English and Latin labels, translations of the descriptions, Wikidata matches, FORD bridges
    and links to Dubium are editorial additions written in this file.
LA: Tabula in trivium/fonti/ fons est nominum, hierarchiae et descriptionum auctoris. Tituli
    Anglici et Latini, versiones descriptionum, consensiones Wikidata, pontes ad FORD et nexus
    ad Dubium additamenta editoria sunt in hac tabula scripta.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "trivium"
SNAPSHOT = ROOT / "fonti" / "categorie-criptasemantica-2026-11-11.json"
OUT = ROOT / "trivium.ttl"
RETRIEVED = "2026-11-11"

# EN: English and Latin labels for every public category, keyed by slug.
# LA: Tituli Anglici et Latini cuiusque categoriae publicae, per clavem (slug).
LABELS = {
    "antropologia": ("Anthropology", "Anthropologia"), "arti-marziali": ("Martial arts", "Artes martiales"),
    "astronomia": ("Astronomy", "Astronomia"), "autori": ("Authors", "Auctores"), "buddismo": ("Buddhism", "Buddhismus"),
    "canali": ("Channels", "Canales"), "comunismo-digitale": ("Digital communism", "Communismus digitalis"),
    "dialettica": ("Dialectic", "Dialectica"), "antropologia-dialettica": ("Anthropology", "Anthropologia"),
    "antropologia-culturale": ("Cultural anthropology", "Anthropologia culturalis"), "etnologia": ("Ethnology", "Ethnologia"),
    "arte-e-tecnica": ("Art and technics", "Ars et technica"), "curatela": ("Curatorship", "Curatela"),
    "filosofia-della-tecnica": ("Philosophy of technics", "Philosophia technicae"), "storia-dellarte": ("Art history", "Historia artis"),
    "arte-contemporanea": ("Contemporary art", "Ars hodierna"), "arte-medievale": ("Medieval art", "Ars mediaevalis"),
    "tecnologia": ("Technology", "Technologia"), "epistemologia": ("Epistemology", "Epistemologia"),
    "cosmologia": ("Cosmology", "Cosmologia"), "filosofia-della-scienza": ("Philosophy of science", "Philosophia scientiae"),
    "ermeneutica": ("Hermeneutics", "Hermeneutica"), "estetica": ("Aesthetics", "Aesthetica"), "critica-darte": ("Art criticism", "Critica artis"),
    "femminismo": ("Feminism", "Feminismus"), "fenomenologia": ("Phenomenology", "Phaenomenologia"),
    "studi-husserliani": ("Husserl studies", "Studia Husserliana"), "filosofia-politica": ("Political philosophy", "Philosophia politica"),
    "imperialismo": ("Imperialism", "Imperialismus"), "filosofia-teoretica": ("Theoretical philosophy", "Philosophia theoretica"),
    "filosofia-della-differenza": ("Philosophy of difference", "Philosophia differentiae"),
    "filosofia-della-matematica": ("Philosophy of mathematics", "Philosophia mathematicae"),
    "filosofia-della-musica": ("Philosophy of music", "Philosophia musicae"), "filosofia-e-societa": ("Philosophy and society", "Philosophia et societas"),
    "gnoseologia": ("Gnoseology", "Gnoseologia"), "gnoseologia-metafisica": ("Metaphysical gnoseology", "Gnoseologia metaphysica"),
    "informatica": ("Computer science", "Informatica"), "architettura-dellinformazione": ("Information architecture", "Architectura informationis"),
    "architettura-dellinformazione-filosofica": ("Philosophical information architecture", "Architectura informationis philosophica"),
    "big-data": ("Big data", "Data ingentia"), "intelligenza-artificiale": ("Artificial intelligence", "Intellegentia artificialis"),
    "machine-learning": ("Machine learning", "Disciplina machinalis"), "logica": ("Logic", "Logica"), "fondamenti": ("Foundations", "Fundamenta"),
    "fondamenti-della-matematica": ("Foundations of mathematics", "Fundamenta mathematicae"),
    "materialismo-dialettico": ("Dialectical materialism", "Materialismus dialecticus"), "analisi-logistica": ("Logistical analysis", "Analysis logistica"),
    "analisi-strategica": ("Strategic analysis", "Analysis strategica"), "critica-delleconomia-politica": ("Critique of political economy", "Critica oeconomiae politicae"),
    "lavoro": ("Labour", "Labor"), "sindacato": ("Trade union", "Collegium opificum"), "lotta-di-classe": ("Class struggle", "Certamen classium"),
    "teoria-critica": ("Critical theory", "Theoria critica"), "teoria-marxista": ("Marxist theory", "Theoria Marxiana"),
    "materialismo-storico": ("Historical materialism", "Materialismus historicus"),
    "storia-del-movimento-operaio": ("History of the labour movement", "Historia motus opificum"), "metafisica": ("Metaphysics", "Metaphysica"),
    "cibernetica": ("Cybernetics", "Cybernetica"), "teoria-dei-sistemi": ("Systems theory", "Theoria systematum"),
    "metafisica-generale": ("General metaphysics", "Metaphysica generalis"), "filosofia-prima": ("First philosophy", "Philosophia prima"),
    "ontologia": ("Ontology", "Ontologia"), "ontologia-formale": ("Formal ontology", "Ontologia formalis"),
    "ontologia-teoretica": ("Theoretical ontology", "Ontologia theoretica"), "ontologia-e-semantica": ("Ontology and semantics", "Ontologia et semantica"),
    "politica": ("Politics", "Politica"), "geopolitica": ("Geopolitics", "Geopolitica"), "relazioni-internazionali": ("International relations", "Relationes internationales"),
    "polemologia": ("Polemology", "Polemologia"), "politica-italiana": ("Italian politics", "Politica Italica"), "politica-estera": ("Foreign policy", "Politica externa"),
    "politiche-istituzionali": ("Institutional policies", "Politicae institutionales"), "politiche-normative": ("Regulatory policies", "Politicae normativae"),
    "scienze-politiche": ("Political science", "Scientiae politicae"), "studi-postcoloniali": ("Postcolonial studies", "Studia postcolonialia"),
    "psicanalisi": ("Psychoanalysis", "Psychoanalysis"), "psicologia": ("Psychology", "Psychologia"), "neuroscienze": ("Neuroscience", "Neuroscientiae"),
    "neuroscienze-cognitive": ("Cognitive neuroscience", "Neuroscientiae cognitivae"), "psicologia-sociale": ("Social psychology", "Psychologia socialis"),
    "psicologia-dello-sviluppo": ("Developmental psychology", "Psychologia evolutionis"), "scienze-cognitive": ("Cognitive science", "Scientiae cognitivae"),
    "architetture-neurali": ("Neural architectures", "Architecturae neurales"), "spiritualismo": ("Spiritualism", "Spiritualismus"),
    "storia": ("History", "Historia"), "globalizzazione-storia": ("Globalisation", "Globalizatio"), "storia-contemporanea": ("Contemporary history", "Historia aetatis nostrae"),
    "storia-del-pensiero-matematico": ("History of mathematical thought", "Historia cogitationis mathematicae"), "storia-dellafrica": ("History of Africa", "Historia Africae"),
    "storia-della-sardegna": ("History of Sardinia", "Historia Sardiniae"), "storia-delle-religioni": ("History of religions", "Historia religionum"),
    "storia-dellessere": ("History of being", "Historia essendi"), "storia-della-filosofia": ("History of philosophy", "Historia philosophiae"),
    "autori-storia-della-filosofia": ("Authors", "Auctores"), "heidegger": ("Heidegger", "Heidegger"), "nietzsche": ("Nietzsche", "Nietzsche"),
    "filosofia-antica": ("Ancient philosophy", "Philosophia antiqua"), "filosofia-contemporanea": ("Contemporary philosophy", "Philosophia aetatis nostrae"),
    "filosofia-italiana": ("Italian philosophy", "Philosophia Italica"), "filosofia-moderna": ("Modern philosophy", "Philosophia recentior"),
    "storia-della-filosofia-contemporanea": ("History of contemporary philosophy", "Historia philosophiae aetatis nostrae"),
    "epistemologia-e-metafisica": ("Epistemology and metaphysics", "Epistemologia et metaphysica"), "etica": ("Ethics", "Ethica"),
    "etica-e-societa": ("Ethics and society", "Ethica et societas"), "filosofia-orientale": ("Eastern philosophy", "Philosophia orientalis"),
    "geografia": ("Geography", "Geographia"), "biologia": ("Biology", "Biologia"), "evoluzionismo": ("Evolutionism", "Evolutionismus"),
    "evoluzione": ("Evolution", "Evolutio"), "genetica": ("Genetics", "Genetica"), "scienze-biologiche": ("Biological sciences", "Scientiae biologicae"),
    "fisica": ("Physics", "Physica"), "fisica-teorica": ("Theoretical physics", "Physica theoretica"), "globalizzazione": ("Globalisation", "Globalizatio"),
    "giainismo": ("Jainism", "Iainismus"), "grammatica": ("Grammar", "Grammatica"), "filologia": ("Philology", "Philologia"),
    "filosofia-del-linguaggio": ("Philosophy of language", "Philosophia linguae"), "letteratura": ("Literature", "Litterae"),
    "saggistica": ("Essay writing", "Scripta disputatoria"), "saggistica-contemporanea": ("Contemporary essay writing", "Scripta disputatoria aetatis nostrae"),
    "linguistica": ("Linguistics", "Linguistica"), "linguistica-storica": ("Historical linguistics", "Linguistica historica"),
    "psicolinguistica-linguistica": ("Psycholinguistics", "Psycholinguistica"),
    "psicolinguistica-evoluzionistica-psicolinguistica-linguistica": ("Evolutionary psycholinguistics", "Psycholinguistica evolutionis"),
    "mitologia": ("Mythology", "Mythologia"), "mito": ("Myth", "Mythus"), "miti-filosofici": ("Philosophical myths", "Mythi philosophici"),
    "semantica": ("Semantics", "Semantica"), "studi-classici": ("Classical studies", "Studia classica"),
    "www-semantico": ("World-wide semantic web", "Rete semantica universalis"), "metaversi": ("Metaverses", "Metaversa"), "web-semantico": ("Semantic web", "Rete semantica"),
    "logica-matematica": ("Mathematical logic", "Logica mathematica"), "matematica": ("Mathematics", "Mathematica"),
    "storia-della-matematica": ("History of mathematics", "Historia mathematicae"), "metafisica-gioco": ("Metaphysics of play", "Metaphysica ludi"),
    "illusione-messa-in-gioco": ("Illusion (put into play)", "Illusio (in ludum missa)"), "motore-ermeneutico": ("Hermeneutic search engine", "Machina quaerendi hermeneutica"),
    "musica": ("Music", "Musica"), "biomusicologia": ("Biomusicology", "Biomusicologia"), "notizie": ("News", "Nuntii"),
    "conflitti-contemporanei": ("Contemporary conflicts", "Conflictus aetatis nostrae"), "cronaca": ("Chronicle", "Chronica"),
    "data-journalism": ("Data journalism", "Diurnarium datorum"), "dossier-nato-e-difesa": ("NATO and defence dossier", "Fasciculus de NATO et defensione"),
    "inchieste": ("Investigations", "Inquisitiones"), "politica-interna": ("Domestic politics", "Politica interna"), "territorio-notizie": ("Territory", "Territorium"),
    "umbria": ("Umbria", "Umbria"), "ontologia-fondamentale": ("Fundamental ontology", "Ontologia fundamentalis"), "prodotti": ("Products", "Merces"),
    "profili": ("Profiles", "Vitae"), "programmazione-filosofica": ("Philosophical programming", "Programmatio philosophica"),
    "psicolinguistica": ("Psycholinguistics", "Psycholinguistica"), "psicolinguistica-evoluzionistica": ("Evolutionary psycholinguistics", "Psycholinguistica evolutionis"),
    "recensioni": ("Reviews", "Recensiones"), "retorica": ("Rhetoric", "Rhetorica"), "cultura": ("Culture", "Cultura"),
    "cultura-e-tradizione": ("Culture and tradition", "Cultura et traditio"), "istituzioni-culturali": ("Cultural institutions", "Instituta culturalia"),
    "polemiche-culturali": ("Cultural controversies", "Controversiae culturales"), "studi-culturali": ("Cultural studies", "Studia culturalia"),
    "cultura-e-societa": ("Culture and society", "Cultura et societas"), "arte": ("Art", "Ars"), "mostre-ed-eventi": ("Exhibitions and events", "Exhibitiones et eventus"),
    "societa-algoritmica": ("Algorithmic society", "Societas algorithmica"), "territorio": ("Territory", "Territorium"), "ecologia": ("Ecology", "Oecologia"),
    "economia": ("Economics", "Oeconomia"), "economia-politica": ("Political economy", "Oeconomia politica"), "finanza": ("Finance", "Res nummaria"),
    "industria": ("Industry", "Industria"), "macroeconomia": ("Macroeconomics", "Macrooeconomia"), "analisi-macroeconomica": ("Macroeconomic analysis", "Analysis macrooeconomica"),
    "mercato-dellarte": ("Art market", "Mercatus artis"), "pagamenti": ("Payments", "Solutiones"), "sviluppo": ("Development", "Progressus oeconomicus"),
    "giurisprudenza": ("Jurisprudence", "Iurisprudentia"), "diritti": ("Rights", "Iura"), "diritti-sociali": ("Social rights", "Iura socialia"),
    "diritti-umani": ("Human rights", "Iura humana"), "diritto": ("Law", "Ius"), "beni-culturali": ("Cultural heritage", "Bona culturalia"),
    "costituzione": ("Constitution", "Constitutio"), "innovazione-e-tecnologia": ("Innovation and technology", "Novatio et technologia"),
    "futuro-digitale": ("Digital future", "Futurum digitale"), "poietica": ("Poietics", "Poietica"), "scienze-sociali": ("Social sciences", "Scientiae sociales"),
    "sociologia": ("Sociology", "Sociologia"), "analisi-materialista": ("Materialist analysis", "Analysis materialistica"), "classi-sociali": ("Social classes", "Classes sociales"),
    "conflitti-sociali": ("Social conflicts", "Conflictus sociales"), "sociologia-industriale": ("Industrial sociology", "Sociologia industrialis"),
    "sociologia-del-digitale": ("Sociology of the digital", "Sociologia rerum digitalium"), "transumanesimo": ("Transhumanism", "Transhumanismus"),
    "senza-categoria": ("Uncategorised", "Sine categoria"), "sinergie": ("Synergies", "Synergiae"), "storia-delle-scienze": ("History of science", "Historia scientiarum"),
    "studi-accademici": ("Academic studies", "Studia academica"), "teatro": ("Theatre", "Theatrum"),
}

# EN: Translations of the author's descriptions. The Italian text stays verbatim as the first note.
# LA: Versiones descriptionum auctoris. Textus Italicus ut nota prima ad verbum manet.
NOTES = {
    "dialettica": ("An art born of the contest in discourse: the technique of dialogue is still the guiding thread that, through mastery of analysis and synthesis, leads rational inquiry across the territories of logic, history and cybernetics, to lift the veil that darkens the knowledge of the world.",
                   "Ars ex certamine sermonis orta: ars dialogi adhuc filum ductorium est quod, peritia analysis et synthesis, inquisitionem rationalem per regiones logicae, historiae et cyberneticae ducit, ut velum quod cognitionem mundi obscurat tollat."),
    "grammatica": ("Starting from the vast Hellenistic rhizome of the grammatikē technē, the total art of reading, exegesis, care of texts and understanding of language, the category 'grammar' actualises the field of the 'letter', projected onto the cognitive and technological horizon of our time. Grammar is thus the synthetic womb of all the branches that flowered from that ancient drive to decode the world: the discipline that raises to science writings and arche-writings, texts and hypertexts, tongues and languages, types and characters, signs and communications.",
                   "A vastissimo rhizomate Hellenistico artis grammaticae, artis totius legendi, interpretandi, textus curandi et sermonem intellegendi, categoria 'grammatica' campum 'litterae' in horizonte cognitivo et technologico aetatis nostrae renovat. Grammatica igitur est sinus syntheticus omnium ramorum ex illo antiquo impetu mundum decodificandi natorum: disciplina quae scripturas et archiscripturas, textus et hypertextus, linguas et sermones, typos et characteres, signa et communicationes ad scientiam evehit."),
    "retorica": ("Crown of the classical trivium and pragmatic summit of language, the category 'rhetoric' holds the art of persuasion and the architecture of power, shaping itself as the forge of social action in which discourse becomes law, administration and strategy. It is the domain where the word moulds masses and borders, reaching into the intimate engineering of thought and becoming a driving force able to govern and reprogram human reality.",
                 "Corona trivii classici et vertex pragmaticus sermonis, categoria 'rhetorica' artem persuadendi et architecturam potestatis complectitur, ut fabrica actionis socialis in qua sermo fit lex, administratio et consilium. Est regio in qua verbum multitudines et fines format, usque ad intimam machinationem cogitationis pervenit et vis movens fit quae res humanas regere et reformare potest."),
    "matematica": ("Art of recollection through beings that mediate between the sensible and the intelligible, language of a nature that does not create and is created, a priori study of space and time, or science of imagination and of the construction of meanings, opposite and complementary pole of metaphysics: mathematics has always been, and still is, the lens that expands and details contemplative enjoyment.",
                   "Ars reminiscentiae per entia quae inter sensibile et intellegibile mediant, lingua naturae quae non creat et creatur, studium a priori spatii et temporis, vel scientia imaginationis et constructionis significationum, polus oppositus et complementarius metaphysicae: mathematica semper fuit et adhuc est lens quae fruitionem contemplativam amplificat et distinguit."),
    "geografia": ("The most general discipline for aspiring to the mapping and measurement of the whole sublunar cosmos, of the Earth, matrix of being-there.",
                  "Disciplina generalissima ad totum cosmum sublunarem, Terram, matricem exsistentiae, describendum et metiendum."),
    "astronomia": ("The most general discipline for aspiring to the mapping and measurement of the whole ethereal cosmos, of the Sky, homeland of desire.",
                   "Disciplina generalissima ad totum cosmum aethereum, Caelum, patriam desiderii, describendum et metiendum."),
    "musica": ("Art of all arts and science of all sciences, wellspring of Western poetry and technics, appearance of the will as will: music is the fundamental metaphysical activity of the human being who dwells on the Earth.",
               "Ars omnium artium et scientia omnium scientiarum, fons poesis et technicae occidentalis, species voluntatis ut voluntatis: musica est actio metaphysica fundamentalis hominis Terram incolentis."),
    "autori": ("The community of the Cripta Semantica.", "Communitas Cryptae Semanticae."),
    "recensioni": ("Critical examinations of works.", "Examina critica operum."),
    "prodotti": ("Goods and experiences from the community of the Cripta Semantica, for every need of consumption and consciousness.", "Merces et experientiae e communitate Cryptae Semanticae, ad omnem consumptionis et conscientiae necessitatem."),
    "profili": ("Biographies, curricula and stories of the people who compose or inspire the community of the Cripta Semantica.", "Vitae, curricula et historiae hominum qui communitatem Cryptae Semanticae constituunt vel inspirant."),
    "canali": ("The multichannel network of the Cripta Semantica, between Cripta Filosofica, FINAI and collaborations for content of various kinds.", "Rete multicanalis Cryptae Semanticae, inter Cryptam Philosophicam, FINAI et societates ad materiam varii generis."),
    "sinergie": ("Support, affiliation and partnership activities with the Cripta Semantica.", "Actiones sustentationis, affiliationis et societatis cum Crypta Semantica."),
    "ontologia-fondamentale": ("\"Do we today have an answer to the question of what we properly mean by the word 'being'? Not at all. It is therefore necessary to raise anew the question of the meaning of being.\"", "\"Habemusne hodie responsum ad quaestionem quid proprie voce 'ens' intellegamus? Minime. Necesse est igitur quaestionem de sensu essendi iterum ponere.\""),
    "motore-ermeneutico": ("Algorithmics of search and interpretation.", "Algorithmica quaerendi et interpretandi."),
    "programmazione-filosofica": ("Literate programming lets the flow of coding be tuned to the flow of consciousness and offers unprecedented opportunities in the age of hypertexts: can that paradigm be pushed to evolve towards a philosophical programming?", "Programmatio litterata fluxum codificandi cum fluxu conscientiae concordare sinit et in aetate hypertextuum occasiones novas praebet: potestne illud paradigma ad programmationem philosophicam evolvi?"),
    "www-semantico": ("The World Wide Web, the great world-wide network, as a hyper-library devoted to storing and socialising human and machine semantic capital.", "Rete universalis, Magna Rete Mundana, ut hyperbibliotheca ad capitale semanticum humanum et machinale condendum et communicandum."),
    "comunismo-digitale": ("Initiatives, activities and investments in the field of webfare and of the redistribution of cognitive wealth.", "Incepta, actiones et collocationes in campo 'webfare' et redistributionis divitiarum cognitivarum."),
    "metafisica-gioco": ("\"Play is given also, indeed precisely, where there is no horizon thematically defined by the for-itself of a subjectivity, and where there are no subjects behaving playfully.\"", "\"Ludus datur etiam, immo praecipue, ubi nullus horizon a 'pro se' subiectivitatis thematice definitur, et ubi nulla subiecta ludice se gerunt.\""),
    "etica": ("What is to be done?", "Quid faciendum?"),
    "arti-marziali": ("When martial practice becomes art and spirit.", "Cum exercitatio martialis ars et spiritus fit."),
    "teatro": ("Theatre is the place of vision, of the vision of the divine, and the actor is nothing but a naked mask before their own nothingness. Theatre, from the classical to the post-dramatic age, is thereby assigned the space in which the formation and enjoyment of initiatory paths unfold.", "Theatrum est locus visionis, visionis divini, et histrio nihil est nisi persona nuda coram sua nullitate. Ita theatro, ab aevo classico ad postdramaticum, spatium tribuitur in quo formatio et fruitio itinerum initiationis explicantur."),
    "notizie": ("The notion announces itself to the apprentice by means of the news.", "Notio tironi per nuntium se annuntiat."),
}

# EN: Wikidata items verified on 2026-11-11 with the query recorded in FORMALIZZAZIONE.md. closeMatch, never exactMatch.
# LA: Res Wikidata die 2026-11-11 probatae quaestione in FORMALIZZAZIONE.md servata. closeMatch, numquam exactMatch.
WIKIDATA = {
    "dialettica": "Q9453", "grammatica": "Q8091", "retorica": "Q81009", "logica": "Q8078", "geografia": "Q1071", "astronomia": "Q333",
    "matematica": "Q395", "musica": "Q638", "etica": "Q9465", "antropologia": "Q23404", "antropologia-dialettica": "Q23404",
    "epistemologia": "Q9471", "metafisica": "Q35277", "metafisica-generale": "Q35277", "ontologia": "Q44325", "fenomenologia": "Q179235",
    "ermeneutica": "Q102686", "estetica": "Q35986", "filosofia-del-linguaggio": "Q484761", "filosofia-politica": "Q179805",
    "filosofia-della-scienza": "Q59115", "filosofia-della-matematica": "Q180536", "gnoseologia": "Q2560959", "filologia": "Q40634",
    "economia": "Q159810", "giurisprudenza": "Q4932206", "fisica": "Q413", "biologia": "Q420", "intelligenza-artificiale": "Q11660",
    "cibernetica": "Q123637", "buddismo": "Q748", "giainismo": "Q9232", "informatica": "Q21198", "teatro": "Q11635",
    "storia-delle-scienze": "Q201486", "psicolinguistica": "Q179488", "psicolinguistica-linguistica": "Q179488", "web-semantico": "Q54837",
    "storia-della-filosofia": "Q27654", "filosofia-teoretica": "Q2166096", "filosofia-della-tecnica": "Q5862034", "arte": "Q735",
    "geopolitica": "Q159385", "diritto": "Q7748", "notizie": "Q38926", "recensioni": "Q265158", "semantica": "Q39645", "linguistica": "Q8162",
    "letteratura": "Q8242", "storia": "Q309", "psicologia": "Q9418", "neuroscienze": "Q207011", "sociologia": "Q21201", "femminismo": "Q7252",
    "mitologia": "Q9134", "logica-matematica": "Q1166618", "materialismo-dialettico": "Q181207", "materialismo-storico": "Q190004",
    "transumanesimo": "Q194100", "ecologia": "Q7150", "genetica": "Q7162", "evoluzione": "Q1063", "finanza": "Q43015", "teoria-marxista": "Q7264",
    "teoria-dei-sistemi": "Q269699", "scienze-cognitive": "Q147638", "studi-culturali": "Q1143546", "relazioni-internazionali": "Q166542",
    "polemologia": "Q1367522", "studi-postcoloniali": "Q265425", "ontologia-formale": "Q1437388", "mito": "Q12827256", "saggistica": "Q27801",
    "storia-delle-religioni": "Q846742", "storia-dellarte": "Q50637", "arte-contemporanea": "Q186030", "arte-medievale": "Q3624153",
    "economia-politica": "Q47555", "macroeconomia": "Q39680", "diritti-umani": "Q8458", "costituzione": "Q7755", "big-data": "Q858810",
    "machine-learning": "Q2539", "architettura-dellinformazione": "Q845921", "metaversi": "Q2632041", "globalizzazione": "Q7181",
    "globalizzazione-storia": "Q7181", "imperialismo": "Q7260", "sindacato": "Q178790", "lavoro": "Q268378", "umbria": "Q1280",
    "filosofia-della-musica": "Q2092865", "tecnologia": "Q11016", "neuroscienze-cognitive": "Q1138951", "psicologia-sociale": "Q161272",
    "psicologia-dello-sviluppo": "Q175002", "storia-contemporanea": "Q186075", "filosofia-antica": "Q204100", "filosofia-moderna": "Q860746",
    "filosofia-contemporanea": "Q943303", "etnologia": "Q43455", "antropologia-culturale": "Q28598", "storia-della-matematica": "Q185264",
    "fondamenti-della-matematica": "Q833585", "industria": "Q8148", "sviluppo": "Q4530482", "politica-estera": "Q181648",
    "storia-della-sardegna": "Q1516605", "spiritualismo": "Q2636432", "politica": "Q7163", "heidegger": "Q48301", "nietzsche": "Q9358",
}

# EN: Bridges to the FORD fields of Metrum. broadMatch: the Cripta category is read as narrower than, or within, the field.
# LA: Pontes ad disciplinas FORD partis Metrum. broadMatch: categoria Cryptae ut angustior vel intra campum legitur.
FORD = {
    "dialettica": ["6.3"], "grammatica": ["6.2"], "retorica": ["6.2"], "logica": ["6.3", "1.1"], "matematica": ["1.1"], "musica": ["6.4"],
    "astronomia": ["1.3"], "geografia": ["1.5"], "etica": ["6.3"], "antropologia": ["5.4"], "antropologia-dialettica": ["5.4"],
    "epistemologia-e-metafisica": ["6.3"], "filosofia-orientale": ["6.3"], "buddismo": ["6.3"], "giainismo": ["6.3"], "ontologia-fondamentale": ["6.3"],
    "teatro": ["6.4"], "storia-delle-scienze": ["6.1"], "psicolinguistica": ["5.1"], "psicolinguistica-linguistica": ["5.1"], "www-semantico": ["1.2"],
    "motore-ermeneutico": ["1.2"], "programmazione-filosofica": ["1.2", "6.3"], "metafisica-gioco": ["6.3"], "epistemologia": ["6.3"],
    "filosofia-della-scienza": ["6.3"], "cosmologia": ["1.3"], "informatica": ["1.2"], "intelligenza-artificiale": ["1.2"], "big-data": ["1.2"],
    "machine-learning": ["1.2"], "psicologia": ["5.1"], "neuroscienze": ["3.1"], "scienze-cognitive": ["5.1"], "storia": ["6.1"],
    "storia-della-filosofia": ["6.3"], "politica": ["5.6"], "geopolitica": ["5.6"], "economia": ["5.2"], "finanza": ["5.2"], "giurisprudenza": ["5.5"],
    "diritto": ["5.5"], "sociologia": ["5.4"], "fisica": ["1.3"], "biologia": ["1.6"], "genetica": ["1.6"], "ecologia": ["1.6"], "filologia": ["6.2"],
    "linguistica": ["6.2"], "letteratura": ["6.2"], "semantica": ["6.2"], "studi-classici": ["6.2"], "mitologia": ["6.3"], "arte": ["6.4"],
    "storia-dellarte": ["6.4"], "estetica": ["6.3"], "fenomenologia": ["6.3"], "ermeneutica": ["6.3"], "ontologia": ["6.3"], "metafisica": ["6.3"],
    "metafisica-generale": ["6.3"], "logica-matematica": ["1.1"], "cibernetica": ["1.2", "2.2"], "tecnologia": ["2.11"], "scienze-sociali": ["5.9"],
    "femminismo": ["5.4"], "psicanalisi": ["5.1"], "storia-delle-religioni": ["6.3"], "filosofia-politica": ["6.3"], "filosofia-del-linguaggio": ["6.3"],
}

# EN: Readings that connect a category to a concept of Dubium. They are editorial; the formalisation explains each.
# LA: Lectiones quae categoriam cum notione Dubii conectunt. Editoriae sunt; formalizatio singulas explicat.
DUBIUM = {
    "ontologia-fondamentale": ["ontologiaFondamentale", "problemaSensoEssere"], "ontologia": ["ontologiaEnte"], "ontologia-formale": ["ontologiaFormale"],
    "ontologia-e-semantica": ["ontologiaInformatica", "significato"], "fenomenologia": ["ontologiaFenomenologica"], "metafisica": ["metafisicaOccidentale"],
    "metafisica-generale": ["metafisicaOccidentale"], "filosofia-prima": ["ontologiaFondamentale"], "logica": ["strutturaLogica", "giudizio"],
    "filosofia-del-linguaggio": ["enunciato"], "semantica": ["significato"], "grammatica": ["scrittura", "testo"], "dialettica": ["praticaDialogica", "reminiscenza"],
    "retorica": ["condivisione", "esplicitezza"], "www-semantico": ["web", "capitaleSemantico"], "web-semantico": ["ontologiaInformatica", "organizzazioneSemantica"],
    "informatica": ["macchinaConcreta"], "intelligenza-artificiale": ["macchinaAstratta"], "storia-dellessere": ["sensoEssere", "pensieroOccidentale"],
    "storia-della-filosofia": ["filosofia", "tradizioneTestuale"], "filosofia-antica": ["esordioGreco"], "heidegger": ["problemaEssere"],
    "epistemologia": ["teoria", "scienzaTrasformazione"], "gnoseologia": ["concettualizzazione"], "filosofia-della-matematica": ["quantificazioneOntologica"],
    "programmazione-filosofica": ["codiceSviluppo", "iperscritturaConsapevole"], "notizie": ["articolo"], "recensioni": ["articolo"],
    "canali": ["criptaSito"], "autori": ["esserci"], "matematica": ["reminiscenza"], "cibernetica": ["macchinaAstratta"],
}

GENERI = {"notizie", "recensioni", "autori", "profili", "prodotti", "sinergie", "canali", "senza-categoria"}
PROGRAMMI = {"comunismo-digitale", "www-semantico", "motore-ermeneutico", "programmazione-filosofica", "metafisica-gioco", "studi-accademici"}
TRIVIO = ["grammatica", "dialettica", "retorica"]
QUADRIVIO = ["matematica", "musica", "astronomia", "geografia"]

STANZE = [
    ("stanza-dello-smarrimento", "Stanza dello Smarrimento", "Room of Bewilderment", "Cella Errationis", "https://criptasemantica.it/",
     "Pagina di errore del sito: un labirinto senza uscite dove attende il Minotauro. Chi si perde è invitato a continuare la ricerca in altro modo.",
     "Error page of the site: a labyrinth without exits where the Minotaur waits. Whoever gets lost is invited to continue the search another way.",
     "Pagina erroris situs: labyrinthus sine exitu ubi Minotaurus exspectat. Qui erravit alia via quaerere invitatur."),
    ("stanza-dei-canali", "Stanza dei Canali", "Room of Channels", "Cella Canalium", "https://criptasemantica.it/progetto/canali/",
     "Portuno e le Naiadi governano un labirinto ricorsivo che allude alla teoria dell'informazione: i canali fisici che trasportano i dati dell'iperscrittura.",
     "Portunus and the Naiads rule a recursive labyrinth that alludes to information theory: the physical channels that carry the data of hyperwriting.",
     "Portunus et Naiades labyrinthum recursivum regunt qui theoriam informationis significat: canales physici qui data hyperscripturae vehunt."),
    ("stanza-di-finai", "Stanza di FINAI", "Room of FINAI", "Cella FINAI", "https://criptasemantica.it/chi-siamo/finai/",
     "Un satiro bionico su un trono di calcolo governa i flussi dei dati: la stanza di chi progetta e codifica il sito.",
     "A bionic satyr on a computing throne governs the data flows: the room of the one who designs and codes the site.",
     "Satyrus bionicus in solio computatorio fluxus datorum regit: cella eius qui situm molitur et codificat."),
    ("stanza-della-rosa-blu", "Stanza della Rosa Blu", "Room of the Blue Rose", "Cella Rosae Caeruleae", "https://criptasemantica.it/chi-siamo/alessandro-sevardi/",
     "Una tomba colma di rose blu fra tombe vuote: la stanza della Cripta Filosofica e della comunità tombale da cui nasce la semantica della Cripta.",
     "A tomb full of blue roses among empty tombs: the room of the Cripta Filosofica and of the sepulchral community from which the semantics of the Cripta is born.",
     "Sepulcrum rosis caeruleis plenum inter sepulcra vacua: cella Cryptae Philosophicae et communitatis sepulcralis unde semantica Cryptae nascitur."),
    ("stanza-del-laboratorio-algoritmico", "Stanza del Laboratorio Algoritmico", "Room of the Algorithmic Laboratory", "Cella Laboratorii Algorithmici", "https://criptasemantica.it/chi-siamo/",
     "Il Dottore opera su un mainframe esoterico mentre il Beffardo gli sussurra all'orecchio: la stanza del metodo, dello schedario cooperativo e della scienza libera.",
     "The Doctor operates an esoteric mainframe while the Mocker whispers in his ear: the room of method, of the cooperative card index and of free science.",
     "Doctor machinam arcanam tractat dum Irrisor in aurem susurrat: cella methodi, schedarii communis et scientiae liberae."),
    ("stanza-dellinterpretazione", "Stanza dell'Interpretazione", "Room of Interpretation", "Cella Interpretationis", "https://criptasemantica.it/chi-siamo/finai/",
     "Nominata come portale dalla stanza di FINAI. Il suo contenuto non è ancora pubblicato.",
     "Named as a portal from the room of FINAI. Its content is not yet published.",
     "Ut porta e cella FINAI nominata. Materia eius nondum edita est."),
    ("stanza-della-giustizia", "Stanza della Giustizia", "Room of Justice", "Cella Iustitiae", "https://criptasemantica.it/chi-siamo/",
     "Nominata come portale dalla stanza del Laboratorio Algoritmico. Il suo contenuto non è ancora pubblicato.",
     "Named as a portal from the room of the Algorithmic Laboratory. Its content is not yet published.",
     "Ut porta e cella Laboratorii Algorithmici nominata. Materia eius nondum edita est."),
    ("stanza-degli-articoli", "Stanza degli Articoli", "Room of Articles", "Cella Articulorum", "https://criptasemantica.it/articoli/",
     "Vulcano forgia artefatti nell'officina-cripta: la stanza da cui si raggiunge la rete degli articoli, intesi come articolazioni di un'apertura di senso.",
     "Vulcan forges artefacts in the crypt-workshop: the room from which the network of articles is reached, understood as articulations of an opening of sense.",
     "Vulcanus artefacta in officina-crypta cudit: cella unde rete articulorum attingitur, qui ut articulationes aperturae sensus intelleguntur."),
    ("stanza-del-progetto", "Stanza del Progetto", "Room of the Project", "Cella Consilii", "https://criptasemantica.it/progetto/",
     "Prometeo benedice la Cripta: la stanza dell'ontologia del progetto, della gettatezza e del fondamento assente che fonda.",
     "Prometheus blesses the Cripta: the room of the ontology of the project, of thrownness and of the absent ground that grounds.",
     "Prometheus Cryptam benedicit: cella ontologiae consilii, iactus et fundamenti absentis quod fundat."),
]

HEADER = """@prefix trv: <https://aenigma.criptasemantica.it/trivium#> .
@prefix dub: <https://aenigma.criptasemantica.it/dubium#> .
@prefix mtr: <https://aenigma.criptasemantica.it/metrum#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema: <https://schema.org/> .
@prefix vann: <http://purl.org/vocab/vann/> .
@prefix wd: <http://www.wikidata.org/entity/> .
@base <https://aenigma.criptasemantica.it/trivium#> .

# EN: Trivium names the arts and disciplines through which the Cripta Semantica articulates its hypertext. The
#     source is the public taxonomy of the site; the module gives each category a stable IRI, three labels,
#     its place in the hierarchy and, where verified, a correspondence to Wikidata and a bridge to the FORD fields.
# LA: Trivium artes et disciplinas nominat per quas Crypta Semantica hypertextum suum articulat. Fons est taxonomia
#     publica situs; pars quaeque categoriae IRI stabile, tres titulos, locum in hierarchia et, ubi probatum est,
#     consensionem cum Wikidata et pontem ad disciplinas FORD tribuit.
# EN: This file is generated by tools/trivium_from_taxonomy.py. Edit the generator, then regenerate.
# LA: Haec tabula a tools/trivium_from_taxonomy.py gignitur. Generatorem muta, deinde regenera.

<https://aenigma.criptasemantica.it/trivium#> a owl:Ontology ;
    owl:versionIRI <https://aenigma.criptasemantica.it/trivium#v0.1.0> ;
    owl:versionInfo "0.1.0" ;
    dcterms:isPartOf <https://aenigma.criptasemantica.it/aenigma#> ;
    vann:preferredNamespacePrefix "trv" ;
    vann:preferredNamespaceUri "https://aenigma.criptasemantica.it/trivium#" ;
    rdfs:label "Trivium. Le arti e le discipline della Cripta Semantica"@it, "Trivium. The arts and disciplines of the Cripta Semantica"@en, "Trivium. Artes et disciplinae Cryptae Semanticae"@la ;
    dcterms:title "Trivium. Le arti e le discipline della Cripta Semantica"@it, "Trivium. The arts and disciplines of the Cripta Semantica"@en, "Trivium. Artes et disciplinae Cryptae Semanticae"@la ;
    rdfs:comment "Secondo modulo di Aenigma. Schemi SKOS delle discipline, dei generi editoriali, delle linee di programma e delle stanze del sito, con etichette in tre lingue, descrizioni d'autore, corrispondenze Wikidata verificate e ponti verso le discipline FORD e verso Dubium."@it,
                 "Second module of Aenigma. SKOS schemes of the disciplines, editorial genres, programme lines and rooms of the site, with labels in three languages, the author's descriptions, verified Wikidata correspondences and bridges to the FORD fields and to Dubium."@en,
                 "Secunda pars Aenigmatis. Schemata SKOS disciplinarum, generum editoriorum, linearum consilii et cellarum situs, cum titulis trium linguarum, descriptionibus auctoris, consensionibus Wikidata probatis et pontibus ad disciplinas FORD et ad Dubium."@la ;
    dcterms:description "Il nome riprende il trivio delle arti liberali: grammatica, dialettica e retorica sono le tre categorie fondanti del sito, affiancate da un quadrivio in cui la geografia prende il posto della geometria. Le altre categorie sono rami di questi tronchi o sezioni del lavoro editoriale."@it,
                        "The name recalls the trivium of the liberal arts: grammar, dialectic and rhetoric are the three founding categories of the site, flanked by a quadrivium in which geography takes the place of geometry. The other categories are branches of these trunks or sections of the editorial work."@en,
                        "Nomen trivium artium liberalium resumit: grammatica, dialectica et rhetorica tres categoriae situs fundamentales sunt, quibus quadrivium adiungitur in quo geographia locum geometriae tenet. Ceterae categoriae rami horum truncorum vel partes operis editorii sunt."@la ;
    dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;
    dcterms:creator <https://criptasemantica.it/chi-siamo/finai/>, <https://criptasemantica.it/chi-siamo/alessandro-sevardi/> ;
    dcterms:publisher <https://criptasemantica.it/> ;
    dcterms:source <https://criptasemantica.it/wp-json/wp/v2/categories> ;
    dcterms:issued "2026-11-11"^^xsd:date ;
    dcterms:modified "2026-11-11"^^xsd:date ;
    dcterms:language "it", "en", "la" ;
    rdfs:seeAlso <https://github.com/FINAI-Is-Not-An-Influencer/Aenigma>, <https://criptasemantica.it/articoli/> .

# EN: Four kinds of concept. A category is a discipline, an editorial genre or a programme line; a room is a place of the site.
# LA: Quattuor genera notionum. Categoria est disciplina, genus editorium vel linea consilii; cella est locus situs.
trv:Disciplina a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "disciplina"@it, "discipline"@en, "disciplina"@la ;
    rdfs:comment "Un'arte o un campo del sapere usato dal sito per ordinare gli articoli."@it, "An art or field of knowledge used by the site to order its articles."@en, "Ars vel campus scientiae quo situs articulos ordinat."@la .
trv:Genere a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "genere o sezione editoriale"@it, "editorial genre or section"@en, "genus vel pars editoria"@la .
trv:Programma a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "linea di programma"@it, "programme line"@en, "linea consilii"@la ;
    rdfs:comment "Un indirizzo di lavoro del progetto, non ancora una disciplina."@it, "A working direction of the project, not yet a discipline."@en, "Via operis consilii, nondum disciplina."@la .
trv:Stanza a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "stanza della Cripta"@it, "room of the Cripta"@en, "cella Cryptae"@la ;
    rdfs:comment "Un luogo allegorico del sito, descritto nelle immagini e nei testi delle sue pagine."@it, "An allegorical place of the site, described in the images and texts of its pages."@en, "Locus allegoricus situs, in imaginibus et textibus paginarum descriptus."@la .
[] a owl:AllDisjointClasses ; owl:members ( trv:Disciplina trv:Genere trv:Programma trv:Stanza ) .

trv:identificativoCategoria a owl:DatatypeProperty ; rdfs:domain skos:Concept ; rdfs:range xsd:integer ;
    rdfs:label "identificativo della categoria nel sito"@it, "category identifier on the site"@en, "index categoriae in situ"@la .

# EN: Schemes and collections.
# LA: Schemata et collectiones.
trv:discipline a skos:ConceptScheme ; skos:prefLabel "Arti e discipline della Cripta"@it, "Arts and disciplines of the Cripta"@en, "Artes et disciplinae Cryptae"@la ;
    rdfs:label "Arti e discipline della Cripta"@it, "Arts and disciplines of the Cripta"@en, "Artes et disciplinae Cryptae"@la ;
    dcterms:source <https://criptasemantica.it/wp-json/wp/v2/categories> .
trv:generi a skos:ConceptScheme ; skos:prefLabel "Generi e sezioni editoriali"@it, "Editorial genres and sections"@en, "Genera et partes editoriae"@la ;
    rdfs:label "Generi e sezioni editoriali"@it, "Editorial genres and sections"@en, "Genera et partes editoriae"@la .
trv:programmi a skos:ConceptScheme ; skos:prefLabel "Linee di programma"@it, "Programme lines"@en, "Lineae consilii"@la ;
    rdfs:label "Linee di programma"@it, "Programme lines"@en, "Lineae consilii"@la .
trv:stanze a skos:ConceptScheme ; skos:prefLabel "Stanze della Cripta"@it, "Rooms of the Cripta"@en, "Cellae Cryptae"@la ;
    rdfs:label "Stanze della Cripta"@it, "Rooms of the Cripta"@en, "Cellae Cryptae"@la .
trv:trivio a skos:Collection ; skos:prefLabel "Trivio"@it, "Trivium"@en, "Trivium"@la ; rdfs:label "Trivio"@it, "Trivium"@en, "Trivium"@la ;
    skos:closeMatch wd:Q205186 ; skos:member trv:grammatica, trv:dialettica, trv:retorica ;
    skos:scopeNote "Le tre arti del discorso. Sono le categorie con più articoli e il nome del modulo."@it, "The three arts of discourse. They are the categories with most articles and the name of the module."@en, "Tres artes sermonis. Categoriae pluribus articulis instructae et nomen partis."@la .
trv:quadrivio a skos:Collection ; skos:prefLabel "Quadrivio"@it, "Quadrivium"@en, "Quadrivium"@la ; rdfs:label "Quadrivio"@it, "Quadrivium"@en, "Quadrivium"@la ;
    skos:closeMatch wd:Q273822 ; skos:member trv:matematica, trv:musica, trv:astronomia, trv:geografia ;
    skos:scopeNote "Le quattro arti della misura. Il sito pone la geografia, «mappatura del cosmo sublunare», al posto della geometria."@it, "The four arts of measure. The site places geography, 'mapping of the sublunar cosmos', where geometry stood."@en, "Quattuor artes mensurae. Situs geographiam, «descriptionem cosmi sublunaris», loco geometriae ponit."@la .
"""


def lit(text, lang=None):
    # EN: Turtle forbids raw line breaks inside a quoted literal; descriptions from WordPress may contain them.
    # LA: Turtle lineas raptas intra litteram citatam vetat; descriptiones e WordPress eas continere possunt.
    text = " ".join(text.replace("\\", "\\\\").replace('"', '\\"').split())
    return f'"{text}"' + (f"@{lang}" if lang else "")


def tri(it, en, la):
    return f"{lit(it, 'it')}, {lit(en, 'en')}, {lit(la, 'la')}"


def main():
    data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    # EN: Two categories share the slug "logica"; the one nested under Dialettica gets the same suffix the site uses for Antropologia.
    # LA: Duae categoriae clavem "logica" communicant; ea quae sub Dialectica latet idem suffixum accipit quod situs Anthropologiae dat.
    by_id = {c["id"]: c for c in data["categories"]}
    repeated = {slug for slug in {c["slug"] for c in data["categories"]}
                if sum(1 for c in data["categories"] if c["slug"] == slug) > 1}
    categories = {}
    for c in data["categories"]:
        key = c["slug"]
        if key in repeated and c["parent"]:
            key = f"{key}-{by_id[c['parent']]['slug']}"
        if key in categories:
            raise SystemExit("Chiavi non univoche: " + key)
        categories[key] = c
    missing = sorted(c["slug"] for c in categories.values() if c["slug"] not in LABELS)
    if missing:
        raise SystemExit("Etichette mancanti: " + ", ".join(missing))

    def top(c):
        while c["parent"]:
            c = by_id[c["parent"]]
        return c

    def scheme_of(c):
        root = top(c)["slug"]
        if root in GENERI:
            return "generi", "Genere"
        if root in PROGRAMMI:
            return "programmi", "Programma"
        return "discipline", "Disciplina"

    out = [HEADER, "# EN: Categories of the site, one concept each. Notes in Italian are the author's; English and Latin are translations.\n# LA: Categoriae situs, singulae notiones. Notae Italicae auctoris sunt; Anglicae et Latinae versiones."]
    counts = {"discipline": 0, "generi": 0, "programmi": 0}
    def key_of(category):
        return next(k for k, v in categories.items() if v["id"] == category["id"])

    for key in sorted(categories):
        c = categories[key]
        slug = c["slug"]
        en, la = LABELS[slug]
        scheme, cls = scheme_of(c)
        counts[scheme] += 1
        lines = [f"trv:{key} a trv:{cls} ; skos:inScheme trv:{scheme} ; skos:notation {lit(slug)} ; trv:identificativoCategoria {c['id']} ;",
                 f"    skos:prefLabel {tri(c['name'], en, la)} ;",
                 f"    rdfs:label {tri(c['name'], en, la)} ;",
                 f"    dcterms:source <{c['link']}> ;"]
        if c["parent"]:
            lines.append(f"    skos:broader trv:{key_of(by_id[c['parent']])} ;")
        else:
            lines.append(f"    skos:topConceptOf trv:{scheme} ;")
        if c["description"].strip():
            note = [lit(c["description"], "it")]
            if slug in NOTES:
                note += [lit(NOTES[slug][0], "en"), lit(NOTES[slug][1], "la")]
            lines.append("    skos:scopeNote " + ", ".join(note) + " ;")
        if slug in WIKIDATA:
            lines.append(f"    skos:closeMatch wd:{WIKIDATA[slug]} ;")
        if key != slug:
            lines.append(f"    skos:related trv:{slug} ;")
        if slug in FORD:
            lines.append("    skos:broadMatch " + ", ".join(f"mtr:ford-{code.replace('.', '-')}" for code in FORD[slug]) + " ;")
        if slug in DUBIUM:
            lines.append("    skos:related " + ", ".join(f"dub:{name}" for name in DUBIUM[slug]) + " ;")
        lines[-1] = lines[-1][:-1] + "."
        out.append("\n".join(lines))
    for key in sorted(categories):
        c = categories[key]
        if not c["parent"]:
            out.append(f"trv:{scheme_of(c)[0]} skos:hasTopConcept trv:{key} .")
    out.append("\n# EN: Rooms of the Cripta, read from the images and texts of the site. Each note is an editorial reading.\n# LA: Cellae Cryptae, ex imaginibus et textibus situs lectae. Quaeque nota lectio editoria est.")
    for slug, it, en, la, source, nit, nen, nla in STANZE:
        out.append(f"trv:{slug} a trv:Stanza ; skos:inScheme trv:stanze ; skos:topConceptOf trv:stanze ; skos:notation {lit(slug)} ;\n"
                   f"    skos:prefLabel {tri(it, en, la)} ;\n    rdfs:label {tri(it, en, la)} ;\n"
                   f"    dcterms:source <{source}> ;\n    skos:scopeNote {tri(nit, nen, nla)} .")
        out.append(f"trv:stanze skos:hasTopConcept trv:{slug} .")
    out.append("trv:stanza-di-finai skos:related trv:canali, trv:autori, dub:criptaSito .\ntrv:stanza-della-rosa-blu skos:related dub:praticaDialogica, trv:canali .\n"
               "trv:stanza-del-laboratorio-algoritmico skos:related dub:notaIpertestuale, trv:motore-ermeneutico .\ntrv:stanza-degli-articoli skos:related dub:articolo .\n"
               "trv:stanza-del-progetto skos:related dub:progettoCripta, dub:gettatezza .\ntrv:stanza-dei-canali skos:related trv:canali .")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{OUT}: {len(categories)} categories ({counts}), {len(STANZE)} rooms, {len(WIKIDATA)} Wikidata matches, {len(FORD)} FORD bridges, {len(DUBIUM)} Dubium links")


if __name__ == "__main__":
    main()
