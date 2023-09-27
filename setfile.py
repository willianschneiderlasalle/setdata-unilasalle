from hashfile import HashTable

class Set(object):
    def __init__(self, values):
        self.ht = HashTable(len(values))

        for x in range(len(values)):
            self.ht._put(x, values[x])

    def insert(self, value):
        newTable = HashTable(self.ht._getUsedSize()+1)
        
        valid = 0
        
        for v in range(len(self.ht.values)):
            if(self.ht.values[v] != None):
                newTable._put(valid, self.ht.values[v])
                valid += 1
        
        newTable._put(valid, value)

        self.ht = newTable

    def remove(self,value):
        for k in self.ht.keys:
            if(self.ht._get(k) == value):
                self.ht._delete(k)

        newTable = HashTable(self.ht._getUsedSize())
        valid = 0
        
        for v in range(len(self.ht.values)):
            if(self.ht.values[v] != None):
                newTable._put(valid, self.ht.values[v])
                valid += 1

        self.ht = newTable

    def search(self, value):
        for k in self.ht.values:
            if k == value:
                return True
        
        return False
    
    def items(self):
        return self.ht.values

def union(setA, setB):

    unionFound = 0
    temp = []

    for a in setA.ht.keys:
        if(a != None):
            unionFound += 1
            temp.append(setA.ht._get(a))

    for b in setB.ht.keys:
        if(b != None):
            unionFound += 1
            temp.append(setB.ht._get(b))

    newTable = HashTable(len(temp))

    for x in range(len(temp)):
        newTable._put(x, temp[x])

    return newTable.values

def intersection(setA, setB):

    intersecsFound = 0
    temp = []

    for a in setA.ht.keys:
        if(a != None):
            valueA = setA.ht._get(a)
            if(setB.ht._contains(valueA)):
                intersecsFound += 1
                temp.append(valueA)
    
    newTable = HashTable(intersecsFound)

    for x in range(len(temp)):
        newTable._put(x, temp[x])

    return newTable.values

def difference(setA, setB):
    
    diffsFound = 0
    temp = []

    for a in setA.ht.keys:
        if(a != None):
            valueA = setA.ht._get(a)
            if(not setB.ht._contains(valueA)):
                diffsFound += 1
                temp.append(valueA)

    for b in setB.ht.keys:
        if(b != None):
            valueB = setB.ht._get(b)
            if(not setA.ht._contains(valueB)):
                diffsFound += 1
                temp.append(valueB)

    newTable = HashTable(diffsFound)

    for x in range(len(temp)):
        newTable._put(x, temp[x])

    return newTable.values