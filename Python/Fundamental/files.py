# -*- coding: utf-8 -*-

f=open("customer.txt","a")
#print(f.read(10))
#print(f.readline())

#for l in f:
 # print(f.readline())
  
f.write("aaaaaaa")
f.close()


import os
if os.path.exists("customer.txt"):
   os.remove("customer.txt")
else:
    print("File is not exist")
    
os.rmdir("empty")