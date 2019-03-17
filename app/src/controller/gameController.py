
import app.Config as config

score = 0
canvasWidth, canvasHeight = config.canvas['width'], config.canvas['height']

def game(snakeRect, foodRect, food, xspeed, yspeed):
    global score

    snakeRect = snakeRect.move(xspeed, yspeed)
    if snakeRect.left < 0 or snakeRect.right > canvasWidth:
        xspeed = -xspeed
    if snakeRect.top < 0 or snakeRect.bottom > canvasHeight:
        yspeed = -yspeed

    if snakeRect.colliderect(foodRect):
        food.get_rand_pos()
        foodRect, _ = food.draw()
        score += 1

    return snakeRect, xspeed, yspeed, foodRect

def getScore():
    return score
