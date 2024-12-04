class person:
    def __init__(self):
        print("i will be called")
        self.name=input("enter the name")
        self.age=input("enter age value")
        self.phone=input("enter phno ")
        self.occupation=input("enter occupation")

    def name_of_the_dispaly(self):
        print(f"name is {self.name}",f"age is {self.age}",f"phone is {self.phone}",f"occupation is{self.occupation}")


person1=person()
print(person1.name_of_the_dispaly())