#!/bin/bash

# 1. Ambil URL Cloudflare asli yang spesifik (bukan domain API)
URL="https://guarantees-evident-responding-optimize.trycloudflare.com"

echo "🔗 URL Tunnel Terkunci: $URL"
# Ganti bagian git di update_tunnel.sh dengan ini:
cd "$HOME/nama_env_anda/Sambungan"
git add . 
git commit -m "Auto-sync: Update tunnel & semua file sistem"
git push origin main


# 3. Sinkronisasi Git Otomatis ke GitHub
cd "$HOME/nama_env_anda/Sambungan"
git add baruRAJA.html 2>/dev/null
git commit -m "fix: auto sync tunnel to $URL" 2>/dev/null
git push origin main 2>/dev/null

if [ $? -eq 0 ]; then
    echo "🚀 Sukses push pembaruan sirkuit ke GitHub Repository!"
else
    echo "⚠️ Gagal melakukan git push, periksa koneksi."
fi

echo "✅ Proses sinkronisasi otomatis selesai!"
# ... (setelah bagian echo "📝 baruRAJA.html berhasil...")

# Coba Git Push, jika gagal, simpan ke log antrean
echo "🔗 Mencoba sinkronisasi ke GitHub..."

if git push origin main 2>/dev/null; then
    echo "🚀 Sukses push pembaruan sirkuit ke GitHub!"
else
    echo "⚠️ Sinyal drop! Perubahan disimpan lokal. Akan dikirim saat koneksi stabil."
    # Simpan URL ke file khusus agar tidak hilang
    echo "$URL" > "$HOME/nama_env_anda/Sambungan/url_pending.log"
fi

echo "✅ Proses skrip selesai (Status: $([ -f "$HOME/nama_env_anda/Sambungan/url_pending.log" ] && echo 'PENDING' || echo 'SYNCED'))!"

