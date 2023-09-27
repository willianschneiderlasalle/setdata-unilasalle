class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
         
    def _put(self, key, value):
        hashValue = self._hashFunction(key, self.size)
 
        if self.keys[hashValue] == None:
            self.keys[hashValue] = key
            self.values[hashValue] = value
        else:
            if self.keys[hashValue] == key:
                self.values[hashValue] = value  
            else:
                nextSlot = self._rehash(hashValue, self.size)

                while self.keys[nextSlot] != None and self.keys[nextSlot] != key:
                    nextSlot = self._rehash(nextSlot,self.size)

                if self.keys[nextSlot] == None:
                    self.keys[nextSlot] = key
                    self.values[nextSlot] = value
                else:
                    self.values[nextSlot] = value 

    def _delete(self, key):
        hashValue = self._hashFunction(key, self.size)

        if self._get(key) != None:
            if self.keys[hashValue] == key:
                self.keys[hashValue] = None
                self.values[hashValue] = None
            else:
                nextSlot = self._rehash(hashValue, self.size)
                while self.keys[nextSlot] != key:
                    nextSlot = self._rehash(nextSlot,self.size)

                self.keys[hashValue] = None
                self.values[hashValue] = None
    
    def _get(self, key):

        startSlot = self._hashFunction(key,self.size)
        value = None
        shouldStop = False
        isFound = False
        pos = startSlot
         
        while self.keys[pos] != None and not isFound and not shouldStop:
             
            if self.keys[pos] == key:
                isFound = True
                value = self.values[pos]
            else:
                pos=self._rehash(pos,self.size)
                if pos == startSlot:
                    shouldStop = True

        return value
 
    def _contains(self, value):
        for k in self.keys:
            if(k != None):
                if(self._get(k) == value):
                    return True
        
        return False

    def _hashFunction(self, key, size):
            return key % size
 
    def _rehash(self, oldHash, size):
        return (oldHash+1) % size
    
    def _getUsedSize(self):

        size = 0

        for k in self.keys:
            if k != None:
                size += 1

        return size