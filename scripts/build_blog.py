#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

SITE_URL = "https://wau.my.id"
SITE_NAME = "Wauputra"
BLOG_TITLE = "Blog Wauputra"
MONTHS_ID = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]

TITLE_RE = re.compile(r"^(#{1,6})\s+(.*)$")
LIST_RE = re.compile(r"^\s*[-*+]\s+(.*)$")
ORDERED_RE = re.compile(r"^\s*\d+\.\s+(.*)$")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)")
CODE_RE = re.compile(r"`([^`]+)`")
IMAGE_RE = re.compile(r"!\[(.+?)\]\((.+?)\)")
LINK_RE = re.compile(r"\[(.+?)\]\((.+?)\)")
GITHUB_REPO_RE = re.compile(r"^https?://github\.com/([^/\s?#]+)/([^/\s?#]+)(?:/)?$")
GITHUB_BULLET_RE = re.compile(r"^\*\*\[(?P<label>.+?)\]\((?P<url>https?://github\.com/[^)]+)\)\*\*(?::\s*(?P<desc>.*))?$")


@dataclass
class Post:
    title: str
    date: str
    slug: str
    description: str
    keywords: str = ""
    preview_image: str = ""
    tags: List[str] = field(default_factory=list)
    body: str = ""
    source: Path = Path()

    @property
    def sort_key(self):
        try:
            return datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            return datetime.min

    @property
    def pretty_date(self) -> str:
        try:
            dt = datetime.strptime(self.date, "%Y-%m-%d")
            return f"{dt.day} {MONTHS_ID[dt.month - 1]} {dt.year}"
        except ValueError:
            return self.date


BLOG_STYLE = """<style>
  :root { --bg:#0a0a0a; --panel:rgba(20,20,20,.82); --text:#f8fafc; --muted:#b0b0b0; --line:rgba(255,255,255,.1); }
  *{box-sizing:border-box} html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:Inter,system-ui,-apple-system,sans-serif;}
  body{min-height:100vh} a{color:inherit} .wrap{max-width:960px;margin:0 auto;padding:32px 16px 64px}
  .nav{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:28px;flex-wrap:wrap}
  .brand{font-family:'Space Grotesk',Inter,sans-serif;font-size:1.4rem;font-weight:700;text-decoration:none}
  .btn{display:inline-flex;align-items:center;gap:.5rem;padding:.75rem 1rem;border-radius:.9rem;text-decoration:none;border:1px solid var(--line);background:#fff;color:#000;font-weight:600}
  .hero{padding:28px;border-radius:24px;background:linear-gradient(180deg, rgba(255,255,255,.04), rgba(255,255,255,.02));border:1px solid var(--line);margin-bottom:22px}
  h1{margin:0 0 12px;font-family:'Space Grotesk',Inter,sans-serif;font-size:clamp(2rem,4vw,3.4rem);line-height:1.05}
  h2,h3{font-family:'Space Grotesk',Inter,sans-serif}
  p,li{line-height:1.75;color:var(--muted)}
  .grid{display:grid;grid-template-columns:1.4fr .6fr;gap:16px;margin-top:20px}
  .card{padding:22px;border-radius:20px;background:var(--panel);border:1px solid var(--line)}
  .card-thumb{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;margin:0 0 14px;border:1px solid var(--line);background:#111}
  .article-cover{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:20px;margin:0 0 20px;border:1px solid var(--line);background:#111}
  .link-card{margin:14px 0}
  .link-card-inner{display:grid;grid-template-columns:180px 1fr;gap:16px;padding:16px;border-radius:18px;border:1px solid var(--line);background:rgba(255,255,255,.03);text-decoration:none;color:inherit;overflow:hidden}
  .link-card-thumb{width:100%;height:100%;min-height:120px;object-fit:cover;border-radius:14px;border:1px solid var(--line);background:#111}
  .link-card-body{display:flex;flex-direction:column;justify-content:center;gap:6px}
  .link-card-kicker{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:#8f8f8f}
  .link-card-title{font-family:'Space Grotesk',Inter,sans-serif;font-size:1.05rem;font-weight:700;color:var(--text)}
  .link-card-desc{color:var(--muted);line-height:1.6}
  .link-card-url{font-size:.9rem;color:#9f9f9f}
  @media (max-width:700px){.link-card-inner{grid-template-columns:1fr}.link-card-thumb{min-height:180px}}
  .meta{font-size:.92rem;color:#8f8f8f;margin:.35rem 0 0}
  .tag{display:inline-block;margin:0 .45rem .45rem 0;padding:.4rem .7rem;border-radius:999px;background:rgba(255,255,255,.06);border:1px solid var(--line);font-size:.88rem}
  .post-link{display:inline-flex;align-items:center;gap:.5rem;margin-top:8px;padding:.7rem 1rem;border-radius:12px;background:#fff;color:#000;text-decoration:none;font-weight:600}
  .list{display:flex;flex-wrap:wrap;gap:8px}
  article p:first-child{margin-top:0}
  article h2{margin-top:1.6rem}
  article h3{margin-top:1.2rem}
  article ul, article ol{color:var(--muted)}
  pre{overflow:auto;padding:16px;border-radius:16px;background:#050505;border:1px solid var(--line)}
  code{background:rgba(255,255,255,.06);padding:.15rem .35rem;border-radius:.35rem}
  pre code{background:transparent;padding:0}
  @media (max-width:820px){.grid{grid-template-columns:1fr}}
</style>"""


