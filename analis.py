from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

# ID unik perangkat member Anda
ID_MEMBER = "M001" 

class IMCPanggung(App):
    def build(self):
        layout = BoxLayout()
        
        # Tentukan halaman berdasarkan ID Member
        halaman = 'admin.html' if ID_MEMBER == "M001" else 'member.html'
        
        if platform == 'android':
            # Menggunakan WebView Asli Android (Java) lewat Pyjnius
            from jnius import autoclass
            from android.runnable import run_on_ui_thread

            Activity = autoclass('org.kivy.android.PythonActivity').mActivity
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')

            @run_on_ui_thread
            def create_webview():
                webview = WebView(Activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.getSettings().setAllowFileAccess(True)
                webview.getSettings().setAllowContentAccess(True)
                webview.setWebViewClient(WebViewClient())
                
                # Membuka gerbang aset lokal Android yang didaftarkan buildozer
                webview.loadUrl(f'file:///android_asset/{halaman}')
                Activity.setContentView(webview)

            create_webview()
        else:
            # Jika diuji di PC/Termux biasa (Bukan Android)
            from kivy.uix.label import Label
            return Label(text=f"Mode PC: Membuka {halaman} (WebView aktif di Android)")

        return layout

if __name__ == '__main__':
    IMCPanggung().run()

