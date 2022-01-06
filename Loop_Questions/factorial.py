# fact=int(input("Enter a number : "))
# i=1
# sum=1
# while i<=fact:
#     sum=sum*i   
#     i+=1
# print(sum)





randomName=input("Enter a name")
change_In_list=list(randomName)
i=0
j=1
str1=''
str=''
while i<len(change_In_list):
    str1=str1+change_In_list[i]
    k=len(change_In_list)-j
    if change_In_list[k]==change_In_list[i]:
        str=str+change_In_list[k]
    
    j+=1
    i+=1

if str==str1:
    print("This is palindrom")

else:
    print("This is not palindrom")
