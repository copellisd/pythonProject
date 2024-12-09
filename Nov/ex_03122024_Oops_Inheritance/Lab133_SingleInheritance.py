#Single Inheritance

class father:
     key="2bhk"
     def car(self):
         print("father  has car is ->Alto")
         print(self.key)

class son(father):
    key="3bhk"
    def suv(self):
       print("mg hector is ->black")
       print(self.key)

father_obj=father()
father_obj.car()

son_obj=son()
son_obj.suv()

son_obj.car()

