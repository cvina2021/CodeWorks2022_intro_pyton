player ={
    'name': 'Player 1',
    'position': 0,
    'direction': 'right'
}

#Your code here
def move(user_input, speed):
    if user_input == 1:
        player['position'] -= speed
    elif user_input == 2:
        player['position'] += speed
    return player['position']

run_code = True
while run_code:
    user_input = int(input("What do you want to do?\nEnter 1 to move left\n2 to move right\n3 to exit"))
    #Your code here
    if user_input == 3:
        break;
    else:
        speed = int(input("Enter speed: "))
        print(move(user_input, speed))
