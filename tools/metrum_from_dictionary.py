#!/usr/bin/env python3
"""EN: Generate the Metrum module from the snapshot of the qualified protocol dictionary.
LA: Partem Metrum e descriptione protocollorum qualificatorum servata gigne.

EN: The schema, the principles, the scopes and the coverage values are written here.
    Protocols and FORD fields come from the JSON snapshot in metrum/fonti/.
LA: Forma, principia, ambitus et valores ambitus hic scribuntur. Protocolla et
    disciplinae FORD e tabula JSON in metrum/fonti/ sumuntur.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "metrum"
SNAPSHOT = ROOT / "fonti" / "protocolli-2026-11-11.json"
OUT = ROOT / "metrum.ttl"


def lit(text, lang=None):
    text = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{text}"' + (f"@{lang}" if lang else "")


def tri(labels):
    return ", ".join(lit(labels[k], k) for k in ("it", "en", "la"))


FAMILIES = {
    "ricezione": ("Ricezione", "Reception", "Receptio", "Citazioni e riusi che una fonte attribuisce a un'opera o a un soggetto.", "Citations and reuses that a source attributes to a work or an agent.", "Citationes et usus iterati quos fons operi vel subiecto tribuit."),
    "sedi": ("Sedi di pubblicazione", "Publication venues", "Sedes editionis", "Indicatori calcolati sulle riviste e sulle collane, non sui singoli lavori.", "Indicators computed on journals and series, not on single works.", "Indices de periodicis et seriebus computati, non de singulis operibus."),
    "apertura": ("Apertura e accesso", "Openness and access", "Apertura et aditus", "Quote e controlli su accesso aperto, metadati, identificatori e materiali.", "Shares and checks on open access, metadata, identifiers and materials.", "Partes et probationes de aditu aperto, notis datorum, indicibus et instrumentis."),
    "trasferimento": ("Trasferimento", "Transfer", "Translatio", "Riscontri dell'uso della ricerca fuori dall'accademia: policy, brevetti, adozioni.", "Evidence of research use outside academia: policy, patents, adoptions.", "Testimonia usus investigationis extra academiam: acta publica, diplomata, usus."),
    "dati": ("Dati", "Data", "Data", "Citazioni, riusi e contesto dei dati di ricerca.", "Citations, reuses and context of research data.", "Citationes, usus iterati et contextus datorum investigationis."),
    "software": ("Software", "Software", "Programmata", "Citazioni, riusi e riproducibilità del software di ricerca.", "Citations, reuses and reproducibility of research software.", "Citationes, usus iterati et reproductio programmatum investigationis."),
    "metodo": ("Metodo", "Method", "Methodus", "Repliche, preregistrazioni e descrizione dei contributi.", "Replications, preregistrations and contribution descriptions.", "Replicationes, praescriptiones et descriptio conlationum."),
    "umanistica": ("Saperi umanistici", "Humanities", "Studia humanitatis", "Monografie, edizioni critiche, traduzioni e ricezione argomentativa.", "Monographs, critical editions, translations and argumentative reception.", "Monographiae, editiones criticae, versiones et receptio argumentorum."),
    "sociale": ("Ricerca sociale", "Social research", "Investigatio socialis", "Adozioni didattiche e riscontri territoriali.", "Teaching adoptions and territorial evidence.", "Usus didactici et testimonia in communitate."),
    "clinica": ("Ricerca clinica", "Clinical research", "Investigatio clinica", "Recepimento in linee guida e trasferimento clinico.", "Uptake in guidelines and clinical transfer.", "Receptio in praeceptis clinicis et translatio clinica."),
    "tecnica": ("Tecnica", "Engineering", "Ars technica", "Verifiche in ambiente operativo e licenze d'uso.", "Operational verification and licences of use.", "Probationes in ambitu operandi et licentiae usus."),
    "agraria": ("Agraria", "Agricultural research", "Res agraria", "Validazioni in campo e trasferimenti veterinari.", "Field validations and veterinary transfer.", "Probationes in agro et translationes veterinariae."),
    "arti": ("Arti", "Arts", "Artes", "Esposizioni, esecuzioni e valutazioni curatoriali documentate.", "Documented exhibitions, performances and curatorial assessments.", "Exhibitiones, actiones et iudicia curatorialia documentata."),
    "intervento": ("Interventi", "Interventions", "Interventus", "Esiti documentati di un intervento editoriale o bibliografico.", "Documented outcomes of an editorial or bibliographic intervention.", "Exitus documentati interventus editorii vel bibliographici."),
}

SCOPES = {
    "output": ("Prodotto della ricerca", "Research output", "Fructus investigationis"),
    "work": ("Opera o edizione", "Work or edition", "Opus vel editio"),
    "venue": ("Sede di pubblicazione", "Publication venue", "Sedes editionis"),
    "agent": ("Persona o organizzazione", "Person or organisation", "Persona vel institutio"),
    "researcher": ("Ricercatrice o ricercatore", "Researcher", "Investigator"),
    "data": ("Dati di ricerca", "Research data", "Data investigationis"),
    "software": ("Software di ricerca", "Research software", "Programmata investigationis"),
    "artifact": ("Artefatto o esecuzione", "Artefact or performance", "Artefactum vel actio"),
    "intervention": ("Intervento documentabile", "Documentable intervention", "Interventus documentabilis"),
}

TYPES = {
    "count": ("Conteggio intero", "Integer count", "Numerus integer", "xsd:integer"),
    "decimal": ("Decimale non negativo", "Non-negative decimal", "Decimalis non negativus", "xsd:decimal"),
    "signed": ("Decimale con segno", "Signed decimal", "Decimalis cum signo", "xsd:decimal"),
    "percentage": ("Percentuale riportata dalla fonte", "Percentage reported by the source", "Pars centesima a fonte relata", "xsd:decimal"),
    "share": ("Quota calcolata da numeratore e denominatore", "Share computed from numerator and denominator", "Pars e numeratore et denominatore computata", "xsd:decimal"),
    "text": ("Riscontro qualitativo", "Qualitative evidence", "Testimonium qualitativum", "xsd:string"),
}

COVERAGES = {
    "complete": ("Copertura completa", "Complete coverage", "Ambitus integer", "Il corpus dichiarato è stato esaminato per intero.", "The declared corpus was examined in full.", "Corpus declaratum integrum examinatum est."),
    "partial": ("Copertura parziale", "Partial coverage", "Ambitus partialis", "Una parte dichiarata del corpus è stata esaminata; la nota spiega quale.", "A declared part of the corpus was examined; the note explains which.", "Pars declarata corporis examinata est; adnotatio quae pars sit explicat."),
    "unknown": ("Copertura ignota", "Unknown coverage", "Ambitus ignotus", "La fonte non dichiara la copertura; il confronto non è ammesso.", "The source does not declare coverage; comparison is not allowed.", "Fons ambitum non declarat; comparatio non admittitur."),
}

STATES = {
    "observed": ("Osservato", "Observed", "Observatum", "Il valore è stato rilevato e riportato.", "The value was observed and reported.", "Valor observatus et relatus est."),
    "missing": ("Dato assente", "Missing", "Datum absens", "La fonte non fornisce il dato; l'assenza non vale zero.", "The source provides no value; absence is not zero.", "Fons datum non praebet; absentia non est nihil."),
    "suppressed": ("Dato soppresso", "Suppressed", "Datum suppressum", "Il dato esiste ma non viene esposto, per diritti o riservatezza.", "The value exists but is not exposed, for rights or confidentiality.", "Datum exstat sed non exhibetur, propter iura vel secretum."),
    "not-applicable": ("Non applicabile", "Not applicable", "Non applicabile", "Il protocollo non si applica al soggetto.", "The protocol does not apply to the subject.", "Protocollum ad subiectum non pertinet."),
}

UNITS = {
    "adozioni": ("adozioni", "adoptions", "usus"), "anni": ("anni", "years", "anni"), "citazioni": ("citazioni", "citations", "citationes"),
    "documenti": ("documenti", "documents", "documenta"), "eventi": ("eventi", "events", "eventus"), "indice": ("indice", "index value", "index"),
    "licenze": ("licenze", "licences", "licentiae"), "opere": ("opere", "works", "opera"), "percentile": ("percentile", "percentile", "centesima pars"),
    "percento": ("percento", "percent", "pars centesima"), "protocolli": ("protocolli", "protocols", "protocolla"), "punteggio": ("punteggio", "score", "puncta"),
    "rapporto": ("rapporto", "ratio", "ratio"), "repliche": ("repliche", "replications", "replicationes"), "riferimenti": ("riferimenti", "references", "relationes"),
    "riscontri": ("riscontri", "pieces of evidence", "testimonia"), "riusi": ("riusi", "reuses", "usus iterati"), "schede": ("schede", "records", "schedulae"),
    "siti": ("siti", "sites", "loci"), "testo": ("testo", "text", "textus"), "traduzioni": ("traduzioni", "translations", "versiones"),
}

# EN: Method sentences of the built-in protocols, translated from the dictionary.
# LA: Sententiae de methodo protocollorum inclusorum, e lexico versae.
METHODS = {
    "citazioni": ("Count the citations that the source attributes to the work in the declared corpus.", "Citationes numera quas fons operi in corpore declarato tribuit."),
    "opere-citanti": ("Deduplicate the citing works according to the declared identifiers and rules.", "Opera citantia secundum indices et regulas declaratas deduplica."),
    "fwci": ("Use the provider's value with its reference group and computation version.", "Valore praebitoris cum coetu comparando et versione computationis utere."),
    "percentile": ("Report the percentile with the reference set and the date of computation.", "Centesimam partem cum coetu comparando et die computationis refer."),
    "rcr": ("Report the ratio with the co-citation network and the version of the method.", "Rationem cum rete cocitationum et versione methodi refer."),
    "h-index": ("Compute h on the declared set of works and citations of the agent.", "Indicem h in coetu declarato operum et citationum subiecti computa."),
    "g-index": ("Compute g on the same declared set as h.", "Indicem g in eodem coetu declarato ac h computa."),
    "i10-index": ("Count the works with at least ten citations in the declared source.", "Opera numera quae decem saltem citationes in fonte declarato habent."),
    "m-index": ("Divide h by the years since the first publication declared.", "Indicem h per annos ab editione prima declarata divide."),
    "opere-indicizzate": ("Count the works of the agent present in the declared source.", "Opera subiecti in fonte declarato praesentia numera."),
    "quota-accesso-aperto": ("Divide the open-access works by the indexed works of the agent.", "Opera aperte patentia per opera indicata subiecti divide."),
    "riferimenti-bibliografici": ("Count the outgoing references declared by the work.", "Relationes bibliographicas exeuntes ab opere declaratas numera."),
    "citazioni-senza-auto": ("Exclude self-citations according to the declared rule of authorship.", "Autocitationes secundum regulam auctoritatis declaratam exclude."),
    "citazioni-politiche": ("Count citations in policy documents identified by the source.", "Citationes in actis publicis a fonte designatis numera."),
    "citazioni-brevetti": ("Count citations in patents identified by the source.", "Citationes in diplomatibus inventorum a fonte designatis numera."),
    "altmetric": ("Report the provider's score with its date and the sources it counts.", "Puncta praebitoris cum die et fontibus numeratis refer."),
    "jif": ("Report the provider's journal value for the declared year.", "Valorem periodici a praebitore pro anno declarato refer."),
    "citescore": ("Report the provider's journal value for the declared year.", "Valorem periodici a praebitore pro anno declarato refer."),
    "snip": ("Report the provider's normalised journal value for the declared year.", "Valorem periodici normatum a praebitore pro anno declarato refer."),
    "sjr": ("Report the provider's journal value for the declared year.", "Valorem periodici a praebitore pro anno declarato refer."),
    "jci": ("Report the provider's journal value for the declared year.", "Valorem periodici a praebitore pro anno declarato refer."),
    "emivita-citazioni": ("Report the median age of the citations received in the declared year.", "Aetatem mediam citationum anno declarato receptarum refer."),
    "eigenfactor": ("Report the provider's journal value for the declared year.", "Valorem periodici a praebitore pro anno declarato refer."),
    "article-influence": ("Report the provider's journal value for the declared year.", "Valorem periodici a praebitore pro anno declarato refer."),
    "citazioni-dati": ("Count citations of the dataset that resolve to its identifier.", "Citationes datorum quae ad indicem eorum resolvuntur numera."),
    "riusi-dati": ("Count documented reuses of the dataset with a verifiable source.", "Usus iteratos datorum documentatos cum fonte probabili numera."),
    "qualita-dati": ("Describe context, limits and conditions of reuse of the data.", "Contextum, fines et condiciones usus iterati datorum describe."),
    "completezza-metadati": ("Divide the metadata fields present by the fields required by the declared profile.", "Campos notarum praesentes per campos a forma declarata postulatos divide."),
    "riusi-software": ("Count documented reuses of the software with a verifiable source.", "Usus iteratos programmatis documentatos cum fonte probabili numera."),
    "citazioni-software": ("Count citations of the software that resolve to its identifier.", "Citationes programmatis quae ad indicem eius resolvuntur numera."),
    "riproducibilita-software": ("Describe the reproducibility check performed and its outcome.", "Probationem reproductionis factam eiusque exitum describe."),
    "repliche-indipendenti": ("Count independent replications documented with a source.", "Replicationes independentes cum fonte documentatas numera."),
    "esito-replica": ("Describe the argued outcome of a replication.", "Exitum replicationis argumentis munitum describe."),
    "materiali-disponibili": ("Divide the available research materials by those declared in the work.", "Instrumenta investigationis praesto per ea in opere declarata divide."),
    "contributi-credit": ("Describe the contributions with CRediT roles and their source.", "Conlationes secundum munera CRediT cum fonte describe."),
    "monografie-recepite": ("Count reviews, discussions and citations of the monograph with a source.", "Recensiones, disputationes et citationes monographiae cum fonte numera."),
    "edizioni-critiche": ("Describe the contribution of the critical edition to the text and its tradition.", "Conlationem editionis criticae ad textum eiusque traditionem describe."),
    "traduzioni-verificate": ("Count translations verified against the original and the publisher.", "Versiones cum originali et editore probatas numera."),
    "ricezione-argomentativa": ("Describe how the work is taken up in arguments, with sources.", "Describe quomodo opus in argumentis recipiatur, cum fontibus."),
    "diffusione-didattica": ("Count documented teaching adoptions of the output.", "Usus didacticos fructus documentatos numera."),
    "impatto-territoriale": ("Describe documented territorial effects of the output.", "Effectus in communitate fructus documentatos describe."),
    "recepimento-policy": ("Describe uptake in public acts or practices with sources.", "Receptionem in actis vel usu publico cum fontibus describe."),
    "adozioni-cliniche": ("Count uptakes in clinical guidelines identified by the source.", "Receptiones in praeceptis clinicis a fonte designatis numera."),
    "trasferimento-clinico": ("Describe the documented clinical transfer of the output.", "Translationem clinicam fructus documentatam describe."),
    "protocolli-preregistrati": ("Count preregistrations documented in a public registry.", "Praescriptiones in indice publico documentatas numera."),
    "trasferimento-ingegneristico": ("Describe the verification of the output in an operating environment.", "Probationem fructus in ambitu operandi describe."),
    "licenze-applicate": ("Count documented licences of use of the output.", "Licentias usus fructus documentatas numera."),
    "validazione-agronomica": ("Describe the field validation with sites, seasons and sources.", "Probationem in agro cum locis, temporibus et fontibus describe."),
    "siti-agrari-indipendenti": ("Count independent agricultural sites that validated the output.", "Loca agraria independentia quae fructum probaverunt numera."),
    "trasferimento-veterinario": ("Describe the documented veterinary transfer of the output.", "Translationem veterinariam fructus documentatam describe."),
    "esposizioni-curate": ("Count documented curated exhibitions of the artefact.", "Exhibitiones curatas artefacti documentatas numera."),
    "performance-documentate": ("Count documented public performances of the artefact.", "Actiones publicas artefacti documentatas numera."),
    "valutazione-artistica": ("Describe the curatorial or artistic assessment with its source.", "Iudicium curatoriale vel artisticum cum fonte describe."),
    "accessibilita-editoriale": ("Divide the accessibility checks passed by the checks declared.", "Probationes accessibilitatis superatas per probationes declaratas divide."),
    "copertura-identificatori": ("Divide the works with persistent identifiers by the indexed works.", "Opera cum indicibus persistentibus per opera indicata divide."),
    "adozioni-documentate": ("Count independent adoptions verified with a source.", "Usus independentes cum fonte probatos numera."),
    "correzioni-metadati": ("Count the records corrected and verified after the intervention.", "Schedulas post interventum emendatas et probatas numera."),
    "esito-intervento": ("Separate execution, observed outcome, concurrent factors and causal attribution.", "Exsecutionem, exitum observatum, causas concurrentes et attributionem causalem distingue."),
}

# EN: Principles cited by the protocols. Labels are paraphrases; the source carries the exact wording.
# LA: Principia a protocollis citata. Tituli paraphrases sunt; fons verba ipsa praebet.
PRINCIPLES = {
    "dora": ("https://sfdora.org/read/", "DORA", ("Non usare metriche di rivista per valutare singoli articoli o persone", "Do not use journal-based metrics to assess single articles or individuals", "Ne indicibus periodicorum ad singulos articulos vel personas aestimandas utaris")),
    "leiden-1": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 1", ("La valutazione quantitativa sostiene il giudizio qualitativo degli esperti", "Quantitative evaluation should support qualitative, expert assessment", "Aestimatio quantitativa iudicium qualitativum peritorum sustineat")),
    "leiden-2": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 2", ("Misurare rispetto alle missioni di ricerca dell'istituzione, del gruppo o della persona", "Measure performance against the research missions of the institution, group or researcher", "Opus ad missiones investigationis institutionis, coetus vel personae metire")),
    "leiden-3": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 3", ("Proteggere l'eccellenza nella ricerca di rilevanza locale", "Protect excellence in locally relevant research", "Excellentiam investigationis localiter pertinentis tuere")),
    "leiden-4": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 4", ("Tenere aperti, trasparenti e semplici raccolta dei dati e analisi", "Keep data collection and analytical processes open, transparent and simple", "Collectionem datorum et analysin apertas, perspicuas et simplices serva")),
    "leiden-5": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 5", ("Permettere a chi è valutato di verificare dati e analisi", "Allow those evaluated to verify data and analysis", "Aestimatis data et analysin probare sine")),
    "leiden-6": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 6", ("Tenere conto delle differenze fra campi nelle pratiche di pubblicazione e citazione", "Account for variation by field in publication and citation practices", "Varietatem disciplinarum in usu edendi et citandi respice")),
    "leiden-7": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 7", ("Valutare le singole persone con un giudizio qualitativo del loro portafoglio", "Base assessment of individual researchers on a qualitative judgement of their portfolio", "Singulos investigatores iudicio qualitativo operum suorum aestima")),
    "leiden-8": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 8", ("Evitare la concretezza fuori luogo e la falsa precisione", "Avoid misplaced concreteness and false precision", "Concretionem alienam et falsam subtilitatem vita")),
    "leiden-9": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 9", ("Riconoscere gli effetti sistemici della valutazione e degli indicatori", "Recognise the systemic effects of assessment and indicators", "Effectus systematicos aestimationis et indicum agnosce")),
    "leiden-10": ("https://www.nature.com/articles/520429a", "Manifesto di Leiden 10", ("Esaminare regolarmente gli indicatori e aggiornarli", "Scrutinise indicators regularly and update them", "Indices identidem examina et renova")),
    "coara-1": ("https://coara.eu/agreement/the-agreement-full-text/", "CoARA, impegno 1", ("Riconoscere la diversità dei contributi e delle carriere nella ricerca", "Recognise the diversity of contributions to, and careers in, research", "Varietatem conlationum et cursuum in investigatione agnosce")),
    "coara-2": ("https://coara.eu/agreement/the-agreement-full-text/", "CoARA, impegno 2", ("Fondare la valutazione sul giudizio qualitativo e sulla revisione fra pari, con indicatori usati responsabilmente", "Base assessment primarily on qualitative evaluation with peer review, supported by responsible use of indicators", "Aestimationem in iudicio qualitativo et recensione parium funda, indicibus responsabiliter adhibitis")),
    "coara-3": ("https://coara.eu/agreement/the-agreement-full-text/", "CoARA, impegno 3", ("Abbandonare gli usi impropri delle metriche di rivista e di pubblicazione, come fattore d'impatto e indice h", "Abandon inappropriate uses of journal- and publication-based metrics, such as the Journal Impact Factor and the h-index", "Usus improprios indicum periodicorum et editionum, velut JIF et index h, relinque")),
    "coara-4": ("https://coara.eu/agreement/the-agreement-full-text/", "CoARA, impegno 4", ("Evitare l'uso delle classifiche delle organizzazioni di ricerca nella valutazione", "Avoid the use of rankings of research organisations in research assessment", "Ordines institutionum investigationis in aestimatione ne adhibeas")),
    "fair-f": ("https://doi.org/10.1038/sdata.2016.18", "FAIR F", ("Reperibile: identificatori persistenti e metadati ricchi", "Findable: persistent identifiers and rich metadata", "Reperibile: indices persistentes et notae copiosae")),
    "fair-a": ("https://doi.org/10.1038/sdata.2016.18", "FAIR A", ("Accessibile: protocolli aperti e metadati che restano anche senza i dati", "Accessible: open protocols and metadata that outlive the data", "Accessibile: protocolla aperta et notae quae data superstant")),
    "fair-i": ("https://doi.org/10.1038/sdata.2016.18", "FAIR I", ("Interoperabile: vocabolari formali e condivisi", "Interoperable: formal, shared vocabularies", "Interoperabile: lexica formalia et communia")),
    "fair-r": ("https://doi.org/10.1038/sdata.2016.18", "FAIR R", ("Riusabile: licenza chiara, provenienza dettagliata, standard di comunità", "Reusable: clear licence, detailed provenance, community standards", "Iterum usurpabile: licentia perspicua, origo accurata, normae communitatis")),
    "force11-1": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 1", ("Importanza: i dati sono prodotti di ricerca legittimi e citabili", "Importance: data are legitimate, citable products of research", "Momentum: data sunt fructus investigationis legitimi et citabiles")),
    "force11-2": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 2", ("Credito e attribuzione a chi ha contribuito ai dati", "Credit and attribution to all contributors to the data", "Laus et attributio omnibus qui data contulerunt")),
    "force11-3": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 3", ("Evidenza: citare i dati su cui si fonda un'affermazione", "Evidence: cite the data on which a claim relies", "Testimonium: data cita quibus affirmatio nititur")),
    "force11-4": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 4", ("Identificazione univoca e persistente", "Unique and persistent identification", "Designatio singularis et persistens")),
    "force11-5": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 5", ("Accesso ai dati e ai metadati citati", "Access to the cited data and metadata", "Aditus ad data et notas citata")),
    "force11-6": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 6", ("Persistenza degli identificatori e dei metadati oltre la vita dei dati", "Persistence of identifiers and metadata beyond the data's lifespan", "Persistentia indicum et notarum ultra vitam datorum")),
    "force11-7": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 7", ("Specificità e verificabilità della porzione citata", "Specificity and verifiability of the cited portion", "Proprietas et probabilitas partis citatae")),
    "force11-8": ("https://force11.org/info/joint-declaration-of-data-citation-principles-final/", "FORCE11 8", ("Interoperabilità e flessibilità fra comunità", "Interoperability and flexibility across communities", "Interoperabilitas et flexibilitas inter communitates")),
    "software-1": ("https://doi.org/10.7717/peerj-cs.86", "Citazione del software 1", ("Importanza: il software è un prodotto di ricerca citabile", "Importance: software is a citable research product", "Momentum: programma est fructus investigationis citabilis")),
    "software-2": ("https://doi.org/10.7717/peerj-cs.86", "Citazione del software 2", ("Credito e attribuzione a chi lo ha sviluppato", "Credit and attribution to its developers", "Laus et attributio iis qui programma fecerunt")),
    "software-3": ("https://doi.org/10.7717/peerj-cs.86", "Citazione del software 3", ("Identificazione univoca e leggibile dalle macchine", "Unique, machine-actionable identification", "Designatio singularis et machinis legibilis")),
    "software-4": ("https://doi.org/10.7717/peerj-cs.86", "Citazione del software 4", ("Persistenza di identificatori e metadati", "Persistence of identifiers and metadata", "Persistentia indicum et notarum")),
    "software-5": ("https://doi.org/10.7717/peerj-cs.86", "Citazione del software 5", ("Accessibilità del software e dei metadati", "Accessibility of software and metadata", "Aditus ad programma et notas")),
    "software-6": ("https://doi.org/10.7717/peerj-cs.86", "Citazione del software 6", ("Specificità della versione citata", "Specificity of the cited version", "Proprietas versionis citatae")),
    "credit": ("https://credit.niso.org/", "CRediT", ("Descrivere i contributi con quattordici ruoli, distinti dall'ordine degli autori", "Describe contributions with fourteen roles, distinct from author order", "Conlationes quattuordecim muneribus describe, ab ordine auctorum distinctis")),
    "prereg": ("https://www.cos.io/initiatives/prereg", "Preregistrazione", ("Dichiarare ipotesi e metodo prima di raccogliere i dati", "Declare hypotheses and method before collecting data", "Hypotheses et methodum ante data collecta declara")),
}

PRINCIPLE_BY_SOURCE = {
    "https://sfdora.org/read/": ["dora"],
    "https://www.nature.com/articles/520429a": [f"leiden-{n}" for n in range(1, 11)],
    "https://coara.eu/agreement/the-agreement-full-text/": ["coara-1", "coara-2", "coara-3", "coara-4"],
    "https://doi.org/10.1038/sdata.2016.18": ["fair-f", "fair-a", "fair-i", "fair-r"],
    "https://force11.org/info/joint-declaration-of-data-citation-principles-final/": [f"force11-{n}" for n in range(1, 9)],
    "https://doi.org/10.7717/peerj-cs.86": [f"software-{n}" for n in range(1, 7)],
    "https://credit.niso.org/": ["credit"],
    "https://www.cos.io/initiatives/prereg": ["prereg"],
}

# EN: Protocols that the principles explicitly caution against when used on individuals.
# LA: Protocolla quae principia expresse cavent cum ad singulos adhibentur.
CAUTIONS = {
    "dora": ["jif", "citescore", "snip", "sjr", "jci", "eigenfactor", "article-influence"],
    "coara-3": ["jif", "h-index", "g-index", "i10-index", "m-index"],
    "leiden-8": ["altmetric", "percentile"],
}

HEADER = """@prefix mtr: <https://aenigma.criptasemantica.it/metrum#> .
@prefix dub: <https://aenigma.criptasemantica.it/dubium#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema: <https://schema.org/> .
@prefix vann: <http://purl.org/vocab/vann/> .
@base <https://aenigma.criptasemantica.it/metrum#> .

