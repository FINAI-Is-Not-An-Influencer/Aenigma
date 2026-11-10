#!/usr/bin/env bash
set -euo pipefail

# EN: Work from the checkout even when the script is invoked from another directory.
# LA: In repositorio labora, etiamsi scriptum ex alio directorio invocatur.
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
scratch=$(mktemp -d .aenigma-build.XXXXXX)
trap 'rm -r -- "$scratch"' EXIT

cleancss -O2 style.css > "$scratch/style.css"
style_hash=$(openssl dgst -sha256 -binary "$scratch/style.css" | base64)

# EN: Hash precisely the bytes that will appear between the style tags.
# LA: Ipsos octetos intra signa styli futuros digere.
python3 - "$scratch/style.css" "$style_hash" "$scratch/index.html" <<'PY'
from pathlib import Path
import sys

style = Path(sys.argv[1]).read_bytes()
digest = sys.argv[2].encode("ascii")
template = Path("index.src.html").read_bytes()
hash_marker = b"INJECT_CSP_HASH_HERE"
style_marker = b"INJECT_CSS_HERE"
if not style or any(template.count(marker) != 1 for marker in (hash_marker, style_marker)):
    raise SystemExit("Expected non-empty CSS and one of each template marker.")
html = template.replace(hash_marker, b"sha256-" + digest)
html = html.replace(style_marker, b"<style>" + style + b"</style>")
Path(sys.argv[3]).write_bytes(html)
PY

# EN: Replace the served page only after the new document has been generated.
# LA: Paginam publicandam demum post confectionem novi documenti substitue.
mv -- "$scratch/index.html" index.html
