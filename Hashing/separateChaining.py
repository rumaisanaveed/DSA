class separateChaining:
    def __init__(self,tableSize):
        self.tableSize = tableSize
        self.hashTable = [[] for _ in range(tableSize)]

    def insert(self,value):
        h = value % self.tableSize
        self.hashTable[h].append(value)

    def delete(self,value):
        h = value % self.tableSize
        if value not in self.hashTable[h]:
            return "Value not found.Please enter the existing value."
        else:
            self.hashTable[h].remove(value)

    def search(self,value):
        h = value % self.tableSize
        for i in self.hashTable[h]:
            if i == value:
                return "Found"
        return "Not Found"

    def displayHashTable(self):
        for i in range(len(self.hashTable)):
            print(i,end = " ")
            for j in range(len(self.hashTable[i])):
                print(" -->",self.hashTable[i][j], end='')
            print()

h = separateChaining(7)
h.insert(15)
h.insert(11)
h.insert(27)
h.insert(8)
h.insert(12)
print("After adding some values to the hash table:")
h.displayHashTable()
print()
print("Search for value 27:")
print(h.search(27))
print()
h.delete(11)
print("After deleting the value 11:")
h.displayHashTable()