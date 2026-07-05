#!/bin/bash
# =================================================================
# NAMA SKRIP : Piramida Guard Generator
# DESKRIPSI  : Membuka kunci robot teks & mencetak stempel manifes
# DEVICE     : Vivo Y03t - Indramayu Club Digital
# =================================================================

# Warna Terminal
HIJAU='\033[0;32m'
CYAN='\033[0;36m'
KUNING='\033[1;33m'
MERAH='\033[0;31m'
NC='\033[0m' # No Color

clear

# 1. Cetak Visual Gerbang NUR (Sesuai 1000046807.jpg)
echo -e "${HIJAU}"
echo "      ___           ___     "
echo "     /__/\         /__/\    "
echo "     \  \:\        \  \:\   "
echo "      \  \:\        \  \:\  "
echo "  _____\__\:\   _____\__\:\ "
echo " /__/::::::::\ /__/::::::::\\"
echo " \  \:\~~\~~\/ \  \:\~~\~~\/"
echo "  \  \:\  ~~~   \  \:\  ~~~ "
echo "   \  \:\        \  \:\     "
echo "    \  \:\        \  \:\    "
echo "     \__\/         \__\/    "
echo " ───────────────────────────"
echo "  [✦] NUR - DIGITAL GUARDIAN"
echo " ───────────────────────────"
echo -e "${NC}"

# 2. Inisialisasi Berkas Log Teks yang Terkunci
LOG_DIR="04_LOG_SISTEM_FOLDER"
LOG_FILE="$LOG_DIR/log_bank.txt"

if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
    echo -e "${CYAN}[SYSTEM] Folder $LOG_DIR berhasil dibuat.${NC}"
fi

# 3. Proses Generator Stempel Piramida Guard
echo -e "${KUNING}[PROCESS] Membuka kunci robot teks..."
sleep 1
echo -e "[PROCESS] Menyuntikkan stempel Piramida Guard ke dalam manifes..."
sleep 1

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Menulis data manifes terkunci ke log_bank.txt
cat >> "$LOG_FILE" << EOL
==================================================
STEMPEL : Piramida Guard
WAKTU   : $TIMESTAMP
STATUS  : ROBOT TEXT AKTIF & TERKUNCI
--------------------------------------------------
Sistem Pengawas Admin Aktif. 8 Akun Admin Utama 
Indramayu Club telah terdaftar dan terorganisir 
di dalam pangkalan data pusat komando.
==================================================
EOL

# 4. Validasi Output Terminal
echo -e "\n${HIJAU}───────────────────────────────────────────"
echo -e " STATUS SINKRONISASI MANIFES"
echo -e "───────────────────────────────────────────${NC}"
echo -e " STAMP  : ${KUNING}Piramida Guard${NC}"
echo -e " TARGET : ${CYAN}$LOG_FILE${NC}"
echo -e " STATUS : ${HIJAU}BERHASIL DIKUNCI & GENERATE SEKARANG!${NC}"
echo -e "${HIJAU}───────────────────────────────────────────${NC}"

