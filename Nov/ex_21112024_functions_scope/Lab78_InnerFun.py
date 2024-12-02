def outer_fun():
    var=10
    def inner_function1():
        print(var)
    def inner_function2():
        print(var)
    inner_function1()
    inner_function2()
outer_fun()