import pygame
from ball import Ball

pygame.init()

width, height = 615, 415
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

ball = Ball(width // 2, height // 2)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            ball.move(event.key, width, height)

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()