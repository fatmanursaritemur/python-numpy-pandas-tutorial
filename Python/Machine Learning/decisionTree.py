# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor

data=pd.read_csv("positions.csv")
level=data.iloc[:,1].values.reshape(-1,1)
salary=data.iloc[:,2].values.reshape(-1,1)

regression= DecisionTreeRegressor()
regression.fit(level,salary)
print(regression.predict(np.array([[7.2]])))
plt.scatter(level,salary,color="red")
print("***************************************************")
x=np.arange(min(level),max(level),0.01).reshape(-1,1)
plt.plot(x,regression.predict(np.array(x)),color="orange").reshape(-1,1)
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Decision Tree Model")
print("***************************************************")
plt.show()

 
