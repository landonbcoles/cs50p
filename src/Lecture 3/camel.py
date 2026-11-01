words = input("camelCase: ")
length = int(words.count("") - 1)

sentence = ""

for i in range(length):
    if words[i].isupper():
        sentence = sentence + "_" + words[i].lower()
    else:
        sentence = sentence + words[i]

print("snake_case: " + sentence)
