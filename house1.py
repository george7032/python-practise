name = input("Enter your name: ")

match name:
    case "brian":
        print("Room 1")
    case _:
        print("No Room!")
