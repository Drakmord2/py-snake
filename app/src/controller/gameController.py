
import app.Config as config

score = 0
canvasWidth, canvasHeight = config.canvas['width'], config.canvas['height']

def game(running, snake, foodRect, food, xspeed, yspeed):
    global score

    snakeRect = snake.parts[0]
    old_pos = snakeRect.pos.copy()
    snakeRect.pos[0] += xspeed
    snakeRect.pos[1] += yspeed
    snakeRect,_ = snakeRect.build()

    if snakeRect.left < 0 or snakeRect.right > canvasWidth or snakeRect.top < 0 or snakeRect.bottom > canvasHeight:
        running = False

    if snakeRect.colliderect(foodRect): # Head ate the food
        food.get_rand_pos()
        foodRect, _ = food.draw()
        score += 1

    move_body(snake.parts[1], old_pos)

    return running, snake, xspeed, yspeed, foodRect

def move_body(part, pos):
    if part is None or part.next is None:
        return

    old_pos = part.pos.copy()
    part.pos = pos

    move_body(part.prev, old_pos)

def getScore():
    return score
