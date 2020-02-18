# -*- coding: utf-8 -*-

setA={1,2,3,4,5}
setB={1,3,5,7,8,11}

print(setA | setB)
print(setA.union(setB))
print("***********************************")
print(setA & setB)
print(setA in setB) #farklı bir sonuc
print(setB.intersection(setA))

print("***********************************")
print(setA - setB)
print(setA.difference(setB))

print("***********************************")
print(setA ^ setB)
print(setA.symmetric_difference(setB))