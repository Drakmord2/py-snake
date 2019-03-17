
import pygame

import app.Config as config

speed = config.game['snake_speed']

def keyboard_event(event, running, xspeed, yspeed):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            xspeed = -speed
            yspeed = 0
        elif event.key == pygame.K_RIGHT:
            xspeed = speed
            yspeed = 0
        elif event.key == pygame.K_UP:
            yspeed = -speed
            xspeed = 0
        elif event.key == pygame.K_DOWN:
            yspeed = speed
            xspeed = 0
        elif event.key == pygame.K_q:
            running = False
        else:
            pass

    if event.type == pygame.QUIT:
        running = False

    return running, xspeed, yspeed