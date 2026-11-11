#!/usr/bin/env python3
"""EN: Build the static reference site of Aenigma: one catalogue, one schema page, one page per term and the
    guides for every module, in three languages, from the Turtle files and the Markdown guides.
LA: Situm staticum Aenigmatis exstrue: indicem, paginam formae, paginam cuiusque vocis et duces cuiusque partis,
    tribus linguis, e tabulis Turtle et ducibus Markdown.

EN: The generator reads only local files and makes no network request. Adding a module means adding an entry
    to MODULES, its texts in site_text.json and its guides; the layout is shared.
LA: Generator tabulas locales tantum legit nec rete petit. Partem addere est MODULES, textus in site_text.json
    et duces addere; forma communis est.
"""

from hashlib import sha256
from html import escape as esc, unescape
import json
from pathlib import Path
from posixpath import dirname, relpath
import re
import shutil
from subprocess import run
from urllib.parse import urlsplit

from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, SKOS, URIRef
from rdflib.namespace import DCTERMS

REPO = Path(__file__).resolve().parents[1]
SITE = "https://aenigma.criptasemantica.it/"
WIKI = "https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki"
TEXT = json.loads(Path(__file__).with_name("site_text.json").read_text(encoding="utf-8"))
LANGUAGES = {"it": "Italiano", "en": "English", "la": "Latine"}
CSP = ("default-src 'none'; style-src 'self'; script-src 'self'; "
       "base-uri 'none'; form-action 'none'; object-src 'none'")
SHARED_CSS_VERSION = sha256((REPO / "style.css").read_bytes()).hexdigest()[:12]
REFERENCE_CSS_VERSION = sha256((REPO / "reference.css").read_bytes()).hexdigest()[:12]
DUB = Namespace(SITE + "dubium#")
TRV = Namespace(SITE + "trivium#")
MTR = Namespace(SITE + "metrum#")
AEN = Namespace(SITE + "aenigma#")
WD = "http://www.wikidata.org/entity/"
PROPERTY_TYPES = (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)

# EN: The module registry: namespace, prefix, example term and the catalogue groups in reading order.
# LA: Index partium: spatium nominum, praefixum, vox exemplaris et partes indicis ordine legendi.
MODULES = {
    "dubium": {
        "prefix": "dub", "ns": DUB, "example": DUB.essereInQuantoTale, "data": "dubium.ttl",
        "groups": {"concepts": (DUB.Concept,), "positions": (DUB.Position,), "questions": (DUB.Question,),
                   "passages": (DUB.Passage,), "classes": (OWL.Class,), "properties": PROPERTY_TYPES,
                   "relations": (DUB.RelationKind,), "values": (DUB.ReadingMode, DUB.Status, DUB.Force),
                   "schemes": (SKOS.ConceptScheme,)},
    },
    "trivium": {
        "prefix": "trv", "ns": TRV, "example": TRV.dialettica, "data": "trivium.ttl",
        "groups": {"disciplines": (TRV.Disciplina,), "genres": (TRV.Genere,), "programmes": (TRV.Programma,),
                   "rooms": (TRV.Stanza,), "collections": (SKOS.Collection,), "schemes": (SKOS.ConceptScheme,),
                   "classes": (OWL.Class,), "properties": PROPERTY_TYPES},
    },
    "metrum": {
        "prefix": "mtr", "ns": MTR, "example": MTR["p-citazioni"], "data": "metrum.ttl",
        "groups": {"protocols": (MTR.Protocol,), "principles": (MTR.Principle,), "disciplines": (MTR.Discipline,),
                   "families": (MTR.Family,), "values": (MTR.Scope, MTR.ValueType, MTR.Coverage, MTR.ResultState),
                   "schemes": (SKOS.ConceptScheme,), "classes": (OWL.Class,), "properties": PROPERTY_TYPES},
    },
}
TABS = {"index.html": "catalogue", "schema.html": "schema", "guide.html": "guide", "formal.html": "formal"}
HIDDEN = {RDF.type, RDFS.label, RDFS.comment, SKOS.prefLabel, DUB.formula, DUB.locator}
# EN: Predicate labels used in the generic description. Local predicates use their own labels from the graph.
# LA: Tituli praedicatorum in descriptione generali. Praedicata localia titulis propriis e grapho utuntur.
PREDICATE_KEYS = {
    SKOS.broader: "broader", SKOS.narrower: "narrower", SKOS.related: "related", SKOS.closeMatch: "close_match",
    SKOS.broadMatch: "broad_match", SKOS.inScheme: "in_scheme", SKOS.topConceptOf: "top_of", SKOS.hasTopConcept: "top_concepts",
    SKOS.scopeNote: "scope_note", SKOS.definition: "definition", SKOS.notation: "notation", SKOS.member: "members",
    DCTERMS.source: "source", DCTERMS.references: "references", DCTERMS.license: "license", DCTERMS.title: "title",
    DCTERMS.description: "description", DCTERMS.creator: "creator", DCTERMS.publisher: "publisher", DCTERMS.issued: "issued",
    DCTERMS.modified: "modified", DCTERMS.language: "language_tag", DCTERMS.isPartOf: "part_of", DCTERMS.hasPart: "has_part",
    RDFS.subClassOf: "parent", RDFS.subPropertyOf: "parent_property", RDFS.domain: "domain", RDFS.range: "range",
    RDFS.seeAlso: "see_also", OWL.inverseOf: "inverse", OWL.versionInfo: "version", OWL.versionIRI: "version_iri",
    OWL.priorVersion: "prior_version", OWL.disjointWith: "disjoint", OWL.imports: "imports",
}
INVERSE_KEYS = {SKOS.broader: "narrower", SKOS.member: "member_of", SKOS.related: "related", SKOS.inScheme: "in_scheme_members",
                MTR.family: "protocols_in_family", MTR.guidedBy: "guided_protocols", MTR.scope: "protocols_for_scope",
                MTR.valueType: "protocols_for_type", MTR.cautions: "cautioned_by", MTR.discipline: None, RDFS.subClassOf: "children",
                RDFS.domain: "used", RDFS.range: "value_of", DUB.concerns: "questions"}
