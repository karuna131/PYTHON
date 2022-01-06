n=int(input("Enter lenth of dictionary  : "))
d = {}
for i in range(n):
    keys = input("enter key name : ")
    values = int(input("enter key values : "))
    d[keys] = values
print(d)