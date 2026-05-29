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

Ada fase lucu di dunia dev sekarang: tiap minggu ada demo AI agent yang kelihatannya makin sakti. Bisa generate modul, refactor repo, bikin test, bahkan jalanin command sendiri.

Tapi makin sering gw lihat demo kayak gitu, makin kerasa satu hal: masalah besarnya sekarang bukan lagi “seberapa kompleks task yang bisa diselesaikan agent?” tapi “siapa yang megang arah arsitekturnya?”

## Agent itu kuat, tapi gampang lupa daratan

Gw baru baca paper soal *Constraint Decay* di arXiv, dan isinya bikin gw manggut-manggut: bener juga.

Intinya, LLM agent bisa jago bikin sesuatu yang kelihatannya jalan dan aman. Tapi makin berat task-nya, makin besar juga risiko dia ninggalin constraint awal.

Constraint kecil kayak “jangan bypass auth”, “jangan ubah schema publik”, atau “pake Clean Architecture” bisa pelan-pelan luntur karena agent terlalu fokus menyelesaikan task. Bukan karena modelnya goblok, tapi karena prioritasnya sering condong ke “yang penting jalan dulu” daripada “tetap rapi secara struktur”.

Dan ini bahaya, karena di software, hal yang kelihatan kecil di awal sering jadi utang teknis yang paling ngeselin di akhir.

## Claude bukan arsitek lo

Ada hot take yang bilang: “Claude is not your architect.” Gw setuju banget.

AI itu lebih mirip junior yang pengen cepat bantu. Dia bisa produktif, bisa kasih solusi yang kelihatan efisien, tapi secara default dia nggak punya memori organisasi, konteks tim, atau intuisi soal trade-off jangka panjang.

Dia bisa bikin kode yang lolos test lokal, tapi belum tentu aman buat migration path, security, rollback, atau biaya operasional. Bisa juga solusinya nabrak pola yang tim lo bangun bertahun-tahun, cuma karena di konteks chat saat itu polanya nggak cukup jelas.

Arsitektur itu bukan sekadar kode rapi. Arsitektur itu soal keputusan: apa yang dikorbankan, apa yang dijaga, siapa yang bakal maintain, dan siapa yang bangun jam 2 pagi kalau production kebakar wkwkwk.

Kalau keputusan itu lo serahin ke agent tanpa guardrail ketat, tinggal tunggu waktu sampai arsitektur lo berubah jadi “Vibe Architecture”: kelihatan oke pas demo, tapi rapuh pas beneran dideploy.

## Tokenmaxxing bikin dompet ikut mikir

Hal lain yang mulai kerasa: workflow agentic itu bisa mahal banget.

Agent jangan lo bayangin cuma kayak chat biasa yang jawab sekali lalu selesai. Dia bisa planning, baca file, nulis patch, jalanin test, gagal, retry, lalu ulang dari awal. Dalam skala kecil, ini keren. Dalam skala tim, ini bisa jadi biaya orchestration yang serius kalau semua problem dilempar ke agent tanpa batasan jelas.

Ada analogi menarik dari sisi hardware. Laporan Epoch AI pernah nunjukin kalau memory/HBM bisa jadi porsi besar dari biaya komponen AI chip. Di workflow agent, konsepnya mirip: makin banyak konteks yang dibawa, makin panjang loop-nya, makin mahal juga “ingatan” dan koordinasinya.

Jadi problem yang perlu kita pecahin bukan cuma “model mana yang paling pintar”, tapi “seberapa disiplin kita ngasih konteks, batasan, dan review”.

Menurut gw, kemampuan nge-manage agent ini justru jadi skill yang mahal sekarang.

## Opini gw

Buat gw, *Vibe Coding* bukan masa depan lagi. Itu udah jadi basic skill di era AI.

Tapi *Vibe Architecture*? Nah, itu bahaya kalau dilepas sendirian.

Skill penting dev sekarang bukan prompting doang, tapi **orchestration with judgment**: tahu kapan delegasi, kapan stop, kapan review, dan kapan bilang, “bagian ini manusia dulu yang mikirin arsitekturnya.”

Delegasi itu perlu. Oversight itu wajib.

Jangan sampai kita jadi bos yang nggak ngerti apa yang lagi dikerjain anak buah digital kita sendiri. Jangan terlalu mikro-manage, tapi jangan juga terlalu lepas kendali.

Sederhana, tapi rumit. Ya gitu lah wkwkwk.

## Referensi

- [Constraint Decay: The Fragility of LLM Agents in Back End Code Generation](https://arxiv.org/abs/2605.06445)
- [Claude is not your architect](https://www.hollandtech.net/claude-is-not-your-architect/)
- [AI Chip Component Cost Shares — Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)
