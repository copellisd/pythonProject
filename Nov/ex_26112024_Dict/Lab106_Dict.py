my_dict={"name":"datta",#dict is same as map in java.key value pair.accessed with key value.it
         "age":99,      #it shoild should show  with {}
        "role":"SDET",
         "exp":3}

print(my_dict["name"])

#adding/deleting
my_dict["role"]="manual tester"
print(my_dict)
del(my_dict["age"])
print(my_dict)

for key,value in my_dict.items():
    print(key,value)
