#!/usr/bin/env python3
"""Build a review inventory and raw Markdown sources from a WordPress WXR export."""

from __future__ import annotations

import csv
import html
import re
import textwrap
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPORT = ROOT / "alxndrr.WordPress.2026-06-08.xml"
INVENTORY_CSV = ROOT / "post-inventory.csv"
INVENTORY_MD = ROOT / "post-inventory.md"
SOURCE_DIR = ROOT / "source-markdown"

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
}

CATEGORY_MAP = {
    "Boeken": "Books",
    "Films": "Movies",
    "Games": "Games",
    "LEGO": "LEGO",
    "Lego": "LEGO",
    "Leven": "Life",
    "Lijstjes": "Lists",
    "Muziek": "Music",
    "Overig": "Blog",
    "Series": "TV",
    "Tech": "Tech",
}


class BasicMarkdownConverter(HTMLParser):
    """Tiny converter for the fairly simple WordPress post HTML in this export."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.href_stack: list[str | None] = []
        self.list_depth = 0
        self.in_li = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in {"p", "div"}:
            self._blank()
        elif tag in {"br"}:
            self.parts.append("\n")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("_")
        elif tag in {"h1", "h2", "h3", "h4"}:
            self._blank()
            self.parts.append("#" * int(tag[1]) + " ")
        elif tag == "blockquote":
            self._blank()
            self.parts.append("> ")
        elif tag in {"ul", "ol"}:
            self.list_depth += 1
            self._blank()
        elif tag == "li":
            self.in_li = True
            self.parts.append("\n" + "  " * max(self.list_depth - 1, 0) + "- ")
        elif tag == "a":
            self.parts.append("[")
            self.href_stack.append(attrs_dict.get("href"))
        elif tag == "img":
            src = attrs_dict.get("src")
            alt = attrs_dict.get("alt") or "Image"
            if src:
                self._blank()
                self.parts.append(f"![{alt}]({src})")
                self._blank()
        elif tag == "iframe":
            src = attrs_dict.get("src") or ""
            if "youtube" in src or "youtu.be" in src:
                self._blank()
                self.parts.append(src)
                self._blank()

    def handle_endtag(self, tag: str) -> None:
        if tag in {"p", "div", "blockquote"}:
            self._blank()
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("_")
        elif tag in {"h1", "h2", "h3", "h4"}:
            self._blank()
        elif tag in {"ul", "ol"}:
            self.list_depth = max(self.list_depth - 1, 0)
            self._blank()
        elif tag == "li":
            self.in_li = False
        elif tag == "a":
            href = self.href_stack.pop() if self.href_stack else None
            if href:
                self.parts.append(f"]({href})")
            else:
                self.parts.append("]")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def markdown(self) -> str:
        text = "".join(self.parts)
        text = html.unescape(text).replace("\xa0", " ")
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"

    def _blank(self) -> None:
        current = "".join(self.parts)
        if not current.endswith("\n\n"):
            if current.endswith("\n"):
                self.parts.append("\n")
            else:
                self.parts.append("\n\n")


@dataclass
class Post:
    post_id: str
    title: str
    date: str
    slug: str
    link: str
    categories: list[str]
    tags: list[str]
    content_html: str
    thumbnail_id: str
    image_url: str

    @property
    def target_category(self) -> str:
        if not self.categories:
            return "Blog"
        return CATEGORY_MAP.get(self.categories[0], self.categories[0])

    @property
    def source_filename(self) -> str:
        return f"{self.date[:10]}-{self.slug}.md"


def text(node: ET.Element, path: str, default: str = "") -> str:
    return node.findtext(path, default=default, namespaces=NS) or default


def read_export() -> tuple[list[Post], dict[str, str]]:
    root = ET.parse(EXPORT).getroot()
    items = root.find("channel").findall("item")

    attachments: dict[str, str] = {}
    for item in items:
        if text(item, "wp:post_type") != "attachment":
            continue
        post_id = text(item, "wp:post_id")
        url = text(item, "wp:attachment_url") or text(item, "guid")
        if post_id and url:
            attachments[post_id] = url

    posts: list[Post] = []
    for item in items:
        if text(item, "wp:post_type") != "post" or text(item, "wp:status") != "publish":
            continue
        categories: list[str] = []
        tags: list[str] = []
        for category in item.findall("category"):
            value = category.text or ""
            if category.attrib.get("domain") == "category":
                categories.append(value)
            elif category.attrib.get("domain") == "post_tag":
                tags.append(value)

        thumbnail_id = ""
        for meta in item.findall("wp:postmeta", NS):
            if text(meta, "wp:meta_key") == "_thumbnail_id":
                thumbnail_id = text(meta, "wp:meta_value")

        posts.append(
            Post(
                post_id=text(item, "wp:post_id"),
                title=html.unescape(text(item, "title")),
                date=text(item, "wp:post_date"),
                slug=text(item, "wp:post_name"),
                link=text(item, "link"),
                categories=categories,
                tags=tags,
                content_html=text(item, "content:encoded"),
                thumbnail_id=thumbnail_id,
                image_url=attachments.get(thumbnail_id, ""),
            )
        )

    posts.sort(key=lambda post: post.date, reverse=True)
    return posts, attachments


def html_to_markdown(content_html: str) -> str:
    converter = BasicMarkdownConverter()
    converter.feed(content_html)
    return converter.markdown()


def write_inventory(posts: list[Post]) -> None:
    with INVENTORY_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "status",
                "date",
                "source_title",
                "source_slug",
                "old_url",
                "source_categories",
                "source_tags",
                "target_category",
                "image_url",
                "notes",
            ]
        )
        for post in posts:
            writer.writerow(
                [
                    "todo",
                    post.date[:10],
                    post.title,
                    post.slug,
                    post.link,
                    ", ".join(post.categories),
                    ", ".join(post.tags),
                    post.target_category,
                    post.image_url,
                    "",
                ]
            )

    lines = [
        "# WordPress Migration Inventory",
        "",
        "Status legend: `todo`, `drafted`, `review`, `approved`, `skip`.",
        "",
        f"Total published posts: {len(posts)}",
        "",
        "| Status | Date | Source title | Category | Image |",
        "| --- | --- | --- | --- | --- |",
    ]
    for post in posts:
        image = "yes" if post.image_url else "no"
        lines.append(
            f"| todo | {post.date[:10]} | [{post.title}]({post.link}) | "
            f"{', '.join(post.categories)} -> {post.target_category} | {image} |"
        )
    INVENTORY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_source_markdown(posts: list[Post]) -> None:
    SOURCE_DIR.mkdir(exist_ok=True)
    for post in posts:
        safe_title = post.title.replace('"', '\\"')
        source_categories = (
            "\n".join(f"  - {category}" for category in post.categories)
            if post.categories
            else "  - Blog"
        )
        front_matter = textwrap.dedent(
            f"""\
            ---
            source_title: "{safe_title}"
            source_date: {post.date[:10]}
            source_url: "{post.link}"
            source_categories:
            {source_categories}
            suggested_category: {post.target_category}
            thumbnail_url: "{post.image_url}"
            status: source
            ---

            """
        )
        (SOURCE_DIR / post.source_filename).write_text(
            front_matter + html_to_markdown(post.content_html),
            encoding="utf-8",
        )


def main() -> None:
    posts, _ = read_export()
    write_inventory(posts)
    write_source_markdown(posts)
    print(f"Wrote {INVENTORY_CSV.relative_to(ROOT.parent)}")
    print(f"Wrote {INVENTORY_MD.relative_to(ROOT.parent)}")
    print(f"Wrote {len(posts)} source Markdown files to {SOURCE_DIR.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()
