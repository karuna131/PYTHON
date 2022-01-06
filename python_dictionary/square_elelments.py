
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


user=int(input("enter limit of keys  : "))
d={}
for i in range(1, user+1):
    x=i**2
    d[i]=x
print(d)