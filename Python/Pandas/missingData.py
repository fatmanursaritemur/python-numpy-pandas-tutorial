# -*- coding: utf-8 -*-

import pandas as pd

url="https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"
data=pd.read_csv(url)
#print(data.isnull().head(100))
#print("****************************************")
#print(data.notnull().head(100))
#print("****************************************")
#print(data.isnull().sum())
#print(data[data.City.isnull()])
#print("****************************************")
print(data.shape)
#data=data.dropna(how="any")
#print(data.shape)
#print("****************************************")
#data2=data.dropna(subset=['City','Colors Reported'],how='any')
print("****************************************")
data['Shape Reported'].fillna(value='Belirsiz', inplace=True)
print(data['Shape Reported'].value_counts(dropna=False))
print(data.shape)