# -*- coding: utf-8 -*-
import numpy as np

a=np.arange(10)
print(a)
b=a
print(b)
b[0]=100
print(a)
print(b)
print("***************************")
c=a.copy()
c[0]=200
d=a.view()
d.shape=2,5