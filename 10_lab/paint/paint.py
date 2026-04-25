import pygame
import sys

pygame.init()

#  Screen 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

#  Colors 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

colors = [BLACK, RED, GREEN, BLUE]
current_color = BLACK

#  Tools 
tool = "brush"   # brush, rect, circle, eraser
drawing = False
start_pos = (0,0)

screen.fill(WHITE)

#  Main Loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

            mx, my = event.pos

            # Color buttons
            for i, col in enumerate(colors):
                rect = pygame.Rect(10 + i*50, 10, 40, 40)
                if rect.collidepoint(mx, my):
                    current_color = col

            # Tool buttons
            if pygame.Rect(10, 60, 80, 30).collidepoint(mx, my):
                tool = "brush"
            if pygame.Rect(100, 60, 80, 30).collidepoint(mx, my):
                tool = "rect"
            if pygame.Rect(190, 60, 80, 30).collidepoint(mx, my):
                tool = "circle"
            if pygame.Rect(280, 60, 80, 30).collidepoint(mx, my):
                tool = "eraser"

        # Mouse released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            end_pos = event.pos

            # Draw rectangle
            if tool == "rect":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(screen, current_color, (x, y, w, h), 2)

            # Draw circle
            if tool == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

        # Mouse move (brush / eraser)
        if event.type == pygame.MOUSEMOTION and drawing:
            mx, my = event.pos

            if tool == "brush":
                pygame.draw.circle(screen, current_color, (mx, my), 5)

            if tool == "eraser":
                pygame.draw.circle(screen, WHITE, (mx, my), 10)

    #  UI 
    # Draw color palette
    for i, col in enumerate(colors):
        pygame.draw.rect(screen, col, (10 + i*50, 10, 40, 40))

    # Draw tool buttons
    font = pygame.font.SysFont("Arial", 16)

    pygame.draw.rect(screen, BLACK, (10, 60, 80, 30), 2)
    screen.blit(font.render("Brush", True, BLACK), (15, 65))

    pygame.draw.rect(screen, BLACK, (100, 60, 80, 30), 2)
    screen.blit(font.render("Rect", True, BLACK), (110, 65))

    pygame.draw.rect(screen, BLACK, (190, 60, 80, 30), 2)
    screen.blit(font.render("Circle", True, BLACK), (200, 65))

    pygame.draw.rect(screen, BLACK, (280, 60, 80, 30), 2)
    screen.blit(font.render("Eraser", True, BLACK), (290, 65))

    pygame.display.update()