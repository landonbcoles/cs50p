greeting = input("Greeting: ").strip().lower()

if greeting.startswith("h"):
    if greeting == "hello":
        print("$0")
    else:
        print("$20")
else:
    print("$100")