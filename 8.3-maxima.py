def maxima_search(noktalar):
    if not noktalar:
        return []
        
    # Noktaları x koordinatına göre küçükten büyüğe sıralıyoruz
    noktalar.sort(key=lambda p: p[0])
    
    maxima_noktalar = []
    # En sağdaki nokta (en büyük x'e sahip olan) her zaman bir maxima noktasıdır
    mevcut_max_y = float('-inf')
    
    # Sağdan sola doğru (tersten) tarama yapıyoruz
    for i in range(len(noktalar) - 1, -1, -1):
        x, y = noktalar[i]
        # Eğer bu noktanın y değeri, şimdiye kadar gördüğümüz en büyük y değerinden büyükse
        if y > mevcut_max_y:
            maxima_noktalar.append((x, y))
            mevcut_max_y = y
            
    # Sonucu tekrar soldan sağa sıralı hale getirmek için ters çeviriyoruz
    maxima_noktalar.reverse()
    return maxima_noktalar

# Örnek Kullanım:
tüm_noktalar = [(2, 4), (4, 10), (7, 9), (13, 8), (6, 5), (10, 3), (12, 1), (3, 1)]
en_büyük_noktalar = maxima_search(tüm_noktalar)
print("Maxima (Domine Edilemeyen) Noktalar:", en_büyük_noktalar)