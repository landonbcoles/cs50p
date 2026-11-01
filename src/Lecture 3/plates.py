
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numbers = set("0123456789")
    firstNum = False
    recentNum = False
    vanity = ""
    if int(s.count("") - 1) >= 7 or int(s.count("") - 1) <= 2:
        print("1")
        return False
    else:
        for i in range(int(s.count("") - 1)):
            if s[i].isalnum() != True not in numbers:
                print("2")
                return False
            elif s[i] in numbers:
                if firstNum == False and s[i] == 0:
                    print("3")
                    return False
                else:
                    firstNum = True
                    recentNum = True
                    vanity += s[i]
            if s[i] not in numbers and recentNum == True:
                print("4")
                return False
            else:
                vanity += s[i]
        return True
    



main()