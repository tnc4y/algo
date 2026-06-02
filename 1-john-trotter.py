class JohnsonTrotter:
    def __init__(self, n):
        self.n = n
        # Elemanları 1'den n'e kadar oluşturuyoruz
        self.elements = list(range(1, n + 1))
        # Yönleri tutuyoruz: True = Sola (<--), False = Sağa (-->)
        # Başlangıçta tüm elemanlar sola doğru hareket eder
        self.directions = [True] * n

    def get_mobile_element_index(self):
        """
        Dizideki en büyük 'hareketli' (mobile) elemanın indisini bulur.
        Bir eleman, okunun gösterdiği yöndeki komşusundan daha büyükse hareketlidir.
        """
        max_mobile = -1
        mobile_idx = -1

        for i in range(self.n):
            # Sola doğru hareket kontrolü (<--)
            if self.directions[i] and i > 0:
                if self.elements[i] > self.elements[i - 1]:
                    if self.elements[i] > max_mobile:
                        max_mobile = self.elements[i]
                        mobile_idx = i
            # Sağa doğru hareket kontrolü (-->)
            elif not self.directions[i] and i < self.n - 1:
                if self.elements[i] > self.elements[i + 1]:
                    if self.elements[i] > max_mobile:
                        max_mobile = self.elements[i]
                        mobile_idx = i
        return mobile_idx

    def generate_all_permutations(self):
        """
        Tüm permütasyonları sırayla üreterek bir liste halinde döndürür.
        """
        permutations = [list(self.elements)]
        
        while True:
            # 1. En büyük hareketli elemanın indisini bul
            idx = self.get_mobile_element_index()
            
            # Eğer hareketli eleman kalmadıysa tüm permütasyonlar üretilmiştir
            if idx == -1:
                break
                
            mobile_val = self.elements[idx]
            
            # 2. Hareketli elemanı yönü doğrultusunda komşusuyla yer değiştir
            if self.directions[idx]:  # Sola git
                next_idx = idx - 1
            else:                     # Sağa git
                next_idx = idx + 1
                
            # Elemanları ve yönlerini takas et (swap)
            self.elements[idx], self.elements[next_idx] = self.elements[next_idx], self.elements[idx]
            self.directions[idx], self.directions[next_idx] = self.directions[next_idx], self.directions[idx]
            
            # 3. Mevcut hareketli elemandan daha büyük olan tüm elemanların yönünü tersine çevir
            for i in range(self.n):
                if self.elements[i] > mobile_val:
                    self.directions[i] = not self.directions[i]
            
            # Oluşan yeni permütasyonu listeye ekle
            permutations.append(list(self.elements))
            
        return permutations

# ==========================================
# ALGORİTMAYI ÇALIŞTIRMA VE TEST ETME
# ==========================================
if __name__ == "__main__":
    # Örnek: 3 elemanlı (1, 2, 3) bir kümenin tüm permütasyonlarını üretelim (3! = 6 adet)
    n_degeri = 3
    jt = JohnsonTrotter(n_degeri)
    sonuclar = jt.generate_all_permutations()
    
    print(f"=== Johnson-Trotter Algoritması (n={n_degeri}) ===")
    print(f"Toplam Üretilen Permütasyon Sayısı: {len(sonuclar)}")
    print("Permütasyon Listesi:")
    for sira, perm in enumerate(sonuclar, 1):
        print(f"{sira}. Adım: {perm}")