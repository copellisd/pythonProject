#grade calculator
score=int(input("enter score value"))
if(score>=90 and score<=100):
    print("your grade is ","A")
elif(score>=80 and score<=89 ):
    print("your grade is","B")
elif(score>=70 and score<=79):
    print("your grade is","C")
elif(score>=60 and score<=69):
    print("your grade is ","D")
elif(score>=100):
    print("you are superman you cant get a grade")
else:
    print("your grade is ","F")
