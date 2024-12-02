def add_security(func):
     def wrapper():
          print("before running a scooty")
          print("wear helmets,gloves,dash,license")
          func()
          print("after driving a  scooty")
          print("secure driving")

     return wrapper()
@add_security
def drive_ola():
    print("ola")

@add_security
def driving_scooty():
    print("npraml function")
    print("Iam a driving a scooty")