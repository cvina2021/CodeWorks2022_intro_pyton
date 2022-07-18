<<<<<<< HEAD
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
=======
password = "Password123"
trial = 3

while trial > 0:
    user_password = input("Please enter your password: ")
    if user_password == password:
        print("Welcome User")
        break

    else:
        print("Error: Password incorect")
        trial = trial - 1
>>>>>>> 1d516f57a50856cbdffe5dd8b383657a76c748c6
