---
title: Alasan kenapa lo mesti mulai vibe coding apps berbasis CLI dibanding Apps berbasis MCP di era AI Agent
date: 2026-05-11
slug: mcp-vs-cli-mana-yang-lebih-baik
description: Semua orang berlomba-lomba bikin apps dengan UX sebagus mungkin, tapi nggak sadar kalau apps berbasis CLI mulai populer dan powerfull untuk user.
keywords: AI agent, CLI vs MCP, OpenClaw, Peter Steinberger, teknologi AI, unix, efisiensi AI, open source CLI
preview_image: https://wau.my.id/assets/og/mcp-vs-cli.jpg
tags: Tech, AI, CLI, OpenClaw, Opini, Open Source
---

# Alasan kenapa lo mesti mulai vibe coding apps berbasis CLI dibanding Apps berbasis MCP di era AI Agent

![Screenshot asli: CLI vs MCP](https://wau.my.id/assets/blog/mcp-vs-cli-source-91b0ecce1014.jpg)

Baru-baru ini gw lagi ngulik soal *AI agent* dan nemu *hot take* menarik dari **Peter Steinberger**, pendiri **OpenClaw**. Dia punya pendapat yang cukup berani: **CLI (Command Line Interface) itu jauh lebih unggul daripada MCP (Model Context Protocol) untuk AI agent.**

Kutipan Peter yang sering banget sliweran di podcast Lex Fridman itu kira-kira begini:

> *"Screw MCPs. Every MCP would be better as a CLI."*

Menurut gw, argumen dia masuk akal banget. Di saat semua orang lagi berlomba-lomba bikin aplikasi dengan UX visual yang *fancy*, banyak yang nggak sadar kalau aplikasi berbasis CLI justru mulai balik populer dan jauh lebih *powerful* buat *user* yang melek teknologi.

## Kenapa CLI Menang Telak?

### 1. AI Itu Jago Pakai Bash
Model AI sekarang *training data*-nya udah kebanjiran konten teknis dan *bash script*. Mereka udah "terbiasa" sama cara kerja *command line*. MCP butuh *schema* JSON yang ribet, sedangkan CLI? Jauh lebih fleksibel. AI nggak perlu belajar protokol baru, cukup kasih akses ke *shell*.

### 2. CLI Itu *Composable* (Bisa Dirangkai)
Ini poin paling krusial. CLI itu punya prinsip *unix philosophy*: satu alat buat satu tugas, tapi bisa dirangkai. Output CLI bisa lo *pipe* ke `jq`, difilter, digabung sama *script* lain. MCP? Seringkali sifatnya kaku dan cuma jadi "sampah" di *context window* model AI.

### 3. Efisiensi Context Window
Dengan CLI, AI bisa ngerjain hal yang efisien banget: ambil data mentah, filter pake `jq`, terus cuma kirim hasil akhirnya ke model. *Context* tetap ramping, efisien, dan AI jadi lebih fokus.

## *Vibe Coding* dengan CLI
Itu sebabnya gw lagi tertarik banget buat bikin banyak *apps open source* berbasis *CLI-base*. Menurut gw, inilah cara terbaik buat *AI agent* berinteraksi dengan dunia: praktis, modular, dan efisien.

Beberapa *project* yang lagi gw *develop* saat ini:

- **[Hermeneia](https://github.com/wauputr4/hermeneia)**: *Open source* AI *workflow content engine*.
- **[Rute Bayar](https://github.com/pendig/rute-bayar)**: *Open source payment router* khusus untuk *Indonesian payment gateway*.
- **[Kelompok](https://github.com/pendig/kelompok)**: *Open source* CRM yang dirancang khusus untuk *Nonprofits*.
- **[Mizan](https://github.com/pendig/mizan)**: AI Gateway buat *user controlled access*.

## Kesimpulan: Jadi *Engineer* Unix, Bukan Budak Protokol
Filosofi Peter di sini simpel: **AI agent harusnya berinteraksi sama dunia seperti *engineer* Unix.**

Jangan terjebak di *protocol layer* yang kaku. Manfaatkan CLI yang kecil, *modular*, dan bisa dirangkai bebas. Itu kunci biar *AI agent* lo nggak cuma sekadar "pinter", tapi juga "praktis".

Lo gimana? Masih tim MCP yang terstruktur, atau setuju sama gw kalau CLI itu masa depan *AI agent*? *Sharing* di bawah ya.
