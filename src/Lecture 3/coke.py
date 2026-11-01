amountDue = 50
change = 0
while True:
    print("Amount Due: ", end="")
    print(amountDue)
    paid = int(input("Insert Coin: "))

    if paid/25 == 1 or paid/10 == 1 or paid/5 == 1:
        amountDue = amountDue - paid
        if amountDue <= 0:
            change = abs(amountDue)
            print("Change Owed: ", end="")
            print(change)
            break
        

    