# EN: Metrum is the module of qualified measurement. It does not rank anyone: it records how a value was
#     obtained (protocol, corpus, period, coverage, source) so that readers can judge whether two values are comparable.
# LA: Metrum est pars mensurae qualificatae. Neminem ordinat: scribit quomodo valor obtentus sit (protocollum, corpus,
#     tempus, ambitus, fons), ut lectores iudicent num duo valores comparari possint.
# EN: This file is generated by tools/metrum_from_dictionary.py from metrum/fonti/. Edit the generator or the snapshot.
# LA: Haec tabula a tools/metrum_from_dictionary.py e metrum/fonti/ gignitur. Generatorem aut tabulam fontium muta.

<https://aenigma.criptasemantica.it/metrum#> a owl:Ontology ;
    owl:versionIRI <https://aenigma.criptasemantica.it/metrum#v0.1.0> ;
    owl:versionInfo "0.1.0" ;
    dcterms:isPartOf <https://aenigma.criptasemantica.it/aenigma#> ;
    vann:preferredNamespacePrefix "mtr" ;
    vann:preferredNamespaceUri "https://aenigma.criptasemantica.it/metrum#" ;
    rdfs:label "Metrum. La misura qualificata della ricerca"@it, "Metrum. Qualified measurement of research"@en, "Metrum. Mensura investigationis qualificata"@la ;
    dcterms:title "Metrum. La misura qualificata della ricerca"@it, "Metrum. Qualified measurement of research"@en, "Metrum. Mensura investigationis qualificata"@la ;
    rdfs:comment "Terzo modulo di Aenigma. Osservazioni scientometriche con protocollo, corpus, periodo, copertura e fonte; discipline FORD; principi di valutazione responsabile; raccordo con la quantificazione della scrittura descritta nel manifesto."@it,
                 "Third module of Aenigma. Scientometric observations with protocol, corpus, period, coverage and source; FORD fields; principles of responsible assessment; a bridge to the quantification of writing described in the manifesto."@en,
                 "Tertia pars Aenigmatis. Observationes scientometricae cum protocollo, corpore, tempore, ambitu et fonte; disciplinae FORD; principia aestimationis responsabilis; nexus cum quantificatione scripturae in prooemio descripta."@la ;
    dcterms:description "Metrum rende dereferenziabile il vocabolario delle misure usato dal servizio semantico della Cripta: ogni protocollo, disciplina e principio ha un IRI pubblico, tre etichette e una fonte. Una misura è un ente del grafo, non un giudizio."@it,
                        "Metrum makes the measurement vocabulary of the Cripta semantic service dereferenceable: every protocol, field and principle has a public IRI, three labels and a source. A measure is an entity of the graph, not a verdict."@en,
                        "Metrum lexicon mensurarum a ministerio semantico Cryptae adhibitum reperibile reddit: quodque protocollum, disciplina et principium IRI publicum, tres titulos et fontem habet. Mensura est ens graphi, non iudicium."@la ;
    dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;
    dcterms:creator <https://criptasemantica.it/chi-siamo/finai/>, <https://criptasemantica.it/chi-siamo/alessandro-sevardi/> ;
    dcterms:publisher <https://criptasemantica.it/> ;
    dcterms:issued "2026-11-11"^^xsd:date ;
    dcterms:modified "2026-11-11"^^xsd:date ;
    dcterms:language "it", "en", "la" ;
    dcterms:references dub:F08, dub:F19, dub:quantificazioneScrittura, dub:quantificazioneOntologica, dub:capitaleSemantico ;
    dcterms:source <https://doi.org/10.1787/9789264239012-en>, <https://sfdora.org/read/>, <https://www.nature.com/articles/520429a>, <https://coara.eu/agreement/the-agreement-full-text/> ;
    rdfs:seeAlso <https://github.com/FINAI-Is-Not-An-Influencer/Aenigma>, <https://criptasemantica.it/chi-siamo/> .

