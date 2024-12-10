 #static method means with out create the object we call the method with class name.
class A:
    @staticmethod
    def sum(a,b):
        return a+b
    def sub(a,b):
        return a-b

print(A.sum(3,9))
print(A.sub(9,9))

