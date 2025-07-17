# src/lbeam/search.py
import os
import re
import click

def run_search(keywords, recursive, extensions, regex_enabled):
    cwd = os.getcwd()
    click.echo(f"Searching in {cwd} (recursive={recursive})…")

    patterns = [re.compile(k, re.IGNORECASE) for k in keywords] if regex_enabled else []
    for root, dirs, files in os.walk(cwd):
        for fname in files:
            if extensions and not any(fname.endswith(ext) for ext in extensions):
                continue
            path = os.path.join(root, fname)
            try:
                with open(path, 'r', errors='ignore') as f:
                    for line in f:
                        text = line.strip('\n')
                        if (regex_enabled and all(p.search(text) for p in patterns)) or \
                           (not regex_enabled and all(k.lower() in text.lower() for k in keywords)):
                            click.echo(path)
                            break
            except Exception:
                continue
        if not recursive:
            break
