# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor

data=pd.read_csv("positions.csv")
level=data.iloc[:,1].values.reshape(-1,1)
salary=data.iloc[:,2].values
regression= RandomForestRegressor(n_estimators=1000, random_state=0)
regression.fit(level,salary)
print(regression.predict(np.array([[8.3]])))
