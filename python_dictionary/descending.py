dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
d={}
for i in range(len(dict)):
    max=0
    for j in dict:
        if max<dict[j]:
            max=dict[j]
            c=j
    d.update({c:max})
    dict.pop(c)
print(d)






