class xyz:
    def f1(self):
        try:
            a=int(input("enter a value"))
        except Exception as e:
            print("enter only int value")

        else:
            print(a)
        finally:
            print("any how executed")

x_ref=xyz()
x_ref.f1()