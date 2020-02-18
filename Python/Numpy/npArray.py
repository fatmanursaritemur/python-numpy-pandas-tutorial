# -*- coding: utf-8 -*-

import numpy as np

a=np.array([1,2,3,4,5,6])
a=a.reshape(2,3)
print(a)
print(a.dtype)

a
b=np.array([1,2,3,"4",5,6,7]) #hepsini string yaptı
print(b)
print(b.dtype)

c=np.array([[1,3],[4,2],[8,5]])
print(c)
print(c.dtype)
print("*******************************************")
e=np.array([2,5,3,14])
f=np.arange(4)
print(e*f)   #elementwise product
print(e@f)
print(e.dot(f))
print("*******************************************")
g=np.ones((2,4))
k=np.zeros((8,7))
l=np.random.random((2,4))
n=np.sum(f)
j=np.min(f)
m=np.max(f)
t=np.sqrt(f)