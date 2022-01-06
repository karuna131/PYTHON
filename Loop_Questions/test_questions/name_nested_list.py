li=["karuna","kittu","jaiswal"]     # write this name is nested list
li1=[]
i=0
while i<len(li):
    if li[i] not in li1:
        li1.append([li[i]]) 
    i+=1
print(li1)