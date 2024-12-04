class vwo:
    def __init__(self,email,pwd):
        self.email=email
        self.pwd=pwd
    def login(self):
        if self.email=="sruthi.spr13@gmail.com" and self.pwd=="12345":
            print("log in successful")
        else:
            print("log in not successful")

 #e=input("enter email address") this is user input pattern
#p=input("enter pwd ")
#vwo_ref=vwo("email","pwd")
#vwo_ref.login()

vwo_ref=vwo("sruthi.spr13@gmail.com","12345")
vwo_ref.login()