# Metrum. A beginner's guide

[Italiano](README.md) · [Latine](README.la.md) · [Formalisation](FORMALIZZAZIONE.en.md)

Metrum is the third module of [Aenigma](../README.en.md). It serves to say **how** a measure of research was obtained, not to establish who is worth more. Every number that circulates around research (citations, h-index, impact factor, open-access shares, reuses of data and software) comes from a protocol applied to a corpus, within a period, with a certain coverage and from a certain source. Without these five pieces of information two numbers cannot be compared. Metrum makes them mandatory.

If you have never dealt with scientometrics, keep in mind three rules the module embodies: a missing value is not zero; two measures are comparable only if they share the same contract; a principle of responsible assessment does not forbid a measure, it limits its improper use. The "About us" page of the Cripta says that there are no neutral measures of the quality of science, only technical systems that alter it: Metrum is the way to keep that awareness inside the graph.

## Why Metrum

*Metrum* is measure, but also the metre of verse: a rule that makes comparable what would otherwise be mere sound. The Cripta manifesto describes, at the turning point of 1936, the beginning of the "quantification of writing" ([F08 of Dubium](../dubium/en/term/F08.html)). Scientometrics is one of the forms of that quantification. Metrum takes it in as an object of the ontology, with its provenance, instead of suffering it as a verdict.

## A first visit

1. Open the [Metrum catalogue](en/index.html) and search for **Incoming citations**. The protocol entry shows the family (reception), the scope (work or edition), the unit, the method in three languages, the source and the principles that guide it.
2. Open [DORA](en/term/principle-dora.html). The entry lists the protocols whose use the principle limits: the seven venue indicators, starting with the impact factor.
3. Open the FORD field [Philosophical, ethical and religious studies](en/term/ford-6-3.html): you will see the parent field and the Trivium disciplines that bridge to it.
4. Open the [hierarchy](en/schema.html): classes, properties, the fourteen families and the fifty-eight protocols grouped.

## How to read a protocol

| Field | Meaning |
| --- | --- |
| Family | The group it belongs to: reception, venues, openness, transfer, data, software, method, humanities, social research, clinical, engineering, agricultural, arts, interventions. |
| Applies to | The subject scope: work, venue, person or organisation, data, software, artefact, intervention, output. A venue metric does not transfer to an author. |
| Value type | Integer count, decimal, percentage, computed share or textual evidence. |
| Unit | Citations, works, years, percent, text. |
| Method | What is done to obtain the value. A change of method requires a new version in the service. |
| Requires a reference set | True for normalised indicators (field-weighted impact, percentiles). |
| Source | The public document that defines or discusses the indicator. |
| Guided by principle | The relevant DORA, Leiden, CoARA, FAIR, FORCE11 or CRediT principles. |

## How an observation is written

An observation is a single application of a protocol. This is the synthetic example included in [esempi.ttl](esempi.ttl): the work, the corpus and the values are invented, the vocabulary is real.

```turtle
@prefix mtr: <https://aenigma.criptasemantica.it/metrum#> .
@prefix ex: <https://aenigma.criptasemantica.it/metrum/esempi#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:osservazione-1 a mtr:Observation ;
    mtr:protocol mtr:p-citazioni ;            # which measurement contract
    mtr:about ex:opera-dimostrativa ;         # about what
    mtr:state mtr:state-observed ;            # observed, missing, suppressed, not applicable
    mtr:coverage mtr:coverage-complete ;      # how much of the corpus was examined
    mtr:corpusLabel "Corpus sintetico di prova" ;
    mtr:periodStart "2024-01-01"^^xsd:date ; mtr:periodEnd "2024-12-31"^^xsd:date ;
    mtr:acquiredOn "2025-07-01"^^xsd:date ;   # when it was read
    mtr:discipline mtr:ford-6-3 ;             # in which field
    mtr:source <https://example.org/corpus> ; # where the corpus comes from
    mtr:evidence <https://example.org/evidence/1> ;  # the evidence of the observation
    mtr:value 12 .
```

The three lines that matter most are `state`, `coverage` and `evidence`. The state says whether the number exists; the coverage says how much it is worth; the evidence says where to check it. The [SHACL constraints](shapes.ttl) reject an "observed" observation without a value, a missing datum with a value, a partial coverage without an editorial reading, a reversed period.

## From the file to a first query

```python
from rdflib import Graph

graph = Graph().parse("metrum/metrum.ttl", format="turtle")
graph.parse("metrum/esempi.ttl", format="turtle")
query = """
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?observation ?value ?protocol WHERE {
  ?observation a mtr:Observation ; mtr:state mtr:state-observed ;
      mtr:value ?value ; mtr:protocol ?p ; mtr:discipline mtr:ford-6-3 .
  ?p skos:prefLabel ?protocol . FILTER ( lang(?protocol) = "en" )
}
"""
for row in graph.query(query):
    print(*row)
```

You obtain the observations with a value in the FORD field of philosophy, with the protocol name. To know whether two observations are comparable, declare an `mtr:Comparison` between them and validate with the shapes: the comparison is admitted only if they share subject, protocol, corpus, period and fields, with declared coverage.

## Bridges to the other modules

With **Dubium**: the module header refers to `dub:F08` and `dub:F19`, the positions on the quantification of writing and on ontological quantification, and to semantic capital. With **Trivium**: the disciplines of the site declare with `skos:broadMatch` the FORD field in which they sit, so an observation about a "Dialectic" article finds its field. With the **Cripta semantic service**: the classes of the service's operational vocabulary are declared subclasses of those of Metrum, and its protocols share the same key: `citazioni@1.0.0` in the service is `mtr:p-citazioni` here.

## Building and verifying

The file `metrum.ttl` is generated by [tools/metrum_from_dictionary.py](../tools/metrum_from_dictionary.py), which reads the snapshot of the protocol dictionary in `fonti/` and contains, written by hand, the schema, the principles, the scopes and the coverages. From the repository root:

```bash
python3 tools/metrum_from_dictionary.py
python3 tests/verifica.py
python3 tools/build_site.py
```

The verification program checks the counts (58 protocols, 48 fields, 35 principles), the sources, the bridges, the SHACL constraints on the examples and six deliberate alterations of Metrum, all rejected.

## Contributing

A new protocol requires: a lowercase key, a family, scopes, a value type, unit and method in three languages, a public source, the relevant principles. If the method of an existing protocol changes, the key stays and the service records a new version: the Metrum IRI identifies the contract, not its version. A new principle requires a public source and a label in three languages; if it limits the use of some protocol, it says so with `mtr:cautions`.
