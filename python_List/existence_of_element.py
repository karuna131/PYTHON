li = ['a','b','c','a','d','e','d','b','f','g','c','a','f','d','e','b','a']
i = 0 
li2 = []
while i<len(li):
    if li[i] not in li2:
        li2.append(li[i])
        # li2.append(i)
    i+=1
print(li2)