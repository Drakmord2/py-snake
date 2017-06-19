
import pygame

size = width, height = 320, 240
xspeed = 2
yspeed = 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

surf = pygame.Surface((20, 20))
surf.fill(BLACK)
surfrect = pygame.Rect((50, 50), (20, 20))


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = size

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Teste')
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        global xspeed
        global yspeed
        global surfrect

        surfrect = surfrect.move(xspeed, yspeed)
        if surfrect.left < 0 or surfrect.right > width:
            xspeed = -xspeed
        if surfrect.top < 0 or surfrect.bottom > height:
            yspeed = -yspeed

    def on_render(self):
        self._display_surf.fill(WHITE)
        self._display_surf.blit(surf, surfrect)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
