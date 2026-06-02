def quick_sort(dizi):
    if len(dizi) <= 1:
        return dizi
    
    pivot = dizi[0]
    left = [x for x in dizi[1:] if x <= pivot]
    right = [x for x in dizi[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [4,1,8,9,3,8,1,9,4]
sorted_arr = quick_sort(arr)
print(sorted_arr)