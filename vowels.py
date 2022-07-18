<<<<<<< HEAD
user = input("Enter word: ")
output = ""

for x in user:
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        continue
    output = output + x
print(output)
=======
word = input("Enter a word")
word2 = ''
for letter in word:
    if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
        word2 = word2+letter

print(word2)
>>>>>>> 1d516f57a50856cbdffe5dd8b383657a76c748c6
