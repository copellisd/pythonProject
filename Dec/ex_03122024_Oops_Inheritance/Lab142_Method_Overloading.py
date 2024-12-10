
 #Method overloading not supported in python
 #with the default parameters is possible.
 class math:

    def add(self,a=1,b=1):
        return a+b

    def add(self,a=1,b=1,c=1):
        return a+b+c

m=math()
print(m.add(3,5))
print(m.add(3,5,6))
