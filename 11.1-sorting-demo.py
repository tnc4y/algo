# Python Sıralama Örnekleri

sayilar = [42, 7, 12, 89, 24, 1]
meyveler = ["muz", "elma", "çilek", "armut"]

# 1. sorted() Fonksiyonu: Orijinal listeyi bozmaz, yeni bir sıralı liste döndürür.
sirali_sayilar = sorted(sayilar)
print(f"Orijinal Sayılar: {sayilar}")
print(f"Sıralı Sayılar (sorted): {sirali_sayilar}")

# 2. .sort() Metodu: Listeyi olduğu yerde (in-place) değiştirir.
meyveler.sort()
print(f"Sıralı Meyveler (.sort): {meyveler}")

# 3. Tersten Sıralama (Reverse)
tersten_sayilar = sorted(sayilar, reverse=True)
print(f"Büyükten Küçüğe: {tersten_sayilar}")

# 4. Key Parametresi ile Özel Sıralama (Örn: Uzunluğa göre)
isimler = ["Ali", "Mustafa", "Can", "Zeynep"]
uzunluga_gore = sorted(isimler, key=len)
print(f"Uzunluğa Göre İsimler: {uzunluga_gore}")
