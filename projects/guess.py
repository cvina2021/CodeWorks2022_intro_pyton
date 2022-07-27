#your code here
<<<<<<< HEAD
from numpy import random
again = "Yes";

while(again == "Yes"):
    rm = random.randint(11)
    user = int(input("Enter your guess"))
    if user < rm:
        print("Too Low")
    elif user > rm:
        print("Too High")
    else:
        print("Congratulations")
    again = input("Do you want to play again?")
=======
from numpy import random as rand


play = True

while play:
    rm = rand.randint(11)
    trail = 1
    guess = int(input("Guess a number between 0 and 10: "))
    while guess != rm:
        if guess > rm:
            print("your guess is bigger than the number")
        if guess < rm:
            print("your guess is smaller than the number")
        trail=trail+1
        print("Number of trials: "+str(trail))
        guess = int(input("Try again: "))

    print("You guessed right, the number is :"+ str(rm))
    num = input("Do you want to play again? (y|n): ")
    if num == 'n':
        play = False
>>>>>>> 85b7dc786a8bcbc2bc32381f6115227b7b4f17eb