DOCS = [("README", "guide.html"), ("FORMALIZZAZIONE", "formal.html")]


def folder(lang):
    return "." if lang == "it" else lang


def local_name(node, namespace):
    name = str(node).removeprefix(str(namespace))
    if not isinstance(node, URIRef) or not str(node).startswith(str(namespace)) or not re.fullmatch(r"[A-Za-z][\w.-]*", name, re.ASCII):
        raise ValueError(f"Invalid entry: {node}")
    return name


def sorted_values(values):
    return sorted(set(values), key=str)


def translated(graph, node, predicate, lang):
    literals = [value for value in sorted_values(graph.objects(node, predicate)) if isinstance(value, Literal)]
    for preferred in (lang, "it", None):
        for value in literals:
            if value.language == preferred:
                return value
    return literals[0] if literals else None


def literal_html(value, lang, text):
    if value is None:
        return ""
    original, attr = "", ""
    if value.language and value.language != lang:
        attr = f' lang="{esc(value.language)}"'
        if value.language == "it":
            original = f' <small class="original">{esc(text["original"])}</small>'
    return f"<span{attr}>{esc(str(value))}</span>{original}"


def page_path(module, lang, filename):
    return f"{module}/{filename}" if lang == "it" else f"{module}/{lang}/{filename}"


class Site:
    """EN: All modules loaded once, so links can cross module boundaries.
    LA: Omnes partes semel onustae, ut nexus fines partium transire possint.
    """

    def __init__(self):
        self.graphs, self.nodes, self.groups = {}, {}, {}
        for name, module in MODULES.items():
            graph = Graph().parse(REPO / name / module["data"], format="turtle")
            self.graphs[name] = graph
            groups = {}
            for group, types in module["groups"].items():
                nodes = sorted_values(node for kind in types for node in graph.subjects(RDF.type, kind)
                                      if str(node).startswith(str(module["ns"])))
                groups[group] = nodes
            self.groups[name] = groups
            self.nodes[name] = {node: group for group, nodes in groups.items() for node in nodes}
        self.root = Graph().parse(REPO / "aenigma.ttl", format="turtle")

    def module_of(self, node):
        for name, module in MODULES.items():
            if str(node).startswith(str(module["ns"])):
                return name
        return None


