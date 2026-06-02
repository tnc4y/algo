def metni_utf8_bayta_cevir(metin):
    # String bir ifadeyi UTF-8 formatında bayt dizisine dönüştürür
    return metin.encode('utf-8')

def utf8_bayti_metne_cevir(bayt_dizisi):
    # Bayt dizisini tekrar okunabilir string metne dönüştürür
    return bayt_dizisi.decode('utf-8')

# Örnek Kullanım:
acik_metin = "Şifreleme Bilimi"
baytlar = metni_utf8_bayta_cevir(acik_metin)
orjinal_metin = utf8_bayti_metne_cevir(baytlar)

print("=== UTF-8 Dönüşümleri ===")
print("Orijinal Metin:", acik_metin)
print("Metnin Bayt Karşılığı:", list(baytlar))
print("Bayttan Çevrilen Metin:", orjinal_metin)