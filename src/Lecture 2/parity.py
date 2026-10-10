def main():
    x = int(input("What's X? "))
    if isEven(x):
        print("The number is even.")
    else:
        print("The number is odd.")


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False



main()