
import pygame
import time

import app.Config as config
from app.src.model.Snake import Snake
from app.src.model.Food import Food
from app.src.view.rendering import render, init
from app.src.events.keyboard import keyboard_event
from app.src.controller.gameController import game, getScore

speed = config.game['snake_speed']
xspeed, yspeed = speed, 0

snake = Snake()

food = Food()
food_rect, surff = food.draw()

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        self._display_surf, self._running = init()

    def on_event(self, event):
        global yspeed
        global xspeed

        self._running, xspeed, yspeed = keyboard_event(event, self._running, xspeed, yspeed)

    def on_loop(self):
        global xspeed
        global yspeed
        global snake
        global food_rect

        self._running, snake, xspeed, yspeed, food_rect = game(self._running, snake, food_rect, food, xspeed, yspeed)

    def on_render(self):

        objects = snake.draw()
        objects.append([food_rect, surff])

        render(self._display_surf, objects)

    def on_cleanup(self):
        score = getScore()
        print('- Game quitted')
        print('\nFinal Score: {}\n'.format(score))
        pygame.quit()

    def on_execute(self):
        try:
            if self.on_init() is False:
                self._running = False

            on_start = 0
            while self._running:
                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render()

                if on_start == 0:
                    on_start += 1
                    time.sleep(1)

        except KeyboardInterrupt:
            print("\n")
        finally:
            self.on_cleanup()

if __name__ == "__main__":
    app = App()
    app.on_execute()
