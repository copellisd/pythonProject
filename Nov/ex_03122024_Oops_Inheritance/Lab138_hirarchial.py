#hirarchial inheritance is one father has many childs

class father:
    def bhk1(self):
        print("1bhk")

class sister(father):
    def  bhk2(self):
        print("3bhk")

class sister2(father):
    def bhk3(self):
        print("3bhk")

sister_o=sister()
print(sister_o.bhk1())
f=father()
print(f.bhk1())
