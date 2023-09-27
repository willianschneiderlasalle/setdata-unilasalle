#SET: inserção, remoção, consulta de elementos, união, interseção e diferença
#HASHTABLE
# justificativa para a escolha da estrutura de dados, e a complexidade de tempo e espaço esperada para cada uma das operações.

class HashTable(object):
     
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.value = [None] * self.size
         
    def put(self,key,value):
        hashValue = self.hashFunction(key, self.size)
 
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.value[hashValue] = value
        else:
            if self.slots[hashValue] == key:
                self.value[hashValue] = value  
            else:
                nextSlot = self.rehash(hashValue, self.size)

                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot,self.size)

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot]=key
                    self.value[nextSlot]=value
                else:
                    self.value[nextSlot] = value 
    
    def get(self,key):

        startSlot = self.hashFunction(key,self.size)
        value = None
        shouldStop = False
        isFound = False
        pos = startSlot
         
        while self.slots[pos] != None and not isFound and not shouldStop:
             
            if self.slots[pos] == key:
                isFound = True
                value = self.value[pos]
            else:
                pos=self.rehash(pos,self.size)
                if pos == startSlot:
                    shouldStop = True

        if(value == None):
            return "Could not find any value with this key"


        return value
 
    def hashFunction(self,key,size):
        return key % size
 
    def rehash(self,oldHash,size):
        return (oldHash+1) % size
    
test = HashTable(6)

keys = [10, 20, 40, 44, 53, 22]
values = [1, 122, 34, 44, 550, 2]

for x in range(len(keys)):
    test.put(keys[x], values[x])

print(test.slots)
print(test.value)
print(test.get(40))