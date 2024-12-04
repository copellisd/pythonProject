class car:

    def __init__(self):
        self.password="pramod"  #public instanc e variable
        self.__password_secure="12345"#thi 2 underscore symbol is for showing the privateinst,var

    def change_pwd(self):
        self.__password_secure="546"

c=car()
print(c.password)
print(c.__password_secure)