# EN: Classes. An observation is an entity with provenance; a protocol is a plan that can be applied again.
# LA: Classes. Observatio est ens cum origine; protocollum est consilium quod iterum adhiberi potest.
mtr:Observation a owl:Class ; rdfs:subClassOf prov:Entity, schema:Observation ;
    rdfs:label "osservazione qualificata"@it, "qualified observation"@en, "observatio qualificata"@la ;
    rdfs:comment "Una sola applicazione di un protocollo a un soggetto, in un corpus e in un periodo dichiarati, con copertura, stato del risultato e fonte."@it,
                 "One application of a protocol to a subject, within a declared corpus and period, with coverage, result state and source."@en,
                 "Una adhibitio protocolli ad subiectum, in corpore et tempore declaratis, cum ambitu, statu exitus et fonte."@la .
mtr:Protocol a owl:Class ; rdfs:subClassOf skos:Concept, prov:Plan ;
    rdfs:label "protocollo di misura"@it, "measurement protocol"@en, "protocollum mensurae"@la ;
    rdfs:comment "Contratto di misura: che cosa si conta o si descrive, con quale unità, su quali soggetti, secondo quale metodo e quale fonte."@it,
                 "Measurement contract: what is counted or described, in which unit, for which subjects, by which method and source."@en,
                 "Pactum mensurae: quid numeretur vel describatur, qua unitate, de quibus subiectis, qua methodo et quo fonte."@la .