class Catalogue:
    """EN: Render one module in one language. Every page is written relative to its own directory.
    LA: Unam partem una lingua redde. Quaeque pagina ad directorium suum relative scribitur.
    """

    def __init__(self, site, name, lang):
        self.site, self.name, self.lang = site, name, lang
        self.module = MODULES[name]
        self.graph = site.graphs[name]
        self.text = TEXT[lang]
        self.mtext = TEXT[lang]["modules"][name]
        self.groups = site.groups[name]
        self.nodes = site.nodes[name]
        self.directory = ""

    # EN: Labels and links.
    # LA: Tituli et nexus.
    def label(self, node, graph=None):
        graph = graph or self.graph
        value = translated(graph, node, RDFS.label, self.lang) or translated(graph, node, SKOS.prefLabel, self.lang)
        if value is None:
            other = self.site.module_of(node)
            if other and other != self.name:
                value = translated(self.site.graphs[other], node, RDFS.label, self.lang)
        if value is not None:
            return literal_html(value, self.lang, self.text)
        if str(node).startswith(WD):
            return esc("wd:" + str(node)[len(WD):])
        return esc(self.graph.namespace_manager.normalizeUri(node))

    def href(self, target):
        return relpath(target, self.directory or ".") if target else ""

    def link(self, node):
        other = self.site.module_of(node)
        if other and node in self.site.nodes[other]:
            target = page_path(other, self.lang, f"term/{local_name(node, MODULES[other]['ns'])}.html")
            return f'<a href="{esc(self.href(target))}">{self.label(node)}</a>'
        if other and node != URIRef(str(MODULES[other]["ns"])):
            target = page_path(other, self.lang, "index.html") + "#" + local_name(node, MODULES[other]["ns"])
            return f'<a href="{esc(self.href(target))}">{self.label(node)}</a>'
        if other:
            return f'<a href="{esc(self.href(page_path(other, self.lang, "index.html")))}">{self.label(node)}</a>'
        if str(node).startswith(str(AEN)):
            return f'<a href="{esc(self.href("index.html"))}">{self.label(node, self.site.root)}</a>'
        if str(node).startswith(WD):
            # EN: The entity IRI stays in the data; readers are sent to the HTTPS page of the item.
            # LA: IRI rei in datis manet; lectores ad paginam HTTPS rei mittuntur.
            return f'<a href="https://www.wikidata.org/wiki/{esc(str(node)[len(WD):])}" rel="external">{self.label(node)}</a>'
        url = urlsplit(str(node))
        if url.scheme not in {"http", "https"} or not url.hostname or url.username or url.password:
            return self.label(node)
        return f'<a href="{esc(str(node))}" rel="external">{self.label(node)}</a>'

    def value_html(self, value):
        if isinstance(value, Literal):
            return literal_html(value, self.lang, self.text)
        return self.link(value)

    def predicate_label(self, predicate):
        if predicate in PREDICATE_KEYS:
            return esc(self.text[PREDICATE_KEYS[predicate]])
        if str(predicate).startswith(str(self.module["ns"])):
            return self.label(predicate)
        return esc(self.graph.namespace_manager.normalizeUri(predicate))

    def choose_literals(self, values):
        # EN: Show the page language; fall back to Italian; otherwise show untagged literals.
        # LA: Linguam paginae ostende; ad Italicam recurre; aliter litteras sine lingua ostende.
        literals = [v for v in values if isinstance(v, Literal)]
        for preferred in (self.lang, "it"):
            chosen = [v for v in literals if v.language == preferred]
            if chosen:
                return chosen
        return [v for v in literals if not v.language]

    def rows(self, node, skip=()):
        rows = []
        for predicate in sorted_values(self.graph.predicates(node)):
            if predicate in HIDDEN or predicate in skip:
                continue
            values = list(self.graph.objects(node, predicate))
            shown = self.choose_literals(values) + [v for v in values if isinstance(v, URIRef)]
            if not shown:
                continue
            html = ", ".join(self.value_html(v) for v in sorted_values(shown))
            rows.append(f"<dt>{self.predicate_label(predicate)}</dt><dd>{html}</dd>")
        for predicate, key in INVERSE_KEYS.items():
            if key is None or predicate in skip:
                continue
            subjects = [s for s in self.graph.subjects(predicate, node) if isinstance(s, URIRef)]
            if subjects:
                html = ", ".join(self.link(s) for s in sorted_values(subjects)[:120])
                rows.append(f"<dt>{esc(self.text[key])}</dt><dd>{html}</dd>")
        return "<dl>" + "".join(rows) + "</dl>" if rows else ""

    def fields(self, groups):
        rows = []
        for key, values in groups:
            values = sorted_values(values)
            if values:
                rows.append(f'<dt>{esc(self.text[key])}</dt><dd>{", ".join(self.link(v) for v in values)}</dd>')
        return "<dl>" + "".join(rows) + "</dl>" if rows else ""

    # EN: Dubium keeps its dedicated rendering; the other groups use the generic description.
    # LA: Dubium descriptionem propriam servat; ceterae partes descriptione generali utuntur.
    def related_positions(self, node):
        arcs = {arc for prop in (DUB.subjectConcept, DUB.objectConcept, DUB.relationKind) for arc in self.graph.subjects(prop, node)}
        return {position for arc in arcs for position in self.graph.objects(arc, DUB.belongsTo)}

    def arcs(self, node):
        items = []
        for arc in sorted_values(self.graph.subjects(DUB.belongsTo, node)):
            nodes = [self.graph.value(arc, prop, any=False) for prop in (DUB.subjectConcept, DUB.relationKind, DUB.objectConcept)]
            if any(n is None for n in nodes):
                raise ValueError(f"Incomplete Dubium relation: {arc}")
            items.append(f'<li id="{local_name(arc, DUB)}" data-fragment>{" · ".join(self.link(n) for n in nodes)}</li>')
        return f'<details><summary>{esc(self.text["arcs"])} ({len(items)})</summary><ul>{"".join(items)}</ul></details>'

    def gloss(self, node):
        for predicate in (RDFS.comment, SKOS.definition, SKOS.scopeNote):
            value = translated(self.graph, node, predicate, self.lang)
            if value is not None:
                return f"<p>{literal_html(value, self.lang, self.text)}</p>"
        return ""

    def entry_content(self, node, group):
        graph = self.graph
        content = self.gloss(node)
        if self.name == "dubium" and group in {"concepts", "relations"}:
            content += self.fields([("in_positions", self.related_positions(node)), ("questions", graph.subjects(DUB.concerns, node))])
            content += self.rows(node, skip=(SKOS.inScheme, DUB.concerns))
        elif self.name == "dubium" and group in {"positions", "questions"}:
            content += self.fields([("source", graph.objects(node, DUB.derivedFrom)), ("mode", graph.objects(node, DUB.readingMode)),
                                    ("status", graph.objects(node, DUB.status)), ("force", graph.objects(node, DUB.force)),
                                    ("concerns", graph.objects(node, DUB.concerns))])
            if group == "positions":
                formula = esc(str(graph.value(node, DUB.formula)))
                content += f'<p class="formula"><strong>{esc(self.text["formula"])}</strong><code>{formula}</code></p>'
                content += self.arcs(node)
        elif self.name == "dubium" and group == "passages":
            locator = translated(graph, node, DUB.locator, self.lang)
            content += f"<p>{literal_html(locator, self.lang, self.text)}</p>"
            content += self.fields([("source", graph.objects(node, DUB.partOfSource)), ("in_positions", graph.subjects(DUB.derivedFrom, node))])
        elif self.name == "dubium" and group == "values":
            entries = {e for prop in (DUB.readingMode, DUB.status, DUB.force) for e in graph.subjects(prop, node)}
            content += self.fields([("in_positions", entries)])
        else:
            skip = (SKOS.scopeNote, SKOS.definition) if content else ()
            content += self.rows(node, skip=skip)
        return content

    def entry(self, node, group):
        name = local_name(node, self.module["ns"])
        return (f'<article id="{name}" class="entry" data-entry>'
                f'<h3><a href="{esc(self.href(page_path(self.name, self.lang, f"term/{name}.html")))}" title="{esc(self.text["permalink"])}">{self.label(node)}</a></h3>'
                f'<p class="identifier" title="{esc(str(node))}"><code>{self.module["prefix"]}:{name}</code></p>'
                f'{self.entry_content(node, group)}</article>')

    def example(self, node, group):
        # EN: Show triples from the published graph, so each example can be checked.
        # LA: Tripla e grapho publico ostende, ut exemplum probari possit.
        graph = self.graph
        if group == "properties":
            triples = graph.triples((None, node, None))
        elif group == "classes":
            triples = graph.triples((None, RDF.type, node))
        else:
            triples = ((node, p, o) for p in (RDF.type, SKOS.broader, SKOS.closeMatch, MTR.family, MTR.scope, DUB.derivedFrom,
                       DUB.partOfSource, DUB.concerns, SKOS.prefLabel, RDFS.label) for o in graph.objects(node, p))
        triples = sorted((row for row in triples if all(isinstance(t, (URIRef, Literal)) for t in row)), key=lambda r: tuple(map(str, r)))
        if not triples:
            triples = sorted_values(graph.triples((node, RDF.type, None)))

        def as_turtle(term):
            for name, module in MODULES.items():
                if isinstance(term, URIRef) and str(term).startswith(str(module["ns"])) and term != URIRef(str(module["ns"])):
                    return f"{module['prefix']}:{local_name(term, module['ns'])}"
            if isinstance(term, URIRef) and str(term).startswith(WD):
                return "wd:" + str(term)[len(WD):]
            return term.n3(graph.namespace_manager)

        prefixes = sorted({as_turtle(t).split(":")[0] for row in triples[:3] for t in row if isinstance(t, URIRef) and ":" in as_turtle(t) and not as_turtle(t).startswith("<")})
        known = {m["prefix"]: str(m["ns"]) for m in MODULES.values()} | {"wd": WD} | {p: str(n) for p, n in graph.namespaces()}
        sample = [f"@prefix {p}: <{known[p]}> ." for p in prefixes if p in known] + [""]
        for subject, predicate, obj in triples[:3]:
            verb = "a" if predicate == RDF.type else as_turtle(predicate)
            sample.append(f"{as_turtle(subject)} {verb} {as_turtle(obj)} .")
        return (f'<section><h2>{esc(self.text["sample"])}</h2><p>{esc(self.text["sample_note"])}</p>'
                f'<pre><code>{esc(chr(10).join(sample))}</code></pre></section>')

    def render_term(self, node, group):
        name = local_name(node, self.module["ns"])
        self.directory = dirname(page_path(self.name, self.lang, f"term/{name}.html"))
        title = translated(self.graph, node, RDFS.label, self.lang) or translated(self.graph, node, SKOS.prefLabel, self.lang)
        index = self.href(page_path(self.name, self.lang, "index.html"))
        content = f"""
<nav class="breadcrumbs" aria-label="{esc(self.text["path"])}">
  <a href="{esc(index)}">{esc(self.mtext["title"])}</a>
  <a href="{esc(index)}#{group}">{esc(self.text[group])}</a>
</nav>
<article class="term" id="{name}">
  <p class="eyebrow">{esc(self.text[group])}</p>
  <h1>{self.label(node)}</h1>
  <p class="identifier"><code>{self.module["prefix"]}:{name}</code></p>
  <p class="term-iri"><span>IRI</span> <code>{esc(str(node))}</code></p>
  <div class="term-description terminal-panel">{self.entry_content(node, group)}</div>
{self.example(node, group)}
  <p><a href="{esc(index)}#{name}">{esc(self.text["in_catalogue"])}</a></p>
</article>"""
        return self.page(f"term/{name}.html", content, title=str(title) if title is not None else name)

    def tree(self, roots, children):
        def branch(node, ancestors):
            kids = sorted_values(child for child in children(node) if child not in ancestors and child != node)
            nested = "".join(branch(k, ancestors | {node}) for k in kids)
            return f"<li>{self.link(node)}" + (f"<ul>{nested}</ul>" if nested else "") + "</li>"
        return "".join(branch(r, set()) for r in roots)

    def render_schema(self):
        graph, t = self.graph, self.text
        self.directory = dirname(page_path(self.name, self.lang, "schema.html"))
        classes = set(self.groups.get("classes", []))
        roots = sorted_values(n for n in classes if not classes.intersection(graph.objects(n, RDFS.subClassOf)))
        class_tree = self.tree(roots, lambda n: classes.intersection(graph.subjects(RDFS.subClassOf, n)))
        rows = []
        for node in self.groups.get("properties", []):
            domain = ", ".join(self.link(v) for v in sorted_values(graph.objects(node, RDFS.domain)))
            ranges = ", ".join(self.link(v) for v in sorted_values(graph.objects(node, RDFS.range)))
            rows.append(f'<tr><th scope="row">{self.link(node)}</th><td>{domain}</td><td>{ranges}</td></tr>')
        schemes = ""
        for scheme in self.groups.get("schemes", []):
            tops = sorted_values(graph.objects(scheme, SKOS.hasTopConcept))
            if self.name == "metrum" and scheme == MTR.protocolli:
                families = sorted_values(graph.subjects(RDF.type, MTR.Family))
                items = "".join(f"<li>{self.link(f)}<ul>{''.join(f'<li>{self.link(p)}</li>' for p in sorted_values(graph.subjects(MTR.family, f)))}</ul></li>" for f in families)
            else:
                items = self.tree(tops, lambda n: graph.subjects(SKOS.broader, n))
            schemes += f'<section><h2>{self.label(scheme)}</h2><ul class="class-tree">{items}</ul></section>'
        content = f"""
<article class="prose schema-reference">
  <p class="eyebrow">{esc(self.mtext["edition"])}</p>
  <h1>{esc(t["schema"])}</h1>
  <p>{esc(t["schema_note"])}</p>
  <section><h2>{esc(t["classes"])}</h2><ul class="class-tree">{class_tree}</ul></section>
  <section><h2>{esc(t["properties"])}</h2><div class="table-scroll">
    <table><thead><tr><th scope="col">{esc(t["property"])}</th>
      <th scope="col">{esc(t["domain"])}</th><th scope="col">{esc(t["range"])}</th>
    </tr></thead><tbody>{"".join(rows)}</tbody></table>
  </div></section>
  {schemes}
</article>"""
        return self.page("schema.html", content)

    def render_index(self):
        graph, t = self.graph, self.text
        self.directory = dirname(page_path(self.name, self.lang, "index.html"))
        index, sections = [], []
        for group, nodes in self.groups.items():
            if not nodes:
                continue
            label = esc(t[group])
            index.append(f'<a href="#{group}">{label} <span>{len(nodes)}</span></a>')
            cards = "".join(self.entry(node, group) for node in nodes)
            sections.append(f'<section id="{group}" data-group><h2>{label}</h2><div class="entries">{cards}</div></section>')
        ontology = URIRef(str(self.module["ns"]))
        version = graph.value(ontology, OWL.versionInfo)
        version_node = graph.value(ontology, OWL.versionIRI)
        downloads = "".join(f'<li><a href="{esc(self.href(f"{self.name}/{f}"))}">{esc(t[key])}</a></li>' for f, key in (
            (f"{self.name}.ttl", "turtle"), (f"{self.name}.jsonld", "jsonld"), (f"{self.name}.rdf", "rdfxml"),
            ("context.jsonld", "context"), ("shapes.ttl", "shapes")))
        content = f"""
<header class="hero terminal-panel">
  <p class="eyebrow">{esc(self.mtext["edition"])}</p><h1>{esc(self.mtext["title"])}</h1>
  <p class="intro">{esc(self.mtext["description"])}</p>
  <div class="actions"><a class="primary" href="guide.html">{esc(t["start"])}</a>
    <a href="schema.html">{esc(t["schema"])}</a>
    <a href="{esc(self.href(page_path(self.name, self.lang, f"term/{local_name(self.module['example'], self.module['ns'])}.html")))}">{esc(self.mtext["example"])}</a></div>
</header>
<div class="desk">
  <nav class="index" aria-label="{esc(t["sections"])}">{"".join(index)}</nav>
  <div class="results">
    <div class="filter" hidden data-search-panel>
      <label for="lookup">{esc(t["filter"])}</label>
      <input id="lookup" type="search" placeholder="{esc(self.mtext["placeholder"])}" autocomplete="off">
      <p role="status" data-count data-label="{esc(t["count"])}" data-empty="{esc(t["empty"])}"></p>
    </div>
    {"".join(sections)}
    <section id="downloads" class="downloads">
      <h2>{esc(t["download"])}</h2>
      <p id="{local_name(version_node, self.module["ns"])}">{esc(t["version"])} <code>{esc(str(version))}</code></p>
      <ul>{downloads}<li><a href="{esc(self.href("aenigma.ttl"))}">{esc(t["root_file"])}</a></li>
        <li><a href="https://criptasemantica.it/">{esc(t["manifesto"])}</a></li></ul>
    </section>
  </div>
</div>"""
        return self.page("index.html", content, search=True)

    def render_document(self, stem, filename):
        self.directory = dirname(page_path(self.name, self.lang, filename))
        suffix = "" if self.lang == "it" else f".{self.lang}"
        source = REPO / self.name / f"{stem}{suffix}.md"
        return self.page(filename, document(source, self.name, self.lang))

    def page(self, filename, content, search=False, title=None):
        # EN: Use relative links so a plain HTTP server and GitHub Pages serve the same files.
        # LA: Nexus relativos adhibe, ut idem opus localiter et in GitHub Pages praebeatur.
        t = self.text
        current = page_path(self.name, self.lang, filename)
        self.directory = dirname(current)
        assets = self.href(".")
        prefix = "" if assets == "." else assets + "/"
        local_prefix = self.href(dirname(page_path(self.name, self.lang, "index.html")))
        local_prefix = "" if local_prefix == "." else local_prefix + "/"
        title = f'{self.mtext["title"]} · {title or t[TABS[filename]]}'
        home = f"{prefix}index.html"
        modules = [f'<a href="{home}">Aenigma</a>']
        for name in MODULES:
            current_module = ' aria-current="page"' if name == self.name else ""
            modules.append(f'<a href="{esc(self.href(page_path(name, self.lang, "index.html")))}"{current_module}>{esc(TEXT[self.lang]["modules"][name]["title"])}</a>')
        modules.append(f'<a href="{esc(self.href("documentazione.html" if self.lang == "it" else f"{self.lang}/documentazione.html"))}">{esc(t["docs_map"])}</a>')
        modules.append(f'<a href="{WIKI}/{self.lang.upper()}">{esc(t["wiki"])}</a>')
        tabs = []
        for file, key in TABS.items():
            current_tab = ' aria-current="page"' if filename == file else ""
            tabs.append(f'<a href="{local_prefix}{file}"{current_tab}>{esc(t[key])}</a>')
        languages, alternate = [], []
        for code, name in LANGUAGES.items():
            target = page_path(self.name, code, filename)
            current_lang = ' aria-current="page"' if code == self.lang else ""
            languages.append(f'<a href="{esc(self.href(target))}" lang="{code}" hreflang="{code}" data-language{current_lang}>{name}</a>')
            alternate.append(f'<link rel="alternate" hreflang="{code}" href="{SITE}{target}">')
        script = f'<script src="{prefix}search.js" defer></script>' if search else ""
        return f"""<!doctype html>
<html lang="{self.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta http-equiv="Content-Security-Policy" content="{esc(CSP)}">
<meta name="referrer" content="no-referrer">
<meta name="description" content="{esc(self.mtext["description"])}">
<title>{esc(title)}</title>
<link rel="canonical" href="{SITE}{current}">
{"".join(alternate)}
<link rel="stylesheet" href="{prefix}style.css?v={SHARED_CSS_VERSION}">
<link rel="stylesheet" href="{prefix}reference.css?v={REFERENCE_CSS_VERSION}">
{script}
</head>
<body class="reference-page">
<a class="skip-link" href="#main">{esc(t["skip"])}</a>
<div class="container">
  <header>
    <p class="site-brand">AENIGMA</p>
    <nav class="site-nav" aria-label="{esc(t["navigation"])}">{"".join(modules)}</nav>
    <nav class="site-nav module-nav" aria-label="{esc(self.mtext["title"])}">{"".join(tabs)}</nav>
    <nav class="site-languages" aria-label="{esc(t["language"])}">{"".join(languages)}</nav>
  </header>
  <main id="main">{content}</main>
  <footer>
    <nav class="footer-nav" aria-label="{esc(t["footer_nav"])}">
      <a href="{home}">Aenigma</a>
      <a href="https://criptasemantica.it/">Cripta Semantica</a>
      <a href="{home}#nav-policies">{esc(t["legal"])}</a>
    </nav>
  </footer>
</div>
</body>
</html>
"""


