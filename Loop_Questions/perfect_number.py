perfect_no=int(input("check a number is perfect or not : "))
i=1
sum=0
while i<perfect_no:
    if perfect_no%i==0:
        sum+=i
    i+=1
if sum==perfect_no:
    print(perfect_no, "is a perfect number ")
else:
    print(perfect_no, "is not a perfect number ")