def split_tags(raw: str) -> List[str]:
    if not raw:
        return []
    return [t.strip() for t in re.split(r"[,;]", raw) if t.strip()]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def parse_frontmatter(text: str) -> tuple[Dict[str, str], str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    fm_text = parts[0].split("---\n", 1)[1]
    body = parts[1].strip() + "\n"
    data: Dict[str, str] = {}
    def unquote(value: str) -> str:
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            return value[1:-1]
        return value

    for line in fm_text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip().lower()] = unquote(value)
    return data, body


def inline_format(text: str) -> str:
    escaped = html.escape(text)
    escaped = IMAGE_RE.sub(
        lambda m: f'<img src="{html.escape(m.group(2), quote=True)}" alt="{html.escape(m.group(1), quote=True)}" style="max-width:100%;height:auto;border-radius:16px;" />',
        escaped,
    )
    escaped = LINK_RE.sub(lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1))}</a>', escaped)
    escaped = CODE_RE.sub(lambda m: f"<code>{html.escape(m.group(1))}</code>", escaped)
    escaped = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", escaped)
    escaped = ITALIC_RE.sub(lambda m: f"<em>{m.group(1)}</em>", escaped)
    return escaped


def github_link_card(label: str, url: str, desc_html: str = "") -> str:
    match = GITHUB_REPO_RE.match(url.strip())
    if not match:
        return ""
    owner, repo = match.group(1), match.group(2)
    repo_name = repo.replace("-", " ").replace("_", " ").title()
    image_url = f"https://opengraph.githubassets.com/1/{owner}/{repo}"
    desc_html = desc_html.strip() or html.escape(f"GitHub repo • {owner}/{repo}")
    return f'''
<div class="link-card github-card">
  <a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener noreferrer" class="link-card-inner">
    <img class="link-card-thumb" src="{html.escape(image_url, quote=True)}" alt="{html.escape(label, quote=True)} preview" />
    <div class="link-card-body">
      <div class="link-card-kicker">GitHub</div>
      <div class="link-card-title">{html.escape(label or repo_name)}</div>
      <div class="link-card-desc">{desc_html}</div>
      <div class="link-card-url">github.com/{html.escape(owner)}/{html.escape(repo)}</div>
    </div>
  </a>
</div>'''



def markdown_to_html(md: str) -> str:
    lines = md.splitlines()
    out: List[str] = []
    paragraph: List[str] = []
    list_type: Optional[str] = None
    in_code = False
    code_lines: List[str] = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{' '.join(paragraph)}</p>")
            paragraph = []

    def close_list():
        nonlocal list_type
        if list_type == "ul":
            out.append("</ul>")
        elif list_type == "ol":
            out.append("</ol>")
        list_type = None

    for raw in lines:
        line = raw.rstrip()
        if line.strip().startswith("```"):
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                flush_paragraph()
                close_list()
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            flush_paragraph()
            close_list()
            continue

        heading = TITLE_RE.match(line)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            content = inline_format(heading.group(2))
            out.append(f"<h{level}>{content}</h{level}>")
            continue

        bullet = LIST_RE.match(line)
        if bullet:
            flush_paragraph()
            github_bullet = GITHUB_BULLET_RE.match(bullet.group(1).strip())
            if github_bullet:
                close_list()
                out.append(
                    github_link_card(
                        github_bullet.group("label"),
                        github_bullet.group("url"),
                        inline_format(github_bullet.group("desc") or ""),
                    )
                )
                continue
            if list_type != "ul":
                close_list()
                out.append("<ul>")
                list_type = "ul"
            out.append(f"<li>{inline_format(bullet.group(1))}</li>")
            continue

        ordered = ORDERED_RE.match(line)
        if ordered:
            flush_paragraph()
            if list_type != "ol":
                close_list()
                out.append("<ol>")
                list_type = "ol"
            out.append(f"<li>{inline_format(ordered.group(1))}</li>")
            continue

        flush_paragraph()
        close_list()
        out.append(f"<p>{inline_format(line)}</p>")

    flush_paragraph()
    close_list()
    if in_code:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(out)


