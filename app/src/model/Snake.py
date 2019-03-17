
import pygame

import app.Config as config

class Snake(object):
    def __init__(self):
        self.parts = [(0,0), (11,0)]

    def draw(self):

        snakeSize = (10, 10)

        surf = pygame.Surface(snakeSize)
        snake = pygame.Rect((250, 250), snakeSize)
        surf.fill(config.colors['BLACK'])

        return snake, surf
