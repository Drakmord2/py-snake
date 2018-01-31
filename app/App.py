import pygame
from Config import Config

config = Config()
BLACK, WHITE = config.get_colors()
xspeed, yspeed = config.get_speeds()
size, width, height = config.get_sizes()

surf = pygame.Surface((10, 10))
snake = pygame.Rect((0, 0), (10, 10))
surf.fill(BLACK)


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = size

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(WHITE)
        pygame.display.set_caption('Snake')
        self._running = True
        print('- Game started')

    def on_event(self, event):
        global yspeed
        global xspeed
        evento = event.type

        if evento == pygame.QUIT:
            self._running = False

        if evento == pygame.MOUSEBUTTONDOWN or evento == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()

            if x <= width/2:
                if y >= height/2:
                    xspeed = -abs(xspeed)
                    yspeed = abs(yspeed)
                else:
                    xspeed = -abs(xspeed)
                    yspeed = -abs(yspeed)
            else:
                if y >= height/2:
                    xspeed = abs(xspeed)
                    yspeed = abs(yspeed)
                else:
                    xspeed = abs(xspeed)
                    yspeed = -abs(yspeed)

    def on_loop(self):
        global xspeed
        global yspeed
        global snake

        snake = snake.move(xspeed, yspeed)
        if snake.left < 0 or snake.right > width:
            xspeed = -xspeed
        if snake.top < 0 or snake.bottom > height:
            yspeed = -yspeed

    def on_render(self):
        self._display_surf.fill(WHITE)
        self._display_surf.blit(surf, snake)
        pygame.display.flip()

    def on_cleanup(self):
        print('- Game quitted')
        pygame.quit()

    def on_execute(self):
        try:

            if self.on_init() is False:
                self._running = False

            while self._running:
                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render()

        except KeyboardInterrupt:
            print("\n")
        finally:
            self.on_cleanup()
            

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
