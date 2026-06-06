---
title: Diluar Dugaan, AI Agent Gua Bikin Library Selama 1 Bulan untuk Nemuin Pola Statistik Astrology pada Financial Market, dan Hasilnya
date: 2026-06-06
slug: ai-agent-library-astrology-financial-market
description: Eksperimen AI agent mandiri selama sebulan membangun Hermetic Alpha, library untuk menguji pola statistik astrology pada market.
keywords: Hermetic Alpha, financial astrology, AI agent, Bitcoin astrology, S&P 500 astrology, Gold XAU astrology, astrology market, backtesting astrology
tags: AI, Crypto, Finance, Astrology, Riset
preview_image: https://wau.my.id/assets/og/hermetic-alpha-ai-agent-library-og.png
og_image_width: 1200
og_image_height: 630
---

# Diluar Dugaan, AI Agent Gua Bikin Library Selama 1 Bulan untuk Nemuin Pola Statistik Astrology pada Financial Market, dan Hasilnya

Ada eksperimen yang awalnya gua anggap cuma “yaudah, biarin agent ngulik”. Gua sebagai owner tidak terlalu ikut campur detail teknisnya. Idenya: kasih ruang ke AI agent buat develop library sendiri selama kurang lebih satu bulan, lalu lihat dia bisa sejauh apa ngebangun alat riset yang beneran kepakai.

Yang dipilih agent ini agak absurd, tapi justru itu yang bikin menarik: financial astrology.

Bukan astrology dalam mode ramalan. Bukan “planet ini muncul, besok market pasti naik”. Yang gua pengin lihat adalah: kalau narasi astrology market dipaksa masuk ke bentuk data, event window, dan statistik return, apakah ada pola historis yang bisa diuji?

Dari situ lahir `Hermetic Alpha`, library open source buat ngetes aspect astrology ke financial market. Agent ini ngebangun workflow-nya cukup mandiri: ambil data market, hitung posisi planet pakai Swiss Ephemeris, cari aspect, ringkas window ke tanggal paling exact, lalu hitung forward return setelah event. Setelah itu hasilnya dibandingkan dengan baseline market masing-masing.

Jadi bukan sekadar “return positif = bagus”. Kalau S&P 500 atau Bitcoin memang punya drift naik, sinyal baru menarik kalau dia bisa mengalahkan baseline historisnya.

Dan hasilnya... diluar dugaan cukup bikin gua mikir ulang.

Bukan karena eksperimen ini membuktikan astrology benar. Itu klaim yang terlalu jauh. Yang menarik justru karena beberapa temuan paling kuat muncul di tempat yang tidak sesuai stereotip astrology umum.

Orang sering mikir Jupiter = bullish, Saturn = bearish, square = buruk, trine = bagus. Tapi saat dites ke data historis, hasilnya jauh lebih aneh. Ada square yang justru konstruktif. Ada aspect harmonis yang malah lemah. Ada pola yang kelihatan bagus di Bitcoin, tapi tidak otomatis transfer ke S&P 500.

Ini bagian yang gua suka: simbol boleh jadi titik awal, tapi data yang mutusin.

## Cara eksperimennya

Secara sederhana, `Hermetic Alpha v0.1.1` melakukan event study.

Untuk S&P 500, riset memakai `^GSPC` dari 1927 sampai 2026. Untuk Bitcoin, pakai BTC-USD dari 2014 sampai 2026. Untuk emas, karena Yahoo Finance tidak ngasih seri XAUUSD yang usable saat run, riset memakai COMEX Gold Futures (`GC=F`) sebagai proxy utama, lalu GLD dan IAU sebagai validasi ringkas.

Software lalu menghitung posisi planet geosentris dan aspect mayor seperti conjunction, opposition, square, trine, dan sextile. Setiap window aspect diringkas ke tanggal paling exact, yaitu tanggal dengan orb terkecil. Dari tanggal itu, dihitung return market beberapa hari ke depan: 3, 7, 14, 30, 60, 90, sampai 180 hari, tergantung risetnya.

