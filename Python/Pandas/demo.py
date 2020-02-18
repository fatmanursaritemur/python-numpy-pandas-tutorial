# -*- coding: utf-8 -*-

import pandas as pd

notes=pd.read_csv("grades.csv")
notes.columns =["İsim","Soyisim","SSN","T1","T2","T3","T4","Final","Grade"]
print(notes)
print(type(notes))
print(notes.head())
print("*******************************")
print(notes["İsim"])
print(notes.iloc[2])