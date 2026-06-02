def sayi_yerlestir(sayilar, esitsizlikler):
    # Sayıları küçükten büyüğe sıralıyoruz (Ön sıralama yaklaşımı)
    sayilar.sort()
    sonuc = [0] * len(sayilar)
    
    # Küçükten büyüğe yerleştirmek için işaretçiler
    sol = 0
    sag = len(sayilar) - 1
    
    # Esitsizlik kalıplarını analiz ederek yerleştirme yapıyoruz
    # Her adımdaki ihtiyaca göre sıralı dizinin en küçük veya en büyük elemanını seçiyoruz
    for i in range(len(esitsizlikler)):
        if esitsizlikler[i] == '<':
            sonuc[i] = sayilar[sol]
            sol += 1
        else:
            sonuc[i] = sayilar[sag]
            sag -= 1
            
    # Son kalan elemanı boşta kalan yere koyuyoruz
    sonuc[-1] = sayilar[sol]
    return sonuc

# Örnek Kullanım:
sayilar_listesi = [4, 6, 3, 1, 8]
isaretler = ['<', '>', '<', '>']
yerlesim = sayi_yerlestir(sayilar_listesi, isaretler)

# Sonucu görselleştirme
yol_str = ""
for i in range(len(isaretler)):
    yol_str += f"{yerlesim[i]} {isaretler[i]} "
yol_str += str(yerlesim[-1])
print("Sayı Yerleştirme Sonucu:", yol_str)