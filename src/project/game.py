#define the class
class Character:
    #define the class variables
    characters = []

    #define the the init function
    def __init__(name):
        #your code here
        name = name
        level = 0
        lives = 3
        position = 0


    #add the methods
    def move(speed):
        #your code here
        position += speed
        return position

    def level_up():
        #your code here
        level += 1
        return level

    def kill():
        #your code here
        lives -= 1
        return lives

    def bonus():
        #your code here
        lives += 1
        return lives

#create 4 instance of this class and test all the methods
c1 = Character("flow")
print(c1.move(+1))
