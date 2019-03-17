
import pygame

import app.Config as config

def init():
    pygame.init()
    display_surf = pygame.display.set_mode(config.canvas['size'], pygame.HWSURFACE | pygame.DOUBLEBUF)
    display_surf.fill(config.colors['WHITE'])
    pygame.display.set_caption('Snake')
    running = True
    print('\n- Game started')

    return display_surf, running

def render(display_surf, objects):
    display_surf.fill(config.colors['WHITE'])

    for element in objects:
        thing = element[0]
        surf = element[1]

        display_surf.blit(surf, thing)

    pygame.display.flip()
