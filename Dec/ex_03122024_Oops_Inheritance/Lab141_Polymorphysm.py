#polymorphism
#method overloading

class dog:

    def bark(self):
        print("dog is barking")

    def  bark(self,breed):
        print(f"dog with {breed}is barking")

d=dog()
print(d.bark())