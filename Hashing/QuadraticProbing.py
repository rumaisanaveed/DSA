class QuadraticProbing:
    def __init__(self,size):
        self.size = size
        self.hashTable = [None] * size

    def insert(self,key,value):
        # Check if the slot is empty or not
        h = key % self.size
        if self.hashTable[h] == None:
            self.hashTable[h] = key , value
        else:
            # Check for the next empty position
            for i in range(self.size):
                newHash = (h + i * i) % self.size
                if self.hashTable[newHash] == None:
                    self.hashTable[newHash] = key , value
                    break

    def search(self,key):
        h = key % self.size
        if self.hashTable[h][0] == key:
            return self.hashTable[h][1]
        else:
            for i in range(self.size):
                newHash = (h + i * i) % self.size
                if self.hashTable[newHash][0] == key:
                    return self.hashTable[newHash][1]
            return "Not found"

    def update(self,newKey,value,preVKey):
        prevValHash = preVKey % self.size
        if self.hashTable[prevValHash][0] == preVKey:
            self.hashTable[prevValHash] = (newKey , value)
        else:
            for i in range(self.size):
                newHash = (prevValHash + i * i) % self.size
                if self.hashTable[newHash][0] == preVKey:
                    self.hashTable[newHash] = (newKey , value)
                    break

    def delete(self,key):
        h = key % self.size
        if self.hashTable[h][0] == key:
            self.hashTable.remove(self.hashTable[h])
        else:
            for i in range(self.size):
                newHash = (h + i * i) % self.size
                if self.hashTable[newHash][0] == key:
                    self.hashTable.remove(self.hashTable[newHash])
                    break

    def displayHashTable(self):
        for key in self.hashTable:
            if key != None:
               print(key, end = "  ")
        print()

h = QuadraticProbing(7)
h.insert(50,10)
h.insert(700,30)
h.insert(76,40)
h.insert(85,20)
h.insert(92,10)
h.insert(73,60)
h.insert(101,70)
print("After inserting some keys into the hash table:")
h.displayHashTable()
print()
print("Search for a key with value 92:")
print(h.search(92))
print()
h.update(100,50,85)
print("After updating the key with value 85 to 100:")
h.displayHashTable()
print()
h.delete(73)
print("After deleting the key with value 73:")
h.displayHashTable()