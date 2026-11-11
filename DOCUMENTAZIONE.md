# Mappa della documentazione di Aenigma

[English](en/documentazione.html) · [Latine](la/documentazione.html)

La documentazione di Aenigma vive in tre luoghi che si rimandano a vicenda. **Questo sito** è il riferimento: per ogni modulo offre il catalogo, la gerarchia, una guida per iniziare, la formalizzazione e una pagina per ogni termine, in italiano, inglese e latino. **Il repository** conserva i grafi, i vincoli, gli strumenti, le prove e il registro delle versioni. **La Wiki** raccoglie i capitoli enciclopedici, gli esercizi passo per passo e le procedure. Nessuno dei tre basta da solo; insieme formano un'unica opera, pensata perché il lavoro di codifica sia anche un'esperienza di studio.

## Quattro percorsi di lettura

| Se sei… | Comincia da | Poi |
| --- | --- | --- |
| Chi non sa nulla di ontologie | la [guida di Dubium](dubium/guide.html), che parte da un esempio e arriva alla prima interrogazione | il [capitolo 01 della Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-01) e l'[esercizio del capitolo 03](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-03) |
| Chi usa i dati (sviluppatori, redazioni, servizi) | le pagine «File per il riuso» di ogni catalogo: Turtle, JSON-LD, RDF/XML, contesto, SHACL | i [capitoli 05 e 06](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-05) sull'interrogazione e sugli identificatori, le [procedure del capitolo 15](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-15) |
| Chi studia (ontologia, semiotica, scientometria) | le formalizzazioni di [Dubium](dubium/formal.html), [Trivium](trivium/formal.html) e [Metrum](metrum/formal.html) | i [capitoli 02, 04, 10–13](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT) sul modello, sulla mappa del manifesto e sul ponte fra ontologia e scientometria |
| Chi filosofa | il [manifesto della Cripta Semantica](https://criptasemantica.it/) e la scheda [F28](dubium/term/F28.html), dove l'essere è tematizzato senza un ente prescelto | il [capitolo 14](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-14) sui nomi di Aenigma, Dubium, Trivium e Metrum e il [capitolo 16](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-16) sulle domande aperte |

## I tre moduli, pagina per pagina

| Modulo | Catalogo | Gerarchia | Guida | Formalizzazione | Grafo | Vincoli | Esempi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dubium 0.2.0 · la domanda | [catalogo](dubium/index.html) | [gerarchia](dubium/schema.html) | [guida](dubium/guide.html) | [formalizzazione](dubium/formal.html) | [dubium.ttl](dubium/dubium.ttl) · [JSON-LD](dubium/dubium.jsonld) · [RDF/XML](dubium/dubium.rdf) | [shapes.ttl](dubium/shapes.ttl) | [F27](dubium/term/F27.html) |
| Trivium 0.1.0 · le arti | [catalogo](trivium/index.html) | [gerarchia](trivium/schema.html) | [guida](trivium/guide.html) | [formalizzazione](trivium/formal.html) | [trivium.ttl](trivium/trivium.ttl) · [JSON-LD](trivium/trivium.jsonld) · [RDF/XML](trivium/trivium.rdf) | [shapes.ttl](trivium/shapes.ttl) | [Dialettica](trivium/term/dialettica.html) |
| Metrum 0.1.0 · la misura | [catalogo](metrum/index.html) | [gerarchia](metrum/schema.html) | [guida](metrum/guide.html) | [formalizzazione](metrum/formal.html) | [metrum.ttl](metrum/metrum.ttl) · [JSON-LD](metrum/metrum.jsonld) · [RDF/XML](metrum/metrum.rdf) | [shapes.ttl](metrum/shapes.ttl) | [esempi.ttl](metrum/esempi.ttl) · [Citazioni ricevute](metrum/term/p-citazioni.html) |

La [radice aenigma.ttl](aenigma.ttl) importa i tre moduli e li descrive; [void.ttl](void.ttl) elenca le distribuzioni e il numero di triple. Il [registro delle versioni](CHANGELOG.md) racconta che cosa è cambiato e perché.

## I capitoli della Wiki

1. [Ontologia e domanda dell'essere](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-01)
2. [Il modello del grafo](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-02)
3. [Consultare il catalogo passo per passo](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-03)
4. [Leggere la formalizzazione del manifesto](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-04)
5. [Scaricare, interrogare e verificare](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-05)
6. [IRI, prefissi e integrazione editoriale](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-06)
7. [Aggiungere una voce o una lettura](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-07)
8. [Costruire il sito e collaudare un rilascio](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-08)
9. [Glossario e domande frequenti](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-09)
10. [Aenigma come rete di moduli](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-10)
11. [Trivium: le arti e le discipline della Cripta](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-11)
12. [Metrum: misurare la ricerca con provenienza](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-12)
13. [Dall'ontologia alla scientometria e ritorno](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-13)
14. [I nomi: enigma, dubbio, trivio, misura](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-14)
15. [Procedure: aggiungere un modulo, rilasciare una versione, allineare un vocabolario](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-15)
16. [Versioni, cambiamenti e domande aperte](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-16)

## Come verificare da soli

Chi clona il [repository](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma) può riprodurre ogni controllo senza rete: `python3 tests/verifica.py` prova la rete intera (lettura con due parser, intestazioni, riferimenti fra moduli, SHACL con undici alterazioni, inferenze OWL RL); `python3 dubium/tests/verifica.py` prova Dubium; `python3 tools/export.py`, `python3 tools/build_site.py` e `bash minify.sh` rigenerano esportazioni e sito; `python3 tools/check_site.py` risolve ogni collegamento e ogni ancora. Se il sito che leggi e quello che generi coincidono, la documentazione è quella del grafo.

## Licenza e citazione

I grafi, i testi e le pagine di Aenigma sono rilasciati sotto [Creative Commons Attribuzione 4.0](https://creativecommons.org/licenses/by/4.0/); il codice degli strumenti sotto GNU GPL v3 o successiva. Per citare: «Aenigma. L'ontologia della Cripta Semantica, versione 0.2.0, FINAI e Alessandro Sevardi, 2026, https://aenigma.criptasemantica.it/». Per citare un termine, usa il suo IRI: le pagine sono stabili e le versioni precedenti restano citabili.
