class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        i = 1                                          # Quadratic probing increment factor
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value              # Update value if key already exists
                return
            index = (index + i ** 2) % self.size       # Quadratic probing to find next available slot
            i += 1
        self.keys[index] = key
        self.values[index] = value

    def delete(self, key):
        index = self.hash_function(key)
        i = 1                                        # Quadratic probing increment factor
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.rehash(index)
                return
            index = (index + i ** 2) % self.size
            i += 1
        raise KeyError(key)

    def rehash(self, start_index):
        current_index = start_index
        next_index = (start_index + 1) % self.size
        i = 1  # Quadratic probing increment factor
        while self.keys[next_index] is not None:
            hash_value = self.hash_function(self.keys[next_index])
            if (
                next_index > current_index and
                (hash_value <= current_index or hash_value > next_index)
            ) or (
                next_index < current_index and
                (hash_value <= current_index and hash_value > next_index)
            ):
                self.keys[current_index] = self.keys[next_index]
                self.values[current_index] = self.values[next_index]
                self.keys[next_index] = None
                self.values[next_index] = None
                current_index = next_index
            next_index = (next_index + i ** 2) % self.size
            i += 1

    def display(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f'{i}: {self.keys[i]}={self.values[i]}')
            else:
                print(f'{i}: None')


table = HashTable(5)
table.insert("apple", 1)
table.insert("banana", "9")
table.insert("papaya", 7)
table.display()
table.delete("apple")
table.display()
