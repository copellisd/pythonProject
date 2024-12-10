class parent:
    
    def home(self):
        print("1bhk")
        
class child(parent):
    
    def town(self):
        print("2bhk")

    def home(self):
        print("child home")

c=child()
c.home()
c.town()

