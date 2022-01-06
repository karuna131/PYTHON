li=[1,2,3]          # we are creating here posibale pairs
i=0
list1=[]
while i<len(li):
    j=0
    while j<len(li):
        k=0
        while k<len(li):
            l=li[i],li[j],li[k]
            list1.append(l)
            k+=1
        j+=1
    i+=1
print(list1)