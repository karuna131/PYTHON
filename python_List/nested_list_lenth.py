#length of nested list
a=[1,2,[3,4,5],7,[6,7,8],9,10]
i=0
count=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            count+=1
            j+=1
    else:
        count+=1
    i+=1
print(count)