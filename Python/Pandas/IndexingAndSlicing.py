import pandas as pd

notes=pd.read_csv("grades.csv")
notes.columns =["İsim","Soyisim","SSN","T1","T2","T3","T4","Final","Grade"]
print(notes.loc[3:5,"İsim"])
print(notes.loc[3:5,"İsim":"T1"])
print(notes.loc[3:5,["İsim","T4"]])
print(notes.loc[3:5,:"T4"])
print(notes.loc[::-1,:"İsim"])