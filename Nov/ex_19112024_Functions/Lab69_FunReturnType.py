#they dont return anything

def greet():
    print("hello")
greet()

#no return type with argument

def greet_name(name):
    print("hello",name)
greet_name("datta")

#No return type with default argument

def say_hello_default_arg(name="preksha"):
    print("hello",name.upper())
say_hello_default_arg("datta")
say_hello_default_arg()

#multiple arguments

def mul_arg(name1="A",name2="B"):
    print("mul->",name1,name2)

mul_arg()
mul_arg("preksha","sri")
mul_arg("sree")

#Arguments n Return Type

def sum_of_two(a,b):
         return a+b
result=sum_of_two(5,99)
print("sum is",result)



