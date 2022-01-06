my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
li=[]                     #first way to do this question
for i in range(3):
    max=0
    for j in my_dict:
        if max<my_dict[j]:
            max=my_dict[j]
            c=j
    li.append(c)
    my_dict.pop(c)
print(li)


# li=[]                       #second way to do this
# for i in range(3):
#     max=0
#     for j in my_dict:
#         if max<my_dict[j]:
#             x=my_dict[j]
#             my_dict[j]=max
#             max=x
#             c=j
#     li.append(c)
#     my_dict.pop(c)
# print(li)


