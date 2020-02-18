# -*- coding: utf-8 -*-

#substring
message="Hello Worlddd"
print(message)   #Hello World
print(message[2]) #l
print(message[2:5]) #llo
print(message[5:2]) #not error but doesnt work
yenimesaj=message[:2]
print(len(message)) #11
yenimesaj2=message[2:len(message)-1]

#upper lower
print(message.upper())
message=message.replace("l","*")
#replace
print(message)

#split
name="Fatma Nur Saritemur"
print(name.split()) 

namewithdot="Fatma.Nur.Sarıtemur"
print(namewithdot.split("."))
print(namewithdot.split(".")[2]) #birinci elemanı yaz

#input
surname=input("What is your surname?")
firstnumber=input("first number?")
secondnumber=input("second number?")
print(int(firstnumber)+int(secondnumber))