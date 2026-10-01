"""
Script: add_last_updated.py
Adds a '**Last updated:** YYYY-MM-DD' footer to Markdown files under docs/ that lack it.

USAGE:
    python scripts/add_last_updated.py --dry-run
    python scripts/add_last_updated.py

This script edits files in-place. Run locally when you're ready. It does NOT touch ILS-dev.
"""
import os
import re
from datetime import date

docs_root = os.path.join(os.path.dirname(__file__), '..', 'docs')
marker_re = re.compile(r'Last updated:', re.IGNORECASE)


def find_md_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            if f.endswith('.md'):
                yield os.path.join(dirpath, f)


def needs_marker(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    return not bool(marker_re.search(text))


def add_marker(path, date_str):
    with open(path, 'a', encoding='utf-8') as f:
        f.write('\n\n**Last updated:** ' + date_str + '\n')


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()

    today = date.today().isoformat()
    targets = []
    for md in find_md_files(docs_root):
        if needs_marker(md):
            targets.append(md)

    print(f'Found {len(targets)} files missing Last updated marker.')
    if args.dry_run:
        for t in targets:
            print(t)
    else:
        for t in targets:
            add_marker(t, today)
        print(f'Appended Last updated: {today} to {len(targets)} files.')
