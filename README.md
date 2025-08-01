# auto-post-twitter
Auto-Post Twitter (X) Bot
Sebuah bot Python sederhana untuk memposting tweet secara otomatis dan berurutan dari daftar yang sudah ditentukan, lengkap dengan gambar yang menyertainya. Bot ini cocok untuk mengelola konten yang sudah dijadwalkan tanpa intervensi manual.

✨ Fitur Utama
Posting Terjadwal: Bot akan memposting tweet pada interval waktu yang ditentukan.

Pengaturan Jadwal Interaktif: Memungkinkan pengguna untuk mengatur interval posting (menit, jam, atau hari) melalui menu interaktif di terminal saat bot pertama kali dijalankan.

Urutan Posting: Memposting konten secara berurutan sesuai dengan nomor baris di file list.txt.

Media Pendukung: Mengunggah dan menyertakan gambar dari folder lokal di setiap tweet.

Pengamanan API: Menggunakan file .env untuk menyimpan kunci API secara aman, menjaganya dari kebocoran saat diunggah ke GitHub.

Sistem Log: Menampilkan log konsol yang jelas untuk melacak status postingan yang berhasil atau gagal.

🚀 Persyaratan
Pastikan kamu sudah menginstal perangkat lunak berikut di komputermu:

Python 3.6+

Git (opsional, untuk mengelola proyek dengan Git)

🛠️ Instalasi
Ikuti langkah-langkah di bawah ini untuk menyiapkan bot di perangkatmu.

1. Klon Repositori
Jika kamu menggunakan Git, klon repositori ini ke komputer kamu:

git clone https://github.com/dani12po/auto-post-twitter.git
cd auto-post-twitter

2. Instal Ketergantungan
Instal semua pustaka Python yang dibutuhkan dari file requirements.txt:

pip install -r requirements.txt

3. Konfigurasi API
Daftar untuk mendapatkan akses Developer Account di developer.x.com.

Buat aplikasi baru dengan izin "Read and Write".

Salin Consumer Key, Consumer Secret, Access Token, dan Access Token Secret kamu.

Buat file baru bernama .env di direktori utama proyek.

Tempelkan kunci API kamu ke dalam file .env dengan format berikut:

CONSUMER_KEY="masukkan_consumer_key_kamu"
CONSUMER_SECRET="masukkan_consumer_secret_kamu"
ACCESS_TOKEN="masukkan_access_token_kamu"
ACCESS_TOKEN_SECRET="masukkan_access_token_secret_kamu"

⚠️ Peringatan: Jangan pernah membagikan file .env kamu atau mengunggahnya ke GitHub. File .gitignore akan otomatis mengabaikannya.

⚙️ Penggunaan Bot
1. Siapkan Konten Postingan
Buat folder bernama images/ dan letakkan semua file gambar kamu di sana.

Buat file list.txt dan isi dengan tweet dan nama file gambar yang sesuai. Gunakan format [ISI TWEET] | [NAMA FILE GAMBAR].

Contoh list.txt:

Selamat pagi! Ini adalah post pertama dari bot saya. | gambar1.jpg
Kutipan inspiratif hari ini: "Jangan pernah menyerah." | gambar2.png

Buat file post_counter.txt dan isi dengan angka 0. Ini akan menentukan bot untuk memulai dari postingan pertama.

2. Jalankan dan Atur Jadwal Bot
Jalankan skrip Python dari terminal. Bot akan secara otomatis menampilkan menu interaktif:

python bot.py

Setelah menjalankan perintah di atas, kamu akan diminta untuk memilih interval dan frekuensi postingan:

--- Pengaturan Jadwal Posting ---
Pilih interval waktu posting:
1: Menit
2: Jam
3: Hari
Masukkan pilihan (1/2/3): [masukkan pilihanmu]
Masukkan angka frekuensi (misal: 10 untuk setiap 10 menit): [masukkan angka]

Bot akan mulai berjalan di background dan memposting sesuai jadwal yang telah kamu atur.

📂 Struktur File Proyek
.
├── .env                  # File untuk kunci API (jangan di-commit)
├── .gitignore            # File untuk mengabaikan file tertentu
├── bot.py                # Skrip utama bot
├── list.txt              # Daftar konten tweet dan gambar
├── post_counter.txt      # Pelacak nomor postingan
├── requirements.txt      # Daftar pustaka yang dibutuhkan
└── images/               # Folder untuk menyimpan file gambar
