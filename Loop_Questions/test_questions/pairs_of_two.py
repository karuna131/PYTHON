li=[1,2,3]            # we are creating here posible pairs
i=0
list1=[]
while i<len(li):
    j=0
    while j<len(li):
        l=li[i],li[j]
        list1.append(l)
        j+=1
    i+=1
print(list1)