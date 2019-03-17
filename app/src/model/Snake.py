
import pygame

import app.Config as config

class Snake(object):
    def __init__(self):
        self.parts = [ Part([160, 140]) ]

    def draw(self):
        snake = []
        for part in self.parts:
            snakepart, surf = part.build()

            part.rect = snakepart
            part.surf = surf

            snake.append([snakepart, surf])

        return snake

    def add_part(self, pos):
        part = Part(pos)

        self.parts[len(self.parts)-1].prev = part
        part.next = self.parts[len(self.parts)-1]

        self.parts.append(part)

class Part:
    def __init__(self, pos, prev=None, next=None):
        self.pos = pos
        self.prev = prev
        self.next = next
        self.rect = None
        self.surf = None

    def build(self):
        surf = pygame.Surface((10, 10))
        snakepart = pygame.Rect(tuple(self.pos), (10, 10))
        surf.fill(config.colors['BLACK'])

        return snakepart, surf