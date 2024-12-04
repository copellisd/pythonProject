count=0 #global variable

def increment():
    global count #this way we can define global var in class
    count=count+1

increment()
increment()
increment()
increment()
print(count)