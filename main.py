from setfile import *

mySetA = Set(6)
mySetB = Set(6)

setA = [10, 122, 40, 44, 53, 22]
setB = [1, 122, 34, 44, 550, 22]

for a in setA:
    mySetA.insert(a)

for b in setB:
    mySetB.insert(b)

mySetA.remove(122)

print(mySetA.search(122))
print(mySetA.search(10))
print(mySetA.ht.values)

print(union(mySetA, mySetB))
print(intersection(mySetA, mySetB))
print(difference(mySetA, mySetB))
