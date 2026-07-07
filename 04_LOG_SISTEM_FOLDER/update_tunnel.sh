#!/bin/bash

# 1. Ambil URL Cloudflare asli yang spesifik (bukan domain API)
URL="https://guarantees-evident-responding-optimize.trycloudflare.com"

echo "🔗 URL Tunnel Terkunci: $URL"

# 2. Update otomatis ke baruRAJA.html (bukan panggung_member.html)
TARGET_FILE="$HOME/nama_env_anda/Sambungan/baruRAJA.html"

if [ -f "$TARGET_FILE" ]; then
    sed -i "s|https://[^\"']*\.trycloudflare\.com|$URL|g" "$TARGET_FILE"
    echo "📝 baruRAJA.html berhasil disinkronkan ke URL baru!"
else
    echo "⚠️ File baruRAJA.html tidak ditemukan."
fi

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
