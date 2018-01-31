
size = width, height = 320, 240
xspeed = 2
yspeed = 2


class Snake(object):
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self):
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.posx += xspeed
        self.posy += yspeed

        if self.posx > width:
            self.posx = 1
        elif self.posx < 1:
            self.posx = width

        if self.posy > height:
            self.posy = 1
        elif self.posy < 1:
            self.posy = height
