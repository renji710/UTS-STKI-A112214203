# Mesin Pencari STKI dengan Model Boolean dan VSM

Proyek ini adalah implementasi dari sebuah mesin pencari mini sebagai bagian dari Ujian Tengah Semester (UTS) mata kuliah Sistem Temu Kembali Informasi (STKI). Aplikasi ini dibangun menggunakan Python dan Streamlit, serta mengimplementasikan dua model pencarian fundamental: **Model Boolean** untuk pencarian eksak dan **Vector Space Model (VSM)** untuk pencarian berbasis relevansi.

Korpus data yang digunakan adalah kumpulan 10 artikel Wikipedia berbahasa Indonesia dengan tema "Hewan Langka di Indonesia".

---

###  Fitur Utama

-   **Pencarian Berbasis Relevansi:** Menggunakan Vector Space Model (VSM) dengan pembobotan TF-IDF dan perankingan Cosine Similarity untuk menemukan dokumen yang paling relevan.
-   **Pencarian Berbasis Logika Eksak:** Menggunakan Model Boolean yang mendukung operator `AND`, `OR`, dan `NOT` untuk hasil yang presisi.
-   **Antarmuka Web Interaktif:** Dibangun dengan Streamlit untuk pengalaman pengguna yang modern dan mudah digunakan.
-   **Pemilihan Model Dinamis:** Pengguna dapat dengan mudah beralih antara model VSM dan Boolean langsung dari antarmuka.
-   **Tampilan Hasil Informatif:** Setiap hasil pencarian dilengkapi dengan snippet dan opsi "Baca Selengkapnya..." untuk melihat seluruh isi dokumen.

---

###  Teknologi yang Digunakan

-   **Bahasa:** Python 3
-   **Framework Aplikasi:** Streamlit
-   **Pemrosesan Teks (NLP):** NLTK, Sastrawi
-   **Komputasi & Data:** NumPy, Pandas

---

###  Cara Menjalankan Secara Lokal

Untuk menjalankan aplikasi ini di komputer Anda, ikuti langkah-langkah berikut:

1.  **Clone Repositori**
    ```bash
    git clone https://github.com/renji710/UTS-STKI-A112214203.git
    cd UTS-STKI-A112214203
    ```

2.  **Instal Dependensi**
    Pastikan Anda sudah menginstal semua library yang dibutuhkan dengan menjalankan perintah berikut:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Aplikasi Streamlit**
    Setelah instalasi selesai, jalankan aplikasi dengan perintah:
    ```bash
    streamlit run app/main.py
    ```
    Aplikasi akan terbuka secara otomatis di browser Anda.

---

###  Tautan Deployment

Aplikasi ini telah di-deploy menggunakan Streamlit Community Cloud dan dapat diakses secara publik melalui tautan berikut:

**[➡️ Buka Aplikasi Mesin Pencari](https://hewanlangkaindo.streamlit.app/)**

---
