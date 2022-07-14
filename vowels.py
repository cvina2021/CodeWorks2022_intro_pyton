user = input("Enter word: ")
output = ""

for x in user:
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        continue
    output = output + x
print(output)