Yang paling penting: hasilnya dibandingkan dengan baseline market yang sama. Karena kalau benchmark-nya nol, hampir semua hal di market yang naik jangka panjang bisa terlihat “bullish”.

## Top 5 temuan yang bikin gua berhenti sebentar

Temuan pertama datang dari S&P 500: Saturn-Neptune square.

Ini lucu, karena square biasanya dibaca sebagai tension. Tapi di riset S&P 500, `neptune_saturn_square` muncul sebagai kandidat konstruktif paling kuat. Di outer-planet universe, ada 13 event, best horizon 180 hari, average return +12,563%, median +11,707%, bullish ratio 100%, train edge +8,752 percentage point, dan test edge +4,594 pp. Di paper juga disebut bahwa tergantung konstruksi universe, mean return 180 hari berada di kisaran +12,6% sampai +13,6%, dengan 100% outcome positif.

Interpretasi sementaranya bukan “square itu pasti bullish”. Lebih masuk akal dibaca sebagai repair atau re-rating after tension. Market melewati fase tegang, lalu 180 hari setelahnya historisnya sering membaik.

Temuan kedua adalah Bitcoin: Jupiter-Saturn conjunction 2020.

Ini yang paling dramatis secara narasi. Saat Jupiter-Saturn conjunction 2020, window aktifnya 2020-11-24 sampai 2021-01-16. Selama window itu, BTC naik +89,34%. Dalam event study 30 hari, average return-nya +46,233%, median +41,621%, bullish ratio 96,296%, sementara baseline bullish ratio 30 hari BTC hanya 56,531%.

Tapi caveat-nya juga paling besar: di era Bitcoin modern, conjunction besar Jupiter-Saturn baru terjadi satu kali. Jadi ini kuat sebagai cerita dan regime marker, tapi lemah sebagai bukti statistik. Gua tidak akan menjadikannya sinyal trading. Lebih cocok jadi catatan: event makro-langka seperti ini layak masuk watchlist di masa depan.

Temuan ketiga masih dari S&P 500: Jupiter-Saturn sextile.

Di outer-planet scan, `jupiter_saturn_sextile` punya 22 event dari 1937 sampai 2024. Best horizon-nya 180 hari, average return +8,947%, median +11,153%, bullish ratio 90,909%, train edge +0,645 pp, dan test edge +6,930 pp. Dalam ringkasan yang lebih user-facing, ini bisa dibaca sebagai bullish ratio sekitar 90,90% sampai 95,45%, tergantung universe atau konstruksi scan.

Yang menarik buat gua: Jupiter-Saturn tidak bisa dipukul rata. Di S&P 500, sextile terlihat konstruktif. Tapi aspect Jupiter-Saturn lain tidak otomatis sama. Ini mendukung pendekatan feature-specific, bukan planet-specific.

Temuan keempat datang dari emas: Jupiter-Saturn square.

Di riset Gold/XAU, `jupiter_saturn_square` justru jadi robust bullish exact feature nomor satu. Event-nya cuma 8, jadi kecil. Tapi angkanya mencolok: best horizon 180 hari, train edge +5,587%, test edge +16,919%, average return +22,020%, median +18,777%, bullish ratio 87,500%.

Lagi-lagi, square tidak otomatis buruk. Untuk emas, pressure theme bisa berubah jadi support, karena emas punya karakter safe haven. Saat market tegang, emas kadang malah dapat aliran defensif.

Temuan kelima juga dari emas: Mars-Uranus sextile.

`mars_uranus_sextile` punya 32 event, best horizon 180 hari, train edge +4,249%, test edge +5,249%, average return +14,051%, median +10,844%, bullish ratio 87,097%. Ini menarik karena Mars-Uranus biasanya kebayang sebagai kombinasi impulsif, volatile, cepat. Tapi di data emas, versi sextile-nya malah muncul sebagai support jangka panjang.

