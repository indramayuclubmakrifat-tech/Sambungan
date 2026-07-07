# ═══════════════════════════════════════════════════════════
# TAMBAHKAN KODE INI KE bot_makrifat.py
# Letakkan SEBELUM baris app.run()
# ═══════════════════════════════════════════════════════════

import base64, time
from flask import Response

# Penyimpanan frame di memory (tiap member 1 frame terbaru)
FRAME_STORE  = {}   # { 'M001': bytes_jpeg, ... }
FRAME_TS     = {}   # { 'M001': timestamp, ... }

# ── Terima frame dari HP member ──
@app.route('/upload-frame', methods=['POST'])
def upload_frame():
    data      = request.get_json(silent=True) or {}
    member_id = data.get('id','').strip().upper()
    frame_b64 = data.get('frame','')
    if not member_id or not frame_b64:
        return jsonify({"status":"error","pesan":"Data tidak lengkap"}), 400
    try:
        FRAME_STORE[member_id] = base64.b64decode(frame_b64)
        FRAME_TS[member_id]    = time.time()
        return jsonify({"status":"ok","id":member_id})
    except Exception as e:
        return jsonify({"status":"error","pesan":str(e)}), 500

# ── Sajikan frame ke browser lain ──
@app.route('/frame/<member_id>')
def get_frame(member_id):
    mid = member_id.strip().upper()
    if mid not in FRAME_STORE:
        return Response(status=204)   # No Content — slot kosong
    # Hapus frame yang sudah stale > 10 detik (kamera mati)
    if time.time() - FRAME_TS.get(mid, 0) > 10:
        del FRAME_STORE[mid]
        return Response(status=204)
    return Response(
        FRAME_STORE[mid],
        mimetype='image/jpeg',
        headers={
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0',
            'Access-Control-Allow-Origin': '*'
        }
    )

# ── Status semua member yang sedang live ──
@app.route('/live-status')
def live_status():
    now    = time.time()
    aktif  = {mid: True for mid, ts in FRAME_TS.items() if now - ts < 10}
    return jsonify({"live": aktif, "total": len(aktif)})

# ═══════════════════════════════════════════════════════════
# SELESAI — JANGAN LUPA RESTART Flask setelah menambahkan ini
# cd ~/👑raja && kill $(pgrep -f bot_makrifat) && nohup python3 bot_makrifat.py > flask.log 2>&1 &
# ═══════════════════════════════════════════════════════════

