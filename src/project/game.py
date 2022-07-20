class Characters:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self):
        self.position = 0

class Hero(Characters):
    def move(self):
        self.position += 1

class Villian(Characters):
    def move(self):
        self.position -= 1

c1 = Characters("char", 0)
c1.move()
print(c1.position)

hero = Hero("hero", 0)
hero.move()
print(hero.position)

villian = Villian("villian", 0)
villian.move()
print(villian.position)
