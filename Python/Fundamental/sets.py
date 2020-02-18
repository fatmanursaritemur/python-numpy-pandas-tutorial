# -*- coding: utf-8 -*-

studentsSet={"Fatmanur","Zehra","Ayse"}
print(studentsSet) #kafasına göre getiriyor

for student in studentsSet:
    print(student)
    
print("Zehra" in studentsSet)

if "Zehra" in studentsSet:
    print("Listede var")
    
studentsSet.add("Sıkıldım")
studentsSet.update(["Merve","Ayse"])
studentsSet.remove("Ayse")
studentsSet.discard("Ahmet") #bulamazsa hata olmayacak