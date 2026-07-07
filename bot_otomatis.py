import os
import time

# Sirkuit Jalur Berkas yang akan diawasi otomatis
LOG_DIR = "./04_LOG_SISTEM_FOLDER"
AUDIT_LOG = os.path.join(LOG_DIR, "audit_flask.log")
BANK_LOG = os.path.join(LOG_DIR, "log_bank.txt")

def inisialisasi_sistem():
    print("⚡ [Sirkuit Piramida Guard] Mengaktifkan Bot Otomatis...")
    # Pastikan folder log ada
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        print(f"📁 Folder {LOG_DIR} tidak ditemukan, berhasil dibuat otomatis.")

def baca_aktivitas_terakhir(jalur_file):
    if os.path.exists(jalur_file):
        with open(jalur_file, "r") as f:
            baris = f.readlines()
            if baris:
                return baris[-1].strip() # Ambil baris terakhir log
    return "Belum ada aktivitas."

def sirkuit_keputusan(log_terakhir):
    # Logika otomatisasi berdasarkan isi log
    if "ERROR" in log_terakhir.upper():
        print(f"⚠️  [ALARM] Deteksi gangguan pada sistem: {log_terakhir}")
        print("🤖 Bot mengeksekusi tindakan pemulihan...")
        # Tempatkan perintah perbaikan otomatis di sini
    elif "TRANSAKSI" in log_terakhir.upper():
        print(f"💰 [KAS] Deteksi mutasi bank baru: {log_terakhir}")
        # Logika otomatis potong 5% atau verifikasi saldo
    else:
        print(f"🟢 [STATUS NORMAL]: {log_terakhir}")

def jalankan_bot():
    inisialisasi_sistem()
    
    while True:
        print("\n⏳ Bot sedang memindai sirkuit log...")
        
        # 1. Cek Log Flask
        log_flask = baca_aktivitas_terakhir(AUDIT_LOG)
        sirkuit_keputusan(log_flask)
        
        # 2. Cek Log Transaksi Bank
        log_bank = baca_aktivitas_terakhir(BANK_LOG)
        sirkuit_keputusan(log_bank)
        
        # Jeda waktu pemindaian otomatis (misal: tiap 10 detik)
        time.sleep(10)

if __name__ == "__main__":
    try:
        jalankan_bot()
    except KeyboardInterrupt:
        print("\n🛑 Bot otomatis dimatikan secara aman oleh pengguna.")

