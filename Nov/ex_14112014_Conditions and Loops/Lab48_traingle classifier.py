side1=int(input("enter side1 value"))
side2=int(input("enter side2 value"))
side3=int(input("enter side3 value"))
if(side1==side2 and side2==side3):
    print("equaliteral traingle")
elif(side1==side2 or side2==side3 or side1==side3):
    print("isoceles traingle")
else:
    print("scalene traingle")