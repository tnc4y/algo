#doğrusal sınama(Linear Probing)
class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        i = 0
        while i < self.size:
            idx = (self.hash(key) + i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                return idx
            i += 1
        raise Exception("Hash table overflow")

    def search(self, key):
        i = 0
        while i < self.size:
            idx = (self.hash(key) + i) % self.size
            if self.table[idx] == key:
                return idx
            if self.table[idx] is None:
                return -1
            i += 1
        return -1


#karesel sınama (Quadratic Probing)
class QuadraticProbingHashTable:
    def __init__(self, size, s1=1, s2=3):
        self.size = size
        self.table = [None] * size
        self.s1 = s1
        self.s2 = s2

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        i = 0
        while i < self.size:
            idx = (self.hash(key) + self.s1 * i + self.s2 * i * i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                return idx
            i += 1
        raise Exception("Hash table overflow")

    def search(self, key):
        i = 0
        while i < self.size:
            idx = (self.hash(key) + self.s1 * i + self.s2 * i * i) % self.size
            if self.table[idx] == key:
                return idx
            if self.table[idx] is None:
                return -1
            i += 1
        return -1


#İkili Özetleme (Double Hashing)
class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        i = 0
        while i < self.size:
            idx = (self.hash1(key) + i * self.hash2(key)) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                return idx
            i += 1
        raise Exception("Hash table overflow")

    def search(self, key):
        i = 0
        while i < self.size:
            idx = (self.hash1(key) + i * self.hash2(key)) % self.size
            if self.table[idx] == key:
                return idx
            if self.table[idx] is None:
                return -1
            i += 1
        return -1


#Ayrık Zincirleme (Separate Chaining)
class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash(key)
        if key not in self.table[idx]:
            self.table[idx].append(key)

    def search(self, key):
        idx = self.hash(key)
        if key in self.table[idx]:
            return idx, self.table[idx].index(key)
        return -1


#örnek kullanım
if __name__ == "__main__":
    keys = [82, 27, 35, 47, 64]

    print("=== Linear Probing ===")
    lp_table = LinearProbingHashTable(10)
    for key in keys:
        idx = lp_table.insert(key)
        print(f"Inserted {key} at index {idx}")
    print("Search 47:", lp_table.search(47))

    print("\n=== Quadratic Probing ===")
    qp_table = QuadraticProbingHashTable(10)
    for key in keys:
        idx = qp_table.insert(key)
        print(f"Inserted {key} at index {idx}")
    print("Search 47:", qp_table.search(47))

    print("\n=== Double Hashing ===")
    dh_table = DoubleHashingHashTable(10)
    for key in keys:
        idx = dh_table.insert(key)
        print(f"Inserted {key} at index {idx}")
    print("Search 47:", dh_table.search(47))

    print("\n=== Separate Chaining ===")
    sc_table = SeparateChainingHashTable(10)
    for key in keys:
        sc_table.insert(key)
        print(f"Inserted {key} in chain at index {key % 10}")
    print("Search 47:", sc_table.search(47))