class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value  # Update value if key already exists
                return
            index = (index + 1) % self.size  # Linear probing to find next available slot
        self.keys[index] = key
        self.values[index] = value

    def delete(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.rehash(index)
                return
            index = (index + 1) % self.size
        raise KeyError(key)

    def rehash(self, index):
        current_index = index
        next_index = (index + 1) % self.size
        while self.keys[next_index] is not None:
            self.keys[current_index] = self.keys[next_index]
            self.values[current_index] = self.values[next_index]
            self.keys[next_index] = None
            self.values[next_index] = None
            current_index = next_index
            next_index = (next_index + 1) % self.size

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
