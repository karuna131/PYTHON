import json
d={"name": "David",
     "class":"I",
     "age": 6  
 }
f=json.dumps(d)
print(f)


#for file

# address=open("Q2.json","w")
# json.dump(d,address,indent=4)
# address.close()



# with open("Q3.json","w") as h:
#     f=json.dump(d,h,indent=4)
#     print(f)