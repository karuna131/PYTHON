import json
s="Name Abhishek Designation CEO,of,navgurukul Gender male Age 29"
x=s.split()
d={}
#print(x)
for i in range(0,len(x),2):
    d.update({x[i]:x[i-7]})
print(d)
with open("Q7.json","w") as h:
    f=json.dump(d,h, indent=4)
    print(f)

