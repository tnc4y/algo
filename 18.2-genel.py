import base64

def xor_isleme_sok(girdi, anahtar):
    """
    Girdiyi UTF-8 baytlarına çevirir ve anahtar baytları ile XOR işlemine sokar.
    XOR simetrik olduğu için aynı fonksiyon hem şifreler hem de çözer.
    """
    # Girdi düz metin (string) ise UTF-8 standartlarına göre bayt dizisine çeviriyoruz
    if isinstance(girdi, str):
        girdi_baytlari = girdi.encode('utf-8')
    else:
        girdi_baytlari = girdi

    # Anahtar kelimeyi de aynı şekilde UTF-8 bayt dizisine çeviriyoruz
    anahtar_baytlari = anahtar.encode('utf-8')
    sonuc_baytlari = bytearray()

    # Her bir baytı anahtarın ilgili baytı ile XOR (Özel Veya) işlemine sokuyoruz
    for i in range(len(girdi_baytlari)):
        secilen_anahtar_bayti = anahtar_baytlari[i % len(anahtar_baytlari)]
        sonuc_baytlari.append(girdi_baytlari[i] ^ secilen_anahtar_bayti)

    return bytes(sonuc_baytlari)


def base64_kodla(bayt_verisi):
    """
    XOR sonrası oluşan okunamaz ham baytları güvenli ASCII string'e çevirir.
    """
    kodlanmis_baytlar = base64.b64encode(bayt_verisi)
    return kodlanmis_baytlar.decode('ascii')


def base64_coz(base64_metni):
    """
    Base64 formatındaki metni tekrar orijinal ham şifreli bayt dizisine döndürür.
    """
    if isinstance(base64_metni, str):
        base64_metni = base64_metni.encode('ascii')
    return base64.b64decode(base64_metni)


# ==========================================
# ANA SİSTEM TESTİ VE ÇALIŞTIRMA BLOKLARI
# ==========================================
if __name__ == "__main__":
    # Sunumda işlenen kurallara uygun örnek veriler
    orijinal_mesaj = "Kriptoloji ve Algoritma Analizi Ders Notlari - 2026"
    sifre_anahtari = "XorGizliAnahtari!"

    print("--- 1. ADIM: Orijinal Metin ---")
    print(orijinal_mesaj)
    print()

    # ------------------------------------------
    # ŞİFRELEME PROSEDÜRÜ (Metin -> UTF-8 -> XOR -> Base64)
    # ------------------------------------------
    print("--- 2. ADIM: Şifreleme İşlemi ---")
    
    # Metin UTF-8'e çevrilir ve XOR ile karıştırılır
    ham_sifreli_baytlar = xor_isleme_sok(orijinal_mesaj, sifre_anahtari)
    
    # Bozuk/okunamaz ham baytlar Base64 ile temiz ASCII metne dönüştürülür
    b64_sifreli_metin = base64_kodla(ham_sifreli_baytlar)
    
    print("Üretilen Şifreli Base64 Metni (Ağda taşınmaya hazır):")
    print(b64_sifreli_metin)
    print()

    # ------------------------------------------
    # DEŞİFRELEME / ÇÖZME PROSEDÜRÜ (Base64 -> Ham Bayt -> XOR -> UTF-8)
    # ------------------------------------------
    print("--- 3. ADIM: Deşifreleme (Şifre Çözme) İşlemi ---")
    
    # Base64 metni çözülerek ham şifreli bayt dizisi geri alınır
    geri_alinan_baytlar = base64_coz(b64_sifreli_metin)
    
    # Ham baytlar aynı anahtar kelimeyle tekrar XOR işlemine sokulur (Şifre açılır)
    orijinal_utf8_baytlar = xor_isleme_sok(geri_alinan_baytlar, sifre_anahtari)
    
    # Elde edilen UTF-8 bayt dizisi tekrar okunabilir string metne decode edilir
    cozulen_orijinal_metin = orijinal_utf8_baytlar.decode('utf-8')
    
    print("Sistemden Başarıyla Geri Çözülen Orijinal Metin:")
    print(cozulen_orijinal_metin)