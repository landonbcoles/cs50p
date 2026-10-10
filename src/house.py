name = input("What is your name? ").lower()

match name:
    case "harry" | "hermione" | "ron":
        print("Griffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")
