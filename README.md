# 🔐 Aplikasi Web Simulasi Kriptografi Klasik

> **TUGAS 1 KRIPTOGRAFI** · Semester 6 · Tahun Ajaran 2025/2026 Genap

---

## 📋 Deskripsi

Aplikasi web interaktif untuk mempelajari dan mensimulasikan **5 algoritma kriptografi klasik**. Dibangun dengan **Flask (Python)** dan mengusung tema premium **"Aurora Glass Cryptography Lab"** dengan tampilan glassmorphism, animasi aurora, dan desain responsif.

Setiap algoritma menampilkan:
- Proses enkripsi **dan** dekripsi
- **Step-by-step calculation** per karakter/blok
- **Rumus matematis** yang digunakan
- **Visualisasi matriks dan tabel** (Hill & Playfair)
- Riwayat operasi tersimpan dalam **session history**

---

## ✨ Fitur Utama

| Fitur | Keterangan |
|---|---|
| 5 Cipher Klasik | Caesar, Vigenere, Affine, Hill, Playfair |
| Enkripsi & Dekripsi | Untuk semua algoritma |
| Step-by-step | Detail kalkulasi per karakter / blok |
| Formula Matematis | Rumus ditampilkan dengan jelas |
| Matrix Visualization | Hill 2×2/3×3 + Invers modulo 26 |
| Playfair 5×5 Table | Grid interaktif dengan hover effect |
| History | 20 riwayat tersimpan di session |
| Dark/Light Mode | Tersimpan di localStorage |
| Copy Result | Clipboard API + fallback |
| Validasi Input | Error message ramah pengguna |
| Responsive UI | Mobile 360px – Desktop 4K |
| Aurora Glass Theme | Glassmorphism + animated gradient |

---

## 🔑 Algoritma yang Tersedia

### 1. Caesar Cipher
- **Enkripsi:** `C = (P + k) mod 26`
- **Dekripsi:** `P = (C - k) mod 26`
- Kunci: angka shift 1–25

### 2. Vigenere Cipher
- **Enkripsi:** `C_i = (P_i + K_i) mod 26`
- **Dekripsi:** `P_i = (C_i - K_i) mod 26`
- Kunci: kata kunci (keyword) huruf A–Z

### 3. Affine Cipher
- **Enkripsi:** `C = (a·P + b) mod 26`
- **Dekripsi:** `P = a⁻¹·(C - b) mod 26`
- Kunci: integer `a` (coprime dengan 26) dan `b`

### 4. Hill Cipher
- **Enkripsi:** `C = K × P (mod 26)`
- **Dekripsi:** `P = K⁻¹ × C (mod 26)`
- Kunci: matriks 2×2 atau 3×3 yang invertibel modulo 26

### 5. Playfair Cipher
- Grid 5×5 dari keyword (J = I)
- Aturan: same row, same column, rectangle
- Kunci: kata kunci (keyword) huruf

---

## 🛠 Teknologi

- **Backend:** Python 3, Flask, Werkzeug
- **Templating:** Jinja2
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **UI Framework:** Bootstrap 5 (CDN)
- **Icons:** Font Awesome 6 (CDN)
- **Fonts:** Google Fonts (Outfit, JetBrains Mono)
- **Deployment:** Gunicorn

---

## 📁 Struktur Folder

```
kriptografi/
├── app.py                    # Entry point Flask, routing utama aplikasi
├── requirements.txt          # Python dependencies (Flask, Werkzeug)
├── README.md                 # Dokumentasi proyek
├── .gitignore               # Git ignore configuration
│
├── crypto/                   # Modul algoritma kriptografi
│   ├── __init__.py
│   └── algorithms.py         # Implementasi 5 cipher: caesar, vigenere, affine, hill, playfair
│
├── templates/                # Template HTML Jinja2
│   ├── base.html            # Base template dengan navbar & theme toggle
│   ├── index.html           # Halaman awal (daftar cipher tersedia)
│   ├── cipher.html          # Form enkripsi/dekripsi & hasil
│   └── history.html         # Riwayat operasi tersimpan
│
└── static/                   # File aset statis
    ├── css/
    │   └── style.css         # Styling Aurora Glass theme
    └── js/
        └── main.js           # Dark/Light mode, copy result, validasi input
```

---

## 🚀 Cara Menjalankan Lokal

### 1. Buat Virtual Environment
```bash
python -m venv venv
```

### 2. Aktivasi Virtual Environment

**Windows:**
```cmd
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
python app.py
```

Atau menggunakan Flask CLI:
```bash
flask run
```

### 5. Buka di Browser
```
http://127.0.0.1:5000
```

Aplikasi akan membuka di halaman awal yang menampilkan daftar 5 algoritma cipher klasik.

---

## 🔧 Fitur-Fitur Utama

### Enkripsi & Dekripsi
Aplikasi mendukung proses enkripsi dan dekripsi untuk semua 5 algoritma cipher. Setiap algoritma memiliki form input tersendiri dengan validasi input yang ketat.

### Step-by-Step Calculation
Pengguna dapat melihat langkah demi langkah bagaimana karakter atau blok teks dienkripsi, termasuk rumus matematis yang digunakan.

### History Management
Setiap operasi enkripsi/dekripsi tersimpan dalam session history (maksimal 30 item). User dapat melihat riwayat lengkap dan menghapusnya kapan saja.

