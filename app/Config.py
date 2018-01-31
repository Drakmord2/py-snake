

class Config:

    def __init__(self):
        self.size = self.width, self.height = 500, 500  # 320, 240
        self.xspeed = 2
        self.yspeed = 2
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

    def get_sizes(self):
        return self.size, self.width, self.height

    def get_speeds(self):
        return self.xspeed, self.yspeed

    def get_colors(self):
        return self.BLACK, self.WHITE
