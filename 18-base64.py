import base64

def xor_sifrele_coz(metin_veya_sifre, anahtar):
    if isinstance(metin_veya_sifre, str):
        girdi_baytları = metin_veya_sifre.encode('utf-8')
    else:
        girdi_baytları = metin_veya_sifre

    anahtar_baytları = anahtar.encode('utf-8')
    sonuc_baytlari = bytearray()

    for i in range(len(girdi_baytları)):
        secilen_anahtar_bayti = anahtar_baytları[i % len(anahtar_baytları)]
        xor_sonucu = girdi_baytları[i] ^ secilen_anahtar_bayti
        sonuc_baytlari.append(xor_sonucu)

    return bytes(sonuc_baytlari)

def base64_kodla(bayt_verisi):
    kodlanmis_baytlar = base64.b64encode(bayt_verisi)
    return kodlanmis_baytlar.decode('utf-8')

def base64_coz(base64_metin):
    return base64.b64decode(base64_metin.encode('utf-8'))

# Örnek Kullanım:
mesaj = "GizliMesaj"
gizli_anahtar = "Kripto123"

sifreli_baytlar = xor_sifrele_coz(mesaj, gizli_anahtar)
okunabilir_sifreli_metin = base64_kodla(sifreli_baytlar)
orijinal_sifreli_baytlar = base64_coz(okunabilir_sifreli_metin)

print("\n=== Base64 Dönüşümleri ===")
print("XOR Şifreli Baytların Base64 Hali:", okunabilir_sifreli_metin)
print("Base64'ten Geri Alınan Baytlar:", list(orijinal_sifreli_baytlar))
