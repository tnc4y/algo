def anagram_bul(dosya_adi):
    anagram = {}
    with open(dosya_adi, 'r', encoding='utf-8') as f:
        for satir in f:
            kelime = satir.strip().lower()
            anahtar = ''.join(sorted(kelime))
            if anahtar in anagram:
                anagram[anahtar].append(kelime)
            else:
                anagram[anahtar] = [kelime]
    return anagram

anagramlar = anagram_bul('file.txt')
for anahtar, kelimeler in anagramlar.items():
    if len(kelimeler) > 1:
        print(f"Anagram: {kelimeler}")


