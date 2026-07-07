import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

LOG_FILE = "audit_sistem.log"

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "aktif", "pesan": "Sirkuit Audit Indramayu Club Siaga!"}), 200

@app.route('/api/audit', methods=['POST'])
def tambah_log():
    data = request.json
    aktivitas = data.get('aktivitas', 'Aktivitas Tidak Diketahui')
    akun = data.get('akun', 'Sistem')
    
    # Simpan log ke file lokal
    with open(LOG_FILE, "a") as f:
        f.write(f"[{akun}] - {aktivitas}\n")
        
    return jsonify({"status": "sukses", "pesan": "Log audit berhasil dikunci!"}), 200

if __name__ == '__main__':
    # Berjalan di port 8891 khusus jalur audit
    app.run(host='0.0.0.0', port=8891, debug=True)
