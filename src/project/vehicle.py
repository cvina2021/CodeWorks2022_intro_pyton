#create the parent class
class Vehicle:
    def __init__(self,name,color):
        #your code here
        self.name = name
        self.color = color

    def max_speed(self):
        #your code here
        self.max_speed = 0
        print(self.max_speed)

class Car(Vehicle):
    def max_speed(self):
        #your code here
        self.max_speed = 250
        print(self.max_speed)

class Bus(Vehicle):
    def max_speed(self):
        #your code here
        self.max_speed = 150
        print(self.max_speed)


#creat instance of the three classes and call the max_speed() function on them
v1 = Vehicle("Veh", "red").max_speed()
c1 = Car("car", "blue").max_speed()
b1 = Bus("bus", "yellow").max_speed()
