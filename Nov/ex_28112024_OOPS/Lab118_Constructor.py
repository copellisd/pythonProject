class dog:
    # Class attributes
    name = None
    breed = None
    height = None
    weight = None

    # Constructor
    def __init__(self):
        print("I will be called")

    # Methods
    def bark(self):
        print("Barking")

    def sleep(self):
        print("I am sleeping")

    def talk(self):
        print("I am talking")


# Creating instances
d = dog()  # Constructor will be called
r = dog()  # Constructor will be called

# Accessing attributes
print(d.name)  # None
print(r.name)  # None
