---
title: AI Agent emang Jago Ngoding, Tapi Jangan Kasih Dia Kunci Arsitektur Sendirian
date: 2026-05-29
slug: ai-agent-jago-ngoding-kunci-arsitektur
description: AI agent makin jago bantu coding, tapi keputusan arsitektur tetap butuh manusia yang paham konteks, guardrail, dan trade-off jangka panjang.
keywords: AI agent coding, vibe coding, vibe architecture, constraint decay, Claude bukan arsitek, arsitektur software AI
tags: AI, Tech, Coding, Arsitektur, Opini
preview_image: https://wau.my.id/assets/og/ai-agent-jago-ngoding-kunci-arsitektur.png
og_image_width: 1200
og_image_height: 630
---

# AI Agent emang Jago Ngoding, Tapi Jangan Kasih Dia Kunci Arsitektur Sendirian

Ada fase lucu di dunia dev sekarang: tiap minggu ada demo AI agent yang kelihatan makin sakti. Bisa generate modul, refactor repo, bikin test, bahkan jalanin command sendiri. Tapi makin gw lihat, makin kerasa satu hal: masalah besarnya bukan lagi “AI bisa nulis kode atau nggak”. Masalahnya: siapa yang megang arah arsitekturnya?

## Agent itu kuat, tapi gampang “Lupa Daratan”

Gw baru baca paper soal *Constraint Decay* di arXiv, dan isinya bikin gw manggut-manggut. Intinya, LLM agent bisa jago bikin sesuatu yang kelihatan jalan, tapi makin berat task-nya, makin besar risiko dia ninggalin constraint awal.

Satu batasan kecil kayak “jangan bypass auth”, “jangan ubah schema publik”, atau “pake Clean Architecture” bisa luntur karena agent terlalu fokus bikin kodenya selesai. Ini bukan karena modelnya bodoh, tapi karena prioritasnya sering condong ke “yang penting jalan” dibanding “tetap rapi secara struktur”.

## Claude bukan arsitek Lo

Ada hot take yang bilang: “Claude is not your architect.” Gw setuju banget. AI itu kayak junior cepat yang secara default nggak punya memori organisasi, konteks tim, atau intuisi soal trade-off jangka panjang.

Dia bisa kasih kode yang terlihat efisien, tapi mungkin nabrak pola yang udah tim Lo bangun bertahun-tahun. Solusinya bisa lolos test lokal, tapi belum tentu aman buat migration path, security, rollback, atau biaya operasional.

Arsitektur itu bukan cuma kode rapi. Arsitektur itu soal keputusan: apa yang dikorbankan, apa yang dijaga, siapa yang maintenance, dan siapa yang bangun jam 2 pagi kalau production kebakar.

Kalau keputusan itu Lo serahin ke agent tanpa guardrail ketat, Lo cuma nunggu waktu sampai arsitektur Lo jadi “Vibe Architecture”: kelihatan oke pas demo, tapi rapuh pas masuk dunia nyata.

## Fenomena “Tokenmaxxing” yang bikin dompet kering

Yang juga mulai kerasa: workflow agentic itu bisa mahal. Agent itu bukan cuma “chat sekali lalu selesai”. Dia bisa planning, baca file, nulis patch, jalanin test, gagal, retry, lalu ulang dari awal.

Dalam skala kecil, ini keren. Dalam skala tim, ini bisa jadi biaya orchestration yang serius kalau semua problem dilempar ke agent tanpa batasan jelas.

Ada analogi menarik dari sisi hardware: laporan Epoch AI pernah nunjukin memory/HBM bisa jadi porsi terbesar dari biaya komponen AI chip. Buat workflow agent, ini nyambung secara konsep: makin banyak konteks dan makin panjang loop-nya, makin mahal “ingatan” dan koordinasinya.

Jadi masalahnya bukan cuma “model mana yang paling pinter”, tapi “seberapa disiplin Lo ngasih konteks, batasan, dan review”.

## Opini gw

Buat gw, *Vibe Coding* itu emang masa depan, tapi *Vibe Architecture* itu bahaya kalau dilepas sendirian.

Skill penting dev sekarang bukan prompting aja, tapi **orchestration with judgment**: tahu kapan delegasi, kapan stop, kapan review, dan kapan bilang: “ini bagian manusia dulu yang mikirin arsitekturnya.”

Delegasi itu perlu. Oversight itu wajib.

Jangan sampai Lo jadi bos yang nggak tahu apa yang dikerjain anak buah digitalnya.

## Referensi

- [Constraint Decay: The Fragility of LLM Agents in Back End Code Generation](https://arxiv.org/abs/2605.06445)
- [Claude is not your architect](https://www.hollandtech.net/claude-is-not-your-architect/)
- [AI Chip Component Cost Shares — Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)
