import json
d=[["neelam","programer","24","2400",],["komal","trainer","24","20000"],["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"]]
li=["name","Designation","Age","salary"]
dic={}
for i in range(0, len(d)):
    for j in range(0, len(d)):
        dic.update({li[j]:d[i][j]})
    #print(dic)
dic1={}
for i in range(0,4):
    user=input("enter keys : ")
    dic1.update({user:dic})
print(dic1)
with open("Q8.json","w") as dict2:
    final=json.dump(dic1,dict2,indent=4)
    print(final)