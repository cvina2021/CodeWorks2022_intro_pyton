correctPass = "python"

i = 0
while i < 3:
    user = input("Enter password: ")
    if (user == correctPass):
        print("Welcome")
        break;
    else:
        print("Error")
        i = i + 1
