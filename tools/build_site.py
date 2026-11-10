#!/usr/bin/env python3
"""EN: Build the static catalogue and the three editions of the guides.
LA: Indicem staticum et tres editiones ducum gigne.
"""

from html import escape as esc, unescape
import json
from pathlib import Path
from posixpath import dirname, relpath
import re
from subprocess import run
from urllib.parse import urlsplit

from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef

ROOT = Path(__file__).resolve().parents[1] / "dubium"
DUB = Namespace("https://aenigma.criptasemantica.it/dubium#")
SITE = "https://aenigma.criptasemantica.it/dubium/"
WIKI = "https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki"
TEXT = json.loads(Path(__file__).with_name("site_text.json").read_text(encoding="utf-8"))
LANGUAGES = {"it": "Italiano", "en": "English", "la": "Latine"}
CSP = ("default-src 'none'; style-src 'self'; script-src 'self'; "
       "base-uri 'none'; form-action 'none'; object-src 'none'")
GROUPS = {
    "concepts": (DUB.Concept,), "positions": (DUB.Position,), "questions": (DUB.Question,),
    "passages": (DUB.Passage,), "classes": (OWL.Class,),
    "properties": (OWL.ObjectProperty, OWL.DatatypeProperty),
    "relations": (DUB.RelationKind,), "values": (DUB.ReadingMode, DUB.Status, DUB.Force),
}
TABS = {"index.html": "catalogue", "schema.html": "schema",
        "guide.html": "guide", "formal.html": "formal"}
DOCS = {
    f"{stem}{'' if lang == 'it' else '.' + lang}.md": path
    for lang in LANGUAGES
    for stem, output in [("README", "guide.html"), ("FORMALIZZAZIONE", "formal.html")]
    for path in [f"{lang}/{output}" if lang != "it" else output]
}


def folder(lang):
    return "." if lang == "it" else lang


def local_id(node):
    # EN: Only names in this namespace may become fragment identifiers.
    # LA: Sola nomina huius spatii in signa fragmentorum vertuntur.
    name = str(node).removeprefix(str(DUB))
    if not isinstance(node, URIRef) or not str(node).startswith(str(DUB)) or not re.fullmatch(r"[A-Za-z][\w.-]*", name, re.ASCII):
        raise ValueError(f"Invalid Dubium entry: {node}")
    return name


def sorted_values(values):
    return sorted(set(values), key=str)


def term_file(node):
    return f"term/{local_id(node)}.html"


def translated(graph, node, predicate, lang):
    literals = [value for value in sorted_values(graph.objects(node, predicate))
                if isinstance(value, Literal)]
    for preferred in (lang, "it", None):
        for value in literals:
            if value.language == preferred:
                return value
    return None


def literal_html(value, lang, text):
    if value is None:
        return ""
    original = ""
    attr = ""
    if value.language and value.language != lang:
        attr = f' lang="{esc(value.language)}"'
        if value.language == "it":
            original = f' <small class="original">{esc(text["original"])}</small>'
    return f"<span{attr}>{esc(str(value))}</span>{original}"


