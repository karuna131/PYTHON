






#In while loop
i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ", end=" ")
        b+=1
    c=1
    while c<=i:                                         
        print("*", end=" ")                                      
        c+=1                                                   
    d=i-1                                                       
    while d>0:
        print("*", end=" ")
        d=d-1
    print()
    i+=1





# In for loop
for i in range(1,6):
    for b in range(5-i):
        print(" ", end=" ")
    for c in range(i):
        print("*", end=" ")
    for d in range(0,i-1):
        print("*", end=" ")
    print()