def read_posts(posts_dir: Path) -> List[Post]:
    posts: List[Post] = []
    for path in sorted(posts_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(raw)
        title = fm.get("title") or path.stem.replace("-", " ").title()
        slug = fm.get("slug") or slugify(title)
        date_value = fm.get("date") or "1970-01-01"
        description = fm.get("description") or body.split("\n\n", 1)[0].replace("#", "").strip()
        keywords = fm.get("keywords", "")
        preview_image = fm.get("preview_image", "")
        tags = split_tags(fm.get("tags", ""))
        posts.append(Post(title=title, date=date_value, slug=slug, description=description, keywords=keywords, preview_image=preview_image, tags=tags, body=body, source=path))
    return sorted(posts, key=lambda p: p.sort_key, reverse=True)


def pretty_date(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return f"{dt.day} {MONTHS_ID[dt.month - 1]} {dt.year}"
    except ValueError:
        return date_str


def page_head(title: str, description: str, canonical: str, keywords: str = "", extra_meta: str = "", extra_ld: str = "") -> str:
    keywords_meta = f'<meta name="keywords" content="{html.escape(keywords)}" />\n  ' if keywords else ''
    return f"""<!doctype html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{html.escape(description)}" />
  <meta name="robots" content="index,follow" />
  {keywords_meta}<link rel="canonical" href="{html.escape(canonical, quote=True)}" />
  <meta property="og:site_name" content="{SITE_NAME}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(description)}" />
  <meta property="og:url" content="{html.escape(canonical, quote=True)}" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{html.escape(title)}" />
  <meta name="twitter:description" content="{html.escape(description)}" />
  {extra_meta}
  {BLOG_STYLE}
  {extra_ld}
</head>"""


def render_index(posts: List[Post]) -> str:
    cards: List[str] = []
    for post in posts:
        tags_html = ''.join(f'<span class="tag">{html.escape(tag)}</span>' for tag in post.tags)
        thumb_html = f'<img class="card-thumb" src="{html.escape(post.preview_image, quote=True)}" alt="{html.escape(post.title, quote=True)}" />' if post.preview_image else ''
        cards.append(f"""
        <article class="card" style="margin-bottom:16px;">
          {thumb_html}
          <p class="meta">{html.escape(pretty_date(post.date))} • {html.escape(', '.join(post.tags) if post.tags else 'Artikel')}</p>
          <h3 style="margin:0 0 8px; color:var(--text);">{html.escape(post.title)}</h3>
          <p>{html.escape(post.description)}</p>
          <div class="list">{tags_html}</div>
          <a class="post-link" href="/blog/{html.escape(post.slug)}/">Baca artikel →</a>
        </article>""")
    tags = ["Tech", "AI", "Crypto", "Tips and Trick", "Opini Teknologi", "Pribadi"]
    ld = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": BLOG_TITLE,
        "url": f"{SITE_URL}/blog/",
        "description": "Blog personal Wauputra berisi tulisan seputar teknologi, AI, crypto, tips and trick, opini teknologi, dan catatan pribadi.",
        "blogPost": [
            {
                "@type": "BlogPosting",
                "headline": p.title,
                "datePublished": p.date,
                "url": f"{SITE_URL}/blog/{p.slug}/",
            }
            for p in posts
        ],
    }
    ld_script = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    return f"""{page_head(BLOG_TITLE + ' | Tech, AI, Crypto, dan Catatan Pribadi', 'Blog personal Wauputra berisi tulisan seputar teknologi, AI, crypto, tips and trick, opini teknologi, dan catatan pribadi.', f'{SITE_URL}/blog/', 'blog teknologi, AI, crypto, tips and trick, opini teknologi, blog pribadi Wauputra', extra_ld=ld_script)}
<body>
  <div class="wrap">
    <div class="nav">
      <a class="brand" href="/">Wauputra</a>
      <a class="btn" href="/">← Kembali ke Home</a>
    </div>

    <section class="hero">
      <p class="meta">Blog personal • Tech • AI • Crypto • Opini</p>
      <h1>Blog Wauputra</h1>
      <p>
        Tempat gw nulis hal-hal seputar <strong>teknologi</strong>, <strong>news AI</strong>, <strong>crypto</strong>,
        tips and trick, opini teknologi, dan juga sedikit catatan pribadi.
      </p>
      <p>
        Gw bikin blog ini buat nyimpen ide, insight, dan hal-hal yang menurut gw layak dibagi ke orang lain.
      </p>
    </section>

    <div class="grid">
      <section>
        <h2>Artikel Terbaru</h2>
        {''.join(cards) if cards else '<div class="card"><p>Belum ada artikel.</p></div>'}
      </section>

      <aside class="card">
        <h2>Topik</h2>
        <div class="list">
          {''.join(f'<span class="tag">{t}</span>' for t in tags)}
        </div>
      </aside>
    </div>
  </div>
</body>
</html>"""


def render_post(post: Post) -> str:
    tags_html = ''.join(f'<span class="tag">{html.escape(tag)}</span>' for tag in post.tags)
    body_md = post.body.lstrip()
    if body_md.startswith(f"# {post.title}"):
        body_md = body_md.split("\n", 1)[1].lstrip("\n")
    body_html = markdown_to_html(body_md)
    cover_html = (
        f'<img class="article-cover" src="{html.escape(post.preview_image, quote=True)}" alt="{html.escape(post.title, quote=True)}" />'
        if post.preview_image else ''
    )
    social_meta = ""
    if post.preview_image:
        social_meta = (
            f'<meta property="og:image" content="{html.escape(post.preview_image, quote=True)}" />\n  '
            f'<meta property="og:image:alt" content="{html.escape(post.title)}" />\n  '
            f'<meta name="twitter:image" content="{html.escape(post.preview_image, quote=True)}" />\n  '
            f'<meta name="twitter:image:alt" content="{html.escape(post.title)}" />\n  '
        )
    ld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post.title,
        "description": post.description,
        "datePublished": post.date,
        "dateModified": post.date,
        "author": {"@type": "Person", "name": SITE_NAME},
        "publisher": {"@type": "Person", "name": SITE_NAME},
        "mainEntityOfPage": f"{SITE_URL}/blog/{post.slug}/",
        "url": f"{SITE_URL}/blog/{post.slug}/",
    }
    if post.preview_image:
        ld["image"] = post.preview_image
    ld_script = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    return f"""{page_head(f'{post.title} | Wauputra', post.description, f'{SITE_URL}/blog/{post.slug}/', post.keywords, extra_meta=social_meta, extra_ld=ld_script)}
<body>
  <div class="wrap">
    <div class="nav">
      <a class="brand" href="/blog/">Blog Wauputra</a>
      <a class="btn" href="/blog/">← Semua Artikel</a>
    </div>

    <article class="hero">
      <p class="meta">{html.escape(pretty_date(post.date))} • {html.escape(', '.join(post.tags) if post.tags else 'Artikel')}</p>
      <h1>{html.escape(post.title)}</h1>
      {cover_html}
      <div class="list" style="margin-bottom:12px;">{tags_html}</div>
      {body_html}
    </article>

    <div class="grid">
      <section class="card">
        <h2>Artikel lain</h2>
        <a class="post-link" href="/blog/">Lihat daftar artikel →</a>
      </section>
      <aside class="card">
        <h2>Topik yang sering muncul</h2>
        <div class="list">
          {tags_html or '<span class="tag">Tech</span>'}
        </div>
      </aside>
    </div>
  </div>
</body>
</html>"""


