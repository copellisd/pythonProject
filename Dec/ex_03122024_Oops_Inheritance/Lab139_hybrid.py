#hybrid inheritance
#multiple types of inheritance
#such as multiple,multilevel,hirarchial

class a:
    def methoda(self):
        return "method a"

class b(a):
    def methodb(self):
        return  "method b"

class c(a):
    def methodc(self):
        return "method c"

class d(b,c):
    def methodd(self):
        return "method d"

d_obj=d()
print(d_obj.methodc())
print(d_obj.methodb())
print(d_obj.methoda())
print(d_obj.methodd())