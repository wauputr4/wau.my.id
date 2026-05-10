# wau.my.id

Static personal website and blog for **wau.my.id**.

## Isi repo

- `index.html` — homepage utama
- `blog/` — output blog static
  - `blog/index.html` — halaman daftar artikel
  - `blog/<slug>/index.html` — halaman artikel
- `content/blog/` — source Markdown untuk artikel
- `scripts/build_blog.py` — generator HTML, sitemap, dan robots
- `robots.txt` — file SEO dasar
- `sitemap.xml` — peta URL untuk search engine

## Workflow nambah artikel

1. Tambah file Markdown baru di `content/blog/`.
2. Isi frontmatter:

```yaml
---
title: Judul Artikel
date: 2026-05-10
slug: judul-artikel
description: Deskripsi singkat artikel.
keywords: keyword1, keyword2
tags: Tech, AI, Pribadi
---
```

3. Tulis isi artikel pakai Markdown.
4. Jalankan generator:

```bash
python3 scripts/build_blog.py --repo .
```

5. Commit hasilnya dan push ke GitHub.
6. Deploy ke `/var/www/wau.my.id/html`.

## Catatan

- Homepage utama dijaga tetap stabil.
- Tambah artikel cukup lewat Markdown, generator yang urus HTML dan sitemap.
- Kalau nambah post baru, pastikan slug unik.
