#parameterized constructor

class dog:
    # Class attributes
    name = None
    breed = None
    height = None
    weight = None

    # Constructor
    def __init__(self,name,breed):
        print("I will be called")
        self.name=name
        self.breed=breed

    # Methods
    def bark(self):
        print("Barking")

    def sleep(self):
        print("I am sleeping")

    def talk(self):
        print("I am talking")


# Creating instances
d = dog("aa","mustin")  # Constructor will be called
r = dog("bb","herd")  # Constructor will be called

# Accessing attributes
print(d.name)
print(id(d))# None
print(r.name)  # None
print(id(r))