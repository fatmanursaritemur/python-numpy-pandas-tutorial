# -*- coding: utf-8 -*-

import json
data='{"firstName":"fatmanur","lastname":"saritemur"}'
y=json.loads(data)
type(y) #sonuc yok bunu taniyamadi
print(y["firstName"])
customer={
        "firstName":"fatmanur","lastname":"saritemur"
        }
customerJson=json.dumps(customer)
print(customer)