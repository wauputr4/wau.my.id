# wau.my.id

Static personal website and blog for **wau.my.id**.

## Isi repo

- `index.html` — homepage utama
- `blog/` — output blog static
  - `blog/index.html` — halaman daftar artikel
  - `blog/<slug>/index.html` — halaman artikel
- `content/blog/` — source Markdown untuk artikel
- `scripts/build_blog.py` — generator HTML, sitemap, dan robots
- `scripts/publish.sh` — helper publish 1 langkah: build kalau perlu, commit, push
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
4. Jalankan publish helper:

```bash
./scripts/publish.sh -m "Add new article"
```

Helper ini akan:
- auto-detect kalau ada perubahan di `content/blog/`
- jalanin `python3 scripts/build_blog.py --repo .` kalau perlu
- `git add -A`
- commit
- push ke GitHub

5. Cloudflare Pages auto-build dari GitHub repo, jadi deploy terjadi otomatis setelah push.

## Workflow non-blog

Kalau yang diubah bukan artikel blog, cukup edit file homepage/CSS/gambar/statik lain lalu jalankan:

```bash
./scripts/publish.sh -m "Update site"
```

Script akan skip build blog kalau `content/blog/` tidak berubah.

## Catatan Cloudflare Pages

- Framework preset: `None`
- **Build command wajib diisi**: `python3 scripts/build_blog.py --repo .`
- Build output directory: `.`
- Tidak ada deploy command terpisah di Pages; deploy terjadi otomatis setelah push ke GitHub.
- Custom domain: `wau.my.id`

## Catatan

- Homepage utama dijaga tetap stabil.
- Tambah artikel cukup lewat Markdown, generator yang urus HTML dan sitemap.
- Kalau nambah post baru, pastikan slug unik.
