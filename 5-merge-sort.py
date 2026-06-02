def merge_sort(dizi):
    if len(dizi) <= 1:
        return dizi
    mid = len(dizi) // 2
    left = merge_sort(dizi[:mid])
    right = merge_sort(dizi[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    results = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1

    results.extend(left[i:])
    results.extend(right[j:])

    return results

arr = [8,3,2,9,8,1,5,4]
sorted_arr = merge_sort(arr)
print(sorted_arr)
