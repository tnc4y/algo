import heapq

graf = {
    0: [(1, 8), (2, 2), (3, 5)],
    1: [(0, 8), (3, 2), (5, 13)],
    2: [(0, 2), (3, 2), (4, 5)],
    3: [(0, 5), (1, 2), (2, 2), (4, 1), (5, 6), (6, 3)],
    4: [(2, 5), (3, 1), (6, 1)],
    5: [(1, 13), (3, 6), (6, 2), (7, 3)],
    6: [(3, 3), (4, 1), (5, 2), (7, 6)],
    7: [(5, 3), (6, 6)]
}

def dijkstra(graf, baslangic):
    n = len(graf)
    mesafe = [float('inf')] * n
    onceki = [None] * n
    mesafe[baslangic] = 0
    kuyruk = [(0, baslangic)]
    while kuyruk:
        mevcut_mesafe, dugum = heapq.heappop(kuyruk)
        if mevcut_mesafe > mesafe[dugum]:
            continue
        for komsu, agirlik in graf[dugum]:
            yeni_mesafe = mevcut_mesafe + agirlik
            if yeni_mesafe < mesafe[komsu]:
                mesafe[komsu] = yeni_mesafe
                onceki[komsu] = dugum
                heapq.heappush(kuyruk, (yeni_mesafe, komsu))
    return mesafe, onceki

def yol_olustur(onceki, hedef):
    yol = []
    while hedef is not None:
        yol.append(hedef)
        hedef = onceki[hedef]
    yol.reverse()
    return yol

baslangic = 0
mesafe, onceki = dijkstra(graf, baslangic)

print("Düğüm | En Kısa Mesafe | İzlenen Yol")
for i in range(len(mesafe)):
    yol = yol_olustur(onceki, i)
    yol_str = " -> ".join(map(str, yol))
    print(f"  {i}   |       {mesafe[i]}        | {yol_str}")