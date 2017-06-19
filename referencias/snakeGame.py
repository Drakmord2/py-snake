# Snake Game

import random
from time import sleep

clear = "\n"*50
board = []


def make_board():
    for i in range(11):
        board.append([])
        for j in range(11):
            if j == 0 or j == 10:
                board[i].append("|")
            elif i == 0 or i == 10:
                board[i].append("---")
            else:
                board[i].append("   ")


class Food(object):
    def __init__(self):
        self.fx = random.randint(1, 9)
        self.fy = random.randint(1, 9)

    def eaten(self):
        self.fx = random.randint(1, 9)
        self.fy = random.randint(1, 9)


class Snake(object):
    def __init__(self, posx, posy, xspeed, yspeed):
        self.posx = posx
        self.posy = posy
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self, xspeed, yspeed):
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.posx += xspeed
        self.posy += yspeed

        if self.posx > 9:
            self.posx = 1
        elif self.posx < 1:
            self.posx = 9

        if self.posy > 9:
            self.posy = 1
        elif self.posy < 1:
            self.posy = 9


def show(posx, posy, fx, fy):
    board[posx][posy] = " * "
    board[fx][fy] = " # "
    for i in range(11):
        for j in range(11):
            print(board[i][j], end=" ")
        print(end="\n\n")
    board[posx][posy] = "   "
    board[fx][fy] = "   "


def play():
    cobra = Snake(1, 1, 0, 1)
    comida = Food()
    if cobra.posx == comida.fx and cobra.posy == comida.fy:
        comida.eaten()

    try:
        while True:
            print(clear)
            show(cobra.posx, cobra.posy, comida.fx, comida.fy)
            cobra.update(0, 1)
            sleep(1)
    except KeyboardInterrupt:
        return True


if __name__ == "__main__":
    make_board()
    play()

