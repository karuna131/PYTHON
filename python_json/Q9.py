import json
d={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
user1=input("enter what you want from this list : ") 
user2=int(input("Enter the quantity of  "))

for i in d:
    
    for j in d[i]:
        if user1==j:
            x=user2*int(d[i][j])
            print(x)
d[i].pop(user1)  
user=input("Enter a item : ")
ask=input("Enter value :")
d[i][user]=ask

with open("Q9.json","w") as h:
    f=json.dump(d,h,indent=4)
    print(f)







