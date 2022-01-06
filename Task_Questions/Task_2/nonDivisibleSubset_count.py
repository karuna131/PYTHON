def nonDivisiblesubset(S, k):
    frequncy=[0]*k
    for i in S:
        frequncy[i%k]+=1
    return (max(frequncy))
k=int(input("enter the divisor:-"))
n=int(input("enter size of list:-"))
S=[]
for i in range(0,n):
    S.append(int(input("enter the element : ")))
print()
print(nonDivisiblesubset(S,k)) 