mtr:Family a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "famiglia di protocolli"@it, "protocol family"@en, "familia protocollorum"@la .
mtr:Scope a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "ambito del soggetto"@it, "subject scope"@en, "ambitus subiecti"@la ;
    rdfs:comment "Il tipo di soggetto a cui un protocollo si applica. Una misura di rivista non si trasferisce a un autore."@it,
                 "The kind of subject a protocol applies to. A venue metric does not transfer to an author."@en,
                 "Genus subiecti ad quod protocollum pertinet. Mensura periodici ad auctorem non transfertur."@la .
mtr:ValueType a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "tipo di valore"@it, "value type"@en, "genus valoris"@la .
mtr:Coverage a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "copertura del corpus"@it, "corpus coverage"@en, "ambitus corporis"@la .
mtr:ResultState a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "stato del risultato"@it, "result state"@en, "status exitus"@la ;
    rdfs:comment "Osservato, assente, soppresso o non applicabile. Un dato assente non vale zero."@it,
                 "Observed, missing, suppressed or not applicable. A missing value is not zero."@en,
                 "Observatum, absens, suppressum vel non applicabile. Datum absens non est nihil."@la .
mtr:Discipline a owl:Class ; rdfs:subClassOf skos:Concept ;
    rdfs:label "disciplina FORD"@it, "FORD field"@en, "disciplina FORD"@la ;
    rdfs:comment "Campo di ricerca e sviluppo secondo il Manuale di Frascati 2015 (classificazione FORD). I codici organizzano il lavoro editoriale; non misurano il merito."@it,
                 "Field of research and development according to the Frascati Manual 2015 (FORD classification). Codes organise editorial work; they do not rate merit."@en,
                 "Campus investigationis secundum Manuale Frascati 2015 (classificatio FORD). Codices opus editorium ordinant; meritum non aestimant."@la .
