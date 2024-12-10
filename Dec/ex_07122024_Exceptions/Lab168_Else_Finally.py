try:
    num1=int(input("enter num1 value"))
    num2=int(input("enter num2 value"))
    result=num1/num2
except Exception  as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

else:
    print(result)

