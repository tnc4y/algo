from collections import deque

dugumler = ['S', 'A', 'B', 'C', 'D']

graf = {
    0: [1, 2, 3],
    1: [0, 4],
    2: [0, 4],
    3: [0, 4],
    4: [1, 2, 3]
}

def bfs_kuyruk_ve_sonuc(graf, baslangic):
    ziyaret_edildi = [False] * len(graf)
    kuyruk = deque([baslangic])
    ziyaret_edildi[baslangic] = True
    ziyaret_sirasi = []
    while kuyruk:
        dugum = kuyruk.popleft()
        ziyaret_sirasi.append(dugumler[dugum])
        for komsu in graf[dugum]:
            if not ziyaret_edildi[komsu]:
                ziyaret_edildi[komsu] = True
                kuyruk.append(komsu)
    print("Ziyaret sırası (sonuç):", ' '.join(ziyaret_sirasi))

print("Enine Arama Sonuclari:")
bfs_kuyruk_ve_sonuc(graf, 0)

