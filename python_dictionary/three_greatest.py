my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }

li=[]
for i in range(3):
    max=0
    for j in my_dict:
        if my_dict[j]>max:
            a=my_dict[j]
            my_dict[j]=max
            max=a
    #print(max)
    li.append(max)
print(li)

    