def prettify_xml(xml_bytes: bytes) -> str:
    return minidom.parseString(xml_bytes).toprettyxml(indent="  ", encoding="utf-8").decode("utf-8")


def generate_sitemap(posts: List[Post]) -> str:
    urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    urls = [
        (f"{SITE_URL}/", date.today().isoformat()),
        (f"{SITE_URL}/blog/", date.today().isoformat()),
    ]
    urls += [(f"{SITE_URL}/blog/{p.slug}/", p.date) for p in posts]
    for loc, lastmod in urls:
        url = SubElement(urlset, "url")
        SubElement(url, "loc").text = loc
        SubElement(url, "lastmod").text = lastmod
        SubElement(url, "changefreq").text = "weekly"
        SubElement(url, "priority").text = "1.0" if loc == f"{SITE_URL}/" else "0.8"
    return prettify_xml(tostring(urlset, encoding="utf-8"))


def generate_robots() -> str:
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def write_site(repo_root: Path, posts: List[Post]) -> None:
    blog_dir = repo_root / "blog"
    blog_dir.mkdir(parents=True, exist_ok=True)
    (blog_dir / "index.html").write_text(render_index(posts), encoding="utf-8")
    for post in posts:
        post_dir = blog_dir / post.slug
        post_dir.mkdir(parents=True, exist_ok=True)
        (post_dir / "index.html").write_text(render_post(post), encoding="utf-8")
    (repo_root / "robots.txt").write_text(generate_robots(), encoding="utf-8")
    (repo_root / "sitemap.xml").write_text(generate_sitemap(posts), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build static blog pages from Markdown posts.")
    parser.add_argument("--repo", default=".", help="Path to the site repository")
    parser.add_argument("--source", default="content/blog", help="Path to Markdown sources")
    args = parser.parse_args()

    repo_root = Path(args.repo).expanduser().resolve()
    source_dir = (repo_root / args.source).resolve()
    if not source_dir.exists():
        raise SystemExit(f"Markdown source folder not found: {source_dir}")

    posts = read_posts(source_dir)
    write_site(repo_root, posts)
    print(f"Built {len(posts)} post(s) into {repo_root / 'blog'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