def document(source, module, lang, directory=None):
    # EN: Markdown is local and trusted as prose; disable raw HTML and check link rewrites.
    # LA: Markdown localis ut prosa legitur; HTML crudum excluditur et nexus probantur.
    raw = source.read_text(encoding="utf-8")
    html = run(["pandoc", "--from=gfm-raw_html", "--to=html5", "--wrap=none"], input=raw, text=True, capture_output=True, check=True).stdout
    mapping = {f"{stem}{'' if code == 'it' else '.' + code}.md": page_path(module, code, output)
               for code in LANGUAGES for stem, output in DOCS} if module else {}
    directory = directory if directory is not None else dirname(page_path(module, lang, "guide.html"))

    def rewrite(match):
        link = unescape(match[1])
        path, mark, fragment = link.partition("#")
        url = urlsplit(link)
        if url.scheme in {"http", "https"} and url.hostname and not url.username and not url.password:
            return match[0]
        if url.scheme or url.netloc or path.startswith("/"):
            raise ValueError(f"Unsupported documentation link: {link}")
        if not path:
            return match[0]
        if path in mapping:
            target = mapping[path]
        elif module is None:
            target = path
        elif path.startswith("../"):
            target = path[3:]
        else:
            target = f"{module}/{path}"
        if ".." in target.split("/"):
            raise ValueError(f"Unsupported documentation link: {link}")
        return f'href="{esc(relpath(target, directory) + mark + fragment)}"'

    result = re.sub(r'href="([^"]+)"', rewrite, html)
    return f'<article class="prose">{result}</article>'


