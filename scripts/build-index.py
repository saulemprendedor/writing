#!/usr/bin/env python3
"""Regenerate the article index in README.md from the articles themselves.

The index is never edited by hand. It is rebuilt from the YAML frontmatter of
the `articulo.<lang>.md` files under a series directory, and written between
the ARTICLES:START / ARTICLES:END markers in README.md.

The README is bilingual, so there is one block per language of the README —
English and Spanish — each written between its own pair of markers and built
from the articles in that language. An article with no translation yet falls
back to its Spanish metadata, marked so the reader knows before clicking.

Why: an index maintained by hand is wrong by the sixth article, and one
maintained by hand in two languages is wrong by the second. Here the articles
are the source of truth and the README is a derived artifact — so it cannot
drift, and `--check` makes that a build failure instead of a surprise.

    python3 scripts/build-index.py            regenerate README.md
    python3 scripts/build-index.py --check    exit 1 if README.md is stale
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# Only these reach the public index. A draft in the repo is work in progress,
# not something a visitor should stumble into.
PUBLIC_STATUSES = {"published"}

# The language every article is written in first, and the one an untranslated
# entry falls back to.
SOURCE_LANG = "es"

# Display names for the translation links, so each label reads in the
# language it leads to.
LANG_NAMES = {"es": "Español", "en": "English", "pt": "Português"}

# One block per language the README is written in, with the markers it sits
# between and the wording around each entry.
BLOCKS = {
    "es": {
        "start": "<!-- ARTICLES:START -->",
        "end": "<!-- ARTICLES:END -->",
        "series": {
            "dev-genius": "DEV Genius — cómo construí un sistema de agentes que entrega software",
        },
        "linkedin": "Leerlo en LinkedIn",
        "untranslated": "en español",
    },
    "en": {
        "start": "<!-- ARTICLES_EN:START -->",
        "end": "<!-- ARTICLES_EN:END -->",
        "series": {
            "dev-genius": "DEV Genius — how I built an agent system that ships software",
        },
        "linkedin": "Read it on LinkedIn",
        # The LinkedIn originals are all in Spanish; saying so before the
        # click is cheaper than a reader finding out after it.
        "linkedin_note": " (in Spanish)",
        "untranslated": "in Spanish",
    },
}


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


def collect() -> dict[str, list[dict[str, object]]]:
    """Every published article, with one metadata set per language it exists in."""
    series: dict[str, list[dict[str, object]]] = {}

    for source in sorted(ROOT.glob(f"*/*/articulo.{SOURCE_LANG}.md")):
        if source.parts[len(ROOT.parts)] in {"drafts", "scripts"}:
            continue

        by_lang: dict[str, dict[str, str]] = {}
        for sibling in sorted(source.parent.glob("articulo.*.md")):
            lang = sibling.stem.split(".")[-1]
            meta = parse_frontmatter(sibling)
            if meta.get("status") not in PUBLIC_STATUSES:
                continue
            meta["path"] = str(sibling.relative_to(ROOT))
            by_lang[lang] = meta

        if SOURCE_LANG not in by_lang:
            continue

        source_meta = by_lang[SOURCE_LANG]
        entry = {"by_lang": by_lang, "episode": int(source_meta.get("episode", "0"))}
        series.setdefault(source_meta.get("series", "sin-serie"), []).append(entry)

    for items in series.values():
        items.sort(key=lambda e: e["episode"])  # type: ignore[arg-type,return-value]
    return series


def render(series: dict[str, list[dict[str, object]]], lang: str) -> str:
    """The index as the README's `lang` section shows it."""
    block = BLOCKS[lang]
    lines: list[str] = []

    for name, items in series.items():
        if not items:
            continue

        lines.append(f"### {block['series'].get(name, name)}\n")  # type: ignore[union-attr]

        for entry in items:
            by_lang: dict[str, dict[str, str]] = entry["by_lang"]  # type: ignore[assignment]
            # The reader's language when it exists; the original otherwise,
            # said out loud rather than silently swapped.
            meta = by_lang.get(lang, by_lang[SOURCE_LANG])
            translated = lang in by_lang

            title = meta.get("title", "(sin título)")
            suffix = "" if translated else f" — {block['untranslated']}"
            lines.append(f"**{entry['episode']}. [{title}]({meta['path']})**{suffix}  ")

            if meta.get("summary"):
                lines.append(f"{meta['summary']}  ")

            # LinkedIn lives on the Spanish original, whatever language the
            # entry is being rendered in.
            source_meta = by_lang[SOURCE_LANG]
            tail: list[str] = []
            if source_meta.get("linkedin_url"):
                note = block.get("linkedin_note", "")
                tail.append(
                    f"[{block['linkedin']}]({source_meta['linkedin_url']}){note}"
                )
            if source_meta.get("date"):
                tail.append(source_meta["date"])
            # The languages other than the one this entry is already showing —
            # which is the fallback, not `lang`, when there is no translation.
            shown = lang if translated else SOURCE_LANG
            tail += [
                f"[{LANG_NAMES.get(other, other)}]({by_lang[other]['path']})"
                for other in sorted(by_lang)
                if other != shown
            ]
            lines.append(" · ".join(tail))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    series = collect()
    updated = current = README.read_text(encoding="utf-8")

    for lang, block in BLOCKS.items():
        start, end = block["start"], block["end"]
        if start not in updated or end not in updated:
            raise SystemExit(f"README.md: faltan los marcadores {start} / {end}")

        head, rest = updated.split(start, 1)
        _, tail = rest.split(end, 1)
        updated = f"{head}{start}\n\n{render(series, lang)}\n{end}{tail}"

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
