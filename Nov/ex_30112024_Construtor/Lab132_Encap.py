class home:
    def __init__(self):
        self.public_var="father"
        self.__private_var="child"

    def mom(self):
        print(self.public_var)
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("private wife")


h=home()
h.mom()
print(h.public_var)
#print(h.__private_var)h is ref obj ie out side object.so we cant access private variable.
#mom function is public function and with in class so it can access bot h public n private.
#ex:above mom function

#h.__wife() this is not access because wife is private.
