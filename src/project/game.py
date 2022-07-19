player ={
    'name': 'Player 1',
    'position': 0,
    'direction': 'right'
}

#Your code here
<<<<<<< HEAD
def move(user_input, speed):
    if user_input == 1:
        player['position'] -= speed
    elif user_input == 2:
        player['position'] += speed
    return player['position']
=======
def move(speed):
    player['position'] = player['position'] + speed

    return player['position']







>>>>>>> a7fe24fe685caec56fe6947234844f7126e87ed9

run_code = True
while run_code:
    user_input = int(input("What do you want to do?\nEnter 1 to move left\n2 to move right\n3 to exit"))
    #Your code here
<<<<<<< HEAD
    if user_input == 3:
        break;
    else:
        speed = int(input("Enter speed: "))
        print(move(user_input, speed))
=======
    if user_input == 1:
        user_input = int(input("How fast to the left?"))
        print("Updated Position:"+ str(move(user_input)))

    elif user_input == 3:
            print("Good Bye!")
            run_code = False
>>>>>>> a7fe24fe685caec56fe6947234844f7126e87ed9
