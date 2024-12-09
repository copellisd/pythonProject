class calc:
    def add(self,*args):
        for a in args:
            print(a)

c=calc()
c.add(1,2)
c.add(1,2,9)
c.add(9,9,9,9)