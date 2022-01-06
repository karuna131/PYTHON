harshad=int(input("Enter a number : "))
c = harshad
i=0
sum = 0
while i<=harshad:
    f=harshad%10
    sum += f
    harshad//=10
    i+=1
if c%sum == 0:
    print(c,"is a Harshad number")
else:
    print(c," is Not Harshad Number")