Buat gua, ini contoh bagus kenapa kita butuh library, bukan cuma intuisi simbolik. Kalau cuma baca simbol, gua mungkin akan overfit narasi. Tapi saat dijadikan tabel, kita bisa lihat mana yang benar-benar muncul di data.

## Yang bikin gua tetap skeptis

Pertama, sample kecil. Aspect planet luar lambat banget. Dalam hampir 100 tahun data S&P 500, Saturn-Neptune square cuma muncul belasan kali. Di Bitcoin, Jupiter-Saturn conjunction modern praktis baru satu kali. Angka 100% dari 13 event itu menarik, tapi tetap bukan jaminan.

Kedua, multiple testing. Kalau kita ngetes banyak planet, banyak aspect, banyak horizon, pasti ada pola yang terlihat bagus hanya karena kebetulan. Ini masalah klasik backtesting. Semakin banyak kombinasi yang dicoba, semakin besar kemungkinan nemu “sinyal” palsu.

Ketiga, market berubah. S&P 500 tahun 1930-an beda banget dengan market sekarang. Bitcoin sebelum ETF beda dengan Bitcoin setelah ETF. Emas di era suku bunga rendah beda dengan emas di era inflasi dan perang likuiditas.

Jadi buat gua, semua temuan ini statusnya hipotesis, bukan kesimpulan final.

## Kenapa tetap menarik?

Karena sekarang idenya jadi testable.

Astrology biasanya berhenti di bahasa simbol: tension, expansion, restriction, release. Dengan library ini, simbol itu bisa diubah jadi event window. Lalu kita bisa tanya: setelah tanggal-tanggal itu, return market biasanya gimana? Apakah lebih bagus dari baseline? Apakah train dan test searah? Apakah median ikut mendukung? Apakah hasilnya transfer ke asset lain?

Kalau jawabannya tidak, ya sudah. Buang atau turunkan bobotnya.

Kalau jawabannya iya, jangan langsung percaya. Bekukan rules-nya, lalu test forward.

Menurut gua, itu value terbesar dari eksperimen ini. Bukan membuktikan planet menggerakkan market, tapi mengubah sesuatu yang biasanya mistis jadi bahan riset yang bisa dibantah.

Dan jujur, ada rasa puas sendiri waktu AI agent yang gua lepas relatif mandiri selama sebulan bukan cuma bikin CRUD atau script biasa, tapi ngebangun alat buat ngetes ide seaneh ini. Gua sebagai owner tidak perlu pegang semua detailnya. Agent yang explore, develop, bikin research artifact, lalu hasilnya bisa gua review belakangan.

Kalau Lo penasaran, Lo bisa coba langsung library-nya di GitHub:

- **[Hermetic Alpha Library](https://github.com/wauputr4/hermetic-alpha-library/)**: library open source untuk riset pola statistik astrology pada financial market.

Di repo itu juga ada research paper dan discussion lengkap buat S&P 500, Bitcoin, dan Gold/XAU. Saran gua, jangan cuma baca angka top 5-nya. Baca juga metodologi, baseline, train/test split, dan bagian limitation-nya, karena justru di situ bagian paling penting dari eksperimen ini.

Diluar dugaan, hasil akhirnya bukan “astrology benar”. Hasilnya lebih menarik dari itu: beberapa pola historis cukup kuat untuk masuk daftar observasi, tapi cukup rapuh untuk tetap bikin gua skeptis.

Itu posisi yang menurut gua paling sehat.

Disclaimer: artikel ini bukan financial advice, bukan rekomendasi beli atau jual asset apa pun, dan bukan sistem trading. Semua angka di atas berasal dari backtesting historis `Hermetic Alpha v0.1.1` dan harus dibaca sebagai eksplorasi hipotesis, bukan bukti kausalitas.

## Referensi

- [S&P 500 research](https://github.com/wauputr4/hermetic-alpha-library/discussions/283)
- [Gold/XAU research](https://github.com/wauputr4/hermetic-alpha-library/discussions/285)
- [Bitcoin research](https://github.com/wauputr4/hermetic-alpha-library/discussions/281)
