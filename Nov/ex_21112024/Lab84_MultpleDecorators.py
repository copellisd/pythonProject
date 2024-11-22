def decor_1(func):
     def wrapper():
         print("decor1")
         func()
         print("hi")
     return wrapper()
def decor_2(func):
    def wrapper():
        print("decor2")
        func()
        print("hello")
    return wrapper()
@decor_1
@decor_2
def say_hello():
    print("datta")