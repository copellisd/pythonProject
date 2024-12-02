

my_list=[1,2,3]
print(my_list[0])
print(my_list[1])
print(my_list[2])

my_list.append(4)    #append is add at the en nd of the file
print(my_list)

my_list.extend([9,8,9])
print(my_list)
my_list.insert(1,"datta")
print( my_list)
print(len(my_list))
my_list[2]="bad"
print(my_list)

my_list.remove("bad")
print(my_list)

my_list_copy=my_list.copy()
print(my_list)
print(my_list_copy)
