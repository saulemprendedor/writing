#!/usr/bin/env python3
"""Regenerate the article index in README.md from the articles themselves.

The index is never edited by hand. It is rebuilt from the YAML frontmatter of
every `articulo.es.md` under a series directory, and written between the
ARTICLES:START / ARTICLES:END markers in README.md.

Spanish is the source language, so it is what the index lists. A translation
(`articulo.<lang>.md` beside it) is linked from its entry once it is
published — one line per article, not one per language.

Why: an index maintained by hand is wrong by the sixth article. Here the
articles are the source of truth and the README is a derived artifact — so it
cannot drift, and `--check` makes that a build failure instead of a surprise.

    python3 scripts/build-index.py            regenerate README.md
    python3 scripts/build-index.py --check    exit 1 if README.md is stale
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START = "<!-- ARTICLES:START -->"
END = "<!-- ARTICLES:END -->"

# Series get a heading of their own, in publication order.
SERIES_TITLES = {
    "dev-genius": "DEV Genius — cómo construí un sistema de agentes que entrega software",
}

# Only these reach the public index. A draft in the repo is work in progress,
# not something a visitor should stumble into.
PUBLIC_STATUSES = {"published"}

# The source language: the file the index is built from, and the one every
# article has. Anything else beside it is a translation.
SOURCE_LANG = "es"

# Display names for the translation links, so the label reads in the language
# it leads to rather than in Spanish.
LANG_NAMES = {"en": "English", "pt": "Português"}


def parse_frontmatter(path: pathlib.Path) -> dict[str, str]:
    """Minimal YAML frontmatter reader — flat `key: value` pairs only.

    Deliberately not a YAML dependency: the contract is flat by design, and a
    parser that accepts more than the contract allows invites drift.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise SystemExit(f"{path}: falta el frontmatter")

    _, block, _ = text.split("---", 2)
    data: dict[str, str] = {}
    for line in block.strip().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"')
    return data


def translations(article: pathlib.Path) -> str:
    """Renders the links to the published translations sitting beside an article.

    Absent, empty; that way an article without translations reads exactly as
    it did before there were any.
    """
    links: list[str] = []
    for sibling in sorted(article.parent.glob("articulo.*.md")):
        lang = sibling.stem.split(".")[-1]
        if lang == SOURCE_LANG:
            continue
        if parse_frontmatter(sibling).get("status") not in PUBLIC_STATUSES:
            continue
        name = LANG_NAMES.get(lang, lang)
        links.append(f"[{name}]({sibling.relative_to(ROOT)})")

    return "".join(f" · {link}" for link in links)


def collect() -> dict[str, list[dict[str, str]]]:
    series: dict[str, list[dict[str, str]]] = {}
    for article in sorted(ROOT.glob(f"*/*/articulo.{SOURCE_LANG}.md")):
        if article.parts[len(ROOT.parts)] in {"drafts", "scripts"}:
            continue
        meta = parse_frontmatter(article)
        meta["path"] = str(article.relative_to(ROOT))
        meta["translations"] = translations(article)
        series.setdefault(meta.get("series", "sin-serie"), []).append(meta)

    for items in series.values():
        items.sort(key=lambda m: int(m.get("episode", "0")))
    return series


def render(series: dict[str, list[dict[str, str]]]) -> str:
    lines: list[str] = []

    for name, items in series.items():
        public = [m for m in items if m.get("status") in PUBLIC_STATUSES]
        if not public:
            continue

        lines.append(f"### {SERIES_TITLES.get(name, name)}\n")
        for meta in public:
            episode = meta.get("episode", "?")
            title = meta.get("title", "(sin título)")
            lines.append(f"**{episode}. [{title}]({meta['path']})**  ")
            if meta.get("summary"):
                lines.append(f"{meta['summary']}  ")
            if meta.get("linkedin_url"):
                lines.append(
                    f"[Leerlo en LinkedIn]({meta['linkedin_url']}) · {meta.get('date', '')}"
                    f"{meta.get('translations', '')}"
                )
            else:
                lines.append(f"{meta.get('date', '')}{meta.get('translations', '')}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    body = render(collect())
    current = README.read_text(encoding="utf-8")

    if START not in current or END not in current:
        raise SystemExit(f"README.md: faltan los marcadores {START} / {END}")

    head, rest = current.split(START, 1)
    _, tail = rest.split(END, 1)
    updated = f"{head}{START}\n\n{body}\n{END}{tail}"

    if "--check" in sys.argv:
        if updated != current:
            print("README.md está desactualizado. Corré: python3 scripts/build-index.py")
            return 1
        print("README.md al día.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print("README.md regenerado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
