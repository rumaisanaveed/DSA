class HashTable:
    def __init__(self,size):
        self.size = size
        self.hashTable = [0] * size

    def getIndex(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        i = hash % self.size
        return i

    def insert(self,key,value):
        idx = self.getIndex(key)
        if self.hashTable[idx] == 0:
           self.hashTable[idx] = key, value
        else:
            return "Collision occured."

    def search(self,key):
        idx = self.getIndex(key)
        keyVal = self.hashTable[idx]
        if keyVal is None:
            return "Please enter a valid key-value pair."
        else:
            return keyVal[1]

    def update(self,key,value):
        idx = self.getIndex(key)
        if self.hashTable[idx] != 0:
            self.hashTable[idx] = key , value

    def delete(self,key):
        idx = self.getIndex(key)
        keyV = self.hashTable[idx]
        self.hashTable.remove(keyV)

    def displayTable(self):
        for key in self.hashTable:
            if key != 0:
               print(key)

h = HashTable(7)
h.insert("Rumaisa",3)
h.insert("Bushra",4)
h.insert("Muzna",6)
h.insert("Eshal",7)
print("After adding some key-value pairs into the hash table:")
h.displayTable()
print()
print("Search for a specific key and returns its value:")
print(h.search("Rumaisa"))
print()
h.update("Rumaisa",9)
print("After updating the value of a specific key:")
h.displayTable()
print()
h.delete("Rumaisa")
print("After deleting the specific key-value pair:")
h.displayTable()