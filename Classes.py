#Classes combine info and behavior; use CamelCase when naming classes
from math import sqrt
from random import randint

class Rocket:
    # Simulates a rocket ship for a game
    def __init__(self, x=0, y=0):
        #each rocket has an (x,y) position, __init__() method sets the values for any parameters that need to be defined
        # when an object is first created
        self.x = x
        self.y = y
    # def move_up(self):
    #     #increment the y-position of the rocket, methods are just a function that are part of a class
    #     self.y += 1
    def move_rocket(self, x_increment=0, y_increment=1):
        #Move rocket according to parameters given, default behavior is to move rocket up 1 unit
        self.x += x_increment
        self.y += y_increment
    def get_distance(self, other_rocket):
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
#Create a rocket object, have it start to move up
# my_rocket = Rocket()
# print("Rocket altitude:", my_rocket.y)
#
# my_rocket.move_up()
# print("Rocket altitude:", my_rocket.y)
#
# my_rocket.move_up()
# print("Rocket altitude:", my_rocket.y)

#Create a fleet of 5 rockets, and store them in a list
# my_rockets = []
# for x in range (0,5):
#     new_rocket = Rocket()
#     my_rockets.append(new_rocket)
# my_rockets = [Rocket() for x in range (0,5)]

#Move the first rocket up
# my_rockets[0].move_up()

#Show that each rocket is a separate object
# for rocket in my_rockets:
#     print("Rocket Altitude:", rocket.y)

# Series of Rockets at different starting places
# rockets = []
# rockets.append(Rocket())
# rockets.append(Rocket(0,10))
# rockets.append(Rocket(100,0))
#
# for index, rocket in enumerate(rockets):
#     print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
#Create 3 rockets
# rockets = [Rocket() for x in range(0,3)]
# rockets[0].move_rocket()
# rockets[1].move_rocket(10,10)
# rockets[2].move_rocket(-10,0)
# for index, rocket in enumerate(rockets):
#     print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
 # Make 2 rockets at different places
# rocket_0 = Rocket()
# rocket_1 = Rocket(10,5)

 # Show the distance between them
# distance = rocket_0.get_distance(rocket_1)
# print("The rockets are %f units apart." % distance)


# class NewClass(ParentClass):
#
#     def __init__(self, arguments_new_class, arguments_parent_class):
#         super().__init__(arguments_parent_class)
#         # Code for initializing an object of the new class.
class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed

shuttles = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    flights_completed = randint(0,10)
    shuttles.append(Shuttle(x,y, flights_completed))

rockets = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    rockets.append(Rocket(x,y))

# Show the number of flights completed for each shuttle.
for index, shuttle in enumerate(shuttles):
    print("Shuttle %d has completed %d flights." % (index, shuttle.flights_completed))

print("\n")
# Show the distance from the first shuttle to all other shuttles.
first_shuttle = shuttles[0]
for index, shuttle in enumerate(shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print("The first shuttle is %f units away from shuttle %d." % (distance, index))

print("\n")
# Show the distance from the first shuttle to all other rockets.
for index, rocket in enumerate(rockets):
    distance = first_shuttle.get_distance(rocket)
    print("The first shuttle is %f units away from rocket %d." % (distance, index))