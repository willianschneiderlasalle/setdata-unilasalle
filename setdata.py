#SET: inserção, remoção, consulta de elementos, união, interseção e diferença
#HASHTABLE
# justificativa para a escolha da estrutura de dados, e a complexidade de tempo e espaço esperada para cada uma das operações.

class HashTable(object):
    def __init__(self,size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
         
    def put(self,key,value):
        hashValue = self.hashFunction(key, self.size)
 
        if self.keys[hashValue] == None:
            self.keys[hashValue] = key
            self.values[hashValue] = value
        else:
            if self.keys[hashValue] == key:
                self.values[hashValue] = value  
            else:
                nextSlot = self.rehash(hashValue, self.size)

                while self.keys[nextSlot] != None and self.keys[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot,self.size)

                if self.keys[nextSlot] == None:
                    self.keys[nextSlot] = key
                    self.values[nextSlot] = value
                else:
                    self.values[nextSlot] = value 

    def delete(self,key):
        hashValue = self.hashFunction(key, self.size)

        if self.get(key) != None:
            if self.keys[hashValue] == key:
                self.keys[hashValue] = None
                self.values[hashValue] = None
            else:
                nextSlot = self.rehash(hashValue, self.size)
                while self.keys[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot,self.size)

                self.keys[hashValue] = None
                self.values[hashValue] = None

        
    
    def get(self,key):

        startSlot = self.hashFunction(key,self.size)
        value = None
        shouldStop = False
        isFound = False
        pos = startSlot
         
        while self.keys[pos] != None and not isFound and not shouldStop:
             
            if self.keys[pos] == key:
                isFound = True
                value = self.values[pos]
            else:
                pos=self.rehash(pos,self.size)
                if pos == startSlot:
                    shouldStop = True

        return value
 
    def hashFunction(self,key,size):
        return key % size
 
    def rehash(self,oldHash,size):
        return (oldHash+1) % size
    
myTable = HashTable(6)

keys = [10, 20, 40, 44, 53, 22]
values = [1, 122, 34, 44, 550, 2]

for x in range(len(keys)):
    myTable.put(keys[x], values[x])

myTable.get(40)
myTable.delete(40)
print(myTable.keys)
print(myTable.values)