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
same_Email = False
for user in users:
    if user[email] == email:
        same_Email = True
        return
    else:
        same_Email = False
if same_Email == False:
    if password1 == password2:
         user.update({
            email: {
              'name': name,
              'password': 'Password'
            }
          })
    else:
        return

def signIn(email, password):
    #your code here

def changePassword(email, CurrentPassword, newPassword):
    #your code here

def updateFile():
    #your code here
