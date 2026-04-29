import pygame
import random
import sys


pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)


WHITE = (0,0,0)
GREEN = (0,200,0)
RED = (200,0,0)
BLACK = (255,255,255)


snake = [(100,100), (80,100), (60,100)]
direction = "RIGHT"


def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, BLOCK)
        y = random.randrange(0, HEIGHT, BLOCK)

        
        if (x, y) not in snake:
            weight = random.choice([1, 2, 3])  
            return (x, y, weight)

food = spawn_food()

food_timer = pygame.time.get_ticks()
FOOD_LIFETIME = 5000 

score = 0


level = 1
speed = 10


running = True
while running:

   
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

    
    fx, fy, weight = food

    if new_head == (fx, fy):
        score += weight  
        food = spawn_food()
        food_timer = pygame.time.get_ticks()
    else:
        snake.pop()

    
    if pygame.time.get_ticks() - food_timer > FOOD_LIFETIME:
        food = spawn_food()
        food_timer = pygame.time.get_ticks()

    
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

    
    if new_head in snake[1:]:
        running = False

    
    if score // 5 + 1 > level:
        level = score // 5 + 1
        speed += 2  

     
    screen.fill(BLACK)

    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

    
    if weight == 1:
        food_color = (255, 0, 0)      
    elif weight == 2:
        food_color = (255, 165, 0)    
    else:
        food_color = (255, 255, 0)    

    pygame.draw.rect(screen, food_color, (fx, fy, BLOCK, BLOCK))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10,10))
    screen.blit(level_text, (10,40))

    pygame.display.update()
    clock.tick(speed)  

screen.fill(BLACK)
game_over = font.render("Game Over", True, RED)
screen.blit(game_over, (WIDTH//2 - 80, HEIGHT//2))
pygame.display.update()

pygame.time.delay(2000)
pygame.quit()