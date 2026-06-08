#!/usr/bin/env python3
"""Download WordPress featured images into the Jekyll assets folder."""

from __future__ import annotations

import csv
import re
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
MIGRATION = ROOT / "_migration"
INVENTORY = MIGRATION / "post-inventory.csv"
ASSET_ROOT = ROOT / "assets" / "img" / "migrated"
MAP_FILE = MIGRATION / "image-map.csv"


def clean_filename(name: str) -> str:
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-")
    return name or "image"


def main() -> None:
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []
    with INVENTORY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(row)

    output_rows = []
    for row in rows:
        url = row["image_url"]
        if not url:
            output_rows.append([row["source_slug"], "", "", "missing"])
            continue

        parsed = urlparse(url)
        filename = clean_filename(Path(parsed.path).name)
        post_dir = ASSET_ROOT / row["source_slug"]
        post_dir.mkdir(exist_ok=True)
        target = post_dir / filename
        site_path = f"/assets/img/migrated/{row['source_slug']}/{filename}"

        status = "exists"
        if not target.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "alexx-fyi-migration/1.0"})
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    target.write_bytes(response.read())
                status = "downloaded"
            except urllib.error.URLError as exc:
                status = f"error: {exc}"

        output_rows.append([row["source_slug"], url, site_path, status])
        print(f"{status}: {row['source_slug']}")

    with MAP_FILE.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["source_slug", "source_image_url", "site_image_path", "status"])
        writer.writerows(output_rows)

    print(f"Wrote {MAP_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
