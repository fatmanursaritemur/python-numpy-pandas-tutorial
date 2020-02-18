# -*- coding: utf-8 -*-

import pandas as pd

data=[10,23,22,33,11]
df=pd.DataFrame(data)
print(df)

data2=[["Fatmanur",22,"İstanbul"],["Zehra",21,"İstanbul"]]
df2=pd.DataFrame(data2, columns=["İsim","Yas","Sehir"])
print(df2)

data3={"İsim":["Fatmanur","Zehra","Ali"],
       "Yas":[12,34,22],
      "Sehir":["İstanbul","Konya","Antalya"] }
df3=pd.DataFrame(data3,columns=["İsim","Yas","Sehir"], index=[1,2,3])
print(df3["Yas"])
print("**********************************")
del df3["Sehir"]
df2.pop("Sehir")
print(df3)
print("**********************************")
print(df3.loc[2])
print("**********************************")
print(df3.iloc[1])

df4=df3.append(df2) #genisletme
print(df4)
print("**********************************")
print(df4.head)
print(df4.tail)