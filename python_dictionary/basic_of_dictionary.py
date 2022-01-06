# student = {"name":"kavi", "age":20, "course":["maths","pysics"]}
# print(student["name"])
# print(student["course"][0])
# print(student["age"])



#get method

student = {"name":"kavi", "age":20, "course":["maths","pysics"]}

#student['phone'] = '86737777235263'
print(student.get('phone', 989878374738))



# city_population = {"Chicago":2720546, "NewYorkCity":8550405, "Boston":667137}
# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))


#case sensitive hoti he

Dict = {'ball':'green', 'Ball':'red'}
print(Dict['ball'])
print(Dict['Ball'])
#print(Dict['bat']) #keyError


#dict() function (dictionary me convert kr dega)

student = dict(name = "Ravina", age=20)
print(student)


# key hamesha unique hoti hai
my_dict = {1:'apple', 2:'ball'}
print(my_dict)



#dictionary with mixed keys

mixed = {'name':'john', 1:[2,4,3]}
print(mixed)


#nested Dictionary

Dic = {1:'NAVGURUKUL', 2:'IN', 3:{'A':'WELCOME', 'B':'To', 'C':'PUNE CAMPUS'}}
print(Dic)
print(Dic[3]['A'])
print(Dic[3]['A'],Dic[3]['B'],Dic[3]['C'])


person = {'name':'jack',  'age':20,  'gender':'male',   4:'organisation'}
result = person['age']
print(result)
x=person.get("bone", 1500)
print(x)



student={'name': 'karuna', 'age':20, 'college':'SSISM'}
for value in student.items():
    print(value, end=" ")


std={'place': "bhopal" , "address":123}
for key, value in std.items():
    print(key, value)
