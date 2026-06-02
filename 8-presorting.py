from collections import Counter


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def is_unique(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False

arr = [4,1,8,9,3,8,1,9,4,9]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
print("Bu liste benzersiz mi?", is_unique(sorted_arr))

def find_duplicates(arr):
    arr.sort()
    duplicates = set()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            duplicates.add(arr[i])
    return duplicates

duplicates = find_duplicates(arr)
print("Tekrar eden elemanlar:", duplicates)


def presort_mode(A):
    A.sort()
    n = len(A)
    modeFrequency = 0
    modeValue = None
    i = 0
    while i<=n-1:
        if i < n-1 and A[i] == A[i+1]:
            count = 1
            while i < n-1 and A[i] == A[i+1]:
                count += 1
                i += 1
            if count >= modeFrequency:
                modeFrequency = count
                modeValue = A[i]
        i += 1
    return modeValue

mode = presort_mode(arr)
print("Mod değeri:", mode)






