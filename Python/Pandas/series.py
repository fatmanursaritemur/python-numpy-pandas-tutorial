# -*- coding: utf-8 -*-

import pandas as pd
import numpy  as np

data=np.array(["Fatmanur","Saritemur","12"])
b=pd.Series(data, index=[1,2,3])
print(b)

data2={"math":12, "biolog7":64, "chemistry":21}
d=pd.Series(data2, index=["math","biology7"])
print(d)
print("***************************")
print(d[0])

e=pd.Series(7,index=[1])
print(e)