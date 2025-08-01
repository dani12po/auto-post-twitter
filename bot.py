import tweepy
import schedule
import time
import os
from dotenv import load_dotenv

# --- 1. Konfigurasi Kunci dan Token API ---
# Muat variabel lingkungan dari file .env
load_dotenv()

# Ambil kunci dan token dari variabel lingkungan
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# --- 2. Inisiasi Klien API ---
try:
    # Inisiasi klien untuk API v1.1 (digunakan untuk upload media)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Inisiasi klien untuk API v2 (digunakan untuk posting tweet)
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    print("Inisiasi klien API v1.1 & v2 berhasil! Bot siap beroperasi.")
except Exception as e:
    print(f"ERROR: Gagal inisiasi klien. Pastikan kunci API sudah benar di file .env.")
    print(e)
    exit()

# --- 3. Fungsi untuk Mengelola Konten dan Urutan ---
def load_post_data_by_line(post_number):
    """Membaca data postingan berdasarkan nomor baris dari list.txt."""
    try:
        with open("list.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if post_number > 0 and post_number <= len(lines):
                line = lines[post_number - 1].strip()
                parts = line.split('|')
                if len(parts) == 2:
                    return {
                        'text': parts[0].strip(),
                        'image_file': parts[1].strip()
                    }
        return None
    except FileNotFoundError:
        print("ERROR: File list.txt tidak ditemukan.")
        return None

def load_post_counter():
    """Membaca nomor postingan terakhir dari post_counter.txt."""
    try:
        with open("post_counter.txt", 'r') as f:
            counter = int(f.read().strip())
        return counter
    except (FileNotFoundError, ValueError):
        print("Peringatan: File post_counter.txt tidak ditemukan atau formatnya salah. Memulai dari 0.")
        return 0

def save_post_counter(counter):
    """Menyimpan nomor postingan berikutnya ke post_counter.txt."""
    with open("post_counter.txt", 'w') as f:
        f.write(str(counter))

# --- 4. Fungsi Utama Bot untuk Posting ---
def post_next_tweet_with_image():
    """
    Mengambil data dari file berdasarkan urutan, mengunggah gambar, dan mempostingnya.
    """
    current_post_number = load_post_counter() + 1
    post_data = load_post_data_by_line(current_post_number)
    
    if not post_data:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Peringatan: Postingan ke-{current_post_number} tidak ditemukan di list.txt. Semua postingan sudah selesai.")
        return

    tweet_text = post_data['text']
    image_file = post_data['image_file']
    image_path = os.path.join("images", image_file)
    
    media_ids = []
    if os.path.exists(image_path):
        try:
            response_media = api.media_upload(image_path)
            media_ids.append(response_media.media_id)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Berhasil mengunggah media: {image_file}")
        except tweepy.TweepyException as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Terjadi kesalahan saat mengunggah media: {e}")
            
    try:
        response = client.create_tweet(text=tweet_text, media_ids=media_ids)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Berhasil memposting tweet ke-{current_post_number}: {tweet_text}")
        print(f"ID Tweet: {response.data['id']}")
        
        save_post_counter(current_post_number)
        
    except tweepy.TweepyException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Terjadi kesalahan saat memposting tweet: {e}")
        print("Postingan gagal. Nomor urutan tidak diubah.")
        
# --- 5. Penjadwalan Bot ---
schedule.every(1).minutes.do(post_next_tweet_with_image)

# --- 6. Jalankan Bot ---
print("Bot sedang berjalan. Menunggu jadwal posting pertama...")

while True:
    schedule.run_pending()
    time.sleep(1)