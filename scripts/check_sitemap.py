#!/usr/bin/env python3
"""Fail closed when the published sitemap stops covering every locale."""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET


SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
NS = {"sm": SITEMAP_NS}


def read_locations(path: Path) -> tuple[str, list[str]]:
    root = ET.parse(path).getroot()
    kind = root.tag.removeprefix(f"{{{SITEMAP_NS}}}")
    return kind, [node.text or "" for node in root.findall("sm:url/sm:loc", NS)]


def main() -> int:
    public = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    root_sitemap = public / "sitemap.xml"
    kind, root_locations = read_locations(root_sitemap)

    errors: list[str] = []
    if kind != "urlset":
        errors.append(f"{root_sitemap} must be a urlset, got {kind!r}")
    if not root_locations:
        errors.append(f"{root_sitemap} contains no URLs")
    if len(root_locations) != len(set(root_locations)):
        errors.append(f"{root_sitemap} contains duplicate URLs")

    for location in root_locations:
        parsed = urlparse(location)
        if parsed.scheme != "https" or parsed.netloc != "kyungseo.github.io":
            errors.append(f"non-canonical sitemap URL: {location!r}")

    locale_locations: set[str] = set()
    locale_sitemaps = sorted(path for path in public.glob("*/sitemap.xml"))
    if not locale_sitemaps:
        errors.append("no locale sitemaps were generated for completeness comparison")
    for path in locale_sitemaps:
        child_kind, locations = read_locations(path)
        if child_kind != "urlset":
            errors.append(f"{path} must be a urlset, got {child_kind!r}")
        locale_locations.update(locations)

    root_set = set(root_locations)
    missing = sorted(locale_locations - root_set)
    extra = sorted(root_set - locale_locations)
    if missing:
        errors.append(f"root sitemap misses {len(missing)} locale URL(s): {missing}")
    if extra:
        errors.append(f"root sitemap has {len(extra)} unexpected URL(s): {extra}")

    robots = (public / "robots.txt").read_text(encoding="utf-8")
    expected = "Sitemap: https://kyungseo.github.io/sitemap.xml"
    if expected not in robots:
        errors.append(f"robots.txt does not contain {expected!r}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        f"sitemap OK: {len(root_locations)} unique URLs across "
        f"{len(locale_sitemaps)} locales"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
