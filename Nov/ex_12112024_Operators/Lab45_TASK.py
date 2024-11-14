num1 = int(input("pls enter num1\n"))
num2 = int(input("pls enter num2\n"))

if(num1 > num2):
    print(f"num1 is greater:{num1}")
else:
    print(f"num2 is greater:{num2}")

print("-------")

print(f"num1 is greater:{num1}" if num1 > num2 else f"num2 is greater:{num2}")