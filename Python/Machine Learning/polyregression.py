# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data=pd.read_csv("positions.csv")
print(data.columns)

level=data.iloc[:,1].values.reshape(-1,1)
salary=data.iloc[:,2].values.reshape(-1,1)
regression=LinearRegression()
regression.fit(level,salary)

assume=regression.predict(np.array([[8.3]]))
plt.scatter(level,salary, color="red")

print("********************************")
print("********************************")
regressionPoly=PolynomialFeatures(degree = 4)
levelPoly=regressionPoly.fit_transform(level)
regression2=LinearRegression()
regression2.fit(levelPoly,salary)
assume2=regression2.predict(regressionPoly.fit_transform([[8.3]]))
plt.plot(level,regression2.predict(levelPoly))
plt.show()