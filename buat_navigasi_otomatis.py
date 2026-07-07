import os
import re

def buat_sirkuit_navigasi():
    print("⚡ [Sirkuit Indramayu Club] Memulai pembuatan tombol navigasi otomatis...")
    
    # 1. Kumpulkan semua file HTML yang ada di folder ini secara berurutan
    semua_file = sorted([f for f in os.listdir('.') if f.endswith('.html')])
    
    # File pengecualian yang tidak perlu diberi tombol (misal halaman login/index)
    pengecualian = ['login.html', 'index.html']
    file_target = [f for f in semua_file if f not in pengecualian]
    
    total_file = len(file_target)
    print(f"📁 Ditemukan {total_file} file HTML target untuk dipasang tombol.")

    # 2. Loop untuk menyuntikkan tombol ke setiap file
    for i, file_sekarang in enumerate(file_target):
        # Tentukan file sebelum (Back) dan sesudah (Next)
        file_back = file_target[i - 1] if i > 0 else "index.html"
        file_next = file_target[i + 1] if i < total_file - 1 else "DASHBOARD.html"
        
        # Template Kode HTML Tombol Otomatis
        kode_tombol = f"""
<!-- SIRKUIT TOMBOL OTOMATIS BACK & NEXT -->
<div class="sirkuit-navigasi" style="text-align: center; margin: 30px 0; padding: 10px;">
    <button onclick="window.location.href='{file_back}'" style="padding: 10px 20px; font-weight: bold; background-color: #e74c3c; color: white; border: none; border-radius: 5px; cursor: pointer; margin-right: 10px;">
        ⬅️ BACK ({file_back})
    </button>
    <button onclick="window.location.href='{file_next}'" style="padding: 10px 20px; font-weight: bold; background-color: #2ecc71; color: white; border: none; border-radius: 5px; cursor: pointer;">
        NEXT ({file_next}) ➡️
    </button>
</div>
<!-- END SIRKUIT TOMBOL OTOMATIS -->
"""
        
        try:
            with open(file_sekarang, 'r', encoding='utf-8') as f:
                konten = f.read()
            
            # Hapus sirkuit tombol lama jika sebelumnya sudah pernah dibuat (agar tidak dobel)
            konten_bersih = re.sub(r'<!-- SIRKUIT TOMBOL OTOMATIS.*?END SIRKUIT TOMBOL OTOMATIS -->', '', konten, flags=re.DOTALL)
            
            # Suntikkan tombol tepat sebelum penutup tag </body> atau di paling bawah file
            if "</body>" in konten_bersih:
                konten_baru = konten_bersih.replace("</body>", f"{kode_tombol}\n</body>")
            else:
                konten_baru = konten_bersih + kode_tombol
                
            with open(file_sekarang, 'w', encoding='utf-8') as f:
                f.write(konten_baru)
                
            print(f"🟢 Sukses memasang tombol di: {file_sekarang} [ {file_back} <-> {file_next} ]")
            
        except Exception as e:
            print(f"❌ Gagal memproses {file_sekarang}: {e}")

if __name__ == "__main__":
    buat_sirkuit_navigasi()

