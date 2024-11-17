for i in range(1,100):
    print("Value",i)

    if (i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")

    elif (i % 3 == 0):
        print("fizz")

    elif (i % 5 == 0):
        print("buzz")
    else:
        print("none")