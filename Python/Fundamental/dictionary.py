# -*- coding: utf-8 -*-

dictionary= {
        "book":"kitap",
        "table":"masa"
        }
dictionary2=dict(mouse="fare", notebook="defter")
print(dictionary["book"])
dictionary["book"]="ketebe"
dictionary["pencil"]= "kalem"
del(dictionary["book"])
print(dictionary)