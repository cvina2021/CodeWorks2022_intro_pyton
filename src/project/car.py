# define the class
class Car:
#define the class variables

#define the the init function
    def __init__(self, make, model):
        self.make = make
        self.model = model

#add the methods
    def toString(self):
        return self.make + " " + self.model

#create instance of the class and print them out
car1 = Car("Nissan", "Pathfinder")
car2 = Car("Honda", "Truck")
car3 = Car("BMW", "New")
car4 = Car("Nissan", "Path")
print(car1.toString())
print(car2.toString())
print(car3.toString())
print(car4.toString())
