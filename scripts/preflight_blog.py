#!/usr/bin/env python3
"""Safety checks for wau.my.id static blog before preview/publish.

This script is dependency-free so it can run on the server before any publish
step. It checks the bugs that previously slipped through:
- preview_image points to a deployed local asset
- OG dimensions match the real PNG/JPEG/SVG file when declared
- rendered posts do not duplicate the preview image as both cover + body image
- generated HTML has the expected social image tags and article title
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import struct
import sys
from pathlib import Path

SITE_URL = "https://wau.my.id"


class PreflightError(Exception):
    pass


def load_build_blog(repo_root: Path):
    module_path = repo_root / "scripts" / "build_blog.py"
    spec = importlib.util.spec_from_file_location("build_blog", module_path)
    if spec is None or spec.loader is None:
        raise PreflightError(f"Cannot load {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["build_blog"] = module
    spec.loader.exec_module(module)
    return module


def local_asset_path(repo_root: Path, url_or_path: str) -> Path | None:
    value = url_or_path.strip()
    if value.startswith(SITE_URL + "/"):
        return repo_root / value.removeprefix(SITE_URL + "/")
    if value.startswith("/"):
        return repo_root / value.lstrip("/")
    if value.startswith("http://") or value.startswith("https://"):
        return None
    return repo_root / value


def image_size(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    suffix = path.suffix.lower()
    if suffix == ".png":
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            raise PreflightError(f"Invalid PNG: {path}")
        return struct.unpack(">II", data[16:24])
    if suffix in {".jpg", ".jpeg"}:
        if len(data) < 4 or data[:2] != b"\xff\xd8":
            raise PreflightError(f"Invalid JPEG: {path}")
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            i += 2
            if marker in {0xD8, 0xD9}:
                continue
            if i + 2 > len(data):
                break
            length = struct.unpack(">H", data[i:i + 2])[0]
            if marker in range(0xC0, 0xC4):
                if i + 7 > len(data):
                    break
                height, width = struct.unpack(">HH", data[i + 3:i + 7])
                return width, height
            i += length
        raise PreflightError(f"Cannot read JPEG dimensions: {path}")
    if suffix == ".svg":
        text = path.read_text(encoding="utf-8", errors="ignore")
        view_box = re.search(r"viewBox=['\"][^'\"]*\s(\d+(?:\.\d+)?)\s(\d+(?:\.\d+)?)[" + "'\"]", text)
        if view_box:
            return int(float(view_box.group(1))), int(float(view_box.group(2)))
        width = re.search(r"\bwidth=['\"](\d+)", text)
        height = re.search(r"\bheight=['\"](\d+)", text)
        if width and height:
            return int(width.group(1)), int(height.group(1))
        return None
    return None


def html_img_srcs(rendered_html: str) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []
    for img in re.findall(r"<img\b[^>]*>", rendered_html):
        src = re.search(r"\bsrc=['\"]([^'\"]+)['\"]", img)
        klass = re.search(r"\bclass=['\"]([^'\"]+)['\"]", img)
        if src:
            results.append((src.group(1), klass.group(1) if klass else ""))
    return results


def check_posts(repo_root: Path, source: str) -> list[str]:
    build_blog = load_build_blog(repo_root)
    posts_dir = (repo_root / source).resolve()
    posts = build_blog.read_posts(posts_dir)
    errors: list[str] = []
    warnings: list[str] = []

    slugs: dict[str, Path] = {}
    for post in posts:
        prefix = f"{post.source.relative_to(repo_root)}: "
        if post.slug in slugs:
            errors.append(f"{prefix}duplicate slug '{post.slug}' also used by {slugs[post.slug].relative_to(repo_root)}")
        slugs[post.slug] = post.source

        if not post.title.strip():
            errors.append(prefix + "missing title")
        if not post.description.strip():
            errors.append(prefix + "missing description")
        if not post.date.strip():
            errors.append(prefix + "missing date")

        rendered_path = repo_root / "blog" / post.slug / "index.html"
        if not rendered_path.exists():
            errors.append(prefix + f"generated HTML missing: {rendered_path.relative_to(repo_root)}; run scripts/build_blog.py first")
            continue
        rendered = rendered_path.read_text(encoding="utf-8")
        if f"<h1>{post.title}</h1>" not in rendered:
            errors.append(prefix + "rendered article title not found in expected <h1>")

        if post.preview_image:
            asset = local_asset_path(repo_root, post.preview_image)
            if asset is None:
                warnings.append(prefix + f"preview_image is remote, cannot verify local file: {post.preview_image}")
            elif not asset.exists():
                errors.append(prefix + f"preview_image file missing: {asset.relative_to(repo_root)}")
            elif asset.stat().st_size < 1024:
                errors.append(prefix + f"preview_image looks too small/empty: {asset.relative_to(repo_root)} ({asset.stat().st_size} bytes)")
            else:
                try:
                    size = image_size(asset)
                    if size and post.og_image_width and post.og_image_height:
                        declared = (int(post.og_image_width), int(post.og_image_height))
                        if declared != size:
                            errors.append(prefix + f"og_image_width/height {declared[0]}x{declared[1]} does not match {asset.relative_to(repo_root)} {size[0]}x{size[1]}")
                except Exception as exc:
                    errors.append(prefix + str(exc))

            if f'<meta property="og:image" content="{post.preview_image}"' not in rendered:
                errors.append(prefix + "rendered HTML missing og:image for preview_image")
            if f'<meta name="twitter:image" content="{post.preview_image}"' not in rendered:
                errors.append(prefix + "rendered HTML missing twitter:image for preview_image")

            img_srcs = html_img_srcs(rendered)
            cover_count = sum(1 for src, klass in img_srcs if src == post.preview_image and "article-cover" in klass)
            body_count = sum(1 for src, klass in img_srcs if src == post.preview_image and "article-cover" not in klass)
            body_mentions_preview = any(token in post.body for token in (f"]({post.preview_image})", f'src="{post.preview_image}"', f"src='{post.preview_image}'"))
            if body_mentions_preview and cover_count:
                errors.append(prefix + "preview_image is used in body, but rendered HTML still adds article-cover duplicate")
            if cover_count and body_count:
                errors.append(prefix + "rendered HTML duplicates preview_image as article-cover and body image")

    return [*("ERROR: " + e for e in errors), *("WARN: " + w for w in warnings)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run blog preflight checks before publishing.")
    parser.add_argument("--repo", default=".", help="Path to the site repository")
    parser.add_argument("--source", default="content/blog", help="Path to Markdown sources")
    args = parser.parse_args()

    repo_root = Path(args.repo).expanduser().resolve()
    messages = check_posts(repo_root, args.source)
    for message in messages:
        print(message, file=sys.stderr if message.startswith("ERROR") else sys.stdout)
    if any(message.startswith("ERROR") for message in messages):
        print("Blog preflight failed.", file=sys.stderr)
        return 1
    checked = len(list((repo_root / args.source).glob("*.md")))
    print(f"Blog preflight passed for {checked} post(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
