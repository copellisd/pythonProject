class calc:
    def __init__(self):
        print("i will be")

    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

c=calc()
print(c.sum(2,3))
print(c.mul(2,3))
print(c.sub(4,2))
print(c.div(6,2))

