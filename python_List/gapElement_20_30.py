li=[1,2,3,4,5,6,7,8,9,10]
i=0
a=3
a2=5
li2=[]
while i<len(li):
    if li[i]==a:
        li2.append(20)
        a+=4
    if li[i]==a2:
        li2.append(30)
        a2+=4
    li2.append(li[i])
    i+=1
print(li2)