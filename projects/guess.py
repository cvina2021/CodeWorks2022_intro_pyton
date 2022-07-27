#your code here
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
