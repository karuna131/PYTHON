dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
d={}
for i in dict:
    for j in dict:
        if dict[i]<dict[j]:
            c=dict[i]
            dict[i]=dict[j]
            dict[j]=c
            y=j
#print(dict)
dict.update({y:dict[j]})
    #dict.pop(c)
print(dict)