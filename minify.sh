#!/bin/bash
# minify.sh

cleancss -O2 style.css > style.min.css

CSS_HASH=$(openssl dgst -sha256 -binary style.min.css | base64)
CSP_STRING="sha256-${CSS_HASH}"

printf "<style>" > style.wrapped.css
cat style.min.css >> style.wrapped.css
printf "</style>" >> style.wrapped.css

sed "s@INJECT_CSP_HASH_HERE@${CSP_STRING}@g" index.src.html > index.tmp.html

sed -e '/INJECT_CSS_HERE/r style.wrapped.css' -e '/INJECT_CSS_HERE/d' index.tmp.html > index.html

rm style.min.css style.wrapped.css index.tmp.html

echo "[+] Compilazione completata. Firma CSP esatta: ${CSP_STRING}"
