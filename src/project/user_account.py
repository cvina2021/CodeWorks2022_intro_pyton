#User account managment
users = []
def creat_user(user_name, email, password1, password2):
    #YOUR CODE HERE
    for x in users:
        if x['email'] == email:
            return "Error - Email already exists"

    if password1 == password2:
        users.append({
        'username' : user_name,
        'email' : email,
        'password1' : password1,
        'password2' : password2
        })
        return "Welcome"
    else:
        return "Error - Password does not match"

def get_user(email):
    #YOUR CODE HERE
    for x in users:
        if x['email'] == email:
            return x['username']



def get_all_users():
    #YOUR CODE HERE
    allusers = []
    for x in users:
        allusers.append(x['username'])
    return allusers


#Testing the Code

## try creating three new users and print out the results
print(creat_user("vina", "vina@gmail.com", "vinachen", "vinachen"))
print(creat_user("laura", "laura@gmail.com", "llc", "llc"))
print(creat_user("evan", "evan@gmail.com", "evanhey", "evanhey"))

## Try adding one of the three users you added and print out the results
print(creat_user("laura", "laura@gmail.com", "llc", "llc"))
## Try adding a new user with passwords that don't matches and print out the results
print(creat_user("henry", "henry@gmail.com", "henrybye", "henryhey"))
## Get the second users print out their user name and email
email = "laura@gmail.com"
print(get_user(email))
print(email)
## Get all users and print only their user names
print(get_all_users())
