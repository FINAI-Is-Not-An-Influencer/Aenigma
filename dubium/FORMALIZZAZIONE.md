# Formalizzazione del manifesto

La domanda da conservare è «qual è il senso dell'essere?». Il manifesto la collega alla storia della filosofia, a un modo di scrivere nel Web e alla dipendenza fra diversi modi d'indagine. Il modello permette di seguire questi collegamenti fino al passo che li sostiene, confrontando ciò che il testo afferma con le scelte introdotte per formalizzarlo. [Manifesto della Cripta Semantica](https://criptasemantica.it/)

[Guida per iniziare](README.md) · [English](FORMALIZZAZIONE.en.md) · [Latine](FORMALIZZAZIONE.la.md)

## Come leggere i simboli

La formalizzazione ha tre livelli.

1. **Schema OWL.** Fonti, passi, riferimenti concettuali, voci della ricerca e asserzioni sono tipi distinti. Domanda e posizione sono sottoclassi disgiunte di voce della ricerca. L'inversa di `belongsTo` collega una posizione alle sue asserzioni.
2. **Grafo del discorso.** Un'asserzione relazionale `r` proietta una formula nella forma ⟨concetto di partenza, relazione, concetto di arrivo⟩ entro la posizione `p`. La notazione è `Arco(r,p,s,k,o)`. Ogni posizione collega il passo, il modo di lettura, lo statuto, la forza e la formula. `Parafrasi` indica una riformulazione attribuita alla fonte. `Lettura` esplicita una scelta del modello. `Estensione` individua un raccordo da una pagina di contesto.
3. **Formule.** La notazione è uno strumento di lettura a più registri. `∀x:D` e `∃x:D` restringono la variabile al dominio indicato. `¬`, `∧`, `∨`, `→` e `↔` hanno i consueti usi logici. `:=` introduce un'abbreviazione. `◇` marca una possibilità, `Oₘ` un compito prescritto dal manifesto, `⟦…⟧` una menzione concettuale. I predicati descrittivi, modali e genealogici hanno la lettura indicata nella rispettiva scheda. Una formula complessa può generare più archi di consultazione. Questi archi perdono parte della struttura logica della formula, che resta disponibile in `dub:formula`.

`OInf`, `OAn` e `OFen` abbreviano le indagini informatica, analitica e fenomenologica. `D(T)` è il dominio interpretativo di una teoria e `Dᵣ` è un ambito oggettuale aperto rispetto a una regione. `x∈D` restringe `x` a quell'ambito. `Oₘ` e `◇` restano operatori descrittivi della fonte. Le formule non specificano una semantica a mondi possibili e sono conservate come testo da interpretare. L'inferenza riguarda solo lo schema OWL.

### Passi del testo e schede

| Passo | Articolazione | Schede |
| --- | --- | --- |
| P0 | Titolo, epigrafe, parola «essente», comprensione presunta e perplessità. | F01, Q01 |
| P1 | Compito di porre il problema dell'essere, esordio greco, oralità, memoria scritta, dialogo, reminiscenza e trasformazione della psiche. | F02–F05, Q02 |
| P2 | Tradizione, soglia del 1936, macchina astratta, iperstoria, infosfera, quantificazione della scrittura e destinazione ipertestuale. | F06–F09 |
| P3 | Analogia tra scrittura e iperscrittura, livelli elementare e consapevole, Web, contenuti, significati e capitale semantico. | F10–F13 |
| P4 | Ontologia come specificazione, condivisione e riflessività, trasmissibilità generale o di un contenuto determinato. | F14–F16 |
| P5 | Impegno analitico, contenuto e modo della specificazione, enunciati, variabili vincolate, valori e duplice esigenza di quantificazione. | F17–F20 |
| P6 | Dipendenza fenomenologica, piano formale e regionale, giudizio, usiologia e apertura dell'ambito oggettuale. | F21–F25, Q03 |
| P7 | Ente come cosa, essere di un ente, essere in quanto tale, quattro compiti della tematizzazione, referente-limite e nulla. | F26–F30, Q04 |
| P8 | Senso delle ontologie dell'ente, totalità inespressa, ricerca dell'essenza, problema del senso e produzione dell'ipertesto. | F31–F35, Q05–Q06 |

## Scelte interpretative

**Una genealogia attribuita al testo.** La familiarità dei destinatari dell'epigrafe e la precedente fiducia di chi parla occupano ruoli distinti in F01. F03 e F07 conservano la cronologia e il primato della macchina astratta come affermazioni del manifesto. La soglia filosofica del 1936 è distinta dall'anno bibliografico. L'articolo di Turing riporta ricezione e lettura nel 1936 e figura nel volume 42 dei *Proceedings* (1936–37). Il manifesto lascia implicito il nome di Turing. [Articolo di Turing](https://fab.cba.mit.edu/classes/862.22/notes/computation/Turing-1936.pdf)

**Scrittura, capacità e quantificatori.** F08 tratta la quantificazione della scrittura come processo storico-tecnico. F19 tratta la quantificazione ontologica come relazione fra teoria, enunciato, variabile e valore. La formula `Q(T,φ,v,d)` richiede un'assegnazione ammissibile di `d` a `v` entro `T` e `φ`. F16 distingue `∀c∈D ◇Veicola(p,c)` e `◇Veicola(p,c₀)`. La prima attribuisce una capacità per ogni contenuto del dominio e lascia aperta la questione se tutti siano veicolabili insieme. F21 comprende gli orientamenti a oggetti e iperoggetti, consapevoli o inconsapevoli. La lettura F25 rende esplicito che il dominio è relativo al contesto di ricerca.

**Il doppio uso di “ontologico”.** F26 registra la trattazione ontologica dell'ente in quanto cosa. F27 riguarda i casi in cui un'ontologia dell'ente tematizza l'essere in rapporto a un ente. F28 mette la tematizzazione dell'essere in quanto tale e l'assenza di una cosa prescelta entro l'ambito del compito indicato nel manifesto. Questi tre ruoli sono interrogabili tramite `readingMode`. F29 distingue l'esserci dell'essere, da indicare, dall'esserci a cui è accessibile il contenuto in F13. Sono due sensi registrati secondo la funzione nei rispettivi passi.

**Il nulla e la fondazione.** F30 è una lettura del riferimento-limite. I simboli in ⟦…⟧ parlano di menzioni nel testo, quindi il modello può conservare quel riferimento senza quantificare su un oggetto chiamato «Nulla». `owl:Nothing` è la classe vuota di OWL e ha una funzione logica diversa. F31 rappresenta la fondazione di senso dall'ontologia fondamentale alle ontologie dell'ente. X03 rappresenta il sostegno ontico dall'ontologia informatica alla ricerca, come indicato nella pagina Progetto. Le due direzioni hanno relazioni distinte e nessuna proprietà di transitività. F32 mantiene aperta la totalità dell'indagine. [Progetto](https://criptasemantica.it/progetto/)

## Contesto pubblico

X01–X03 collegano progettualità, gettatezza, le sue quattro determinazioni e la mappa dell'Ente al manifesto. X04 distingue l'ipertesto, il sito che ospita le note e le note che possono riprendere l'ipertesto. X05 collega l'articolo all'articolazione di un'apertura di senso. Le schede X hanno proprie fonti e si possono filtrare in blocco. [Progetto](https://criptasemantica.it/progetto/), [Chi siamo](https://criptasemantica.it/chi-siamo/), [Articoli](https://criptasemantica.it/articoli/)

Nelle applicazioni editoriali un articolo, una tesi, una fonte, un'opera e una misura di ricezione sono risorse con compiti diversi. Un raccordo a Dubium può indicare se l'articolo discute, sviluppa, problematizza o applica una posizione, specificando la fonte e la motivazione. L'IRI della scheda `dub:F27`, per esempio, designa una posizione del manifesto. Un articolo può tematizzare il suo contenuto anche con lessico e identificatori propri.

## Interrogazione di esempio

Questa query recupera chi, secondo il manifesto, riceve senso dall'ontologia fondamentale. Restituisce la posizione, il modo di lettura, il passo e la fonte, oltre al concetto collegato.

```sparql
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>

SELECT ?concetto ?posizione ?lettura ?passo ?fonte WHERE {
  ?arco a dub:RelationAssertion ;
    dub:subjectConcept ?concetto ;
    dub:relationKind dub:rel-riceveSensoDa ;
    dub:objectConcept dub:ontologiaFondamentale ;
    dub:belongsTo ?posizione .
  ?posizione dub:derivedFrom ?passo ; dub:readingMode ?lettura .
  ?passo dub:partOfSource ?fonte .
}
```

Il risultato atteso è `dub:ontologiaEnte` nella posizione `dub:F31`, lettura `dub:Fondamentale`, passo `dub:P8` del manifesto. Per ritrovare il riferimento-limite del nulla, si può cercare `dub:rel-haFiguraLimite`, che riconduce a F30 e al passo P7.

## Estensione e verifica

Per un nuovo passo si crea una scheda con un localizzatore riproducibile. Per una nuova posizione si dichiara la forza dell'enunciato, si indica quale testo la sostiene e si aggiungono gli archi che aiutano a ritrovarla. Una lettura concorrente prende un proprio identificatore e conserva la propria provenienza. È possibile usare più posizioni sullo stesso passo senza far coincidere i loro contenuti.

Con SHACL si verifica che una scheda contenga i dati necessari e che una domanda resti interrogativa. Con OWL si possono dedurre le relazioni strutturali, a partire dalla forma esplicita del grafo. Le prove non decidono la verità delle tesi, la correttezza storiografica dei primati o l'adeguatezza filosofica di tutte le letture. [OWL 2](https://www.w3.org/TR/owl2-syntax/), [SHACL](https://www.w3.org/TR/shacl/)

## Repertorio delle formule

| Scheda | Passo | Formula |
| --- | --- | --- |
| **F01** · Dalla familiarità alla perplessità | P0 | `Cita(epigrafe,sofista244a) ∧ AutoreAttribuito(sofista244a,platone) ∧ TraduzioneAttribuita(epigrafe,pietroChiodi) ∧ Familiarità(voi, «essente», t₀) ∧ Crede(noi, Comprende(noi, «essente»), t₁) ∧ Perplessi(noi, «essente», t₂) ∧ t₁ < t₂` |
| **F02** · Necessità di porre il problema | P1 | `Oₘ Porre(problemaEssere) ∧ Innesca(Oₘ Porre(problemaEssere), pensieroOccidentale)` |
| **F03** · Localizzazione dell'esordio | P1 | `EsordioDi(esordioGreco, pensieroOccidentale) ∧ Luogo(esordioGreco, grecia) ∧ Collocato(esordioGreco, «VII sec. a.C.; I–II sec. AUC»)` |
| **F04** · Filosofia orale e trasmissione scritta | P1 | `CorpoTradizionale(filosofia, pensieroOccidentale) ∧ Orale(filosofia) ∧ ∀p:PraticaDialogica, t:Testo [Trasferisce(filosofia,p,t) → Registra(t,Risultati(p)) ∧ Registra(t,Ricordi(p))]` |
| **F05** · Fine ed effetto del dialogo | P1 | `Fine(praticaDialogica, Reminiscenza(essere)) ∧ ∀a [Partecipa(a,praticaDialogica) → Effetto(praticaDialogica, ScienzaTrasformazione(Psiche(a)))]` |
| **F06** · La tradizione fino alla svolta | P2 | `Tramanda(tradizioneTestuale,filosofia) ∧ Accresce(tradizioneTestuale,filosofia) ∧ Intervallo(tradizioneTestuale,esordioGreco,svolta1936) ∧ DataNelManifesto(svolta1936,1936,2689_AUC)` |
| **F07** · Macchina astratta, iperstoria e infosfera | P2 | `Individua(pubblicazioneMacchina,svolta1936) ∧ Pubblica(pubblicazioneMacchina,macchinaAstratta) ∧ PrimaSecondoIlTesto(macchinaAstratta) ∧ Inaugura(svolta1936,iperstoria) ∧ FaNascere(svolta1936,infosfera)` |
| **F08** · Ostensione della quantificazione nell'ipertesto | P2 | `Avvia(svolta1936,quantificazioneScrittura) ∧ ConLaGenesiDi(web, Ostende(ipertesto,quantificazioneScrittura))` |
| **F09** · Destinazione ipertestuale posteriore alla svolta | P2 | `∀p:ProduzioneFilosofica [Posteriore(p,svolta1936) → DestinataAllaTrasposizione(p,ipertesto)] ∧ IndipendenteDa(destinazioneIpertestuale,consapevolezza)` |
| **F10** · Analogia fra storia e iperstoria | P3 | `InizioCon(storia,scrittura) ∧ Corrisponde(Inizio(iperstoria),Comparsa(iperscrittura))` |
| **F11** · I due livelli dell'iperscrittura | P3 | `∀p [(IperScrittura(p) → Produce(p,ipertesti)) ∧ (Elem(p) → MetteInFunzione(p,testi,macchineAstratte)) ∧ (Consap(p) → MetteInCircuito(p,contenuti,codici,web))]` |
| **F12** · Orientamento del Web | P3 | `SviluppoDi(sviluppoWeb,web) ∧ Fine(sviluppoWeb,Accumulare(capitaleSemantico)) ∧ Fine(sviluppoWeb,Distribuire(capitaleSemantico))` |
| **F13** · Come si costituisce il capitale semantico | P3 | `Costituisce(organizzazioneSemantica,capitaleSemantico) ∧ Media(ontologiaInformatica,organizzazioneSemantica) ∧ ∀c,m [Organizza(organizzazioneSemantica,c,m) → (AccessibileA(c,esserci) ∧ AccessibileA(m,macchinaConcreta))]` |
| **F14** · Specificazione formale, esplicita e condivisa | P4 | `OInf(o) ↔ ∃s,c [Specifica(o,s,c) ∧ Formale(s) ∧ Esplicita(s) ∧ Concettualizzazione(c) ∧ Condivisa(c)]` |
| **F15** · Riflessività della possibilità di trasmissione | P4 | `∀p [Riflessiva(p) → (RifletteSu(p,Consapevolezza(p)) ∧ MiraA(p,PossibilitàDiVeicolare) ∧ ¬FinePrimario(p,VeicolareUnContenuto))]` |
| **F16** · Portata generale e determinata della trasmissibilità | P4 | `Generale(p,D) := ∀c∈D ◇ Veicola(p,c); Determinata(p,c₀) := c₀∈D ∧ ◇ Veicola(p,c₀)` |
| **F17** · Dipendenza dell'informatica dall'analitica | P5 | `∀o:OInf ∃a:OAn [Presuppone(o,a) ∧ ImplicaNelManifesto(o,a) ∧ Integra(Implementazione(o),a) ∧ (Esplicito(Implementazione(o),a) ∨ Implicito(Implementazione(o),a))]` |
| **F18** · Che cosa esiste, che cosa e come si specifica | P5 | `∀a:OAn [Individua(a,Entità,Tipi) ∧ Fornisce(a,Contenuto(concettualizzazione)) ∧ Fornisce(a,Modo(specificazione))]` |
| **F19** · Quantificazione relativa alla teoria | P5 | `Q(T,φ,v,d) := EnunciatoDi(φ,T) ∧ Vincolata(v,φ) ∧ d∈D(T) ∧ ∃g [Ammissibile(g,T,φ) ∧ g(v)=d]` |
| **F20** · Duplice esigenza di quantificazione | P5 | `∀o:OInf ∃T:Teoria [Richiede(o,ContenutoQuantificato(T)) ∧ ConsisteIn(o,iperscrittura) ∧ Richiede(iperscrittura,QuantificazioneOntologica(scritturaSovrastata))]` |
| **F21** · Dipendenza fenomenologica dell'analitica | P6 | `∀a:OAn ∃p:OFen [EffettoDi(a,p)]` |
| **F22** · Articolazione formale e regionale | P6 | `Articolazione(ontologiaFenomenologica; ontologiaFormale, ontologiaRegionale)` |
| **F23** · Oggetto in generale, struttura enunciativa e giudizio | P6 | `ValidePerOgniOggetto(StruttureFormali) ∧ ∀x [IndividuatoDaAnalitica(x) → Specifica(ontologiaFormale,EssereEntità(x))] ∧ Inquadra(ontologiaFormale,StruttureEnunciative) ∧ Richiede(ontologiaFormale,NozioneGiudizio)` |
| **F24** · Usiologia e possibilità regionali | P6 | `∀r:Regione [Fissa(Usiologia(r),EssenzeSpecifiche(r)) ∧ ∀x∈D(r) [IndividuatoDaAnalitica(x) → Specifica(ontologiaRegionale(r),ComePossibile(x,r))]]` |
| **F25** · Il dominio della quantificazione è aperto regionalmente | P6 | `Apre(aperturaFenomenologica,Dᵣ;usiologia(r)) ∧ Quantifica(T,Dᵣ) ∧ PerOgniOggetto_Dᵣ(φ) := ∀x∈Dᵣ φ(x)` |
| **F26** · L'ente trattato ontologicamente nella metafisica | P7 | `∀o [(OFen(o) ∨ OAn(o) ∨ OInf(o)) → (Segue(o,metafisicaOccidentale) ∧ Tema(o,ente,OntologicoComeCosa))]` |
| **F27** · L'essere trattato onticamente nella metafisica | P7 | `∀o:OntologiaDellEnte ∀b [TematizzaEssere(o,b) → ∃x∈D(o) [b=EssereDi(x) ∧ Tratta(o,b,OnticoRelativo)]]` |
| **F28** · Tematizzare l'essere indipendentemente dalla cosa | P7 | `Oₘ [Tratta(oFond,essereInQuantoTale,OntologicoTematico) ∧ ¬∃x [Cosa(x) ∧ OggettoPrescelto(oFond,x)]]` |
| **F29** · Quattro compiti della tematizzazione | P7 | `Oₘ [SpecificaFormalmente(concettualizzazioneEssere) ∧ Indica(esserciDellEssere) ∧ Esprime(essenzaEssere) ∧ Esplicita(ModoPossibilità(essereInQuantoTale))]` |
| **F30** · Ente ontico e nulla come riferimento-limite | P7 | `RiferimentoNelPasso(⟦essere in quanto tale⟧,⟦ente onticamente inteso⟧) ∧ FiguraLimite(⟦ente onticamente inteso⟧,⟦nulla⟧) ∧ ¬Presupposto(∃x [Cosa(x) ∧ ReferentePrescelto(x)])` |
| **F31** · Fondazione del senso delle ontologie dell'ente | P8 | `∀o:OntologiaDellEnte [RiceveSensoDa(o,ontologiaFondamentale)]` |
| **F32** · L'inespresso nella totalità | P8 | `Problematico(essereInQuantoTale) ∧ A_CausaDi(¬EspressaNellaSuaTotalità(ontologiaFondamentale), Problematico(essereInQuantoTale))` |
| **F33** · Ricerca posizionale sull'essenza | P8 | `Sviluppa(ricercaFondamentale,ontologiaFondamentale) ∧ RicercaPosizionale(ricercaFondamentale,problemaEssenzaEssere)` |
| **F34** · Iperscrittura e filo conduttore | P8 | `Oₘ Porre(problemaSensoEssere) ∧ Realizza(iperscritturaFondamentale,Porre(problemaSensoEssere)) ∧ ∀l,p [Pertinenti(l,p,ricercaOntologica) → PuòRaccordare(iperscritturaFondamentale,l,p;problemaSensoEssere)]` |
| **F35** · Cripta come ipertesto prodotto | P8 | `Ipertesto(criptaIpertesto) ∧ Produce(iperscritturaFondamentale,criptaIpertesto)` |
| **X01** · Progettare il fondamento del progettare | XProgetto | `Realizza(criptaIpertesto,progettoCripta) ∧ Tematizza(progettoCripta,progettualita) ∧ Interroga(progettoCripta,FondamentoDelProgettare(progettoCripta))` |
| **X02** · Determinabilità della gettatezza | XProgetto | `DeterminabileCome(gettatezza; oggetto, soggetto, progetto, rigetto) ∧ Riguarda(gettatezza,progettualita)` |
| **X03** · Direzioni della fondazione | XProgetto | `SostegnoOntico(ontologiaInformatica,ricercaFondamentale) ∧ Obiettivo(progettoCripta,mappaEnte) ∧ FondazioneDiSenso(ontologiaFondamentale,ontologiaEnte)` |
| **X04** · Cripta come sito, ipertesto e note | XChiSiamo | `Raccoglie(criptaSito,note) ∧ RicorreIn(criptaIpertesto,note) ∧ PuòComunicare(notaIpertestuale,notaIpertestuale′)` |
| **X05** · Articolo come articolazione di un'apertura | XArticoli | `Artefatto(articolo) ∧ Articola(articolo,senso) ∧ Raccordabile(articolo,ricercaOntologica)` |
