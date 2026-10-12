# RANCANGAN SAMPLING: METODE STRATIFIED RANDOM SAMPLING (STRA)
## TOPIK A: MENAKSIR RATA-RATA PENGELUARAN UNTUK TRANSPORTASI PER BULAN
**Mata Kuliah:** Praktik Teknik Sampling dan Survai (TSS)  
**Departemen:** Statistika, Fakultas Sains dan Analitika Data (FSAD), Institut Teknologi Sepuluh Nopember (ITS)  
**Sumber Data:** `Data kelas TSS A (Responses).xlsx` ($N = 43$ Mahasiswa)  

---

## DAFTAR ISI
1. [Struktur Tim & Pembagian Jobdesk per Slide (7 Anggota)](#1-struktur-tim--pembagian-jobdesk-per-slide)
2. [Ringkasan Parameter Data Prior (Hasil Ekstraksi Excel)](#2-ringkasan-parameter-data-prior)
3. [Penjabaran Slide Presentasi & Naskah Lisan (Slide 1 - 8)](#3-penjabaran-slide-presentasi--naskah-lisan)
   - [Slide 1: Judul dan Identitas Tim (Cover)](#slide-1-judul-dan-identitas-tim-cover)
   - [Slide 2: Latar Belakang & Identifikasi Masalah — PIC: Nina](#slide-2-latar-belakang--identifikasi-masalah--pic-nina)
   - [Slide 3: Komponen Rancangan Sampling — PIC: Rayya](#slide-3-komponen-rancangan-sampling--pic-rayya)
   - [Slide 4: Skema Stratifikasi & Parameter Prior — PIC: Felda](#slide-4-skema-stratifikasi--parameter-prior--pic-felda)
   - [Slide 5: Batas Kesalahan & Ukuran Sampel Total ($n$) — PIC: Brenanda](#slide-5-batas-kesalahan--ukuran-sampel-total-n--pic-brenanda)
   - [Slide 6: Alokasi Sampel ke Strata ($n_h$) & Prosedur Sampling — PIC: Azalea](#slide-6-alokasi-sampel-ke-strata-n_h--prosedur-sampling--pic-azalea)
   - [Slide 7: Formula Estimator, Presisi, & Efisiensi Desain — PIC: Zulfa](#slide-7-formula-estimator-presisi--efisiensi-desain--pic-zulfa)
   - [Slide 8: Refleksi Pembelajaran & Penutup — PIC: Najibah](#slide-8-refleksi-pembelajaran--penutup--pic-najibah)
4. [Panduan Manajemen Waktu Presentasi (Total 5 Menit)](#4-panduan-manajemen-waktu-presentasi)
5. [Antisipasi Tanya Jawab Dosen / Q&A Defense (Bobot 30%)](#5-antisipasi-tanya-jawab-dosen--qa-defense)
6. [Lampiran Sintaks R & Rumus Excel](#6-lampiran-sintaks-r--rumus-excel)

---

## 1. STRUKTUR TIM & PEMBAGIAN JOBDESK PER SLIDE

Sesuai ketentuan penugasan (maksimal 7 slide materi + 1 slide refleksi) dengan alokasi waktu presentasi **maksimal 5 menit**, tugas dibagi rata ke **7 anggota**: 1 anak bertanggung jawab penuh atas 1 slide (materi visual slide, naskah bicara lisan, dan penguasaan konsep saat Q&A).

| Slide | Topik / Konten Bahasan | Penanggung Jawab (PIC) | Peran Teknis & Substansi |
| :---: | :--- | :--- | :--- |
| **Slide 1** | **Cover & Identitas Tim** | *Bersama / Pembuka* | Menampilkan judul topik, nama kelas, dan daftar 7 anggota lengkap. |
| **Slide 2** | **Latar Belakang & Masalah** | **1. Nina** | Menjelaskan latar belakang riset, fenomena heterogenitas biaya transport, dan alasan digunakannya STRA. |
| **Slide 3** | **Komponen Sampling** | **2. Rayya** | Menguraikan elemen teknis: target population, sampled population, sampling frame, unit sampling/observasi, & variabel. |
| **Slide 4** | **Skema Stratifikasi & Prior** | **3. Felda** | Menjelaskan rasionalisasi pemilihan moda kendaraan sebagai strata dan menyajikan tabel parameter data prior ($N_h, W_h, \bar{Y}_h, S_h$). |
| **Slide 5** | **Ukuran Sampel ($n$)** | **4. Brenanda** | Menjelaskan penentuan $B$ dan $D$, penurunan rumus ukuran sampel STRA, hasil komputasi $n = 31$, serta perbandingan terhadap SRS. |
| **Slide 6** | **Alokasi Sampel ($n_h$)** | **5. Azalea** | Menyajikan tabel pembagian sampel ke 4 strata, argumentasi mengapa memilih Alokasi Proporsional vs Neyman, serta mekanisme pengundian acak. |
| **Slide 7** | **Estimator & Efisiensi** | **6. Zulfa** | Menguraikan rumus penaksir $\bar{y}_{st}$, varians penaksir $V(\bar{y}_{st})$, selang kepercayaan 95%, dan keunggulan efisiensi STRA. |
| **Slide 8** | **Refleksi & Kerja Sama Tim** | **7. Najibah** | Menyampaikan refleksi pembelajaran tim, strategi menghadapi kendala data riil, tabel peran anggota, serta menutup presentasi. |

---

## 2. RINGKASAN PARAMETER DATA PRIOR

Berdasarkan dataset `Data kelas TSS A (Responses).xlsx`, seluruh 43 responden telah dianalisis untuk variabel pengeluaran transportasi bulanan ($Y$):

### A. Parameter Populasi Kelas ($N = 43$)
- **Ukuran Populasi ($N$):** $43$ mahasiswa
- **Rata-rata Populasi ($\mu$):** $\text{Rp } 226.058,14$
- **Varians Populasi ($S^2$ / Sampel):** $104.630.788.205,98$
- **Standar Deviasi Populasi ($S$):** $\text{Rp } 323.466,83$
- **Pengeluaran Minimum:** $\text{Rp } 0$ (Jalan kaki / tanpa biaya bensin)
- **Pengeluaran Maksimum:** $\text{Rp } 1.550.000$ (Sepeda motor komuter non-kos)

### B. Karakteristik Data Prior Berdasarkan Moda Transportasi (4 Strata)
Variabel ini terbukti memisahkan pengeluaran secara paling kontras dan logis:

| Stratum ($h$) | Kategori Moda Kendaraan | Ukuran Stratum ($N_h$) | Bobot ($W_h$) | Rata-rata ($\bar{Y}_h$) | Simpangan Baku ($S_h$) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Sepeda Motor | 25 | 0,5814 (58,1%) | Rp 172.200,00 | Rp 296.019,00 |
| **2** | Kendaraan Umum / Ojol | 9 | 0,2093 (20,9%) | Rp 344.666,67 | Rp 146.734,45 |
| **3** | Jalan Kaki | 6 | 0,1395 (14,0%) | Rp 18.916,67 | Rp 28.161,00 |
| **4** | Mobil Pribadi | 3 | 0,0698 (7,0%) | Rp 733.333,33 | Rp 665.832,81 |
| **Total** | | **43** | **1,0000 (100%)** | **Rp 226.058,14** | — |

*Nilai Agregat untuk Formula Sampel:*
- $\sum_{h=1}^4 N_h S_h^2 = 3.719.218.500.000,00$
- $\sum_{h=1}^4 N_h S_h = 10.887.549,56$
- $\left(\sum_{h=1}^4 N_h S_h\right)^2 = 118.538.735.507.371,39$

---

## 3. PENJABARAN SLIDE PRESENTASI & NASKAH LISAN

---

### SLIDE 1: JUDUL DAN IDENTITAS TIM (COVER)
- **Tanggung Jawab:** Seluruh Tim / Dibuka oleh Pembicara Pertama (Nina)

#### Konten Visual Slide:
- **Logo Resmi:** Departemen Statistika FSAD ITS
- **Judul Utama:** DESAIN RANCANGAN SAMPLING "STRATIFIED RANDOM SAMPLING"
- **Topik Khusus:** Topik A — Menaksir Rata-rata Pengeluaran Transportasi Bulanan Mahasiswa Kelas TSS
- **Susunan Tim Peneliti (Kelompok X):**
  1. Nina
  2. Rayya
  3. Felda
  4. Brenanda Caesa Pamudya
  5. Azalea
  6. Indana Zulfa Nuraini
  7. Najibah Radhwa Aisyah
- **Dosen Pengampu:** Prof. Dr. Dra. Ismaini Zain, M.Si. / Tim Dosen Pengampu TSS

---

### SLIDE 2: LATAR BELAKANG & IDENTIFIKASI MASALAH — PIC: NINA
- **Penanggung Jawab:** **Nina**
- **Estimasi Durasi Bicara:** 40 Detik
- **Visual Pendukung (Grafik EDA 1):** `histogram_sebaran_populasi.png` (letakkan di sisi kanan slide)

#### Konten Visual Slide PPT:
- **Latar Belakang Studi:**
  - Transportasi merupakan kebutuhan pokok operasional perkuliahan harian mahasiswa ITS.
  - Sensus kelas Topik 1 bertindak sebagai **Prior Information**.
  - Penelitian ulang bulan depan dirancang berbasis **sampel** guna efisiensi waktu dan sumber daya.
- **Masalah Utama:**
  - Pengeluaran transportasi sangat bervariasi ($S = \text{Rp } 323.467$, rentang Rp 0 s.d. Rp 1.550.000).
  - Metode Simple Random Sampling (SRS) berisiko bias dan tidak efisien pada data yang heterogen.
- **Visualisasi Bukti Empiris (Grafik EDA):**
  - Menampilkan grafik histogram sebaran: distribusi data menjulur ke kanan (*right-skewed*) dengan disparitas ekstrem antara pejalan kaki (Rp 0) vs pemakai kendaraan/komuter (> Rp 1 juta).
- **Tujuan Sampling:**
  - Menaksir rata-rata pengeluaran transportasi bulanan ($\mu$) menggunakan metode **Stratified Random Sampling (STRA)** dengan toleransi galat $B = 25\% \times \text{mean}$ pada tingkat kepercayaan $95\%$.

#### Naskah Lisan Presentasi (Nina):
> *"Selamat pagi/siang Bapak/Ibu dosen dan rekan-rekan. Saya Nina, mewakili Kelompok [X]. Pada Slide 2 ini, kami mengangkat isu mobilitas mahasiswa di era modern. Seperti terlihat pada grafik histogram di sebelah kanan, sebaran biaya transportasi mahasiswa di kelas kita sangat heterogen dan menjulur ke kanan—mulai dari yang jalan kaki dengan biaya nol rupiah hingga yang berkomuter dengan biaya di atas satu juta rupiah.*  
> *Data kelas sebelumnya kita manfaatkan sebagai prior information. Mengingat keragaman yang sangat tinggi ini, metode Simple Random Sampling kurang efisien. Oleh sebab itu, kami merancang metode Stratified Random Sampling agar kelompok mahasiswa yang beragam ini dapat terwakili secara akurat dan presisi untuk mengestimasi rata-rata pengeluaran transportasi bulanan."*

---

### SLIDE 3: KOMPONEN RANCANGAN SAMPLING — PIC: RAYYA
- **Penanggung Jawab:** **Rayya**
- **Estimasi Durasi Bicara:** 35 Detik

#### Konten Visual Slide PPT:
Tabel Definisi Komponen Sampling:

| Komponen Sampling | Definisi dalam Rancangan |
| :--- | :--- |
| **Populasi Target** | Seluruh mahasiswa aktif kelas Teknik Sampling dan Survei A Departemen Statistika ITS. |
| **Populasi Terjangkau** | 43 mahasiswa kelas TSS A yang tercatat dan mengisi data kuesioner kelas. |
| **Kerangka Sampel (*Sampling Frame*)** | Daftar 43 nama mahasiswa bernomor urut $1, 2, \dots, 43$ dengan atribut kendaraan. |
| **Unit Sampling & Unit Observasi** | Mahasiswa secara individual. |
| **Variabel Utama ($Y$)** | Pengeluaran transportasi per bulan dalam Rupiah (skala kontinu). |
| **Variabel Stratifikasi ($X$)** | Moda kendaraan yang digunakan ke kampus (4 strata: Motor, Ojol, Jalan Kaki, Mobil). |

#### Naskah Lisan Presentasi (Rayya):
> *"Halo semuanya, saya Rayya. Pada Slide 3, saya akan menjelaskan komponen inti dari rancangan sampling kami. Populasi target sekaligus populasi terjangkau kami adalah seluruh 43 mahasiswa kelas TSS A yang telah terdata. Kerangka sampel yang kami gunakan adalah daftar nomor urut 1 sampai 43 lengkap dengan nama dan moda transportasinya. Unit sampling dan observasi adalah masing-masing individu mahasiswa.*  
> *Variabel utama yang diukur adalah biaya transportasi bulanan dalam satuan rupiah, dan kami menetapkan moda kendaraan menuju kampus sebagai variabel pembentuk strata."*

---

### SLIDE 4: SKEMA STRATIFIKASI & PARAMETER PRIOR — PIC: FELDA
- **Penanggung Jawab:** **Felda**
- **Estimasi Durasi Bicara:** 45 Detik
- **Visual Pendukung (Grafik EDA 2):** `boxplot_strata_transportasi.png` (sangat krusial disandingkan di samping tabel)

#### Konten Visual Slide PPT:
- **Kaidah Stratifikasi:**
  - *Within-stratum:* Sehomogen mungkin (keragaman di dalam kelompok kecil).
  - *Between-strata:* Seheterogen mungkin (perbedaan antar kelompok besar).
- **Tabel Karakteristik Data Prior per Stratum:**

| Stratum ($h$) | Kategori Moda | $N_h$ | Bobot ($W_h$) | Mean ($\bar{Y}_h$) | Simpangan Baku ($S_h$) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Sepeda Motor | 25 | 58,1% | Rp 172.200 | Rp 296.019 |
| **2** | Umum / Ojol | 9 | 20,9% | Rp 344.667 | Rp 146.734 |
| **3** | Jalan Kaki | 6 | 14,0% | Rp 18.917 | Rp 28.161 |
| **4** | Mobil Pribadi | 3 | 7,0% | Rp 733.333 | Rp 665.833 |
| **Total** | | **43** | **100%** | **Rp 226.058** | — |

- **Bukti Visual (Grafik Boxplot per Strata):**
  - Kotak *Jalan Kaki* rapat mendekati Rp 0; *Motor* terkonsentrasi di tengah; *Ojol* berada di 250-550 rb; *Mobil* di kuadran atas. Ini membuktikan secara visual varians antar-strata sangat besar dan varians intra-strata mengecil.

#### Naskah Lisan Presentasi (Felda):
> *"Saya Felda. Pada Slide 4, kami menyajikan rasionalisasi stratifikasi dan data prior. Mengapa kami memilih moda transportasi? Karena jenis kendaraan menentukan langsung konsumsi bensin atau ongkos harian ojek online.*  
> *Jika Bapak/Ibu dosen dan rekan-rekan memperhatikan grafik boxplot di sebelah tabel, prinsip emas STRA terpenuhi dengan sempurna: disparitas antar-stratum sangat tinggi (mean berkisar dari 18 ribu hingga 733 ribu rupiah), sementara keragaman di dalam stratum berhasil ditekan. Pemilahan 4 strata ini menjadi kunci efisiensi rancangan sampling kita."*

---

### SLIDE 5: BATAS KESALAHAN & UKURAN SAMPEL TOTAL ($n$) — PIC: BRENANDA
- **Penanggung Jawab:** **Brenanda Caesa Pamudya**
- **Estimasi Durasi Bicara:** 45 Detik

#### Konten Visual Slide PPT:
- **Parameter Batas Kesalahan (*Bound on Error*):**
  - $B = 25\% \times \mu = 0,25 \times 226.058,14 = \text{Rp } 56.514,53$
  - Tingkat kepercayaan 95% ($\alpha = 0,05 \implies z = 2$)
  - $D = \frac{B^2}{4} = \frac{(56.514,53)^2}{4} = 798.473.163,28$
- **Formula Ukuran Sampel STRA (Alokasi Proporsional):**
  $$n = \frac{N \sum_{h=1}^4 N_h S_h^2}{N^2 D + \sum_{h=1}^4 N_h S_h^2}$$
- **Substitusi Numerik:**
  $$n = \frac{43 \times 3.719.218.500.000}{43^2 (798.473.163) + 3.719.218.500.000} = 30,78 \approx \mathbf{31\text{ mahasiswa}}$$
- **Komparasi Efisiensi:**
  - $n_{SRS} = \frac{N S^2}{(N-1)D + S^2} = 32,38 \approx \mathbf{33\text{ mahasiswa}}$
  - STRA menghemat ukuran sampel sekaligus meningkatkan representasi kelompok.

#### Naskah Lisan Presentasi (Brenanda):
> *"Saya Brenanda. Di Slide 5, kita menghitung ukuran sampel total. Sesuai standar latihan praktikum, kami menetapkan Bound on Error sebesar 25% dari rata-rata populasi, yaitu Rp 56.515, sehingga diperoleh nilai D sebesar 798,47 juta rupiah.*  
> *Dengan memasukkan nilai varians masing-masing stratum ke dalam formula ukuran sampel STRA beralokasi proporsional, didapatkan ukuran sampel teoritis 30,78 yang dibulatkan ke atas menjadi 31 mahasiswa. Bila dibandingkan dengan SRS yang memerlukan 33 mahasiswa, STRA terbukti lebih efisien karena membutuhkan ukuran sampel yang lebih sedikit untuk mencapai tingkat presisi yang sama."*

---

### SLIDE 6: ALOKASI SAMPEL KE STRATA ($n_h$) & PROSEDUR SAMPLING — PIC: AZALEA
- **Penanggung Jawab:** **Azalea**
- **Estimasi Durasi Bicara:** 45 Detik
- **Visual Pendukung (Grafik EDA 3):** `bar_alokasi_populasi_sampel.png` (letakkan di sebelah tabel alokasi)

#### Konten Visual Slide PPT:
- **Tabel Alokasi Sampel Definitif ($n = 31$):**

| Stratum ($h$) | Kategori Moda | Populasi ($N_h$) | Proporsi ($W_h$) | Perhitungan ($n \cdot W_h$) | Sampel Terpilih ($n_h$) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Sepeda Motor | 25 | 0,5814 | 18,02 | **18** |
| **2** | Umum / Ojol | 9 | 0,2093 | 6,49 | **6** |
| **3** | Jalan Kaki | 6 | 0,1395 | 4,33 | **4** |
| **4** | Mobil Pribadi | 3 | 0,0698 | 2,16 | **3** |
| **Total** | | **43** | **1,0000** | **31,00** | **31** |

- **Bukti Visual (Grafik Bar Chart Komparasi):**
  - Diagram batang memperlihatkan secara jelas bahwa alokasi sampel hijau ($n_h$) merefleksikan komposisi populasi biru ($N_h$) secara proporsional sempurna tanpa mendistorsi bobot kelompok.
- **Catatan Pemilihan Alokasi Proporsional vs Neyman:**
  *Alokasi Neyman menghasilkan $n_{mobil} \approx 4,2 > N_4 = 3$ (melebihi populasi stratum). Oleh karena itu, Alokasi Proporsional dipilih karena realistis, seimbang, dan bebas risiko over-allocation.*
- **Prosedur Pengundian Lapangan:**
  - Tiap stratum diberi nomor urut terpisah $1 \dots N_h$.
  - Penarikan sampel acak dilakukan menggunakan *Simple Random Sampling without Replacement* (SRSWOR) via random number generator Excel `=RANDBETWEEN()` atau R `sample()`.

#### Naskah Lisan Presentasi (Azalea):
> *"Saya Azalea. Pada Slide 6, total 31 sampel tersebut kami alokasikan ke masing-masing stratum secara proporsional: 18 mahasiswa motor, 6 mahasiswa angkutan umum atau ojol, 4 pejalan kaki, dan 3 pengguna mobil. Diagram batang di samping tabel menggambarkan bagaimana sampel hijau kami secara presisi merefleksikan komposisi riil populasi kelas.*  
> *Kami memilih alokasi proporsional karena pada alokasi Neyman terjadi kondisi di mana sampel mobil melebihi total mahasiswa pengguna mobil di kelas. Untuk prosedur penarikannya, setiap stratum dibuatkan sub-daftar mandiri, lalu ditarik sampel acak sederhana tanpa pengembalian menggunakan generator bilangan acak."*

---

### SLIDE 7: FORMULA ESTIMATOR, PRESISI, & EFISIENSI DESAIN — PIC: ZULFA
- **Penanggung Jawab:** **Indana Zulfa Nuraini**
- **Estimasi Durasi Bicara:** 40 Detik

#### Konten Visual Slide PPT:
- **Estimator Rata-rata Berstrata ($\bar{y}_{st}$):**
  $$\bar{y}_{st} = \sum_{h=1}^4 W_h \bar{y}_h = \frac{1}{N} \sum_{h=1}^4 N_h \bar{y}_h$$
- **Estimator Varians Penaksir:**
  $$\widehat{V}(\bar{y}_{st}) = \sum_{h=1}^4 W_h^2 \left(\frac{N_h - n_h}{N_h}\right) \frac{s_h^2}{n_h}$$
- **Selang Kepercayaan 95% (*Confidence Interval*):**
  $$\bar{y}_{st} \pm 2 \sqrt{\widehat{V}(\bar{y}_{st})}$$
- **Evaluasi Relatif Efisiensi (*Design Effect / Deff*):**
  $$\text{RE} = \frac{V_{SRS}(\bar{y})}{V_{STRA}(\bar{y}_{st})} > 1$$
  Estimator STRA dijamin tak bias (*unbiased*) dan memiliki varians yang lebih minimum dibandingkan penaksir SRS murni.

#### Naskah Lisan Presentasi (Zulfa):
> *"Saya Zulfa. Pada Slide 7, setelah sampel survei diperoleh bulan depan, estimasi rata-rata pengeluaran dihitung menggunakan estimator tak bias $\bar{y}_{st}$ yang merupakan rata-rata terboboti per stratum. Varians penaksir dihitung dengan menyertakan faktor koreksi populasi berhingga.*  
> *Selang kepercayaan 95% dibentuk dengan batas kesalahan dua kali simpangan baku penaksir. Secara teoretis, varians penaksir pada STRA selalu lebih kecil atau sama dengan SRS karena variabilitas antar-strata berhasil dieliminasi dari galat estimasi, sehingga rancangan ini terbukti superior dan presisi."*

---

### SLIDE 8: REFLEKSI PEMBELAJARAN & PENUTUP — PIC: NAJIBAH
- **Penanggung Jawab:** **Najibah Radhwa Aisyah**
- **Estimasi Durasi Bicara:** 30 Detik

#### Konten Visual Slide PPT:
- **Refleksi Pembelajaran Tim:**
  - Mengintegrasikan teori sampling dengan kompleksitas data riil, terutama saat menghadapi varians ekstrem pada kelompok populasi kecil.
  - Memahami pentingnya kompromi metodologis (memilih Alokasi Proporsional demi menghindari *over-allocation*).
- **Tabel Kontribusi dan Peran Anggota Kelompok:**

| No | Anggota Tim | NRP | Peran Teknis dalam Penugasan |
| :---: | :--- | :---: | :--- |
| 1 | Nina | [NRP] | Analisis latar belakang, perumusan fenomena heterogenitas, dan presenter Slide 2. |
| 2 | Rayya | [NRP] | Identifikasi komponen kerangka sampling, unit analisis, dan presenter Slide 3. |
| 3 | Felda | [NRP] | Eksplorasi data prior, penghitungan parameter per stratum, dan presenter Slide 4. |
| 4 | Brenanda | [NRP] | Perumusan Bound on Error, formula matematis $n$, dan presenter Slide 5. |
| 5 | Azalea | [NRP] | Simulasi alokasi proporsional vs Neyman, prosedur SRS, dan presenter Slide 6. |
| 6 | Zulfa | [NRP] | Penurunan formula estimator $\bar{y}_{st}$, evaluasi efisiensi, dan presenter Slide 7. |
| 7 | Najibah | [NRP] | Sintesis refleksi tim, kompilasi slide akhir, penutup, dan presenter Slide 8. |

#### Naskah Lisan Presentasi (Najibah):
> *"Saya Najibah. Sebagai penutup pada Slide 8, pembelajaran utama yang kami peroleh adalah bahwa penerapan teori di lapangan menuntut kepekaan analitis terhadap karakteristik data, bukan sekadar memasukkan angka ke rumus. Seluruh tujuh anggota kelompok kami telah bekerja sama secara terintegrasi dengan pembagian tugas yang jelas sebagaimana tertera pada tabel.*  
> *Sekian pemaparan rancangan sampling dari Kelompok [X]. Terima kasih atas perhatian Bapak/Ibu dosen dan rekan-rekan, kami membuka sesi diskusi dan tanya jawab."*

---

## 4. PANDUAN MANAJEMEN WAKTU PRESENTASI

Total alokasi waktu dari dosen adalah **maksimal 5 menit (300 detik)**. Pembagian waktu 7 anggota telah disinkronkan:

| Urutan | Slide | Pemateri | Target Durasi | Kumulatif Waktu |
| :---: | :---: | :--- | :---: | :---: |
| 1 | Slide 1 & 2 | **Nina** (Cover & Latar Belakang) | 40 detik | 0:40 |
| 2 | Slide 3 | **Rayya** (Komponen Sampling) | 35 detik | 1:15 |
| 3 | Slide 4 | **Felda** (Skema Stratifikasi & Prior) | 45 detik | 2:00 |
| 4 | Slide 5 | **Brenanda** (Batas Kesalahan & Ukuran Sampel $n$) | 45 detik | 2:45 |
| 5 | Slide 6 | **Azalea** (Alokasi Sampel $n_h$ & Prosedur) | 45 detik | 3:30 |
| 6 | Slide 7 | **Zulfa** (Estimator & Efisiensi Desain) | 40 detik | 4:10 |
| 7 | Slide 8 | **Najibah** (Refleksi, Peran Tim, & Penutup) | 30 detik | **4:40** *(Aman di bawah 5 menit!)* |

---

## 5. ANTISIPASI TANYA JAWAB DOSEN / Q&A DEFENSE

Bobot penilaian **Kemampuan Menjawab dan Kerja Sama Tim adalah 30%**. Berikut adalah pembagian siapa yang menjawab sesuai keahlian slidenya:

#### Q1 (Untuk Felda / Rayya): *"Mengapa memilih moda transportasi sebagai strata, bukan status tempat tinggal (kos vs tidak kos)?"*
> **Jawaban (Felda/Rayya):**  
> *"Berdasarkan data prior, variabel moda transportasi berhubungan langsung secara mekanis terhadap pengeluaran bensin dan ongkos harian. Variabel ini memisahkan kelompok ekstrem secara sempurna: pejalan kaki terisolasi pada biaya rata-rata 18 ribu dengan varians sangat kecil, sedangkan pengguna mobil mencapai rata-rata 733 ribu. Jika menggunakan status kos vs tidak kos, kelompok 'tidak kos' masih sangat heterogen karena di dalamnya bercampur mahasiswa naik mobil, motor jarak dekat, dan motor komuter jarak jauh."*

#### Q2 (Untuk Brenanda / Azalea): *"Mengapa pada akhirnya memilih Alokasi Proporsional daripada Alokasi Neyman?"*
> **Jawaban (Brenanda/Azalea):**  
> *"Secara teori, Alokasi Neyman memang meminimumkan varians penaksir. Namun, pada dataset kelas kita, ukuran stratum mobil pribadi sangat kecil ($N_4 = 3$) dengan simpangan baku yang luar biasa besar ($S_4 = 665.833$). Jika rumus Neyman diterapkan murni, ia menuntut ukuran sampel $n_4 \approx 4,19$, yang melebihi total mahasiswa di stratum tersebut ($n_4 > N_4$). Oleh karena itu, Alokasi Proporsional adalah pilihan paling solid, realistis, dan mencerminkan proporsi riil populasi mahasiswa kelas."*

#### Q3 (Untuk Zulfa / Nina): *"Bagaimana membuktikan bahwa rancangan STRA ini lebih efisien daripada SRS?"*
> **Jawaban (Zulfa/Nina):**  
> *"Pertama, dari ukuran sampel dengan Bound of Error yang sama ($B = 25\% \times \text{mean}$), SRS memerlukan 33 sampel sedangkan STRA hanya butuh 31 sampel. Kedua, dari sisi varians penaksir, teorema pembagian varians menjamin bahwa variabilitas antar-strata ($Between-strata\ variance$) terisolasi dan tidak masuk ke dalam galat baku penaksir $\bar{y}_{st}$, sehingga standar error STRA pasti lebih kecil atau sama dengan SRS."*

---

## 6. LAMPIRAN SINTAKS R & RUMUS EXCEL

### Sintaks R:
```R
# Parameter Ringkasan Per Stratum
Nh <- c(25, 9, 6, 3)
Sh <- c(296019.00, 146734.45, 28161.00, 665832.81)
Ybar_h <- c(172200.00, 344666.67, 18916.67, 733333.33)

N <- sum(Nh)
Ybar_pop <- sum(Nh * Ybar_h) / N
B <- 0.25 * Ybar_pop
D <- (B^2) / 4

# Ukuran Sampel STRA Proporsional
num_prop <- N * sum(Nh * Sh^2)
denom_prop <- (N^2 * D) + sum(Nh * Sh^2)
n_prop <- num_prop / denom_prop
cat("Ukuran sampel proporsional:", ceiling(n_prop), "\n")

# Alokasi nh
nh_prop <- n_prop * (Nh / N)
hasil <- data.frame(Moda=c("Motor","Ojol","Jalan Kaki","Mobil"), Nh=Nh, Wh=Nh/N, nh_teoritis=nh_prop, nh_bulat=round(nh_prop))
print(hasil)
```

### Rumus Excel:
- **Rata-rata Stratum:** `=AVERAGE(K2:K26)`
- **Varians Sampel Stratum:** `=VAR.S(K2:K26)`
- **Bound on Error ($B$):** `=0.25 * C3` *(C3 adalah rata-rata populasi)*
- **Nilai $D$:** `=(B^2)/4`
- **Ukuran Sampel Proporsional:** `=(N * SUMPRODUCT(Nh, Sh^2)) / ((N^2 * D) + SUMPRODUCT(Nh, Sh^2))`
- **Alokasi Tiap Stratum:** `=$n$ * (Nh / N)`
