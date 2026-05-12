---
title: Alasan Kreator OpenClaw Tak Lagi Membaca Kode Baris per Baris
date: 2026-05-12
slug: alasan-kreator-openclaw-tak-lagi-membaca-kode-baris-per-baris
description: Peter Steinberger menganggap banyak kode itu membosankan dan lebih fokus ke niat, arsitektur, dan review AI daripada baca kode baris per baris.
keywords: OpenClaw, Peter Steinberger, ambient programming, AI agent, code review, AI review, software development, intent based programming
preview_image: https://wau.my.id/assets/blog/openclaw-article.jpg
tags: Tech, AI, Open Source, Opini
---

# Alasan Kreator OpenClaw Tak Lagi Membaca Kode Baris per Baris

![Ilustrasi OpenClaw dan ambient programming](https://wau.my.id/assets/blog/openclaw-article.jpg)

Peter Steinberger, kreator framework AI **OpenClaw**, punya cara kerja yang agak beda dari kebanyakan engineer. Dia nggak lagi ngabisin waktu buat baca kode satu baris demi satu baris. Buat dia, cara kerja lama itu udah mulai kalah efisien di era AI agent yang makin matang.

Yang dia dorong sekarang disebut sebagai *ambient programming*. Intinya sederhana: AI yang nulis kode, AI yang ngetes, dan manusia cukup ikut ngarahin arah besarnya lalu klik buat konfirmasi. Buat banyak orang, ini kedengeran ekstrem. Tapi kalau Lo lihat cara kerja software modern hari ini, sebenarnya masuk akal juga.

## 1. Banyak Kode Itu Emang Ngebosenin

Menurut Steinberger, sebagian besar kode itu bukan bagian yang seru. Banyak kode cuma tugasnya mindahin data dari satu bentuk ke bentuk lain. Ada juga bagian yang isinya mekanis banget: nyusun UI, nyamain tombol, ngatur layout, atau ngerjain hal repetitif yang sebenarnya nggak butuh kreativitas tinggi.

Nah, di titik itu dia merasa nggak perlu buang energi buat baca semuanya secara manual. Kalau sebuah bagian cuma jadi mesin penggerak biasa, ya biarin AI yang handle. Gw paham sih kenapa dia mikir gitu. Kalau kerjaan lo tiap hari ketemu hal yang sifatnya template dan berulang, lama-lama baca semuanya satu per satu memang kerasa buang waktu.

## 2. Fokus ke Niat, Bukan Implementasi

Hal yang paling menarik dari pendekatan dia adalah cara dia melihat *pull request*. Saat ada PR masuk, Steinberger nggak lagi ngelihatnya sebagai kumpulan baris kode yang harus dibedah satu-satu.

Dia justru nanya hal yang lebih penting: **apakah Lo paham niat dari PR ini?**

Buat dia, pertanyaan utama bukan lagi "ini ditulis pake cara apa", tapi "masalah apa yang sebenarnya lagi diselesaikan?". Kalau niatnya jelas dan arsitekturnya masuk akal, detail implementasi bisa dibantu AI. Jadi manusia fokus ke arah, bukan ke keribetan syntax.

Menurut gw, ini pergeseran mindset yang lumayan besar. Developer zaman sekarang nggak cukup cuma jago baca kode; Lo juga harus jago ngebaca problem dan ngejaga supaya solusi yang lahir tetap waras.

## 3. AI Review Lebih Cepat dan Lebih Konsisten

Alasan ketiga cukup praktis: review manual itu makan waktu.

Kalau Lo harus baca semua kode sendiri, apalagi kalau PR-nya panjang, fokus bisa habis cuma buat cek detail kecil. Steinberger lebih milih pakai AI buat bantu menilai apakah ada bug, hal berbahaya, atau keputusan arsitektur yang kurang pas. Dengan begitu, dia bisa ngobrol sama AI dulu, nyusun solusi terbaik, baru merge kalau semuanya udah aman.

Buat dia, AI bukan cuma alat bantu nulis kode, tapi juga partner buat review dan validasi. Jadi proses coding berubah dari kerja manual yang berat jadi diskusi bolak-balik antara manusia dan mesin.

## Yang Lagi Berubah Itu Bukan Cuma Tool, Tapi Cara Pikir

Pendekatan Steinberger nunjukin satu hal penting: dunia software lagi geser.

Dulu, programmer dianggap hebat kalau bisa nguasain detail implementasi dan baca semua kode dengan teliti. Sekarang, nilai utama makin bergeser ke kemampuan Lo buat:

- jelasin masalah dengan jelas
- nentuin niat produk
- nyusun arsitektur yang bener
- pakai AI buat ngerjain bagian yang repetitif

Artinya, *programming* nggak lagi cuma soal ngetik kode. Lebih dari itu, ini soal ngarahin sistem supaya hasil akhirnya sesuai tujuan.

Gw pribadi lihat ini bukan sebagai tanda kalau developer jadi nggak penting. Justru kebalikannya: developer yang ngerti konteks, tujuan, dan desain sistem bakal makin berharga. Soalnya AI bisa nulis banyak hal, tapi tetap butuh manusia yang tahu mau dibawa ke mana.

## Penutup

Jadi, alasan OpenClaw creator nggak lagi baca kode baris per baris itu bukan karena dia males ngurus detail. Lebih tepatnya, dia sadar kalau detail yang repetitif bisa di-handle AI, sementara manusia harus fokus ke hal yang lebih penting: niat, arah, dan kualitas keputusan.

Kalau Lo tanya gw, ini memang keliatan kayak masa depan kerja software. Bukan berarti kode jadi nggak penting, tapi cara kita berinteraksi sama kode udah berubah. Sekarang yang paling penting bukan cuma bisa nulis, tapi juga bisa ngarahin.