mtr:Principle a owl:Class ; rdfs:subClassOf prov:Entity ;
    rdfs:label "principio di valutazione responsabile"@it, "principle of responsible assessment"@en, "principium aestimationis responsabilis"@la ;
    rdfs:comment "Enunciato citabile di una dichiarazione pubblica (DORA, Leiden, CoARA, FAIR, FORCE11, CRediT) che orienta o limita l'uso di un protocollo."@it,
                 "Citable statement of a public declaration (DORA, Leiden, CoARA, FAIR, FORCE11, CRediT) that guides or limits the use of a protocol."@en,
                 "Enuntiatum citabile declarationis publicae (DORA, Leiden, CoARA, FAIR, FORCE11, CRediT) quod usum protocolli dirigit vel finit."@la .
mtr:Corpus a owl:Class ; rdfs:subClassOf prov:Entity ;
    rdfs:label "corpus dichiarato"@it, "declared corpus"@en, "corpus declaratum"@la .
mtr:Comparison a owl:Class ; rdfs:subClassOf prov:Entity ;
    rdfs:label "confronto fra osservazioni"@it, "comparison between observations"@en, "comparatio observationum"@la ;
    rdfs:comment "Due osservazioni dello stesso soggetto sono confrontabili solo con lo stesso protocollo, la stessa unità, le stesse discipline, lo stesso periodo, lo stesso corpus e copertura dichiarata. La variazione è descrittiva."@it,
                 "Two observations of the same subject are comparable only with the same protocol, unit, fields, period, corpus and declared coverage. The variation is descriptive."@en,
                 "Duae observationes eiusdem subiecti comparari possunt solum eodem protocollo, eadem unitate, iisdem disciplinis, eodem tempore, eodem corpore et ambitu declarato. Variatio descriptiva est."@la .

[] a owl:AllDisjointClasses ;
    owl:members ( mtr:Observation mtr:Protocol mtr:Family mtr:Scope mtr:ValueType mtr:Coverage mtr:ResultState mtr:Discipline mtr:Principle mtr:Corpus mtr:Comparison ) .

# EN: Properties of an observation. Provenance properties specialise PROV-O; the subject link specialises schema.org.
# LA: Proprietates observationis. Proprietates originis PROV-O, nexus subiecti schema.org specificant.
mtr:protocol a owl:ObjectProperty ; rdfs:domain mtr:Observation ; rdfs:range mtr:Protocol ;
    rdfs:label "segue il protocollo"@it, "follows protocol"@en, "protocollum sequitur"@la .
mtr:about a owl:ObjectProperty ; rdfs:subPropertyOf schema:observationAbout ; rdfs:domain mtr:Observation ;
    rdfs:label "riguarda il soggetto"@it, "about subject"@en, "de subiecto"@la .
mtr:corpus a owl:ObjectProperty ; rdfs:domain mtr:Observation ; rdfs:range mtr:Corpus ;
    rdfs:label "nel corpus"@it, "within corpus"@en, "in corpore"@la .
mtr:corpusLabel a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:string ;
    rdfs:label "descrizione del corpus"@it, "corpus description"@en, "descriptio corporis"@la .
mtr:periodStart a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:date ;
    rdfs:label "inizio del periodo"@it, "period start"@en, "initium temporis"@la .
mtr:periodEnd a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:date ;
    rdfs:label "fine del periodo"@it, "period end"@en, "finis temporis"@la .
mtr:acquiredOn a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:date ;
    rdfs:label "data di acquisizione"@it, "acquisition date"@en, "dies acquisitionis"@la .
mtr:coverage a owl:ObjectProperty ; rdfs:domain mtr:Observation ; rdfs:range mtr:Coverage ;
    rdfs:label "copertura"@it, "coverage"@en, "ambitus"@la .
mtr:state a owl:ObjectProperty ; rdfs:domain mtr:Observation ; rdfs:range mtr:ResultState ;
    rdfs:label "stato del risultato"@it, "result state"@en, "status exitus"@la .
mtr:discipline a owl:ObjectProperty ; rdfs:domain mtr:Observation ; rdfs:range mtr:Discipline ;
    rdfs:label "disciplina"@it, "field"@en, "disciplina"@la .