class Catalogue:
    """EN: Render all names from the same local graph in a stable order.
    LA: Omnia nomina eodem grapho locali ordine stabili exhibe.
    """

    def __init__(self, graph, lang):
        self.graph = graph
        self.lang = lang
        self.text = TEXT[lang]
        self.groups = {}
        for group, types in GROUPS.items():
            nodes = sorted_values(node for kind in types for node in graph.subjects(RDF.type, kind)
                                  if str(node).startswith(str(DUB)))
            if group in {"concepts", "relations"}:
                nodes.sort(key=lambda node: str(translated(graph, node, RDFS.label, lang)).casefold())
            self.groups[group] = nodes
        self.nodes = {node for nodes in self.groups.values() for node in nodes}

    def label(self, node):
        value = translated(self.graph, node, RDFS.label, self.lang)
        if value is not None:
            return literal_html(value, self.lang, self.text)
        return esc(self.graph.namespace_manager.normalizeUri(node))

    def link(self, node, prefix=""):
        if node in self.nodes:
            href = prefix + term_file(node)
        elif str(node).startswith(str(DUB)) and node != URIRef(str(DUB)):
            href = prefix + "index.html#" + local_id(node)
        else:
            # EN: External resources are explicit links. Rendering makes no requests.
            # LA: Res externae per nexus expressos monstrantur. Generator eas non petit.
            url = urlsplit(str(node))
            if url.scheme not in {"http", "https"} or not url.hostname or url.username or url.password:
                return self.label(node)
            href = str(node)
        return f'<a href="{esc(href)}">{self.label(node)}</a>'

    def fields(self, groups, prefix=""):
        rows = []
        for key, values in groups:
            values = sorted_values(values)
            if values:
                links = ", ".join(self.link(value, prefix) for value in values)
                rows.append(f'<dt>{esc(self.text[key])}</dt><dd>{links}</dd>')
        return "<dl>" + "".join(rows) + "</dl>" if rows else ""

    def related_positions(self, node):
        arcs = {arc for prop in (DUB.subjectConcept, DUB.objectConcept, DUB.relationKind)
                for arc in self.graph.subjects(prop, node)}
        return {position for arc in arcs for position in self.graph.objects(arc, DUB.belongsTo)}

    def arcs(self, node, prefix):
        # EN: Expose statement IDs inside the parent position. Scope stays visible.
        # LA: Signa assertionum intra sententiam monstrantur. Ambitus conspicitur.
        items = []
        for arc in sorted_values(self.graph.subjects(DUB.belongsTo, node)):
            nodes = [self.graph.value(arc, prop, any=False) for prop in
                     (DUB.subjectConcept, DUB.relationKind, DUB.objectConcept)]
            if any(node is None for node in nodes):
                raise ValueError(f"Incomplete Dubium relation: {arc}")
            terms = [self.link(node, prefix) for node in nodes]
            items.append(f'<li id="{local_id(arc)}" data-fragment>{" · ".join(terms)}</li>')
        label = esc(self.text["arcs"])
        return f'<details><summary>{label} ({len(items)})</summary><ul>{"".join(items)}</ul></details>'

    def entry_content(self, node, group, prefix=""):
        graph = self.graph
        gloss = literal_html(translated(graph, node, RDFS.comment, self.lang), self.lang, self.text)
        content = f"<p>{gloss}</p>" if gloss else ""
        if group in {"concepts", "relations"}:
            content += self.fields([("in_positions", self.related_positions(node)),
                                    ("questions", graph.subjects(DUB.concerns, node))], prefix)
        elif group in {"positions", "questions"}:
            content += self.fields([
                ("source", graph.objects(node, DUB.derivedFrom)),
                ("mode", graph.objects(node, DUB.readingMode)),
                ("status", graph.objects(node, DUB.status)),
                ("force", graph.objects(node, DUB.force)),
                ("concerns", graph.objects(node, DUB.concerns)),
            ], prefix)
            if group == "positions":
                formula = esc(str(graph.value(node, DUB.formula)))
                content += f'<p class="formula"><strong>{esc(self.text["formula"])}</strong><code>{formula}</code></p>'
                content += self.arcs(node, prefix)
        elif group == "passages":
            locator = translated(graph, node, DUB.locator, self.lang)
            content += f"<p>{literal_html(locator, self.lang, self.text)}</p>"
            content += self.fields([
                ("source", graph.objects(node, DUB.partOfSource)),
                ("in_positions", graph.subjects(DUB.derivedFrom, node)),
            ], prefix)
        elif group == "classes":
            content += self.fields([
                ("parent", graph.objects(node, RDFS.subClassOf)),
                ("children", graph.subjects(RDFS.subClassOf, node)),
                ("used", graph.subjects(RDFS.domain, node)),
                ("value_of", graph.subjects(RDFS.range, node)),
            ], prefix)
        elif group == "properties":
            inverse = list(graph.objects(node, OWL.inverseOf)) + list(graph.subjects(OWL.inverseOf, node))
            content += self.fields([
                ("domain", graph.objects(node, RDFS.domain)),
                ("range", graph.objects(node, RDFS.range)),
                ("inverse", inverse),
            ], prefix)
        elif group == "values":
            entries = {entry for prop in (DUB.readingMode, DUB.status, DUB.force)
                       for entry in graph.subjects(prop, node)}
            content += self.fields([("in_positions", entries)], prefix)
        return content

    def entry(self, node, group):
        name = local_id(node)
        iri = esc(str(node))
        permalink = esc(self.text["permalink"])
        return (f'<article id="{name}" class="entry" data-entry>'
                f'<h3><a href="{term_file(node)}" title="{permalink}">{self.label(node)}</a></h3>'
                f'<p class="identifier" title="{iri}"><code>dub:{name}</code></p>'
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
            triples = ((node, prop, obj) for prop in (RDF.type, DUB.derivedFrom, DUB.partOfSource,
                       DUB.concerns, RDFS.label) for obj in graph.objects(node, prop))
        triples = sorted((row for row in triples if all(isinstance(term, (URIRef, Literal))
                         for term in row)), key=lambda row: tuple(map(str, row)))
        if not triples:
            # EN: Fall back to the actual declaration when the term has no asserted instance or use.
            # LA: Si vox exemplo aut usu asserto caret, declarationem ipsam exhibe.
            triples = sorted_values(graph.triples((node, RDF.type, None)))

        def as_turtle(term):
            if isinstance(term, URIRef) and str(term).startswith(str(DUB)) and term != URIRef(str(DUB)):
                return "dub:" + local_id(term)
            return term.n3()

        sample = [f"@prefix dub: <{DUB}> .", ""]
        for subject, predicate, obj in triples[:3]:
            verb = "a" if predicate == RDF.type else as_turtle(predicate)
            sample.append(f"{as_turtle(subject)} {verb} {as_turtle(obj)} .")
        turtle = esc("\n".join(sample))
        t = self.text
        return (f'<section><h2>{esc(t["sample"])}</h2><p>{esc(t["sample_note"])}</p>'
                f'<pre><code>{turtle}</code></pre></section>')

    def render_term(self, node, group):
        t = self.text
        name = local_id(node)
        title = translated(self.graph, node, RDFS.label, self.lang)
        group_label = esc(t[group])
        label = self.label(node)
        content = f"""
<nav class="breadcrumbs" aria-label="{esc(t["path"])}">
  <a href="../index.html">{esc(t["catalogue"])}</a>
  <a href="../index.html#{group}">{group_label}</a>
</nav>
<article class="term" id="{name}">
  <p class="eyebrow">{group_label}</p>
  <h1>{label}</h1>
  <p class="identifier"><code>dub:{name}</code></p>
  <p class="term-iri"><span>IRI</span> <code>{esc(str(node))}</code></p>
  <div class="term-description">{self.entry_content(node, group, "../")}</div>
{self.example(node, group)}
  <p><a href="../index.html#{name}">{esc(t["in_catalogue"])}</a></p>
</article>"""
        return page(self.lang, term_file(node), content, title=str(title) if title is not None else name)

    def render_schema(self):
        graph, t = self.graph, self.text
        classes = set(self.groups["classes"])
        roots = sorted_values(node for node in classes if not classes.intersection(
            graph.objects(node, RDFS.subClassOf)))

        def branch(node, ancestors):
            children = sorted_values(classes.intersection(graph.subjects(RDFS.subClassOf, node))
                                     - ancestors - {node})
            nested = "".join(branch(child, ancestors | {node}) for child in children)
            return f'<li>{self.link(node)}' + (f'<ul>{nested}</ul>' if nested else "") + '</li>'

        tree = "".join(branch(node, set()) for node in roots)
        rows = []
        for node in self.groups["properties"]:
            domain = ", ".join(self.link(value) for value in sorted_values(graph.objects(node, RDFS.domain)))
            ranges = ", ".join(self.link(value) for value in sorted_values(graph.objects(node, RDFS.range)))
            rows.append(f'<tr><th scope="row">{self.link(node)}</th><td>{domain}</td><td>{ranges}</td></tr>')
        content = f"""
<article class="prose schema-reference">
  <p class="eyebrow">{esc(t["edition"])}</p>
  <h1>{esc(t["schema"])}</h1>
  <p>{esc(t["schema_note"])}</p>
  <section><h2>{esc(t["classes"])}</h2><ul class="class-tree">{tree}</ul></section>
  <section><h2>{esc(t["properties"])}</h2><div class="table-scroll">
    <table><thead><tr><th scope="col">{esc(t["property"])}</th>
      <th scope="col">{esc(t["domain"])}</th><th scope="col">{esc(t["range"])}</th>
    </tr></thead><tbody>{"".join(rows)}</tbody></table>
  </div></section>
</article>"""
        return page(self.lang, "schema.html", content)

    def render(self):
        graph, t = self.graph, self.text
        index, sections = [], []
        for group, nodes in self.groups.items():
            label = esc(t[group])
            index.append(f'<a href="#{group}">{label} <span>{len(nodes)}</span></a>')
            cards = "".join(self.entry(node, group) for node in nodes)
            sections.append(f'<section id="{group}" data-group><h2>{label}</h2><div class="entries">{cards}</div></section>')
        prefix = "../" if self.lang != "it" else ""
        version = graph.value(URIRef(str(DUB)), OWL.versionInfo)
        version_node = graph.value(URIRef(str(DUB)), OWL.versionIRI)
        nav = "".join(index)
        content = f"""
<header class="hero">
  <p class="eyebrow">{esc(t["edition"])}</p><h1>{esc(t["title"])}</h1>
  <p class="intro">{esc(t["description"])}</p>
  <div class="actions"><a class="primary" href="guide.html">{esc(t["start"])}</a>
    <a href="schema.html">{esc(t["schema"])}</a>
    <a href="{term_file(DUB.essereInQuantoTale)}">{esc(t["example"])}</a></div>
</header>
<div class="desk">
  <nav class="index" aria-label="{esc(t["sections"])}">{nav}</nav>
  <div class="results">
    <div class="filter" hidden data-search-panel>
      <label for="lookup">{esc(t["filter"])}</label>
      <input id="lookup" type="search" placeholder="{esc(t["placeholder"])}" autocomplete="off">
      <p role="status" data-count data-label="{esc(t["count"])}" data-empty="{esc(t["empty"])}"></p>
    </div>
    {"".join(sections)}
    <section id="downloads" class="downloads">
      <h2>{esc(t["download"])}</h2>
      <p id="{local_id(version_node)}">{esc(t["version"])} <code>{esc(str(version))}</code></p>
      <ul><li><a href="{prefix}dubium.ttl">{esc(t["turtle"])}</a></li>
        <li><a href="{prefix}shapes.ttl">{esc(t["shapes"])}</a></li>
        <li><a href="https://criptasemantica.it/">{esc(t["manifesto"])}</a></li></ul>
    </section>
  </div>
</div>"""
        return page(self.lang, "index.html", content, search=True)


def page(lang, filename, content, search=False, title=None):
    # EN: Use relative links so a plain HTTP server and GitHub Pages serve the same files.
    # LA: Nexus relativos adhibe, ut idem opus localiter et in GitHub Pages praebeatur.
    t = TEXT[lang]
    directory = dirname(f"{folder(lang)}/{filename}")
    assets = relpath(".", directory)
    local = relpath(folder(lang), directory)
    prefix = "" if assets == "." else assets + "/"
    local_prefix = "" if local == "." else local + "/"
    title = f'Dubium · {title or t[TABS[filename]]}'
    tabs = []
    for file, key in TABS.items():
        current = ' aria-current="page"' if filename == file else ""
        tabs.append(f'<a href="{local_prefix}{file}"{current}>{esc(t[key])}</a>')
    tabs.append(f'<a href="{WIKI}/{lang.upper()}">{esc(t["wiki"])}</a>')
    languages, alternate = [], []
    for code, name in LANGUAGES.items():
        target = f"{folder(code)}/{filename}"
        href = relpath(target, directory)
        current = ' aria-current="page"' if code == lang else ""
        languages.append(f'<a href="{href}" lang="{code}" hreflang="{code}" data-language{current}>{name}</a>')
        alternate.append(f'<link rel="alternate" hreflang="{code}" href="{site_url(code, filename)}">')
    script = f'<script src="{prefix}search.js" defer></script>' if search else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta http-equiv="Content-Security-Policy" content="{esc(CSP)}">
<meta name="referrer" content="no-referrer">
<meta name="description" content="{esc(t["description"])}">
<title>{esc(title)}</title>
<link rel="canonical" href="{site_url(lang, filename)}">
{"".join(alternate)}
<link rel="stylesheet" href="{prefix}../style.css">
<link rel="stylesheet" href="{prefix}site.css">
{script}
</head>
<body>
<a class="skip" href="#main">{esc(t["skip"])}</a>
<div class="shell">
  <header class="masthead">
    <a class="wordmark" href="{prefix}../index.html">AENIGMA</a>
    <nav aria-label="Dubium">{"".join(tabs)}</nav>
    <nav class="languages" aria-label="{esc(t["language"])}">{"".join(languages)}</nav>
  </header>
  <main id="main">{content}</main>
  <footer><a href="https://criptasemantica.it/">Cripta Semantica</a> <span>Dubium · RDF / OWL</span></footer>
</div>
</body>
</html>
"""


def site_url(lang, filename):
    route = "" if lang == "it" else f"{lang}/"
    return SITE + route + filename


def document(source, lang):
    # EN: Markdown is local and trusted as prose; disable raw HTML and escape link rewrites.
    # LA: Markdown localis ut prosa legitur; HTML crudum excluditur et nexus proteguntur.
    raw = source.read_text(encoding="utf-8")
    html = run(
        ["pandoc", "--from=gfm-raw_html", "--to=html5", "--wrap=none"],
        input=raw, text=True, capture_output=True, check=True,
    ).stdout

    def rewrite(match):
        link = unescape(match[1])
        path, mark, fragment = link.partition("#")
        url = urlsplit(link)
        if url.scheme in {"http", "https"} and url.hostname and not url.username and not url.password:
            return match[0]
        if url.scheme or url.netloc or path.startswith("/") or ".." in path.split("/"):
            raise ValueError(f"Unsupported documentation link: {link}")
        if not path:
            return match[0]
        target = DOCS.get(path, path)
        return f'href="{esc(relpath(target, folder(lang)) + mark + fragment)}"'

    result = re.sub(r'href="([^"]+)"', rewrite, html)
    return f'<article class="prose">{result}</article>'


def main():
    graph = Graph().parse(ROOT / "dubium.ttl", format="turtle")
    outputs = {}
    for lang in LANGUAGES:
        current = ROOT / folder(lang)
        catalogue = Catalogue(graph, lang)
        outputs[current / "index.html"] = catalogue.render()
        outputs[current / "schema.html"] = catalogue.render_schema()
        for group, nodes in catalogue.groups.items():
            for node in nodes:
                outputs[current / term_file(node)] = catalogue.render_term(node, group)
        suffix = "" if lang == "it" else f".{lang}"
        for stem, filename in [("README", "guide.html"), ("FORMALIZZAZIONE", "formal.html")]:
            outputs[current / filename] = page(lang, filename, document(ROOT / f"{stem}{suffix}.md", lang))
    # EN: Render all pages successfully before replacing any output.
    # LA: Omnes paginas ante mutationem tabularum perfice.
    for file, content in outputs.items():
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
