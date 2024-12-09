#OVerriding
#overriding the method
class father:

    def home(self):
        print("1 bhk")

class sruthi(father):

    def home(self):
        print("3bhk")

s=sruthi()
s.home() #prints local method first.here we create object for sruthi.so that  method executs.

f=father()
f.home()