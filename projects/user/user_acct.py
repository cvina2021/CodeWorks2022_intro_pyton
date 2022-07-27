import json

users = {}

def loadfile():
    try:
        with open("users.json") as file:
            jsonString = json.load(file)
            print(jsonString)
            users.update(jsonString)
            print("File loaded to program")
            print(users)
    except:
        print("File could not be found")


def createUser(name, email, password1, password2):
    #your code here
    if email not in users:
        if password1 == password2:
            user.update({
               email: {
                 'name': name,
                 'password': 'Password'
               }
             })
            print("Welcome " + name + "!\n\n")
        else:
            print("Error : the passwords do not match \n\n")
    else:
        print("Error: user with this email already exist\n\n")

def signIn(email, password):
    #your code here
    if email in users:
        if password == users[email]['password']:
            print("Welcome\n\n")
            return True
        else:
            print("Password did not match\n\n")
            return False
    else:
        print("No Email Found\n\n")
        return False

def changePassword(email, CurrentPassword, newPassword):
    #your code here
    if signIn(email, CurrentPassword) == True:
        users[email]['password'] = newPassword
        print("Password Updated\n\n")
    else:
        print("Error\n\n")

def updateFile():
    #your code here
    with open("users.json", 'w') as file:
        jsonString = json.dump(users, file)
