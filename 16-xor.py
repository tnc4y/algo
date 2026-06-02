def xor_sifrele_coz(metin_veya_sifre, anahtar):
    # Eğer girdi string ise önce UTF-8 baytlarına çeviriyoruz
    if isinstance(metin_veya_sifre, str):
        girdi_baytları = metin_veya_sifre.encode('utf-8')
    else:
        girdi_baytları = metin_veya_sifre

    anahtar_baytları = anahtar.encode('utf-8')
    sonuc_baytlari = bytearray()

    # Her bir baytı anahtarın ilgili baytı ile XOR işlemine sokuyoruz
    for i in range(len(girdi_baytları)):
        secilen_anahtar_bayti = anahtar_baytları[i % len(anahtar_baytları)]
        xor_sonucu = girdi_baytları[i] ^ secilen_anahtar_bayti
        sonuc_baytlari.append(xor_sonucu)

    return bytes(sonuc_baytlari)

# Örnek Kullanım:
mesaj = "GizliMesaj"
gizli_anahtar = "Kripto123"

# Şifreleme (Çıktı okunamaz baytlar olacağı için liste olarak yazdırıyoruz)
sifreli_baytlar = xor_sifrele_coz(mesaj, gizli_anahtar)
# Deşifreleme (Aynı fonksiyon ve aynı anahtar kullanılır)
cozulen_baytlar = xor_sifrele_coz(sifreli_baytlar, gizli_anahtar)
cozulen_metin = cozulen_baytlar.decode('utf-8')

print("\n=== XOR Şifreleme ===")
print("Şifrelenmiş Bayt Dizisi:", list(sifreli_baytlar))
print("Deşifre Edilen Metin:", cozulen_metin)