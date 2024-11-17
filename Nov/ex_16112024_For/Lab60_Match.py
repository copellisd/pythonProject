browser_name=input("enter browser name")
match browser_name:
    case "firefox":
        print("starting firefox")
    case  "safari":
        print("starting safari")
    case"chrome":
        print("starting chrome")
    case "edge":
        print("starting edge")
    case _:
        print("browser not found")