def root_page(site, lang, path):
    """EN: The documentation map is a root page outside any module; it shares the frame of the reference.
    LA: Tabula documentorum pagina radicis extra partes est; compagem indicis communicat.
    """
    t = TEXT[lang]
    directory = dirname(path)
    rel = lambda target: relpath(target, directory or ".")
    prefix = "" if rel(".") == "." else rel(".") + "/"
    suffix = "" if lang == "it" else f".{lang}"
    content = document(REPO / f"DOCUMENTAZIONE{suffix}.md", None, lang, directory)
    modules = [f'<a href="{esc(rel("index.html"))}">Aenigma</a>']
    for name in MODULES:
        modules.append(f'<a href="{esc(rel(page_path(name, lang, "index.html")))}">{esc(t["modules"][name]["title"])}</a>')
    modules.append(f'<a href="{esc(rel(path))}" aria-current="page">{esc(t["docs_map"])}</a>')
    modules.append(f'<a href="{WIKI}/{lang.upper()}">{esc(t["wiki"])}</a>')
    languages, alternate = [], []
    for code, name in LANGUAGES.items():
        target = "documentazione.html" if code == "it" else f"{code}/documentazione.html"
        current = ' aria-current="page"' if code == lang else ""
        languages.append(f'<a href="{esc(rel(target))}" lang="{code}" hreflang="{code}"{current}>{name}</a>')
        alternate.append(f'<link rel="alternate" hreflang="{code}" href="{SITE}{target}">')
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta http-equiv="Content-Security-Policy" content="{esc(CSP)}">
<meta name="referrer" content="no-referrer">
<meta name="description" content="{esc(t["docs_description"])}">
<title>Aenigma · {esc(t["docs_map"])}</title>
<link rel="canonical" href="{SITE}{path}">
{"".join(alternate)}
<link rel="stylesheet" href="{prefix}style.css?v={SHARED_CSS_VERSION}">
<link rel="stylesheet" href="{prefix}reference.css?v={REFERENCE_CSS_VERSION}">
</head>
<body class="reference-page">
<a class="skip-link" href="#main">{esc(t["skip"])}</a>
<div class="container">
  <header>
    <p class="site-brand">AENIGMA</p>
    <nav class="site-nav" aria-label="{esc(t["navigation"])}">{"".join(modules)}</nav>
    <nav class="site-languages" aria-label="{esc(t["language"])}">{"".join(languages)}</nav>
  </header>
  <main id="main">{content}</main>
  <footer>
    <nav class="footer-nav" aria-label="{esc(t["footer_nav"])}">
      <a href="{esc(rel("index.html"))}">Aenigma</a>
      <a href="https://criptasemantica.it/">Cripta Semantica</a>
      <a href="{esc(rel("index.html"))}#nav-policies">{esc(t["legal"])}</a>
    </nav>
  </footer>
