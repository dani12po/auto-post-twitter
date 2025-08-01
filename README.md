# auto-post-twitter
Tentu, ini adalah draf lengkap untuk file `README.md` proyek `auto-post-twitter` kamu. Kamu bisa menyalin dan menempelkan ini langsung ke file `README.md` di *repository* GitHub-mu.

-----

### `README.md`

# Auto-Post Twitter (X) Bot

Sebuah bot Python sederhana untuk memposting tweet secara otomatis dan berurutan dari daftar yang sudah ditentukan, lengkap dengan gambar yang menyertai. Bot ini cocok untuk mengelola konten yang sudah dijadwalkan tanpa intervensi manual.

## ✨ Fitur Utama

  - **Posting Terjadwal**: Otomatis memposting tweet pada interval waktu yang ditentukan menggunakan pustaka `schedule`.
  - **Urutan Posting**: Memposting konten secara berurutan sesuai dengan nomor baris di file `list.txt`.
  - **Media Pendukung**: Mengunggah dan menyertakan gambar dari folder lokal di setiap tweet.
  - **Pengamanan API**: Menggunakan file `.env` untuk menyimpan kunci API secara aman, menjaganya dari kebocoran saat diunggah ke GitHub.
  - **Sistem Log**: Menampilkan log konsol yang jelas untuk melacak status postingan yang berhasil atau gagal.

-----

## 🚀 Persyaratan

Pastikan kamu sudah menginstal perangkat lunak berikut di komputermu:

  - **Python 3.6+**
  - **Git** (opsional, untuk mengelola proyek dengan Git)

-----

## 🛠️ Instalasi

Ikuti langkah-langkah di bawah ini untuk menyiapkan bot di perangkatmu.

#### 1\. Klon Repositori

Jika kamu menggunakan Git, klon repositori ini ke komputer kamu:

```bash
git clone https://github.com/dani12po/auto-post-twitter
```

#### 2\. Instal Ketergantungan

Instal semua pustaka Python yang dibutuhkan dari file `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### 3\. Konfigurasi API

1.  Daftar untuk mendapatkan akses **Developer Account** di [developer.x.com](https://developer.x.com).

2.  Buat aplikasi baru dengan izin **"Read and Write"**.

3.  Salin **Consumer Key**, **Consumer Secret**, **Access Token**, dan **Access Token Secret** kamu.

4.  Buat file baru bernama **`.env`** di direktori utama proyek.

5.  Tempelkan kunci API kamu ke dalam file `.env` dengan format berikut:

    ```env
    CONSUMER_KEY="masukkan_consumer_key_kamu"
    CONSUMER_SECRET="masukkan_consumer_secret_kamu"
    ACCESS_TOKEN="masukkan_access_token_kamu"
    ACCESS_TOKEN_SECRET="masukkan_access_token_secret_kamu"
    ```

> **⚠️ Peringatan:** Jangan pernah membagikan file `.env` kamu atau mengunggahnya ke GitHub. File `.gitignore` akan otomatis mengabaikannya.

-----

## ⚙️ Penggunaan Bot

#### 1\. Siapkan Konten Postingan

  * Buat folder bernama **`images/`** dan letakkan semua file gambar kamu di sana.

  * Buat file **`list.txt`** dan isi dengan *tweet* dan nama file gambar yang sesuai. Gunakan format `[ISI TWEET] | [NAMA FILE GAMBAR]`.

    **Contoh `list.txt`:**

    ```
    Selamat pagi! Ini adalah post pertama dari bot saya. | gambar1.jpg
    Kutipan inspiratif hari ini: "Jangan pernah menyerah." | gambar2.png
    ```

  * Buat file **`post_counter.txt`** dan isi dengan angka `0`. Ini akan menentukan bot untuk memulai dari postingan pertama.

#### 2\. Jalankan Bot

Jalankan skrip Python dari terminal:

```bash
python bot.py
```

Bot akan mulai berjalan di *background* dan memposting sesuai jadwal yang sudah ditentukan di dalam skrip (`schedule.every(1).minutes.do(...)`).

#### 3\. Mengubah Jadwal Posting

Jika kamu ingin mengubah interval posting (misalnya, menjadi setiap 1 jam atau setiap hari), buka file `bot.py` dan ubah baris di bagian **Penjadwalan Bot**:

```python
# Ubah baris ini sesuai kebutuhan
schedule.every(1).minutes.do(post_next_tweet_with_image)

# Contoh lain:
# schedule.every().hour.do(post_next_tweet_with_image) # setiap jam
# schedule.every().day.at("09:00").do(post_next_tweet_with_image) # setiap hari jam 9 pagi
```

-----

## 📂 Struktur File Proyek

```
.
├── .env                  # File untuk kunci API (jangan di-commit)
├── .gitignore            # File untuk mengabaikan file tertentu
├── bot.py                # Skrip utama bot
├── list.txt              # Daftar konten tweet dan gambar
├── post_counter.txt      # Pelacak nomor postingan
├── requirements.txt      # Daftar pustaka yang dibutuhkan
└── images/               # Folder untuk menyimpan file gambar
```
