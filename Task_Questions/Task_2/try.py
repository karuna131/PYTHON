# def nonDivisiblesubset(limitOfElements,Numbers):
#     k=3
#     i = 0
#     count=0
#     a=[]
#     while i<limitOfElements:
#         j=i+1
#         while j<limitOfElements:
#             sum = Numbers[i]+Numbers[j]
#             # print(sum)
#             if sum%k!=0:
#                 if Numbers[i] not in a:
#                     a.append(Numbers[i])
#                     print(a)
#                     count+=1
#             j+=1
#         i+=1
#     print(count)

# sizeOfElements=int(input('Enter limit number : '))
# Nuber_of_elements=[]
# for i in range(0, sizeOfElements):
#     input_numbers=int(input('Enter numbers according to limit : '))
#     Nuber_of_elements.append(input_numbers)
# nonDivisiblesubset(sizeOfElements,Nuber_of_elements)








# def nonDivisiblesubset(limitOfElements,Numbers,k):
#     i = 0
#     count=0
#     a=[]
#     while i<limitOfElements:
#         j=i+1
#         while j<limitOfElements:
#             sum = Numbers[i]+Numbers[j]
#             # print(sum)
#             if sum%k!=0:
#                 if Numbers[i] not in a:
#                     a.append(Numbers[i])
#                     print(a)
#                     count+=1
#             j+=1 
#         i+=1
#     for m in range(0,limitOfElements):
#         for l in range(0,limitOfElements):
#             if Numbers[m]==Numbers[-1]:
#                 sum=Numbers[-1]+Numbers[m]
#                 if sum%k!=0:
#                     if Numbers[-1] not in a:
#                         a.append(Numbers[-1])
#                         print(a)
#                         count+=1
#     print(count)

# sizeOfElements=int(input('Enter limit number : '))
# Nuber_of_elements=[]
# for i in range(0, sizeOfElements):
#     input_numbers=int(input('Enter numbers according to limit : '))
#     Nuber_of_elements.append(input_numbers)
# divider = int(input('Enter divider\'s  value : '))
# nonDivisiblesubset(sizeOfElements,Nuber_of_elements,divider)












# def nonDivisiblesubset(limitOfElements,Numbers,k):
#     a = [0]*k
#     for i in range(0, len(Numbers)):
#         a[Numbers[i]%k]+=1
#     c=max(a)
#     print(c)

# sizeOfElements=int(input('Enter limit number : '))
# Nuber_of_elements=[]
# for i in range(0, sizeOfElements):
#     input_numbers=int(input('Enter numbers according to limit : '))
#     Nuber_of_elements.append(input_numbers)
# divider = int(input('Enter divider\'s  value : '))
# nonDivisiblesubset(sizeOfElements,Nuber_of_elements,divider)







# def nonDivisiblesubset(limitOfElements,Numbers,k):
#     a = [0]*k
#     b=[]
#     count=0
#     for i in range(0, len(Numbers)):
#         a[Numbers[i]%k]+=1
#         for j in range(i+1, len(Numbers)):
#             sum = Numbers[i]+Numbers[j]
#             if sum%k!=0:
#                 if Numbers[i] not in b:
#                     b.append(Numbers[i])
#                     # print(b)
#                     count+=1
#     for m in range(0,len(Numbers)):
#         for l in range(0,len(Numbers)):
#             if Numbers[m]==Numbers[-1]:
#                 sum=Numbers[-1]+Numbers[m]
#                 if sum%k!=0:
#                     if Numbers[-1] not in b:
#                         b.append(Numbers[-1])
#                         # print(b)
#                         count+=1
#     c=max(a)
#     print(b)
#     print(c)

# sizeOfElements=int(input('Enter limit number : '))
# Nuber_of_elements=[]
# for i in range(0, sizeOfElements):
#     input_numbers=int(input('Enter numbers according to limit : '))
#     Nuber_of_elements.append(input_numbers)
# divider = int(input('Enter divider\'s  value : '))
# nonDivisiblesubset(sizeOfElements,Nuber_of_elements,divider)








# def nonDivisiblesubset(Numbers,k):
#     a = [0]*k
#     b=[]
#     count=0
#     for i in range(0, len(Numbers)):
#         a[Numbers[i]%k]+=1
#         for j in range(i+1, len(Numbers)):
#             sum = Numbers[i]+Numbers[j]
#             if sum%k!=0:
#                 if Numbers[i] not in b:
#                     b.append(Numbers[i])
#                     # print(b)
#                     count+=1
#     for m in range(0,len(Numbers)):
#         for l in range(0,len(Numbers)):
#             if Numbers[m]==Numbers[-1]:
#                 sum=Numbers[-1]+Numbers[m]
#                 if sum%k!=0:
#                     if Numbers[-1] not in b:
#                         b.append(Numbers[-1])
#                         # print(b)
#                         count+=1
#     f=[]
#     count_=0
#     for i in range(0,len(b)):
#         for j in range(0,len(b)):
#             sum = b[i]+b[j]
#             # print(sum)
#             if sum%k!=0:
#                 if b[i] not in f:
#                     f.append(b[i])
#                     count_+=1
#     for m in range(0,len(b)):
#         for l in range(0,len(b)):
#             if b[m]==b[-1]:
#                 sum=b[-1]+b[m]
#                 if sum%k!=0:
#                     if b[-1] not in f:
#                         f.append(b[-1])
#                         # print(a)
#                         count_+=1
     
#     print(f)
    
#     c=max(a)
#     # print(b)
#     print(c)

# sizeOfElements=int(input('Enter limit number : '))
# Nuber_of_elements=[]
# for i in range(0, sizeOfElements):
#     input_numbers=int(input('Enter numbers according to limit : '))
#     Nuber_of_elements.append(input_numbers)
# divider = int(input('Enter divider\'s  value : '))
# nonDivisiblesubset(Nuber_of_elements,divider)