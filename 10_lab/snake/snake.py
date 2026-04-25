import pygame
import random
import sys

#  Init 
pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

#  Colors 
WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (200,0,0)
BLACK = (0,0,0)

#  Snake 
snake = [(100,100), (80,100), (60,100)]  # list of segments
direction = "RIGHT"

#  Food 
def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, BLOCK)
        y = random.randrange(0, HEIGHT, BLOCK)
        if (x, y) not in snake:
            return (x, y)

food = spawn_food()

score = 0

#  Game Loop 
running = True
while running:

    #  Events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    #  Move snake 
    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= BLOCK
    elif direction == "DOWN":
        head_y += BLOCK
    elif direction == "LEFT":
        head_x -= BLOCK
    elif direction == "RIGHT":
        head_x += BLOCK

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    #  Check food 
    if new_head == food:
        score += 1
        food = spawn_food()
    else:
        snake.pop()

    #  Collision with wall 
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

    #  Collision with itself 
    if new_head in snake[1:]:
        running = False

    #  Drawing 
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10,10))

    pygame.display.update()
    clock.tick(10)  # speed

#  Game Over 
screen.fill(BLACK)
game_over = font.render("Game Over", True, RED)
screen.blit(game_over, (WIDTH//2 - 80, HEIGHT//2))
pygame.display.update()

pygame.time.delay(2000)
pygame.quit()