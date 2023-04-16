class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.hashTable = [None] * size

    def insert(self, key):
        h = key % self.size
        if self.hashTable[h] is None:
            self.hashTable[h] = key
        else:
            for i in range(self.size):
                newHash = (h + i) % self.size
                if self.hashTable[newHash] is None:
                    self.hashTable[newHash] = key
                    break

    def search(self, key):
        h = key % self.size
        if self.hashTable[h] == key:
            return "Found"
        else:
            for i in range(self.size):
                newHash = (h + i) % self.size
                if self.hashTable[newHash] == key:
                    return "Found"
            return "Not found"

    def update(self, newKey, preKey):
        prevValHash = preKey % self.size
        if self.hashTable[prevValHash] == preKey:
            self.hashTable[prevValHash] = newKey
        else:
            for i in range(self.size):
                newHash = (prevValHash + i) % self.size
                if self.hashTable[newHash] == preKey:
                    self.hashTable[newHash] = newKey
                    break

    def delete(self, key):
        h = key % self.size
        val = self.hashTable[h]
        if val == key:
            self.hashTable[h] = None
        else:
            for i in range(self.size):
                newHash = (h + i) % self.size
                if self.hashTable[newHash] == key:
                    self.hashTable[newHash] = None
                    break

    def displayHashTable(self):
        for key in self.hashTable:
            if key is not None:
                print(key, end=" ")
        print()

h = LinearProbing(7)
h.insert(50)
h.insert(700)
h.insert(76)
h.insert(85)
h.insert(92)
h.insert(73)
h.insert(101)
print("After inserting the keys:")
h.displayHashTable()
print()
print("Search for a key with value 92:")
print(h.search(92))
print()
h.update(100,85)
print("After updating the key 85 with 100:")
h.displayHashTable()
print()
h.delete(85)
print("After deleting the key with value 85:")
h.displayHashTable()