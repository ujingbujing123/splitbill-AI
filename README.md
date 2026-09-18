

```
# 🧾 Smart Split Bill — Automated Receipt Parsing & Expense Splitting

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Google Gemini API](https://img.shields.io/badge/Google%20Gemini-Vision%20AI-8E44AD.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Smart Split Bill** adalah aplikasi *Proof of Concept* (PoC) berbasis web yang dirancang untuk menyederhanakan proses pembagian tagihan belanjaan (*split bill*). Dengan memanfaatkan model Vision AI multimodal (**Google Gemini**), aplikasi ini mampu membaca dan mengekstrak data dari nota/struk secara *OCR-free* tanpa mengandalkan pustaka OCR konvensional seperti Tesseract.

---

## 🚀 Fitur Unggulan

* **🤖 AI Receipt Extraction (OCR-Free):** Membaca foto struk belanja secara otomatis untuk mendeteksi detail item, jumlah (*quantity*), harga satuan, subtotal, pajak, *service charge*, dan total tagihan.
* **🎯 Structured Data Output:** Menggunakan **Pydantic Schema** untuk menjamin data hasil ekstraksi AI selalu konsisten dan terstruktur (JSON).
* **👥 Multi-Participant Item Split:** Pengguna dapat mendaftarkan nama partisipan dan menentukan siapa saja yang bertanggung jawab atas setiap item transaksi.
* **📊 Proportional Tax & Service Allocation:** Mengkalkulasi pajak dan *service fee* secara proporsional sesuai rasio belanjaan individu terhadap subtotal.
* **⚖️ Self-Balancing Validation:** Menjamin total pembayaran dari seluruh partisipan persis sama dengan grand total pada struk.

---

## 🎬 Demo Aplikasi



https://github.com/user-attachments/assets/7baf03a5-931c-4d60-ac26-7aebfc014b38



![Demo Smart Split Bill]

---

## 🏗️ Arsitektur & Teknologi

* **Frontend / UI:** [Streamlit](https://streamlit.io/) (Framework aplikasi web interaktif berbasis Python)
* **AI / Extraction Engine:** [Google Gemini API](https://ai.google.dev/) (`gemini-3.6-flash` dengan Structured Output)
* **Data Validation:** [Pydantic v2](https://docs.pydantic.dev/)
* **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)
* **Environment Management:** `python-dotenv`

---

## 📁 Struktur Direktori

```text
smart-split-bill/
├── .env.example            # Template variabel environment (API Key)
├── .gitignore              # Daftar file/folder yang dikecualikan dari Git
├── requirements.txt        # Dependensi pustaka Python
├── README.md               # Dokumentasi proyek
├── app.py                  # Entrypoint utama aplikasi Streamlit (UI/UX)
├── sample_data/            # Contoh foto struk belanja untuk pengujian
│   ├── bill_makanan_1.png
│   └── bill_makanan_2.png
├── testing/                # Script pengujian koneksi API & eksperimen
│   └── api_test.py
└── src/                    # Backend / Logic Engine
    ├── __init__.py         # Python package marker
    ├── extractor.py        # Modul ekstraksi nota dengan Gemini API & Pydantic
    └── calculator.py       # Modul perhitungan matematika & kalkulasi split bill

```

---

## 🛠️ Panduan Instalasi & Penggunaan Lokal

### 1. Prasyarat

* **Python 3.9+** terinstall di sistem.
* **Google Gemini API Key** (Dapatkan secara gratis di [Google AI Studio](https://aistudio.google.com/?utm_source=gemini)).

### 2. Kloning Repositori

```bash
git clone [https://github.com/USERNAME_KAMU/smart-split-bill.git](https://github.com/USERNAME_KAMU/smart-split-bill.git)
cd smart-split-bill

```

### 3. Buat & Aktifkan Virtual Environment

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate

```

### 4. Install Dependensi

```bash
pip install -r requirements.txt

```

### 5. Konfigurasi Environment Variable

Salin file `.env.example` menjadi `.env`, lalu masukkan API Key kamu:

```bash
cp .env.example .env

```

Isi `.env` dengan kredensial kamu:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.6-flash

```

### 6. Jalankan Aplikasi

```bash
python -m streamlit run app.py

```

Aplikasi akan terbuka otomatis di browser pada alamat `http://localhost:8501`.

---

## 🧪 Evaluasi & Analisis PoC

### 📈 Performa Model

* **Akurasi Ekstraksi:** Sangat tinggi pada struk yang jernih dengan pencahayaan cukup. Mampu memisahkan *itemized costs* dan *extra fees* tanpa kesalahan sintaksis berkat pendaftaran *response schema* via Pydantic.
* **Kecepatan Inference:** Rata-rata waktu pemrosesan berkisar antara 1.5 – 3.0 detik menggunakan model `gemini-3.6-flash` via cloud API.

### ⚠️ Limitasi Saat Ini

* Kualitas ekstraksi menurun apabila foto nota buram (*blurry*), terlipat parah, atau pencahayaan sangat redup.
* Saat server Google mengalami trafik tinggi (*Rate Limit / 503 Service Unavailable*), eksekusi memerlukan mekanisme *retry delay*.

### 💡 Rencana Pengembangan (Roadmap)

* [ ] Fitur *edit manual* jika terdapat kesalahan pembacaan harga/item dari AI sebelum melakukan perhitungan.
* [ ] Integrasi QRIS / Payment Gateway untuk pembuatan link pembayaran tagihan (*Shareable Payment Link*).
* [ ] Ekspor rincian tagihan ke format PDF / WhatsApp text message.

---

## 👨‍💻 Penulis

Dibuat oleh **Muhammad Fauzan Shabhysukri** sebagai bagian dari Proof of Concept produk **Smart Split Bill**.

```
