import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
   }
dec=json.dumps(d,sort_keys=True, indent=3)
print(dec)
