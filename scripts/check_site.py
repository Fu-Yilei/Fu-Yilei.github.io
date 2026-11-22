#!/usr/bin/env python3
"""Check built pages, internal links, legacy URLs, and the public contact policy."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / '_site'
HOST = 'fu-yilei.github.io'
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links = path, set(), []
        self.h1 = 0
        self.canonical = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        for name in ('href', 'src'):
            if name in attrs:
                self.links.append(attrs[name])

pages = {}
for file in SITE.rglob('*.html'):
    # Preserve the existing standalone PCA visualization as a separate artifact.
    if 'assets' in file.relative_to(SITE).parts:
        continue
    page = Page(file)
    pages[file] = page
    text = file.read_text()
    if page.h1 != 1:
        errors.append(f'{file}: expected one h1, found {page.h1}')
    if not page.canonical or urlsplit(page.canonical).netloc != HOST:
        errors.append(f'{file}: missing or incorrect production canonical URL')
    if '{{' in text or '{%' in text:
        errors.append(f'{file}: unrendered Liquid template')
    if re.search(r'mailto:|yilei\.fu@bcm\.edu', text, re.I):
        errors.append(f'{file}: email contact is present')

link_count = 0
for file, page in pages.items():
    path = '/' + file.relative_to(SITE).as_posix()
    for link in page.links:
        if not link or link.startswith(('mailto:', 'tel:', 'data:', 'javascript:')):
            continue
        url = urlsplit(urljoin('https://' + HOST + path, link))
        if url.netloc != HOST:
            continue
        target = SITE / unquote(url.path).lstrip('/')
        if target.is_dir():
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{file.relative_to(SITE)}: missing {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{file.relative_to(SITE)}: missing anchor {link}')
        link_count += 1

required = [
    'index.html', 'about/index.html', 'research/index.html',
    'publications/index.html', 'software/index.html', 'notes/index.html',
    '404.html', 'feed.xml', 'sitemap.xml', 'assets/publications.bib',
    'assets/YileiFuPh.D.ThesisDefense.pdf',
    'bioinformatics/2023/12/02/different-human-region-gap-penalties-copy.html',
    'bioinformatics/2023/12/26/talk-about-MethPhaser-at-NCM2023.html',
    'introductions/2023/12/01/about-yilei-fu.html',
    'others/2023/12/02/yilei-defense-slides.html',
    'others/2023/12/02/诗2首-copy.html',
    'others/2023/12/16/sv-in-metagenomes.html',
]
for name in required:
    if not (SITE / name).is_file():
        errors.append(f'Missing required page or asset: {name}')
for name in ('feed.xml', 'sitemap.xml'):
    try:
        ET.parse(SITE / name)
    except (OSError, ET.ParseError) as exc:
        errors.append(f'{name}: {exc}')
if (SITE / 'feed.xml').is_file() and 'yilei.fu@bcm.edu' in (SITE / 'feed.xml').read_text():
    errors.append('Email contact is present in the feed')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'Passed: {len(pages)} pages, {link_count} internal links/assets, six legacy posts, XML feeds, and no email contact in generated pages.')
