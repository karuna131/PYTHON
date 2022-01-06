li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]        #append 20 on 4th index
list1=[]
i=0
a=5
while i<len(li):
    if li[i]==a:
        list1.append(20)
        a+=4
    list1.append(li[i])
    i+=1
print(list1)




# li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]               # append 20 on second index
# list1=[]
# i=0
# while i<len(li):
#     if li[i]%2==0:
#         list1.append(20)
#     else:
#         list1.append(li[i])
# print(list1)