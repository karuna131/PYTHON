# table of 2
i=2
limit=1
while limit<=10:
    print(i)
    i+=2
    limit+=1


#table of 2
i=2
count=1
while count<=10:
    s=count*i
    print(count,"*",i,"=",s)
    count+=1



#we print any table by use input
table=int(input("Enter any table number : "))
count=1
while count<=10:
    s=count*table
    print(count,"*",table,"=",s)
    count+=1