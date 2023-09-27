from hashfile import HashTable

class Set(object):
    def __init__(self, size):
        self.ht = HashTable(size)

    def insert(self, value):
        self.ht._put(self.ht._getUsedSize(), value)

    def remove(self,value):
        for k in self.ht.keys:
            if(self.ht._get(k) == value):
                self.ht._delete(k)

    def search(self, value):
        for k in self.ht.values:
            if k == value:
                return True
        
        return False

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