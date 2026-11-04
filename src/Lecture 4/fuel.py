def main():
    while True:
        try:
            value = input("Fraction: ")
            n, d = value.split("/")
            z  = ((int(n)/int(d))*100)
            if z < 1:
                print("E")
            elif z > 99:
                print("F")
            else:
                print(int(z), end="")
                print("%")
            break
        except (ValueError, ZeroDivisionError):
            pass

main()