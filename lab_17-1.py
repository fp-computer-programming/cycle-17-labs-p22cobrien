# CMOB 4/11/2022

import math

class Circle():
    """ Circle class represents a circle """
   
    def __init__(self):
        """ Create a new circle with radius 1 """
        self.radius = 1
    
    def get_area(self):
        """ Finds the area of the circle """
        return (math.pi * math.sqrt(self.radius))


my_circle = Circle()
my_circle.radius = 3
print(my_circle.get_area())