mtr:source a owl:ObjectProperty ; rdfs:subPropertyOf prov:wasDerivedFrom ; rdfs:domain mtr:Observation ;
    rdfs:label "fonte del corpus"@it, "corpus source"@en, "fons corporis"@la .
mtr:evidence a owl:ObjectProperty ; rdfs:subPropertyOf prov:wasDerivedFrom ; rdfs:domain mtr:Observation ;
    rdfs:label "prova dell'osservazione"@it, "observation evidence"@en, "testimonium observationis"@la .
mtr:value a owl:DatatypeProperty ; rdfs:domain mtr:Observation ;
    rdfs:label "valore"@it, "value"@en, "valor"@la .
mtr:numerator a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:integer ;
    rdfs:label "numeratore"@it, "numerator"@en, "numerator"@la .
mtr:denominator a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:integer ;
    rdfs:label "denominatore"@it, "denominator"@en, "denominator"@la .
mtr:editorialReading a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:string ;
    rdfs:label "lettura redazionale"@it, "editorial reading"@en, "lectio editoria"@la ;
    rdfs:comment "La lettura è distinta dal dato: dice che cosa la redazione ne ricava, non che cosa la fonte ha misurato."@it,
                 "The reading is distinct from the datum: it says what the editors draw from it, not what the source measured."@en,
                 "Lectio a dato distinguitur: dicit quid editores inde colligant, non quid fons mensus sit."@la .
mtr:appliedMethod a owl:DatatypeProperty ; rdfs:domain mtr:Observation ; rdfs:range xsd:string ;
    rdfs:label "metodo applicato"@it, "applied method"@en, "methodus adhibita"@la .

# EN: Properties of a protocol.
# LA: Proprietates protocolli.
mtr:family a owl:ObjectProperty ; rdfs:domain mtr:Protocol ; rdfs:range mtr:Family ;
    rdfs:label "famiglia"@it, "family"@en, "familia"@la .
mtr:scope a owl:ObjectProperty ; rdfs:domain mtr:Protocol ; rdfs:range mtr:Scope ;
    rdfs:label "si applica a"@it, "applies to"@en, "pertinet ad"@la .
mtr:valueType a owl:ObjectProperty ; rdfs:domain mtr:Protocol ; rdfs:range mtr:ValueType ;
    rdfs:label "tipo di valore"@it, "value type"@en, "genus valoris"@la .
mtr:unit a owl:DatatypeProperty ; rdfs:domain mtr:Protocol ; rdfs:range rdf:langString ;
    rdfs:label "unità"@it, "unit"@en, "unitas"@la .
mtr:method a owl:DatatypeProperty ; rdfs:domain mtr:Protocol ; rdfs:range rdf:langString ;
    rdfs:label "metodo"@it, "method"@en, "methodus"@la .
mtr:requiresReferenceSet a owl:DatatypeProperty ; rdfs:domain mtr:Protocol ; rdfs:range xsd:boolean ;
    rdfs:label "richiede un insieme di riferimento"@it, "requires a reference set"@en, "coetum comparandum requirit"@la .
mtr:guidedBy a owl:ObjectProperty ; rdfs:domain mtr:Protocol ; rdfs:range mtr:Principle ;
    rdfs:label "orientato dal principio"@it, "guided by principle"@en, "principio directum"@la .
mtr:cautions a owl:ObjectProperty ; rdfs:domain mtr:Principle ; rdfs:range mtr:Protocol ;
    rdfs:label "mette in guardia sull'uso di"@it, "cautions against the use of"@en, "cavet de usu"@la ;
    rdfs:comment "Il principio non vieta il protocollo: ne limita l'uso improprio, per esempio su singole persone."@it,
                 "The principle does not forbid the protocol: it limits improper use, for example on individuals."@en,
                 "Principium protocollum non vetat: usum improprium finit, velut de singulis personis."@la .
mtr:datatype a owl:ObjectProperty ; rdfs:domain mtr:ValueType ;
    rdfs:label "tipo di dato XML Schema"@it, "XML Schema datatype"@en, "genus dati XML Schema"@la .
mtr:first a owl:ObjectProperty ; rdfs:domain mtr:Comparison ; rdfs:range mtr:Observation ;
    rdfs:label "prima osservazione"@it, "first observation"@en, "observatio prior"@la .
mtr:second a owl:ObjectProperty ; rdfs:domain mtr:Comparison ; rdfs:range mtr:Observation ;
    rdfs:label "seconda osservazione"@it, "second observation"@en, "observatio posterior"@la .

# EN: Concept schemes for the controlled values.
# LA: Schemata notionum pro valoribus definitis.
mtr:protocolli a skos:ConceptScheme ; rdfs:label "Protocolli di misura"@it, "Measurement protocols"@en, "Protocolla mensurae"@la ;
    skos:prefLabel "Protocolli di misura"@it, "Measurement protocols"@en, "Protocolla mensurae"@la ;
    dcterms:source <https://coara.eu/agreement/the-agreement-full-text/> .
mtr:famiglie a skos:ConceptScheme ; rdfs:label "Famiglie di protocolli"@it, "Protocol families"@en, "Familiae protocollorum"@la ;
    skos:prefLabel "Famiglie di protocolli"@it, "Protocol families"@en, "Familiae protocollorum"@la .
mtr:ford a skos:ConceptScheme ; rdfs:label "Campi di ricerca e sviluppo (FORD)"@it, "Fields of research and development (FORD)"@en, "Campi investigationis (FORD)"@la ;
    skos:prefLabel "Campi di ricerca e sviluppo (FORD)"@it, "Fields of research and development (FORD)"@en, "Campi investigationis (FORD)"@la ;
    dcterms:source <https://doi.org/10.1787/9789264239012-en> .
mtr:valori a skos:ConceptScheme ; rdfs:label "Ambiti, tipi, coperture e stati"@it, "Scopes, types, coverages and states"@en, "Ambitus, genera, ambitus corporis et status"@la ;
    skos:prefLabel "Ambiti, tipi, coperture e stati"@it, "Scopes, types, coverages and states"@en, "Ambitus, genera, ambitus corporis et status"@la .
