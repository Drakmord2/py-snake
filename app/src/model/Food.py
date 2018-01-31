
import random

size = width, height = 320, 240
xspeed = 2
yspeed = 2


class Food(object):
    def __init__(self):
        self.fx = random.randint(1, width)
        self.fy = random.randint(1, height)

    def eaten(self):
        self.fx = random.randint(1, width)
        self.fy = random.randint(1, height)
