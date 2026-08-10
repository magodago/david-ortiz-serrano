#!/usr/bin/env python3
"""QA tecnico del render: enlaces, ids, assets, SEO, contenido prohibido."""
import re, os

html = open('/home/dorti/david-ortiz-web/index.html').read()
root = '/home/dorti/david-ortiz-web'

nav_targets = re.findall(r'<a href="#([^"]+)"', html)
ids = set(re.findall(r'id="([^"]+)"', html))
missing = [t for t in nav_targets if t not in ids]
print("NAV targets sin id:", missing or "ninguno OK")

assets = re.findall(r'(?:src|href)="(?!https?://|#|mailto:|tel:|data:)([^"]+)"', html)
missing_assets = []
for a in assets:
    p = os.path.join(root, a.split('?')[0])
    if not os.path.exists(p):
        missing_assets.append(a)
print("Assets faltantes:", missing_assets or "ninguno OK")
print("Assets:", sorted(set(assets)))

ext = re.findall(r'href="(https?://[^"]+)"', html)
for e in sorted(set(ext)):
    print("EXT:", e)

for el in ['ai-canvas', 'progress', 'nav-toggle', 'nav-links', 'data-parallax']:
    print(el, "presente" if el in html else "FALTA")

for m in ['description', 'og:title', 'og:image', 'twitter:card', 'application/ld+json']:
    print("SEO", m, "OK" if m in html else "FALTA")

for bad in ['proactivo', 'team building', 'white rabbit', 'glitch', 'Orbitron']:
    print("prohibido:", bad, "->", "PRESENTE!" if bad.lower() in html.lower() else "limpio")
