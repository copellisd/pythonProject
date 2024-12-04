a=10
class person:
    b=20 #instance variable belongs to class
    def print_function(self):
           c=30  #local variable
           print(c)
           print(self.b)
           a="hello"
           print(a)
person_ref=person()
print(person_ref.print_function())