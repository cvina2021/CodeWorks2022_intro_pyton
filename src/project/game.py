#define the class
class Character:
    #define the class variables
    characters = []

    #define the the init function
    def __init__(self, name):
        #your code here
        self.name = name
        self.level = 0
        self.lives = 3
        self.position = 0
        self.characters.append(self)

    #add the methods
    def move(self, speed):
        #your code here
        self.position += speed
        return self.position

    def level_up(self):
        #your code here
        self.level += 1
        return self.level

    def kill(self):
        #your code here
        self.lives -= 1
        return self.lives

    def bonus(self):
        #your code here
        self.lives += 1
        return self.lives

#create 4 instance of this class and test all the methods
c1 = Character("flow")
c1.move(5)
c1.kill()
print(c1.position)

c2 = Character("flo")
c2.move(-9)
c2.level_up()
c2.level_up()
print(c2.level)

c3 = Character("3")
c3.kill()
c3.bonus()
c3.bonus()
print(c3.lives)

c4 = Character("four")
c4.kill()
c4.bonus()
print(c4.lives)
