#bölme yönetmi
def hash_division(key, size):
    return key % size
# çarpma yönetmi
def hash_multiplication(key, size, A=0.618):
    frac = (key * A) % 1
    return int(size * frac)
#orta-kare yönetmi
def hash_mid_square(key, size, r=2):
    squared = key * key
    squared_str = str(squared).zfill(r*2)  # en az 2r hane olsu
    mid_start = (len(squared_str) // 2) - (r // 2)
    mid_digits = squared_str[mid_start:mid_start + r]
    return int(mid_digits) % size
# katlama yönetmi
def hash_folding(key, size, part_size=2):
    key_str = str(key)
    total = 0
    for i in range(0, len(key_str), part_size):
        part = key_str[i:i+part_size]
        total += int(part)
    return total % size
