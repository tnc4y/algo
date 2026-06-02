def graycode(n):
    if n == 0:
        return ['']
    first = graycode(n - 1)
    second = first[::-1]
    return ['0' + x for x in first] + ['1' + x for x in second]

def subsets_with_gray(elements):
    n = len(elements)
    gray_codes = graycode(n)
    subsets = []
    for code in gray_codes:
        subset = [elements[i] for i in range(n) if code[i] == '1']
        subsets.append(subset)
    return subsets

elemanlar = ['a', 'b', 'c']
for alt_kume in subsets_with_gray(elemanlar):
    print(alt_kume)