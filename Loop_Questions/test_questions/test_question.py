# a={"karuna":29,"priyanka":26,"minaksi":16}            
# for i in a:
#     print(a[i])




# import json
# # a={"karuna":29,"priyanka":26,"minaksi":16}  
# with open("data.json","r") as information:
#     b=json.load(information)
#     print(b)




# a=[10,20,30,40] 
# b=[100,200,300,400]
# i=0
# while i<=len(a):
#     print(a[i],b[-i+(-1)])
#     i+=1




# number=int(input("Enter any number : ")) 
# sum=0
# i=0
# while i<=number:
#     a=number%10
#     c=a//10
#     sum=a+c
#     i=i+1
# print(sum)




# limit=int(input("Enter limit : "))
# i=0
# d={}
# while i<limit:
#     key_user=input("Enter any key name : ")
#     value_user=input("Enter your age : ")
#     d.update({key_user:value_user})
#     print(d)
#     i+=1


# a={"priyanka":13,"karuna":12,"navin":15,"supriya":1}
# d={}
# for i in range(len(a)):
#     max=0
#     for j in a:
#         if max<a[j]:
#             max=a[j]
#             c=j
#     d.update({c:max})
#     a.pop(c)
# print(d)





# limit=int(input("Enter limit : "))
# li=[]
# i=0
# while i<limit:
#     input_number=int(input("Enter any number : "))
#     li.append(input_number)
#     j=0
#     li2=[]
#     while j<len(li):
#         k=0
#         while k<len(li):
#             l=0
#             while l<len(li):
#                 list_1=[li[j],li[k],li[l]]
#                 li2.append(list_1)
#                 l+=1
#             k+=1
#         j+=1
#     i+=1
# print(li2)




# a=[1,2,2]
# b=[]
# i=0
# while i<len(a):
#     b2=[]
#     j=0
#     while j<a[i]:
#         if a[j] not in b2:
#             b2.append(a[j])
#         j+=1
#     b.append(b2)
#     i+=1
# print(b)





# a=[1,2,2]
# b=[]
# for i in range(len(a)+1):
#     for j in a:               #some error is there
#         b.append(a[j:i])
# print(b)



# a=[1,2[3,4,5],[3,4,5],4,[6,7]]   #this is wrong expration
# print(a[0])

# a=[1,2,[3,4,5],[3,4,5],4,[6,7]]   #this is right expration
# print(a[0])