### Dark/Light Mode
Aplikasi mendukung tema gelap dan terang yang tersimpan di localStorage browser pengguna.

### Responsive Design
Desain UI responsif yang dapat diakses dari berbagai ukuran layar (mobile, tablet, desktop).

---

## 📝 Cara Menggunakan Aplikasi

1. **Buka Aplikasi** → Kunjungi `http://127.0.0.1:5000`
2. **Pilih Cipher** → Klik salah satu dari 5 algoritma cipher yang tersedia
3. **Input Data** → Masukkan teks yang ingin dienkripsi/dekripsi dan kunci sesuai algoritma
4. **Pilih Mode** → Pilih "Encrypt" untuk enkripsi atau "Decrypt" untuk dekripsi
5. **Lihat Hasil** → Hasil akan ditampilkan dengan step-by-step calculation dan formula
6. **Lihat History** → Buka menu History untuk melihat riwayat operasi
---

## 📖 Penjelasan Setiap Modul

### `app.py`
File utama aplikasi Flask yang menangani:
- Route ke halaman utama (`/`) - menampilkan daftar cipher
- Route untuk setiap cipher (`/cipher/<name>`) - form dan hasil enkripsi/dekripsi
- Route history (`/history`) - tampilan riwayat operasi
- Session management untuk menyimpan riwayat operasi (maksimal 30 item)
- Flash messages untuk notifikasi error atau success

### `crypto/algorithms.py`
Modul yang berisi implementasi lengkap 5 algoritma cipher:

- **`caesar(text, shift, mode)`** - Caesar cipher dengan shift 1-25
- **`vigenere(text, key, mode)`** - Vigenère cipher dengan keyword
- **`affine(text, a, b, mode)`** - Affine cipher dengan parameter a dan b
- **`hill(text, matrix, mode)`** - Hill cipher dengan matriks 2×2 atau 3×3
- **`playfair(text, key, mode)`** - Playfair cipher dengan grid 5×5

Setiap fungsi mengembalikan tuple:
- `result` - Hasil enkripsi/dekripsi
- `formula` - Rumus matematis yang digunakan
- `steps` - List langkah-langkah perhitungan detail
- `extra` - Data tambahan (visualisasi matriks, tabel Vigenere, invers, dll)

Fungsi helper:
- **`parse_matrix(s, n)`** - Parse string matriks menjadi list 2D
- **`inv_matrix_mod(m)`** - Hitung invers matriks modulo 26
- **`clean_letters(text)`** - Hapus karakter non-huruf dari teks

### `templates/base.html`
Template dasar HTML dengan:
- Navbar responsif dengan brand "🔐 KriptoClass"
- Theme toggle button untuk dark/light mode
- Container untuk flash messages
- Footer dengan informasi
- Link ke Bootstrap 5, Font Awesome, dan CSS/JS custom

### `templates/index.html`
Halaman awal aplikasi yang menampilkan:
- Daftar 5 algoritma cipher dalam card layout
- Deskripsi singkat setiap algoritma
- Link ke halaman masing-masing cipher

### `templates/cipher.html`
Halaman form dan hasil untuk setiap algoritma:
- Form input untuk teks dan kunci/parameter
- Dropdown untuk mode encrypt/decrypt
- Tombol submit
- Card hasil dengan:
  - Teks hasil (dengan copy to clipboard button)
  - Formula matematis
  - Step-by-step calculation
  - Visualisasi tambahan (matriks, tabel Vigenere, dll)

### `templates/history.html`
Halaman riwayat operasi:
- Tabel dengan kolom: Time, Cipher, Mode, Input, Output
- Tombol Clear History untuk menghapus semua riwayat
- Link kembali ke halaman utama

### `static/css/style.css`
Styling custom dengan:
- Aurora Glass theme (glassmorphism effect dengan semi-transparent background)
- Animated gradient background
- Dark/Light mode dengan CSS variables
- Responsive design (breakpoints untuk mobile, tablet, desktop)
- Custom styles untuk card, form, button, dan table
- Hover effects dan animasi

### `static/js/main.js`
Fungsi JavaScript untuk:
- Toggle dark/light mode dengan icon
- Simpan preferensi tema di localStorage
- Copy hasil enkripsi ke clipboard dengan fallback
- Validasi form input real-time
- Animasi dan UX enhancements

---

## ✅ Catatan Validasi Algoritma

| Algoritma | Aturan Kunci |
|---|---|
| **Caesar** | Shift: angka **1–25** |
| **Vigenere** | Keyword: **hanya huruf** A–Z |
| **Affine** | `a` harus **coprime dengan 26** · Valid: 1,3,5,7,9,11,15,17,19,21,23,25 |
| **Hill** | det(K) mod 26 **≠ 0** dan **coprime 26** · Matriks 2×2 atau 3×3 |
| **Playfair** | Keyword: **hanya huruf** A–Z · J digabung dengan I |

**Catatan umum:**
- Teks tidak boleh kosong
- Spasi dan tanda baca dipertahankan (kecuali Hill & Playfair yang hanya proses huruf)
- Hill & Playfair otomatis menambahkan padding `X` jika diperlukan

---

## 👤 Identitas Tugas

| | |
|---|---|
| **Mata Kuliah** | Kriptografi |
| **Tugas** | Tugas 1 |
| **Semester** | 6 |
| **Tahun Ajaran** | 2025/2026 Genap |
| **Pembuat** | Purnamasari Siregar |
