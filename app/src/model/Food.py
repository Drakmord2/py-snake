
import pygame
import random
import app.Config as config

width, height = config.canvas['width'], config.canvas['height']

class Food(object):
    def __init__(self):
        self.fx = random.randint(20, width-20)
        self.fy = random.randint(20, height-20)

    def get_pos(self):
        return self.fx, self.fy

    def get_rand_pos(self):
        self.fx = random.randint(20, width-20)
        self.fy = random.randint(20, height-20)

        return self.fx, self.fy

    def draw(self):

        foodsize = (15, 15)

        surf = pygame.Surface(foodsize)
        food = pygame.Rect(self.get_pos(), foodsize)
        surf.fill(config.colors['RED'])

        return food, surf
