
import pygame

import app.Config as config

speed = config.game['snake_speed']

def keyboard_event(event, running, xspeed, yspeed):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and xspeed == 0:
            xspeed = -speed
            yspeed = 0
        elif event.key == pygame.K_RIGHT and xspeed == 0:
            xspeed = speed
            yspeed = 0
        elif event.key == pygame.K_UP and yspeed == 0:
            yspeed = -speed
            xspeed = 0
        elif event.key == pygame.K_DOWN and yspeed == 0:
            yspeed = speed
            xspeed = 0
        elif event.key == pygame.K_q:
            running = False
        else:
            pass

    if event.type == pygame.QUIT:
        running = False

    return running, xspeed, yspeed