var APP_ROUTER = {
  DEFAULT_PAGE: 'NurRemote',
  ALLOWED_PAGES: [
    'akuntest2', 'ekonom3', 'emulatorgame9', 'komentar1', 'readme', 'readme2', 'NurRemote',
    'Nur1', 'Nur2', 'Nur3', 'Nur4', 'Nur5', 'Nur6', 'Nur7', 'Nur8', 'Nur9', 'Nur10',
    'Nur11', 'Nur12', 'Nur13', 'Nur14', 'Nur15', 'Nur16', 'Nur17', 'Nur18', 'Nur19'
  ]
};

/**
 * Mengatur jalannya routing halaman berdasarkan parameter URL (?page=NamaHalaman)
 */
function doGet(e) {
  var targetPage = APP_ROUTER.DEFAULT_PAGE;
  
  // Memeriksa apakah ada parameter halaman yang dikirim lewat URL
  if (e && e.parameter && e.parameter.page) {
    var requestedPage = e.parameter.page;
    // Jika halaman yang diminta terdaftar di ALLOWED_PAGES, ganti target halaman
    if (APP_ROUTER.ALLOWED_PAGES.indexOf(requestedPage) !== -1) { 
      targetPage = requestedPage; 
    }
  }
  
  try {
    // Merender halaman HTML menggunakan sistem template bawaan Google Apps Script
    return HtmlService.createTemplateFromFile(targetPage)
        .evaluate()
        .setTitle('✦ NUR - DIGITAL GUARDIAN ✦')
        .addMetaTag('viewport', 'width=device-width, initial-scale=1')
        .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
  } catch (err) {
    // Jika file HTML belum dibuat atau corrupt, tampilkan pesan error ini
    return HtmlService.createHtmlOutput().append('<h3>[Error PiramidaGuard] Gagal memuat komponen: ' + targetPage + '</h3>');
  }
}

/**
 * Fungsi pembantu untuk memanggil sub-file HTML atau CSS ke dalam template utama
 */
function include(filename) {
  try { 
    return HtmlService.createHtmlOutputFromFile(filename).getContent(); 
  } catch (err) { 
    return '<!-- Error include komponen: ' + filename + ' -->'; 
  }
}

