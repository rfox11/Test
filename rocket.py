from math import sqrt
#Create Rocket class without example
class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move_rocket(self, x_move=0, y_move=0):
        self.x += x_move
        self.y += y_move
    def get_distance(self, other_rocket):
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
#Create shuttle class
class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed