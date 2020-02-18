# -*- coding: utf-8 -*-

tupleList=(2,4,"istanbul") # tuple daha performanslı
list=[2,4,"istanbul"]
tupleValue=("aaa",) #tek elemansa virgül koymalıyız tuple'da
print(type(tupleList))
print(type(list))
list[0]=6 # it is works
#tupleList[0]=7 #does not work 
print(tupleList)
print(list)