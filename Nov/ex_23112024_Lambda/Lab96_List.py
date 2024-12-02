#list of items or collection of items
my_list=[1,2,3]
my_list1=[2,"datta","true",12.34] #diff datatypes are allowed
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
#print(my_list[3])
#reassign the values to the  old list
my_list[0]="datta"
my_list[1]="datta1"
my_list[2]="saibaba"
print(my_list)

print("--------------")
for item in my_list1:
    print(item)