"""


def main():
    data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    out = [HEADER]
    out.append("# EN: Families.\n# LA: Familiae.")
    for key, (it, en, la, dit, den, dla) in FAMILIES.items():
        out.append(f"mtr:fam-{key} a mtr:Family ; skos:inScheme mtr:famiglie ; skos:topConceptOf mtr:famiglie ; skos:notation {lit(key)} ;\n"
                   f"    skos:prefLabel {tri({'it': it, 'en': en, 'la': la})} ;\n"
                   f"    rdfs:label {tri({'it': it, 'en': en, 'la': la})} ;\n"
                   f"    skos:definition {tri({'it': dit, 'en': den, 'la': dla})} .")
    out.append("\n# EN: Scopes, value types, coverages and result states.\n# LA: Ambitus, genera valorum, ambitus corporis et status exitus.")
    for key, (it, en, la) in SCOPES.items():
        out.append(f"mtr:scope-{key} a mtr:Scope ; skos:inScheme mtr:valori ; skos:topConceptOf mtr:valori ; skos:notation {lit(key)} ; skos:prefLabel {tri({'it': it, 'en': en, 'la': la})} ; rdfs:label {tri({'it': it, 'en': en, 'la': la})} .")
    for key, (it, en, la, dt) in TYPES.items():
        out.append(f"mtr:type-{key} a mtr:ValueType ; skos:inScheme mtr:valori ; skos:topConceptOf mtr:valori ; skos:notation {lit(key)} ; mtr:datatype {dt} ; skos:prefLabel {tri({'it': it, 'en': en, 'la': la})} ; rdfs:label {tri({'it': it, 'en': en, 'la': la})} .")
    for key, (it, en, la, dit, den, dla) in COVERAGES.items():
        out.append(f"mtr:coverage-{key} a mtr:Coverage ; skos:inScheme mtr:valori ; skos:topConceptOf mtr:valori ; skos:notation {lit(key)} ; skos:prefLabel {tri({'it': it, 'en': en, 'la': la})} ; rdfs:label {tri({'it': it, 'en': en, 'la': la})} ; skos:definition {tri({'it': dit, 'en': den, 'la': dla})} .")
    for key, (it, en, la, dit, den, dla) in STATES.items():
        out.append(f"mtr:state-{key} a mtr:ResultState ; skos:inScheme mtr:valori ; skos:topConceptOf mtr:valori ; skos:notation {lit(key)} ; skos:prefLabel {tri({'it': it, 'en': en, 'la': la})} ; rdfs:label {tri({'it': it, 'en': en, 'la': la})} ; skos:definition {tri({'it': dit, 'en': den, 'la': dla})} .")
    out.append("\n# EN: Principles. Each is a paraphrase with its source; the source holds the authoritative wording.\n# LA: Principia. Quodque paraphrasis est cum fonte; fons verba auctoritate praedita servat.")
    for key, (source, short, (it, en, la)) in PRINCIPLES.items():
        out.append(f"mtr:principle-{key} a mtr:Principle ; dcterms:source <{source}> ; skos:notation {lit(short)} ;\n"
                   f"    rdfs:label {tri({'it': it, 'en': en, 'la': la})} .")
    for key, protocols in CAUTIONS.items():
        out.append(f"mtr:principle-{key} mtr:cautions " + ", ".join(f"mtr:p-{p}" for p in protocols) + " .")
    out.append("\n# EN: FORD fields of the Frascati Manual 2015, with the labels used by the Cripta.\n# LA: Disciplinae FORD Manualis Frascati 2015, cum titulis a Crypta adhibitis.")
    for code, labels in data["disciplines"].items():
        number = code.split(":")[1]
        node = f"mtr:ford-{number.replace('.', '-')}"
        broader = f" ; skos:broader mtr:ford-{number.split('.')[0]}" if "." in number else f" ; skos:topConceptOf mtr:ford"
        out.append(f"{node} a mtr:Discipline ; skos:inScheme mtr:ford ; skos:notation {lit(number)}{broader} ;\n"
                   f"    skos:prefLabel {tri(labels)} ; rdfs:label {tri(labels)} .")
    for code in data["disciplines"]:
        number = code.split(":")[1]
        if "." not in number:
            out.append(f"mtr:ford skos:hasTopConcept mtr:ford-{number} .")
    out.append("\n# EN: Built-in protocols. The key is stable; a change of method takes a new version in the service, not a new IRI here.\n# LA: Protocolla inclusa. Clavis stabilis est; methodo mutata ministerium versionem novam, non IRI novum hic, adhibet.")
    for key, p in data["protocols"].items():
        en, la = METHODS[key]
        unit = UNITS[p["unit"]]
        principles = PRINCIPLE_BY_SOURCE.get(p["source"], [])
        guided = (" ;\n    mtr:guidedBy " + ", ".join(f"mtr:principle-{x}" for x in principles)) if principles else ""
        out.append(
            f"mtr:p-{key} a mtr:Protocol ; skos:inScheme mtr:protocolli ; skos:topConceptOf mtr:protocolli ; skos:notation {lit(key)} ;\n"
            f"    skos:prefLabel {tri(p['label'])} ;\n"
            f"    rdfs:label {tri(p['label'])} ;\n"
            f"    mtr:family mtr:fam-{p['family']} ; mtr:valueType mtr:type-{p['type']} ;\n"
            f"    mtr:scope " + ", ".join(f"mtr:scope-{s}" for s in p["scopes"]) + " ;\n"
            f"    mtr:unit {tri({'it': unit[0], 'en': unit[1], 'la': unit[2]})} ;\n"
            f"    mtr:method {tri({'it': p['method'], 'en': en, 'la': la})} ;\n"
            f"    mtr:requiresReferenceSet {str(bool(p.get('reference'))).lower()} ;\n"
            f"    dcterms:source <{p['source']}>{guided} .")
    # EN: Declare the top concepts of each scheme once, from the inverse already written.
    # LA: Notiones summas cuiusque schematis semel declara, ex inversa iam scripta.
    tops = []
    for key in FAMILIES:
        tops.append(f"mtr:famiglie skos:hasTopConcept mtr:fam-{key} .")
    for group, keys in (("scope", SCOPES), ("type", TYPES), ("coverage", COVERAGES), ("state", STATES)):
        for key in keys:
            tops.append(f"mtr:valori skos:hasTopConcept mtr:{group}-{key} .")
    for key in data["protocols"]:
        tops.append(f"mtr:protocolli skos:hasTopConcept mtr:p-{key} .")
    out.extend(tops)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{OUT}: {len(data['protocols'])} protocols, {len(data['disciplines'])} fields, {len(PRINCIPLES)} principles")


if __name__ == "__main__":
    main()
