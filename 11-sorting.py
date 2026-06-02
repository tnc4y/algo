def sorting_by_counting(A):
    n = len(A)
    if n == 0:
        return A
    count = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and A[i] > A[j]:
                count[i] += 1
    sorted_A = [0] * n
    for i in range(n):
        sorted_A[count[i]] = A[i]
    return sorted_A
        

arr = [62,31,84,96,19,47]
sorted_arr = sorting_by_counting(arr)
print("Counting Sort ile sıralanmış dizi:", sorted_arr)