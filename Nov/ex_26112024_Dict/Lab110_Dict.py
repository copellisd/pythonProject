#dictionary from two lists
key = ["name", "role", "exp"]
value = ["aa", "mt", 9]
my_dict = dict(zip(key, value))
print(my_dict)

#merge two dictionaries

dict1={"a:1,b:2"}
dict2={"c:3,d:4"}
dict=dict1 | dict2
print(dict)
