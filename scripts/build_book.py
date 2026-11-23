"""Render the reviewed edition offline, using only Python's standard library."""
from pathlib import Path
import argparse
import html
import json

ROOT = Path(__file__).resolve().parents[1]


def build(site_dir, output_file):
    items = json.loads((ROOT / 'data/edition.json').read_text(encoding='utf-8'))
    collection = json.loads((ROOT / 'data/collection.json').read_text(encoding='utf-8'))
    ids = [item['id'] for item in items]
    if not items or len(ids) != len(set(ids)):
        raise ValueError('The edition must contain poems with unique IDs')
    for item in items:
        if not all(item.get(key) for key in ('id', 'title', 'date', 'url')):
            raise ValueError(f"Incomplete poem: {item.get('id')}")
    page = (ROOT / 'templates/book-template.html').read_text(encoding='utf-8')
    substitutions = {
        '__POEM_COUNT__': str(len(items)),
        '__YEAR_RANGE__': f"{items[0]['date'][:4]}–{items[-1]['date'][:4]}",
        '__PREFACE_COUNT__': str(sum(bool(p.get('preface')) for p in items)),
        '__STATS__': f"{len(items)} runoa · {items[0]['date'][:4]}–{items[-1]['date'][:4]}",
        '__METHOD__': html.escape(collection['method']),
        '__COVERAGE__': f"Lähteistetty johdanto on {sum(bool(p.get('preface')) for p in items)} runolla {len(items)}:stä.",
        '__POEMS__': json.dumps(items, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c'),
    }
    for token, value in substitutions.items():
        page = page.replace(token, value)
    for folder, view, base in [('', 'reader', './'), ('sisallys', 'contents', '../'), ('kokoelmasta', 'about', '../')]:
        target = site_dir / folder / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page.replace('__PAGE__', view).replace('__BASE__', base), encoding='utf-8')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(page.replace('__PAGE__', 'reader').replace('__BASE__', './'), encoding='utf-8')
    print(f'{len(items)} poems; site: {site_dir}; standalone: {output_file}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, default=ROOT / 'work/pursiaisen-runot/dist')
    parser.add_argument('--output-file', type=Path, default=ROOT / 'outputs/Paivan-sakeet.html')
    args = parser.parse_args()
    build(args.site_dir.resolve(), args.output_file.resolve())
