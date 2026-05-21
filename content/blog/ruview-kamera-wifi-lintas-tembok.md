---
title: Edan, Cuma Modal Sinyal WiFi Bisa Jadi CCTV yang Mantau Lintas Tembok Pakai Teknologi Open Source
date: 2026-05-21
slug: ruview-kamera-wifi-lintas-tembok
description: RuView nunjukin gimana sinyal WiFi bisa dipakai buat mendeteksi gerakan manusia tanpa kamera, lengkap dengan sisi keren dan seramnya.
keywords: RuView, WiFi DensePose, WiFi CSI, ESP32-S3, open source, invisible sensing, teknologi privasi, AI, hardware
preview_image: https://wau.my.id/assets/blog/ruview-kamera-wifi.png
tags: Tech, AI, Open Source, Hardware, Opini
---

# Edan, Cuma Modal Sinyal WiFi Bisa Jadi CCTV yang Mantau Lintas Tembok Pakai Teknologi Open Source

![RuView, kamera dari sinyal WiFi](https://wau.my.id/assets/blog/ruview-kamera-wifi.png)

Gw baru aja nemu satu project open source yang bikin gw mikir, "Njirlah, kita cepet bener dah, teknologi udah bisa lihat tanpa kamera lagi." Namanya **RuView**.

Bayangin lo punya kemampuan buat nge-track gerakan orang di ruangan sebelah, tahu mereka lagi duduk atau berdiri, bahkan sampai tahu detak jantung mereka, tapi lo nggak pakai kamera sama sekali. Lo cuma pakai sinyal WiFi yang udah ada di rumah.

Nah, di titik itu RuView masuk. Project ini lagi rame banget di GitHub, dan buat gw yang suka ngulik CLI sama hardware, ini beneran *gokil sih*.

## Apa Itu RuView?

Intinya tuh **WiFi DensePose**. RuView pakai teknologi yang namanya *WiFi Channel State Information* atau CSI. Jadi, tiap kali sinyal WiFi nembus tembok atau mantul di badan kita, bentuk gelombangnya berubah. RuView ngambil data mentah itu, terus diolah pakai AI buat direkonstruksi jadi kerangka manusia 17 titik atau *skeleton*.

Semuanya jalan di hardware murah meriah kayak **ESP32-S3**, yang harganya sekitar 80-100 ribuan.

## Kenapa Ini Keren Banget? Menurut Gw

Ada tiga alasan kenapa RuView ini beda dari yang lain.

### 1. Privacy-First: No Cloud, No Camera

Buat lo yang parno sama privasi, ini solusinya. Nggak ada gambar yang dikirim ke cloud. Nggak ada lensa yang bisa di-hack. Semuanya cuma data angka dari sinyal radio yang diproses secara lokal.

Lo bisa pasang di kamar mandi atau kamar tidur buat deteksi jatuh, misalnya buat lansia, tanpa rasa nggak enak karena ada kamera yang berpotensi ngintip.

### 2. Power of Rust

Mesin utamanya dibangun pakai **Rust**. Kenapa? Karena processing sinyal WiFi itu butuh kecepatan tinggi banget. RuView diklaim bisa handle sampai 54.000 frames per detik. Bayangin efisiensinya. Bahkan model AI-nya dikompres pakai *4-bit quantization* sampai cuma berukuran 8 KB biar bisa lari kenceng di microcontroller sekecil ESP32.

### 3. Vibe Hacker-Zen

Documentation-nya punya vibe yang unik. Mereka punya ekosistem yang disebut "Cogs", modul-modul yang bisa di-hot swap sesuai kebutuhan. Ada modul buat *fall-detect*, *breathing-sync*, bahkan ada yang eksperimental kayak *ghost-hunter*. Seru banget buat dimainin pas weekend.

## Gimana Cara Mulainya?

Kalau lo punya ESP32-S3 nganggur, lo tinggal flash firmware-nya. Mereka udah support Docker dan punya plugin buat **Claude Code**, jadi lo bisa provisioning hardware langsung lewat CLI.

Buat gw, project kayak gini yang bikin dunia open source tetep menarik. Mereka nggak jualan janji AI yang abstrak, tapi ngasih alat konkret buat kita "ngeliat" dunia yang selama ini nggak kelihatan cuma modal perangkat kecil dan murah.

Menurut gw, ke depannya kita bakal makin sering nemu teknologi *invisible sensing* kayak gini. Nggak perlu lagi naruh sensor di mana-mana, cukup manfaatin "kabut" sinyal WiFi yang emang udah nyelimutin rumah kita.

Tapi satu hal yang menurut gw serem: artinya project kayak gini kalau dibikin skala besar bisa dipakai buat rekam dan mantau aktivitas serumah, se-RT, se-kecamatan, bahkan sekelurahan tanpa CCTV.

Dan itu bikin pertanyaannya jadi lebih serius: teknologi yang kelihatannya privacy-first di level personal, bisa berubah jadi alat pengawasan kalau dipakai tanpa batas dan tanpa aturan yang jelas.
