
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

def render(display_surf, objects, score):
    display_surf.fill(config.colors['WHITE'])

    for element in objects:
        thing = element[0]
        surf = element[1]

        display_surf.blit(surf, thing)

    header(display_surf, score)

    pygame.display.flip()

def header(display_surf, score):
    header_position = (0, 0, config.canvas['width'], 40)
    header_color = config.colors['BLACK']
    display_surf.fill(header_color, header_position)

    font = pygame.font.Font(None, 24)
    title_position = (100, 15)
    text = font.render('Python Snake', 1, config.colors['RED'], config.colors['BLACK'])
    display_surf.blit(text, title_position)

    font = pygame.font.Font(None, 18)
    title_position = (240, 15)
    text = font.render('Score: {}'.format(str(score)), 1, config.colors['RED'], config.colors['BLACK'])
    display_surf.blit(text, title_position)

def result(display_surf, score):
    display_surf.fill(config.colors['BLACK'])

    font = pygame.font.Font(None, 42)
    title_position = (60, 120)
    text = font.render('Python Snake', 1, config.colors['RED'], config.colors['BLACK'])
    display_surf.blit(text, title_position)

    font = pygame.font.Font(None, 32)
    title_position = (80, 180)
    text = font.render('Final Score: {}'.format(str(score)), 1, config.colors['RED'], config.colors['BLACK'])
    display_surf.blit(text, title_position)

    pygame.display.flip()