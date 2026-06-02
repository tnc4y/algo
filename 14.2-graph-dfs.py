dugumler = ['S', 'A', 'B', 'C', 'D']

graf = {
    0: [1, 2, 3],
    1: [0, 4],
    2: [0, 4],
    3: [0, 4],
    4: [1, 2, 3]
}

def dfs(graf, dugum, ziyaret_edildi):
    ziyaret_edildi[dugum] = True
    print(dugumler[dugum], end=' ')
    for komsu in graf[dugum]:
        if not ziyaret_edildi[komsu]:
            dfs(graf, komsu, ziyaret_edildi)

ziyaret_edildi = [False] * len(graf)
print("Derinliğine Arama Sonuclari: ", end='')
dfs(graf, 0, ziyaret_edildi)
print()

def dfs_stack(graf, baslangic):
    ziyaret_edildi = [False] * len(graf)
    yigin = [baslangic]
    while yigin:
        dugum = yigin.pop()
        if not ziyaret_edildi[dugum]:
            print(dugumler[dugum], end=' ')
            ziyaret_edildi[dugum] = True
            for komsu in reversed(graf[dugum]):
                if not ziyaret_edildi[komsu]:
                    yigin.append(komsu)

print("DFS (yığın ile): ", end='')
dfs_stack(graf, 0)
print()