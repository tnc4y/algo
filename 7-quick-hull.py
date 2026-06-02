import matplotlib.pyplot as plt
import numpy as np

def ccw(p, q, r):
    """Üç noktanın yönünü hesaplar."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Kollinear
    elif val > 0:
        return 1  # Saat yönünün tersi
    else:
        return -1 # Saat yönü

def EnUzakNokta(a, b, S):
    """a ve b noktaları arasındaki doğru parçasından en uzak noktayı bulur."""
    if not S:
        return None
    
    max_distance = 0
    farthest_point = None
    for p in S:
        dist = abs((b[1] - a[1]) * p[0] - (b[0] - a[0]) * p[1] + b[0] * a[1] - b[1] * a[0])
        if dist > max_distance:
            max_distance = dist
            farthest_point = p
    return farthest_point

def NoktaEkle(hull, a, b, S):
    """Verilen a ve b noktaları arasındaki konveks örtüyü bulur."""
    p = EnUzakNokta(a, b, S)
    if p is None:
        return

    index_b = hull.index(b)
    hull.insert(index_b, p)

    LAP = []
    LPB = []
    for s in S:
        if s != p:
            if ccw(a, p, s) > 0:
                LAP.append(s)
            if ccw(p, b, s) > 0:
                LPB.append(s)

    NoktaEkle(hull, a, p, LAP)
    NoktaEkle(hull, p, b, LPB)

def QuickHull(S):
    """QuickHull algoritması ile konveks örtüyü hesaplar."""
    if len(S) < 3:
        return S
    
    # En küçük ve en büyük x koordinatlarına sahip noktaları bul
    a = min(S, key=lambda p: p[0])
    b = max(S, key=lambda p: p[0])
    
    CH = [a, b]
    
    # Noktaları iki kümeye ayır
    LS = [p for p in S if ccw(a, b, p) > 0]
    RS = [p for p in S if ccw(b, a, p) > 0]
    
    NoktaEkle(CH, a, b, LS)
    NoktaEkle(CH, b, a, RS)
    return CH

# Örnek noktalar
S = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]

# Konveks örtüyü hesapla
CH = QuickHull(S)

# Noktaları ve konveks örtüyü çiz
plt.figure()
plt.scatter(*zip(*S))

# Konveks örtüyü çiz
CH.append(CH[0]) # Kapalı bir şekil için son noktanın başa eklenmesi
plt.plot(*zip(*CH), 'r-')
plt.axis('equal') # Eşit ölçekli gösterim
plt.show()