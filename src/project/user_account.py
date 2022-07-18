#User account managment
users = []

def creat_user(user_name, email, password1, password2):
    #YOUR CODE HERE
    user_name = input("Enter username: ")
    email = input("Enter email: ")
    password1 = input("Enter password1: ")
    password2 = input("Enter password2: ")

if len(users) == 0:
    users.append({
    'username' : user_name,
    'email' : email,
    'password1' : password1,
    'password2' : password2
    })

    for x in users:
        if x == email:
            return "Error - Email already exists"

    if password1 == password2:
        users.append(email)
        return "Welcome"
    else:
        return "Error - Password does not match"

def get_user(email):
    #YOUR CODE HERE
    for x in users:
        if users[x]['email'] == email:
            return users[x]['username']



def get_all_users():
    #YOUR CODE HERE



#Testing the Code

## try creating three new users and print out the results
creat_user("vina", "vina@gmail.com", "vinachen", "vinachen")
return get_user("vina@gmail.com")
## Try adding one of the three users you added and print out the results

## Try adding a new user with passwords that don't matches and print out the results

## Get the second users print out their user name and email

## Get all users and print only their user names
