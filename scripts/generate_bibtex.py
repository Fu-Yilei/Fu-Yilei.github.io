#!/usr/bin/env python3
"""Regenerate the downloadable bibliography from the site's publication data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
publications = json.loads((ROOT / '_data/publications.json').read_text())
entries = []
for publication in publications:
    authors = ' and '.join(publication['authors'])
    if publication['id'] == 'smaht-benchmark':
        authors = '{Somatic Mosaicism across Human Tissues Network}'
    fields = {
        'title': publication['title'],
        'author': authors,
        'journal': publication['venue'],
        'year': str(publication['year']),
        'doi': publication['doi'],
        'url': publication['url'],
    }
    if publication['status'] == 'preprint':
        fields['note'] = 'Preprint'
    key = f"fu_{publication['id'].replace('-', '_')}_{publication['year']}"
    entries.append('@article{' + key + ',\n' + ',\n'.join(
        f'  {name} = {{{value}}}' for name, value in fields.items()
    ) + '\n}')
(ROOT / 'assets/publications.bib').write_text('\n\n'.join(entries) + '\n')
print(f'Generated {len(entries)} BibTeX entries.')
