# Metrum. Formalisation

[Beginner's guide](README.en.md) · [Italiano](FORMALIZZAZIONE.md) · [Latine](FORMALIZZAZIONE.la.md)

Metrum formalises the measurement of research as an entity of the graph endowed with provenance. The starting point is a thesis of the "About us" page of the Cripta Semantica: there are no neutral measures of the quality of science, only technical systems of measurement that alter it. If so, a measure cannot enter an ontology as a number: it must enter as an observation, with the protocol that produced it, the corpus on which it was taken, the period, the coverage, the result state and the source. This document describes the model, the three rules that govern it, the constraints that enforce them and the bridge to the other modules.

## The model

| Class | Alignments | What it represents |
| --- | --- | --- |
| `mtr:Observation` | `prov:Entity`, `schema:Observation` | A single application of a protocol to a subject. |
| `mtr:Protocol` | `skos:Concept`, `prov:Plan` | The measurement contract: what is counted or described, in which unit, for which subjects, by which method and source. |
| `mtr:Family` | `skos:Concept` | The protocol's group: fourteen families. |
| `mtr:Scope` | `skos:Concept` | The admissible subject kind: nine scopes. |
| `mtr:ValueType` | `skos:Concept` | The value type, with its XML Schema datatype. |
| `mtr:Coverage` | `skos:Concept` | Complete, partial or unknown coverage of the corpus. |
| `mtr:ResultState` | `skos:Concept` | Observed, missing, suppressed, not applicable. |
| `mtr:Discipline` | `skos:Concept` | A FORD field of the Frascati Manual 2015: six fields and forty-two subfields. |
| `mtr:Principle` | `prov:Entity` | A citable statement of a public declaration on responsible assessment. |
| `mtr:Corpus` | `prov:Entity` | A declared corpus, when it has an IRI of its own. |
| `mtr:Comparison` | `prov:Entity` | A declared comparison between two observations. |

The eleven classes are mutually disjoint. The properties of an observation are `protocol`, `about` (subproperty of `schema:observationAbout`), `corpus` and `corpusLabel`, `periodStart`, `periodEnd`, `acquiredOn`, `coverage`, `state`, `discipline`, `source` and `evidence` (both subproperties of `prov:wasDerivedFrom`), `value`, `numerator`, `denominator`, `appliedMethod`, `editorialReading`. The properties of a protocol are `family`, `scope`, `valueType`, `unit`, `method`, `requiresReferenceSet`, `guidedBy`; a principle has `cautions`. The [hierarchy](en/schema.html) lists them with domain and range.

## Three rules

**A missing value is not zero.** The result state is mandatory and distinct from the value. An observed result must have a value; a missing, suppressed or inapplicable result may have none. Whoever aggregates observations cannot turn an absence into a zero without violating the shapes.

**Two measures are compared only under the same contract.** An `mtr:Comparison` is admitted only if the two observations share subject, protocol, corpus, period and fields and if neither has unknown coverage. The acquisition date may change: that is precisely what the comparison describes. The variation remains descriptive; it is not a verdict.

**A principle limits, it does not forbid.** `mtr:cautions` links a principle to the protocols whose improper use it warns against: DORA to the seven venue indicators, CoARA commitment 3 to the impact factor and the h, g, i10 and m indices, Leiden principle 8 to percentiles and attention scores. The protocols stay in the catalogue, because they exist and are used; the graph makes the limit visible.

## SHACL constraints

The [shapes](shapes.ttl) have four targets. `ObservationShape` requires a protocol, a subject, a state, a coverage, a period of dates, an acquisition date, a corpus label, an HTTPS source and evidence, at least one field; three SPARQL constraints enforce the consistency between state and value, the order of the period and the editorial reading for non-complete coverages. `ProtocolShape` requires three labels, a notation, a family, scopes, a value type, unit and method in three languages, the reference-set declaration and a source. `PrincipleShape` and `DisciplineShape` check sources, labels and FORD notations. `ComparisonShape` applies the comparison rule with a SPARQL constraint. The verification program tries six alterations (observation without protocol, value on a missing datum, partial coverage without reading, reversed period, comparison across different protocols, protocol without source), all rejected.

## Families

<!-- table:families -->
| Key | Family | Protocols |  |
| --- | --- | --- | --- |
| `agraria` | Agricultural research | 3 | Field validations and veterinary transfer. |
| `apertura` | Openness and access | 5 | Shares and checks on open access, metadata, identifiers and materials. |
| `arti` | Arts | 3 | Documented exhibitions, performances and curatorial assessments. |
| `clinica` | Clinical research | 2 | Uptake in guidelines and clinical transfer. |
| `dati` | Data | 3 | Citations, reuses and context of research data. |
| `intervento` | Interventions | 2 | Documented outcomes of an editorial or bibliographic intervention. |
| `metodo` | Method | 4 | Replications, preregistrations and contribution descriptions. |
| `ricezione` | Reception | 13 | Citations and reuses that a source attributes to a work or an agent. |
| `sedi` | Publication venues | 8 | Indicators computed on journals and series, not on single works. |
| `sociale` | Social research | 2 | Teaching adoptions and territorial evidence. |
| `software` | Software | 3 | Citations, reuses and reproducibility of research software. |
| `tecnica` | Engineering | 2 | Operational verification and licences of use. |
| `trasferimento` | Transfer | 4 | Evidence of research use outside academia: policy, patents, adoptions. |
| `umanistica` | Humanities | 4 | Monographs, critical editions, translations and argumentative reception. |
<!-- /table -->

## Protocols

Protocols share the key used by the Cripta semantic service. The version (`@1.0.0`) belongs to the service: the Metrum IRI identifies the contract. A local protocol added in the service has no IRI in Metrum until it is published here.

<!-- table:protocols -->
| Key | Concept | Family | Scope | Unit |
| --- | --- | --- | --- | --- |
| `accessibilita-editoriale` | Editorial accessibility checks passed | Openness and access | Research output | percent |
| `adozioni-cliniche` | Uptake in clinical guidance | Clinical research | Research output | documents |
| `adozioni-documentate` | Verified independent adoptions | Transfer | Research output | adoptions |
| `altmetric` | Altmetric attention score | Reception | Work or edition | score |
| `article-influence` | Article Influence Score | Publication venues | Publication venue | index value |
| `citazioni` | Incoming citations | Reception | Work or edition | citations |
| `citazioni-brevetti` | Patent citations | Transfer | Work or edition | documents |
| `citazioni-dati` | Data citations | Data | Research data | citations |
| `citazioni-politiche` | Policy-document citations | Transfer | Work or edition | documents |
| `citazioni-senza-auto` | Citations excluding self-citations | Reception | Work or edition | citations |
| `citazioni-software` | Software citations | Software | Research software | citations |
| `citescore` | CiteScore | Publication venues | Publication venue | ratio |
| `completezza-metadati` | Metadata completeness | Openness and access | Research output | percent |
| `contributi-credit` | Contributions described with CRediT | Method | Research output | text |
| `copertura-identificatori` | Persistent identifier coverage | Openness and access | Person or organisation | percent |
| `correzioni-metadati` | Records corrected and verified | Interventions | Documentable intervention | records |
| `diffusione-didattica` | Documented teaching adoptions | Social research | Research output | adoptions |
| `edizioni-critiche` | Contribution of a critical edition | Humanities | Work or edition | text |
| `eigenfactor` | Eigenfactor Score | Publication venues | Publication venue | index value |
| `emivita-citazioni` | Cited half-life | Publication venues | Publication venue | years |
| `esito-intervento` | Documented intervention outcome | Interventions | Documentable intervention | text |
| `esito-replica` | Reasoned replication outcome | Method | Research output | text |
| `esposizioni-curate` | Documented curated exhibitions | Arts | Artefact or performance | events |
| `fwci` | Field-weighted citation impact | Reception | Work or edition | ratio |
| `g-index` | g-index | Reception | Person or organisation | index value |
| `h-index` | h-index | Reception | Person or organisation | index value |
| `i10-index` | i10-index | Reception | Person or organisation | works |
| `impatto-territoriale` | Community impact evidence | Social research | Research output | text |
| `jci` | Journal Citation Indicator | Publication venues | Publication venue | index value |
| `jif` | Journal Impact Factor | Publication venues | Publication venue | ratio |
| `licenze-applicate` | Documented licenses in use | Engineering | Research output | licences |
| `m-index` | m-index | Reception | Researcher | ratio |
| `materiali-disponibili` | Research material availability | Openness and access | Research output | percent |
| `monografie-recepite` | Monograph reception evidence | Humanities | Work or edition | pieces of evidence |
| `opere-citanti` | Distinct citing works | Reception | Work or edition | works |
| `opere-indicizzate` | Indexed works | Reception | Person or organisation | works |
| `percentile` | Citation percentile | Reception | Work or edition | percentile |
| `performance-documentate` | Documented public performances | Arts | Artefact or performance | events |
| `protocolli-preregistrati` | Documented preregistrations | Method | Research output | protocols |
| `qualita-dati` | Data context and limitations | Data | Research data | text |
| `quota-accesso-aperto` | Open-access share | Openness and access | Person or organisation | percent |
| `rcr` | Relative Citation Ratio | Reception | Work or edition | ratio |
| `recepimento-policy` | Uptake in policy or public practice | Transfer | Research output | text |
| `repliche-indipendenti` | Documented independent replications | Method | Research output | replications |
| `ricezione-argomentativa` | Argumentative reception | Humanities | Research output | text |
| `riferimenti-bibliografici` | Outgoing references | Reception | Work or edition | references |
| `riproducibilita-software` | Software reproducibility evidence | Software | Research software | text |
| `riusi-dati` | Verified data reuse | Data | Research data | reuses |
| `riusi-software` | Documented software reuse | Software | Research software | reuses |
| `siti-agrari-indipendenti` | Independent agricultural validation sites | Agricultural research | Research output | sites |
| `sjr` | SJR | Publication venues | Publication venue | index value |
| `snip` | SNIP | Publication venues | Publication venue | index value |
| `traduzioni-verificate` | Verifiable translations | Humanities | Work or edition | translations |
| `trasferimento-clinico` | Clinical translation evidence | Clinical research | Research output | text |
| `trasferimento-ingegneristico` | Operational verification evidence | Engineering | Research output | text |
| `trasferimento-veterinario` | Veterinary uptake evidence | Agricultural research | Research output | text |
| `validazione-agronomica` | Field validation evidence | Agricultural research | Research output | text |
| `valutazione-artistica` | Curatorial or artistic assessment | Arts | Artefact or performance | text |
<!-- /table -->

## Principles

Principles are paraphrases; the source keeps the authoritative wording. The declarations cited are the San Francisco Declaration on Research Assessment (DORA), the Leiden Manifesto (ten principles), the Agreement on Reforming Research Assessment (CoARA, four core commitments), the FAIR principles, the Joint Declaration of Data Citation Principles (FORCE11, eight principles), the software citation principles (six), the CRediT taxonomy and preregistration.

<!-- table:principles -->
| Key | Principle | Source | Cautions against |
| --- | --- | --- | --- |
| CRediT | Describe contributions with fourteen roles, distinct from author order | [Source](https://credit.niso.org/) | — |
| Citazione del software 1 | Importance: software is a citable research product | [Source](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 2 | Credit and attribution to its developers | [Source](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 3 | Unique, machine-actionable identification | [Source](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 4 | Persistence of identifiers and metadata | [Source](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 5 | Accessibility of software and metadata | [Source](https://doi.org/10.7717/peerj-cs.86) | — |
| Citazione del software 6 | Specificity of the cited version | [Source](https://doi.org/10.7717/peerj-cs.86) | — |
| CoARA, impegno 1 | Recognise the diversity of contributions to, and careers in, research | [Source](https://coara.eu/agreement/the-agreement-full-text/) | — |
| CoARA, impegno 2 | Base assessment primarily on qualitative evaluation with peer review, supported by responsible use of indicators | [Source](https://coara.eu/agreement/the-agreement-full-text/) | — |
| CoARA, impegno 3 | Abandon inappropriate uses of journal- and publication-based metrics, such as the Journal Impact Factor and the h-index | [Source](https://coara.eu/agreement/the-agreement-full-text/) | `g-index`, `h-index`, `i10-index`, `jif`, `m-index` |
| CoARA, impegno 4 | Avoid the use of rankings of research organisations in research assessment | [Source](https://coara.eu/agreement/the-agreement-full-text/) | — |
| DORA | Do not use journal-based metrics to assess single articles or individuals | [Source](https://sfdora.org/read/) | `article-influence`, `citescore`, `eigenfactor`, `jci`, `jif`, `sjr`, `snip` |
| FAIR A | Accessible: open protocols and metadata that outlive the data | [Source](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR F | Findable: persistent identifiers and rich metadata | [Source](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR I | Interoperable: formal, shared vocabularies | [Source](https://doi.org/10.1038/sdata.2016.18) | — |
| FAIR R | Reusable: clear licence, detailed provenance, community standards | [Source](https://doi.org/10.1038/sdata.2016.18) | — |
| FORCE11 1 | Importance: data are legitimate, citable products of research | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 2 | Credit and attribution to all contributors to the data | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 3 | Evidence: cite the data on which a claim relies | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 4 | Unique and persistent identification | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 5 | Access to the cited data and metadata | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 6 | Persistence of identifiers and metadata beyond the data's lifespan | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 7 | Specificity and verifiability of the cited portion | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| FORCE11 8 | Interoperability and flexibility across communities | [Source](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) | — |
| Manifesto di Leiden 1 | Quantitative evaluation should support qualitative, expert assessment | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 10 | Scrutinise indicators regularly and update them | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 2 | Measure performance against the research missions of the institution, group or researcher | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 3 | Protect excellence in locally relevant research | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 4 | Keep data collection and analytical processes open, transparent and simple | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 5 | Allow those evaluated to verify data and analysis | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 6 | Account for variation by field in publication and citation practices | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 7 | Base assessment of individual researchers on a qualitative judgement of their portfolio | [Source](https://www.nature.com/articles/520429a) | — |
| Manifesto di Leiden 8 | Avoid misplaced concreteness and false precision | [Source](https://www.nature.com/articles/520429a) | `altmetric`, `percentile` |
| Manifesto di Leiden 9 | Recognise the systemic effects of assessment and indicators | [Source](https://www.nature.com/articles/520429a) | — |
| Preregistrazione | Declare hypotheses and method before collecting data | [Source](https://www.cos.io/initiatives/prereg) | — |
<!-- /table -->

## FORD fields

The OECD Frascati Manual 2015 classifies research and development into six fields (natural sciences; engineering and technology; medical and health sciences; agricultural and veterinary sciences; social sciences; humanities and the arts) and forty-two subfields. Metrum publishes them as a SKOS scheme with the three-language labels used by the Cripta; the codes organise editorial work and do not rate merit. Trivium bridges to them with `skos:broadMatch`.

## The philosophical bridge

The Cripta manifesto describes, in its second paragraph, a turning point: with the abstract machine of 1936 begins "the process of quantification of writing", which finds in hypertext its final display ([F08](../dubium/en/term/F08.html)). In the fifth paragraph ontological quantification is the relation between the values of the bound variables of a theory and its statements ([F19](../dubium/en/term/F19.html)). Scientometrics is a quantification of the second degree: it does not quantify being, but the writing that treats of it, counting how texts cite, reuse and distribute one another. Metrum holds this gap firm. Its observations concern works, editions, venues, persons as ontic subjects; the question of the sense of what they measure stays in Dubium. This is why the module header refers to F08, to F19 and to semantic capital ([F13](../dubium/en/term/F13.html)), and declares no equivalence.

The second thesis is that of non-neutrality. A measure alters what it measures: whoever knows they are being counted writes in order to be counted. The Leiden Manifesto calls this a systemic effect (principle 9); the "About us" page of the Cripta says it in the lexicon of dialectical materialism. Metrum does not solve the problem, but makes it visible: every observation declares its contract, and every contract carries the principles that limit its use.

## Example queries

The protocols whose use DORA limits, with their family:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?protocol ?family WHERE {
  mtr:principle-dora mtr:cautions ?p .
  ?p skos:prefLabel ?protocol ; mtr:family/skos:prefLabel ?family .
  FILTER ( lang(?protocol) = "en" && lang(?family) = "en" )
}
```

The protocols applicable to research data:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
SELECT ?p WHERE { ?p mtr:scope mtr:scope-data }
```

The Trivium disciplines bridged to a FORD field of the humanities:

```sparql
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?discipline ?field WHERE {
  ?field skos:broader mtr:ford-6 .
  ?discipline skos:broadMatch ?field .
}
```

## Limits

Metrum publishes the protocols the Cripta service knows today; it does not claim to exhaust scientometrics. Methods are described in one sentence: the actual reproduction of an indicator depends on the source and its corpus. The English and Latin labels of the FORD fields are those used by the Cripta, not official OECD translations. The module contains no real observations: those live in the semantic service of the site, which publishes only what the editors have released.
