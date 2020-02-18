
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
data=pd.read_csv("insurance.csv")

expenses=data.expenses.values.reshape(-1,1)
ageBmis=data.iloc[:,[0,2]].values
regression=LinearRegression()
regression.fit(ageBmis,expenses)
print(regression.predict(np.array([[20,20]])))