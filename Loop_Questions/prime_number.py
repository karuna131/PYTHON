num=int(input("Enter a number : "))
i=2
while i<num:
    if num%i==0:
        print(num, "is not prime")
        break
    i+=1
else:
    print(num,"is prime")