class a:
    def method(self):
        return "method a"

class b:
    def method(self):
        return "method b"


class c(b,a):
    pass

c_obj=c()
print(c_obj.method())

