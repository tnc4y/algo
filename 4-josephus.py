def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n
    
n = 103
k = 2
print(f"Josephus({n}, {k}) = {josephus(n, k)}")
