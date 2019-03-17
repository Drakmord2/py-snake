
import pygame

import app.Config as config

class Snake(object):
    def __init__(self):
        p1 = Part([261, 250])
        p2 = Part([250, 250], next=p1)
        p3 = Part([239, 250], next=p2)
        p4 = Part([228, 250], next=p3)
        p5 = Part([217, 250], next=p4)

        p1.prev = p2
        p2.prev = p3
        p3.prev = p4
        p4.prev = p5

        self.parts = [p1, p2, p3, p4, p5]

    def draw(self):
        snake = []
        for part in self.parts:
            snakepart, surf = part.build()

            part.rect = snakepart
            part.surf = surf

            snake.append([snakepart, surf])

        return snake

    def add_part(self, part):
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