</div>
</body>
</html>
"""


def main():
    site = Site()
    outputs = {}
    for name in MODULES:
        for lang in LANGUAGES:
            catalogue = Catalogue(site, name, lang)
            outputs[page_path(name, lang, "index.html")] = catalogue.render_index()
            outputs[page_path(name, lang, "schema.html")] = catalogue.render_schema()
            for group, nodes in catalogue.groups.items():
                for node in nodes:
                    outputs[page_path(name, lang, f"term/{local_name(node, MODULES[name]['ns'])}.html")] = catalogue.render_term(node, group)
            for stem, filename in DOCS:
                outputs[page_path(name, lang, filename)] = catalogue.render_document(stem, filename)
    # EN: Render all pages successfully before replacing any output; then clear stale term pages.
    # LA: Omnes paginas ante mutationem tabularum perfice; deinde paginas vocum obsoletas dele.
    for name in MODULES:
        for lang in LANGUAGES:
            term_dir = REPO / dirname(page_path(name, lang, "term/x.html"))
            if term_dir.is_dir():
                for stale in term_dir.glob("*.html"):
                    if page_path(name, lang, f"term/{stale.name}") not in outputs:
                        stale.unlink()
    for path, content in outputs.items():
        file = REPO / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")
    # EN: Keep the former stylesheet and script paths of Dubium for pages still held in proxy caches.
    # LA: Vias priores styli et scripti Dubii serva pro paginis adhuc in memoriis intermediis retentis.
    shutil.copyfile(REPO / "reference.css", REPO / "dubium" / "site.css")
    shutil.copyfile(REPO / "search.js", REPO / "dubium" / "search.js")
    for lang in LANGUAGES:
        path = "documentazione.html" if lang == "it" else f"{lang}/documentazione.html"
        file = REPO / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(root_page(site, lang, path), encoding="utf-8")
    print(f"{len(outputs)} pages written")


if __name__ == "__main__":
    main()
