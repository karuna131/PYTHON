d= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	    3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
del d[3]['A']
print(d)




people = {1: {'Name': 'kavi', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'meetu', 'Age': '22', 'Sex': 'Female'}}

for id, info in people.items():
    print("Person ID:", id)
    
    for key in info:
        print(key + ':', info[key])