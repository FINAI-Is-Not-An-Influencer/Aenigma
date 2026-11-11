# Aenigma

[English](README.en.md) · [Latine](README.la.md) · [Sito di riferimento](https://aenigma.criptasemantica.it/) · [Mappa della documentazione](https://aenigma.criptasemantica.it/documentazione.html) · [Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT)

Aenigma è l'ontologia web della [Cripta Semantica](https://criptasemantica.it/), l'ipertesto ontologico fondamentale. Dalla versione 0.2.0 è una **rete di tre moduli**, ciascuno con il proprio spazio di nomi, la propria versione, tre lingue e vincoli propri:

| Modulo | Prefisso | Che cosa nomina | Versione |
| --- | --- | --- | --- |
| [Dubium](dubium/README.md) · la domanda | `dub:` | Concetti, posizioni, domande e passi del manifesto filosofico, con la fonte di ogni tesi | 0.2.0 |
| [Trivium](trivium/README.md) · le arti | `trv:` | Le duecento discipline, i generi, le linee di programma e le stanze del sito, con Wikidata e i campi FORD | 0.1.0 |
| [Metrum](metrum/README.md) · la misura | `mtr:` | L'osservazione scientometrica qualificata: protocolli, famiglie, ambiti, coperture, campi FORD e principi di valutazione responsabile | 0.1.0 |

La [radice `aenigma.ttl`](aenigma.ttl) importa i tre moduli e li descrive; [`void.ttl`](void.ttl) ne elenca le distribuzioni. Il nome viene dall'enigma greco: una formulazione che nasconde ciò che mostra. I nomi dell'ontologia non esauriscono le cose; servono a tenere aperta la domanda sul senso dell'essere mentre la si rende consultabile da persone e programmi.

## Dalla filosofia al grafo

Il manifesto della Cripta parte dalla perplessità del *Sofista* sulla parola «essente» e lega la domanda sull'essere alla storia della scrittura: con la macchina astratta del 1936 inizia l'iperstoria e la scrittura si quantifica; l'iperscrittura produce ipertesti e il Web accumula capitale semantico per mezzo di ontologie. Dubium formalizza questo testo passo per passo. Trivium prende sul serio il modo in cui il sito ordina il sapere: il trivio delle arti del discorso e un quadrivio in cui la geografia sostituisce la geometria. Metrum accoglie la quantificazione della scrittura come oggetto dell'ontologia, con la sua provenienza, invece di subirla come un verdetto. Insieme i tre moduli tracciano il percorso dalla domanda ai nomi e dai nomi alla misura, e ritorno. [Capitolo 14 della Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-14)

## Una prima visita

1. Apri la [scheda F27](https://aenigma.criptasemantica.it/dubium/term/F27.html) di Dubium: una posizione del manifesto, il passo che la sostiene, la formula e le relazioni.
2. Apri [Dialettica](https://aenigma.criptasemantica.it/trivium/term/dialettica.html) in Trivium: la descrizione d'autore, i rami, la corrispondenza Wikidata e il campo FORD.
3. Apri [Citazioni ricevute](https://aenigma.criptasemantica.it/metrum/term/p-citazioni.html) in Metrum: famiglia, ambito, unità, metodo e i principi che ne limitano l'uso.
4. Cambia lingua in alto: ogni pagina esiste in italiano, inglese e latino.

## Che cosa contiene il repository

| Percorso | Contenuto |
| --- | --- |
| `aenigma.ttl`, `void.ttl` | Radice della rete e descrizione delle distribuzioni |
| `dubium/`, `trivium/`, `metrum/` | Per ogni modulo: grafo Turtle, JSON-LD, RDF/XML, contesto JSON-LD, vincoli SHACL, guide e formalizzazioni in tre lingue, pagine del sito |
| `metrum/esempi.ttl`, `metrum/fonti/`, `trivium/fonti/` | Esempi sintetici e istantanee delle fonti pubbliche usate dai generatori |
| `tools/` | Generatori dei moduli (`trivium_from_taxonomy.py`, `metrum_from_dictionary.py`), esportatore (`export.py`), generatore del sito (`build_site.py`), tabelle della documentazione (`doc_tables.py`), controllo dei collegamenti (`check_site.py`) |
| `tests/verifica.py`, `dubium/tests/verifica.py` | Collaudo della rete e collaudo di Dubium |
| `index.src.html`, `minify.sh`, `style.css`, `reference.css`, `search.js` | Homepage e telaio grafico del sito |
| `DOCUMENTAZIONE*.md`, `CHANGELOG.md` | Mappa della documentazione e registro delle versioni |

## Riutilizzare i dati

Ogni modulo si carica da solo (`dubium/dubium.ttl`, `trivium/trivium.ttl`, `metrum/metrum.ttl`) oppure tutti insieme dalla radice. I prefissi preferiti sono `dub:`, `trv:`, `mtr:` e `aen:`; `wd:` indica Wikidata. Con RDFLib:

```python
from rdflib import Graph

graph = Graph()
for module in ("dubium", "trivium", "metrum"):
    graph.parse(f"{module}/{module}.ttl", format="turtle")
query = """
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?disciplina ?campo ?concetto WHERE {
  ?disciplina skos:broadMatch ?campo ; skos:related ?concetto .
  ?campo a mtr:Discipline . ?concetto a dub:Concept .
}
"""
for row in graph.query(query):
    print(*row)
```

L'interrogazione attraversa i tre moduli: discipline del sito, campo FORD in cui si collocano, concetto del manifesto con cui leggerle. Le relazioni fra vocabolari sono sempre `skos:closeMatch`, `skos:broadMatch`, `skos:related` o sottoclassi: mai equivalenze.

## Verificare e costruire in locale

Servono Python 3 con RDFLib, pySHACL e OWL-RL, Raptor (`rapper`), Pandoc, OpenSSL e Clean CSS (`cleancss`). Dalla radice del repository:

```bash
python3 tests/verifica.py
python3 dubium/tests/verifica.py
python3 tools/export.py
python3 tools/build_site.py
bash minify.sh
python3 tools/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Il primo programma legge ogni modulo con due parser, controlla intestazioni e versioni, risolve i riferimenti fra moduli, valida con SHACL e respinge undici alterazioni, calcola le inferenze OWL RL e verifica che nessuna classe disgiunta riceva individui comuni. Il generatore del sito non fa richieste di rete; il controllo finale risolve ogni collegamento e ogni ancora delle pagine. [Capitolo 08](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-08) · [Capitolo 15](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-15)

## Contribuire

Una nuova lettura del manifesto entra in Dubium con una posizione nuova e la propria provenienza ([procedura](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-07)). Una nuova categoria del sito entra in Trivium con una nuova istantanea e le etichette nelle tre lingue. Un nuovo protocollo entra in Metrum con famiglia, ambito, unità, metodo in tre lingue, fonte e principi. Un nuovo modulo prende uno spazio di nomi proprio, una voce nella radice e nel generatore del sito, e un collaudo ([procedura](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-15)). Gli identificatori pubblicati non si cambiano; le versioni si dichiarano con `owl:versionIRI` e `owl:priorVersion`.

## Licenze e citazione

Il contenuto dell'ontologia (grafi, testi, pagine) è rilasciato sotto [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) e va attribuito a FINAI e Alessandro Sevardi; il codice degli strumenti è sotto [GNU GPL v3 o successiva](LICENSE). Per citare: «Aenigma. L'ontologia della Cripta Semantica, versione 0.2.0, 2026, https://aenigma.criptasemantica.it/». Il repository su GitHub è la fonte di verità; il sito è pubblicato da GitHub Pages e servito anche dal dominio della Cripta.
