pb_global=10   #global variable

def my_function():
    pb_local=12   #local variable
    print(pb_local)
    print(pb_global)

#print(pb_local) #out of the function local not defined
print(pb_global) #global accepted
my_function()