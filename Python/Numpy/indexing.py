# -*- coding: utf-8 -*-

import numpy as np

sayilar=np.array([0,5,12,4,2,1])
print(sayilar[3])
print(sayilar[2:5])
print(sayilar[::-1])
print("********************************")
sayilar2=np.array([[13,4,2,1],[13,22,6,8]])
print(sayilar2[1,3])
print(sayilar2[:,2]) 
print(sayilar2[-1,:])