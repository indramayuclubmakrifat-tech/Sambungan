import time
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Mengizinkan akses silang domain agar bisa ditembak dari dashboard/HTML

@app.route('/api/audit', methods=['POST'])
def terima_audit():
    data = request.get_json(silent=True) or {}
    akun = data.get('akun', 'SYSTEM').strip().upper()
    aktivitas = data.get('aktivitas', 'Aktivitas tidak diketahui')
    
    # Ambil waktu lokal secara presisi
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Kunci rekam jejak ke dalam file audit_sistem.log
    try:
        with open("audit_sistem.log", "a") as f:
            f.write(f"[{waktu_sekarang}] [{akun}] {aktivitas}\n")
        return jsonify({"status": "sukses", "pesan": "Log audit berhasil dikunci"}), 200
    except Exception as e:
        return jsonify({"status": "error", "pesan": str(e)}), 500

if __name__ == '__main__':
    # Berjalan di port khusus pengawas audit
    app.run(host='0.0.0.0', port=8891)

