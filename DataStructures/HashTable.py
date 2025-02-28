def is_prime(ip: int):
    import math
    try:
        assert ip > 1
        for n in range(math.isqrt(ip), 1, -1):
            if ip % n == 0:
                return False
        else:
            return True
    except AssertionError:
        print("Input number should be greater than 1")


class HashTable:
    def __init__(self, table_size=100):

        self.min_tbl_size = 50
        try:
            assert table_size >= self.min_tbl_size
        except AssertionError:
            print(f"Minimum HashTable should be {self.min_tbl_size}.")
        else:
            self.table_size = table_size
            self.items = 0
            self.array = [[] for _ in range(self.table_size)]
            self.max_load_factor = 3

    def get_load_factor(self) -> float:
        return self.items/self.table_size

    def get_hash(self, key):
        hash_value = 0
        base_val = 256
        for idx, char in enumerate(str(key)):
            hash_value += (ord(char) * (base_val**idx))

        return hash_value % self.table_size

    def __getitem__(self, key):
        key_hash = self.get_hash(key)
        for ele in self.array[key_hash]:
            if len(ele) == 2 and ele[0] == key:
                return ele[1]

    def __setitem__(self, key, value):
        key_hash = self.get_hash(key)
        for idx, val in enumerate(self.array[key_hash]):
            if len(val) == 2 and val[0] == key:
                self.array[key_hash][idx] = (key, value)
                break
        else:
            self.array[key_hash].append((key, value))

        self.items += 1

        if (0.9 * self.max_load_factor) < self.get_load_factor():
            new_size = 2 * self.table_size
            self.resize(new_size)

    def __delitem__(self, key):
        key_hash = self.get_hash(key)
        for idx, ele in enumerate(self.array[key_hash]):
            if len(ele) == 2 and ele[0] == key:
                del self.array[key_hash][idx]
                self.items -= 1

        if (self.get_load_factor() < (0.4 * self.max_load_factor)) and (self.table_size > 2*self.min_tbl_size):
            new_size = (self.table_size // 2)
            self.resize(new_size)

    def __str__(self):
        str_rep = ''
        for idx, ele in enumerate(self.array):
            str_rep += f"{idx} -> {str(ele)}\n"
        return str_rep

    def resize(self, new_size):
        print(f"Load factor is {self.get_load_factor()}, Resizing to {self.__class__.__name__} of {new_size} size")

        import copy
        old_hash_tbl = copy.deepcopy(self.array)

        new_hash_tbl = HashTable(new_size)
        for bucket in old_hash_tbl:
            for ele in bucket:
                if ele:
                    new_hash_tbl[ele[0]] = ele[1]

        self.array = new_hash_tbl.array
        self.table_size = new_hash_tbl.table_size
        self.items = new_hash_tbl.items


if __name__ == "__main__":
    a = HashTable(50)

    for i in range(600):
        a[(i+1)*(i+2)*(i+3)] = i*i*i

    print(a.items, a.table_size, a.get_load_factor())

    for i in range(100, 250):
        del a[(i+1)*(i+2)]

    print(a.items, a.table_size, a.get_load_factor())

    print(a)
