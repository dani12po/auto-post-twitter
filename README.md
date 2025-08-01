# Auto-Post Twitter (X) Bot

Santai saja! Ini bot Python sederhana yang bisa bikin *tweet* otomatis, lengkap dengan gambarnya. Cocok banget buat kamu yang mau ngatur konten tapi nggak mau repot.

## ✨ Fitur-fitur Kerennya

* **Posting Otomatis**: Bot ini bisa *tweet* sendiri, sesuai jadwal yang kamu mau.

* **Jadwal Gampang Diatur**: Mau *tweet* setiap 5 menit? Atau setiap hari jam 9 pagi? Tinggal atur lewat terminal, gampang banget!

* **Posting Berurutan**: Kontennya dijamin rapi, berurutan dari atas ke bawah di `list.txt`.

* **Ada Gambarnya**: Tiap *tweet* bisa sekalian diunggah dengan gambar dari folder kamu. Keren, kan?

* **API Aman**: Kunci API kamu disimpan aman di file `.env`, jadi nggak bakal bocor di GitHub.

* **Laporannya Jelas**: Bot akan kasih tahu di terminal kalau postingannya berhasil atau gagal. Jadi kamu bisa pantau terus!

## 🚀 Persiapan

Sebelum mulai, pastikan kamu sudah punya:

* **Python 3.6+**

* **Git** (buat yang suka pakai Git, ya!)

## 🛠️ Cara Pakainya

Ikuti langkah-langkah ini, gampang kok!

#### 1. Ambil Proyeknya

Kalau kamu pakai Git, *clone* aja proyek ini ke komputermu:

```bash
git clone [https://github.com/dani12po/auto-post-twitter.git
```

#### 2. Pasang Dulu yang Dibutuhkan

Buka terminal, terus ketik perintah ini buat pasang semua yang diperlukan:

```bash
pip install -r requirements.txt
```

#### 3. Atur API-nya

1. Daftar dulu di [developer.x.com](https://developer.x.com) buat dapetin **Developer Account**.

2. Bikin aplikasi baru, jangan lupa kasih izin **"Read and Write"**.

3. Salin semua kunci yang ada (**Consumer Key**, **Consumer Secret**, dll).

4. Bikin file baru di folder proyek, namanya **`.env`**.

5. Tempel kunci-kunci tadi ke file `.env` dengan format ini:

```env
CONSUMER_KEY="masukkan_consumer_key_kamu"
CONSUMER_SECRET="masukkan_consumer_secret_kamu"
ACCESS_TOKEN="masukkan_access_token_kamu"
ACCESS_TOKEN_SECRET="masukkan_access_token_secret_kamu"
```

> **⚠️ Awas ya:** Jangan sekali-kali upload file `.env` ini ke GitHub! Tenang, `.gitignore` udah diatur kok buat ngelindunginnya.

## ⚙️ Cara Menjalankan Bot

#### 1. Siapkan Konten

* Bikin folder **`images/`** dan taruh semua gambarmu di sana.

* Bikin file **`list.txt`** dan tulis *tweet* kamu. Formatnya begini: `[ISI TWEET] | [NAMA FILE GAMBAR]`.

  **Contoh `list.txt`:**

  ```
  kamu ngentoddddddd | gambar1.jpg
  gratisan jan banyak komen!!!! | gambar2.png
  ```

* Bikin file **`post_counter.txt`** dan isi dengan angka `0`. Ini biar bot tahu harus mulai dari postingan pertama.

#### 2. Atur Jadwal & Jalanin!

Jalankan bot dari terminal. Nanti akan ada menu interaktif yang muncul:

```bash
python bot.py
```

Setelah perintah itu, kamu akan ditanya mau atur jadwal seperti apa:

```
--- Atur Jadwal Posting ---
Pilih mau posting setiap:
1: Menit
2: Jam
3: Hari
Masukkan pilihanmu (1/2/3): [pilih salah satu]
Masukkan angkanya (misal: 10 untuk setiap 10 menit): [masukkan angka]
```

Selesai deh! Bot akan langsung jalan di belakang layar sesuai jadwal yang kamu atur.

## 📂 Isi Folder Proyek

```
.
├── .env                  # Kunci API kamu
├── .gitignore            # File yang diabaikan Git
├── bot.py                # Kode utamanya
├── list.txt              # Daftar konten tweet dan gambar
├── post_counter.txt      # Buat nyimpen urutan postingan
├── requirements.txt      # Daftar yang perlu di-install
└── images/               # Folder buat nyimpen gambar
