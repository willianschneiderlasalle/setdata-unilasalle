from setfile import *

dataA = [10, 122, 40, 44, 53, 22]
mySetA = Set(dataA)

dataB = [1, 122, 34, 44, 550, 22]
mySetB = Set(dataB)

print(mySetA.items())
print(mySetB.items())

mySetA.remove(122)
mySetA.insert(223)

print(mySetA.search(122))
print(mySetA.search(10))

print(union(mySetA, mySetB))
print(intersection(mySetA, mySetB))
print(difference(mySetA, mySetB))
