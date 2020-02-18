# -*- coding: utf-8 -*-

import numpy as np

a=np.floor(10*np.random.random((3,6)))
print(a.ravel())
print(a.reshape(2,9))
print(a.T)