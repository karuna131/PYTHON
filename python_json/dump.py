import simplejson
dict1 ={

    "emp1": {

        "name": "Lisa",

        "designation": "programmer",

        "age": "34",

        "salary": "54000"

    },

    "emp2": {

        "name": "Elis",

        "designation": "Trainee",

        "age": "24",

        "salary": "40000"

    },

}
out_file = open("dump.json", "w") 


simplejson.dump(dict1, out_file, indent = 6)


out_file.close()