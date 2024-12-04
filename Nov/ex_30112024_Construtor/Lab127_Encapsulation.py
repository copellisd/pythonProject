class car:
     def __init__(self,o_name,o_make,o_model):
         self.name=o_name
         self.make=o_make
         self.model=o_model
     def start_engine(self):
        print("starting a car with the name is " + self.name)
        print("starting a car with the make " + self.make)
        print("starting a car withe model " + self.model)

lambo=car("lamborgini","dat","2023")
lambo.start_engine()
print("..............")
mg_hector=car("hector","game","2025")
mg_hector.start_engine()