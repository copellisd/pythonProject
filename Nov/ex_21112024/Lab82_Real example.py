import time

def time_decorator(func):

    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print("total time taken by the fun",end_time-start_time)
    return wrapper()



@time_decorator
def test_ui_1():
    print("add a function time taken by the function")
    time.sleep(2)
@time_decorator
def tets_ui_2():
    print("add a time taken by the function")
    time.sleep(5)

