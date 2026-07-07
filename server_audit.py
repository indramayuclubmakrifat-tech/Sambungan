import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def muat_kontrol():
    # Membaca data langsung dari memori lokal Termux (Milidetik!)
    with open('kontrol_sultan.json', 'r') as f:
        return json.load(f)

@app.route('/api/akses', methods=['POST'])
def cek_akses():
    data_input = request.json
    kontrol = muat_kontrol()
    
    # ⚡ Sirkuit Utama Bypass Sultan Nur
    if (data_input.get('kode_meta') == kontrol['kode_meta'] and 
        kontrol['status_master'] == "LOCKED"):
        
        return jsonify({
            "akses": "GRANTED",
            "role": "Sultan Master",
            "log_terakhir": kontrol['last_user'],
            "status_tim": kontrol['akun_nur']
        }), 200

    return jsonify({"akses": "DENIED", "pesan": "Kode Meta Tidak Valid!"}), 403

