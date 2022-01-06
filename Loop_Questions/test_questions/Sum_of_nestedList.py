li=[[1,2,3,4],[5,6,7],[8,9,10]]
i=0
while i<len(li):
    j=0
    sum=0
    while j<len(li):
        sum=li[i]+li[j]
        print(sum)
        j+=1
    i+=1