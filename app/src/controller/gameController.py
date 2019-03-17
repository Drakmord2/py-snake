
import app.Config as config

score = 0
canvasWidth, canvasHeight = config.canvas['width'], config.canvas['height']

def game(running, snake, food_rect, food, xspeed, yspeed):
    global score

    snake_rect = snake.parts[0]
    old_pos = snake_rect.pos.copy()
    snake_rect.pos[0] += xspeed
    snake_rect.pos[1] += yspeed
    snake_rect,_ = snake_rect.build()

    if snake_rect.left < 0 or snake_rect.right > canvasWidth or snake_rect.top < 0 or snake_rect.bottom > canvasHeight:
        running = False

    if snake_rect.colliderect(food_rect):
        new_part_pos = snake.parts[len(snake.parts) - 1].pos

        snake.add_part(new_part_pos)

        food.get_rand_pos()
        food_rect, _ = food.draw()
        score += 1

    move_body(snake.parts[0].prev, old_pos)

    return running, snake, xspeed, yspeed, food_rect

def move_body(part, pos):
    if part is None or part.next is None:
        return

    old_pos = part.pos.copy()
    part.pos = pos

    move_body(part.prev, old_pos)

def getScore():
    return score
