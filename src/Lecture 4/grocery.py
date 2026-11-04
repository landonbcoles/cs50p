list = {}

while True:
    try:
        item = input("item: ").upper()
    except EOFError:
        break

    if item in list:
        list [item] += 1
    else:
        list [item] = 1

for i in sorted(list):
    print(list[i], i)