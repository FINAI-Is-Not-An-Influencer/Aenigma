#!/usr/bin/env python3
"""EN: Verify every local link and fragment of the generated site without a network connection.
LA: Omnem nexum et fragmentum localem situs geniti sine rete proba.

EN: External links are counted, not fetched. A missing file or a missing anchor fails the check.
LA: Nexus externi numerantur, non petuntur. Tabula aut ancora deficiens probationem frustratur.
"""

from html.parser import HTMLParser
from pathlib import Path
from posixpath import normpath
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        for key in ("href", "src"):
            if tag in {"a", "link", "script", "img"} and attributes.get(key):
                self.links.append(attributes[key])


def main():
    pages = {}
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts or ".aenigma-build" in str(path):
            continue
        page = Page()
        page.feed(path.read_text(encoding="utf-8"))
        pages[path] = page
    errors, local, external = [], 0, 0
    for path, page in pages.items():
        for link in page.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                external += 1
                # EN: Vocabulary IRIs of the W3C and purl.org are identifiers published over HTTP; every other link must be HTTPS.
                # LA: IRI lexicorum W3C et purl.org indices sunt per HTTP editi; ceteri nexus HTTPS esse debent.
                if parts.scheme != "https" and parts.hostname not in {"www.w3.org", "purl.org", "xmlns.com", "rdfs.org", "www.wikidata.org"}:
                    errors.append(f"{path.relative_to(ROOT)}: non-HTTPS link {link}")
                continue
            local += 1
            target = path if not parts.path else (path.parent / unquote(parts.path)).resolve()
            if parts.path and parts.path.endswith("/"):
                target = target / "index.html"
            if not target.is_file() or ROOT not in target.parents and target != ROOT:
                errors.append(f"{path.relative_to(ROOT)}: missing file {link}")
                continue
            fragment = unquote(parts.fragment)
            if fragment and target.suffix == ".html":
                ids = pages[target].ids if target in pages else set()
                if fragment not in ids:
                    errors.append(f"{path.relative_to(ROOT)}: missing anchor {link}")
    for error in errors[:50]:
        print(error)
    if errors:
        print(f"{len(errors)} errors")
        sys.exit(1)
    print(f"{len(pages)} pages, {local} local links and anchors resolved, {external} external links listed")


if __name__ == "__main__":
    main()
