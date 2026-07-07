# 👑 LOG KONTROL SISTEM - INDRAMAYU CLUB

Dokumen pelacak perubahan sirkuit, port, dan konfigurasi jaringan panggung digital.

---

## 📌 Status Terakhir Jaringan
*   **Tanggal Pembaruan**: 7 Juli 2026
*   **URL Tunnel Aktif**: `https://guarantees-evident-responding-optimize.trycloudflare.com`
*   **Repository GitHub**: `Sambungan` (main)

---

## 🔌 Pemetaan Port Aktif
*   **Port 8890**: Backend Python Baru (`~/👑raja/bot_makrifat.py`) -> **AKTIF**
*   **Port 8889**: Jalur Alwi Lama -> (Dihindari dari tabrakan sirkuit)
*   **Frontend**: `baruRAJA.html` -> Sudah sinkron ke URL Tunnel baru.

---

## 📜 Log Pembaruan Terakhir
*   Membuat backend Python baru di folder `👑raja`.
*   Menggeser konfigurasi port dari `8889` ke `8890` agar sirkuit aman dari bentrokan.
*   Mematikan terowongan lama dan meluncurkan Cloudflare Tunnel baru ke port `8890`.
*   Memperbarui target URL di `baruRAJA.html` menggunakan `sed` dan sukses di-push ke GitHub.


### [2026-07-07] - Inisialisasi Sirkuit Audit Otomatis
* **Lokasi**: `~/nama_env_anda/Sambungan/04_LOG_SISTEM_FOLDER`
* **Backend**: `server_audit.py` berjalan stabil di **Port 8891** (Menggunakan Python global Termux).
* **Jalur Terowongan**: Menggunakan SSH Remote Port Forwarding (`localhost.run`) untuk menghindari pemblokiran Signal 9 Android.
* **URL Publik Audit**: `https://cdd040179189c1.lhr.life`
* **Fungsi**: Siap menerima log audit, mutasi kas (potongan 5%), dan pelacakan riwayat aktivitas dari front-end.
