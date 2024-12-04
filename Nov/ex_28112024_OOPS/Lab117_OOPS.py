class person:
    #attributes
   id=None
   name=None
   age=None
   email=None
   height=None
   gender=None
   phno=None
   Address=None

# behaviour
def talk(self):#no arg no return
   print("iam talking")

def sleep(self,name):  #no return with arg
   print("iam  a method")
   print("sleep",name)
def sleep2(self,name):#arg with return
      print("am in sleep")
      return None
def walk(self):
      print("am walking")
def walk_return(self):#no arg with return
      return "am walking"

#create a object of a class

geetha=person()
geetha.name="geetha sharma"
geetha.age=99


