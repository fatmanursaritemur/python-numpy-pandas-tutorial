# -*- coding: utf-8 -*-

import numpy as np

a=np.floor(10*np.random.random((2,3)))
b=np.floor(10*np.random.random((2,3)))

c=np.vstack((a,b))
print(c)