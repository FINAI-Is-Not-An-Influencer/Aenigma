# Metrum. Una guida per iniziare

[English](README.en.md) · [Latine](README.la.md) · [Formalizzazione](FORMALIZZAZIONE.md)

Metrum è il terzo modulo di [Aenigma](../README.md). Serve a dire **come** una misura della ricerca è stata ottenuta, non a stabilire chi vale di più. Ogni numero che circola intorno alla ricerca (citazioni, indice h, fattore d'impatto, quote di accesso aperto, riusi di dati e software) nasce da un protocollo applicato a un corpus, in un periodo, con una certa copertura e da una certa fonte. Senza queste cinque informazioni due numeri non si possono confrontare. Metrum le rende obbligatorie.

Se non ti sei mai occupato di scientometria, basta tenere a mente tre regole che il modulo incorpora: un dato assente non vale zero; due misure si confrontano solo se hanno lo stesso contratto; un principio di valutazione responsabile non vieta una misura, ne limita l'uso improprio. La pagina «Chi siamo» della Cripta dice che non esistono misure neutrali della qualità della scienza, ma sistemi tecnici che la alterano: Metrum è il modo di tenere questa consapevolezza dentro il grafo.

## Perché si chiama Metrum

*Metrum* è la misura, ma anche il metro del verso: una regola che rende confrontabile ciò che altrimenti sarebbe solo suono. Il manifesto della Cripta descrive, nella svolta del 1936, l'avvio della «quantificazione della scrittura» ([F08 di Dubium](../dubium/term/F08.html)). La scientometria è una delle forme di quella quantificazione. Metrum la accoglie come oggetto dell'ontologia, con la sua provenienza, invece di subirla come un verdetto.

## La prima visita

1. Apri il [catalogo di Metrum](index.html) e cerca **Citazioni ricevute**. La scheda del protocollo mostra la famiglia (ricezione), l'ambito (opera o edizione), l'unità, il metodo in tre lingue, la fonte e i principi che lo orientano.
2. Apri [DORA](term/principle-dora.html). La scheda elenca i protocolli di cui il principio limita l'uso: i sette indicatori di rivista, a cominciare dal fattore d'impatto.
3. Apri il campo FORD [Filosofia, etica e religione](term/ford-6-3.html): vedrai il campo padre, i protocolli non cambiano ma le discipline di Trivium che vi fanno ponte sì.
4. Apri la [gerarchia](schema.html): classi, proprietà, le quattordici famiglie e i cinquantotto protocolli raggruppati.

## Come leggere un protocollo

| Campo | Che cosa significa |
| --- | --- |
| Famiglia | Il gruppo di appartenenza: ricezione, sedi, apertura, trasferimento, dati, software, metodo, saperi umanistici, ricerca sociale, clinica, tecnica, agraria, arti, interventi. |
| Si applica a | L'ambito del soggetto: opera, sede, persona o organizzazione, dati, software, artefatto, intervento, prodotto. Una misura di rivista non si trasferisce a un autore. |
| Tipo di valore | Conteggio intero, decimale, percentuale, quota calcolata o riscontro testuale. |
| Unità | Citazioni, opere, anni, percento, testo. |
| Metodo | Che cosa si fa per ottenere il valore. Un cambiamento del metodo richiede una nuova versione nel servizio. |
| Richiede un insieme di riferimento | Vero per gli indicatori normalizzati (impatto per campo, percentili). |
| Fonte | Il documento pubblico che definisce o discute l'indicatore. |
| Orientato dal principio | I principi DORA, Leiden, CoARA, FAIR, FORCE11 o CRediT pertinenti. |

## Come si scrive un'osservazione

Un'osservazione è una sola applicazione di un protocollo. Questo è l'esempio sintetico incluso in [esempi.ttl](esempi.ttl): l'opera, il corpus e i valori sono inventati, il vocabolario è reale.

```turtle
@prefix mtr: <https://aenigma.criptasemantica.it/metrum#> .
@prefix ex: <https://aenigma.criptasemantica.it/metrum/esempi#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:osservazione-1 a mtr:Observation ;
    mtr:protocol mtr:p-citazioni ;            # quale contratto di misura
    mtr:about ex:opera-dimostrativa ;         # di che cosa
    mtr:state mtr:state-observed ;            # osservato, assente, soppresso, non applicabile
    mtr:coverage mtr:coverage-complete ;      # quanto del corpus è stato esaminato
    mtr:corpusLabel "Corpus sintetico di prova" ;
    mtr:periodStart "2024-01-01"^^xsd:date ; mtr:periodEnd "2024-12-31"^^xsd:date ;
    mtr:acquiredOn "2025-07-01"^^xsd:date ;   # quando è stato letto
    mtr:discipline mtr:ford-6-3 ;             # in quale campo
    mtr:source <https://example.org/corpus> ; # da dove viene il corpus
    mtr:evidence <https://example.org/evidence/1> ;  # la prova dell'osservazione
    mtr:value 12 .
```

Le tre righe che più contano sono `state`, `coverage` e `evidence`. Lo stato dice se il numero esiste; la copertura dice quanto vale; la prova dice dove controllarlo. I [vincoli SHACL](shapes.ttl) respingono un'osservazione «osservata» senza valore, un dato assente con un valore, una copertura parziale senza lettura redazionale, un periodo rovesciato.

## Dal file alla prima interrogazione

```python
from rdflib import Graph

graph = Graph().parse("metrum/metrum.ttl", format="turtle")
graph.parse("metrum/esempi.ttl", format="turtle")
query = """
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?osservazione ?valore ?protocollo WHERE {
  ?osservazione a mtr:Observation ; mtr:state mtr:state-observed ;
      mtr:value ?valore ; mtr:protocol ?p ; mtr:discipline mtr:ford-6-3 .
  ?p skos:prefLabel ?protocollo . FILTER ( lang(?protocollo) = "it" )
}
"""
for row in graph.query(query):
    print(*row)
```

Ottieni le osservazioni con un valore nel campo FORD della filosofia, con il nome del protocollo. Per sapere se due osservazioni sono confrontabili, dichiara un `mtr:Comparison` fra le due e valida con le forme: il confronto è ammesso solo se condividono soggetto, protocollo, corpus, periodo e discipline, con copertura dichiarata.

## I ponti con gli altri moduli

Con **Dubium**: l'intestazione del modulo rimanda a `dub:F08` e `dub:F19`, le posizioni sulla quantificazione della scrittura e sulla quantificazione ontologica, e al capitale semantico. Con **Trivium**: le discipline del sito dichiarano con `skos:broadMatch` il campo FORD in cui si collocano, così un'osservazione su un articolo di «Dialettica» trova il suo campo. Con il **servizio semantico della Cripta**: le classi del vocabolario operativo del servizio sono dichiarate sottoclassi di quelle di Metrum, e i suoi protocolli hanno la stessa chiave: `citazioni@1.0.0` nel servizio è `mtr:p-citazioni` qui.

## Costruire e verificare

Il file `metrum.ttl` è generato da [tools/metrum_from_dictionary.py](../tools/metrum_from_dictionary.py), che legge l'istantanea del dizionario dei protocolli in `fonti/` e contiene, scritti a mano, lo schema, i principi, gli ambiti e le coperture. Dalla radice del repository:

```bash
python3 tools/metrum_from_dictionary.py
python3 tests/verifica.py
python3 tools/build_site.py
```

Il programma di verifica controlla i conteggi (58 protocolli, 48 campi, 35 principi), le fonti, i ponti, i vincoli SHACL sugli esempi e sei alterazioni volute di Metrum, tutte respinte.

## Contribuire

Un nuovo protocollo richiede: chiave in minuscolo, famiglia, ambiti, tipo di valore, unità e metodo in tre lingue, fonte pubblica, principi pertinenti. Se cambia il metodo di un protocollo esistente, la chiave resta e il servizio registra una nuova versione: l'IRI di Metrum identifica il contratto, non la sua versione. Un nuovo principio richiede una fonte pubblica e un'etichetta in tre lingue; se limita l'uso di qualche protocollo, lo dichiara con `mtr:cautions`.
