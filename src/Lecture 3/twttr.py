sentence = input("Input: ") 
length = int(sentence.count("") - 1)
vowels = set("aeiouAEIOU")
words = ""

for i in range(length):
    if sentence[i].lower() not in vowels:
        words = words + sentence[i]

print("Output: " + words)