# -*- coding: utf-8 -*-

students=["Fatmanur","Zehra","Ayşe"]
print(students)
print(students[1])
 
students.append("Ahmet")
students.remove("Ayşe")
print(students)

#list contructor
citys=list(("Ankara","Adıyaman","İstanbul"))
citys2=citys.copy()
#functions about list

## print(citys.clear())
print(citys.count("Ankara"))
#print("Ankara="+citys.count("Ankara"))  ----hatalı yazım
print("Ankara="+str(citys.count("Ankara")))
print("Ankara indexi="+str(citys.index("Ankara")))
citys.pop(1)
citys.insert(0,"İzmir")
citys.reverse()

citys.extend(citys2)
citys.sort()