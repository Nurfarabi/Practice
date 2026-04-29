import pygame
import sys
import math

pygame.init()

 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

colors = [BLACK, RED, GREEN, BLUE]
current_color = BLACK


tool = "brush"   
drawing = False
start_pos = (0,0)

screen.fill(WHITE)

 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

     
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

            mx, my = event.pos

           
            for i, col in enumerate(colors):
                rect = pygame.Rect(10 + i*50, 10, 40, 40)
                if rect.collidepoint(mx, my):
                    current_color = col

            if pygame.Rect(10, 60, 80, 30).collidepoint(mx, my):
                tool = "brush"
            if pygame.Rect(100, 60, 80, 30).collidepoint(mx, my):
                tool = "rect"
            if pygame.Rect(190, 60, 80, 30).collidepoint(mx, my):
                tool = "circle"
            if pygame.Rect(280, 60, 80, 30).collidepoint(mx, my):
                tool = "eraser"

           
            if pygame.Rect(370, 60, 80, 30).collidepoint(mx, my):
                tool = "square"
            if pygame.Rect(460, 60, 80, 30).collidepoint(mx, my):
                tool = "tri_right"
            if pygame.Rect(550, 60, 80, 30).collidepoint(mx, my):
                tool = "tri_eq"
            if pygame.Rect(640, 60, 80, 30).collidepoint(mx, my):
                tool = "rhombus"

     
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            
            if tool == "rect":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(screen, current_color, (x, y, w, h), 2)

            
            if tool == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

           
            if tool == "square":
                size = max(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], size, size), 2)

           
            if tool == "tri_right":
                points = [
                    start_pos,
                    (end_pos[0], start_pos[1]),
                    end_pos
                ]
                pygame.draw.polygon(screen, current_color, points, 2)

            
            if tool == "tri_eq":
                side = abs(end_pos[0] - start_pos[0])
                height = int(side * math.sqrt(3) / 2)

                points = [
                    (start_pos[0], start_pos[1]),
                    (start_pos[0] + side, start_pos[1]),
                    (start_pos[0] + side//2, start_pos[1] - height)
                ]

                pygame.draw.polygon(screen, current_color, points, 2)

            
            if tool == "rhombus":
                cx = (start_pos[0] + end_pos[0]) // 2
                cy = (start_pos[1] + end_pos[1]) // 2

                dx = abs(start_pos[0] - end_pos[0]) // 2
                dy = abs(start_pos[1] - end_pos[1]) // 2

                points = [
                    (cx, cy - dy),
                    (cx + dx, cy),
                    (cx, cy + dy),
                    (cx - dx, cy)
                ]

                pygame.draw.polygon(screen, current_color, points, 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            mx, my = event.pos

            if tool == "brush":
                pygame.draw.circle(screen, current_color, (mx, my), 5)

            if tool == "eraser":
                pygame.draw.circle(screen, WHITE, (mx, my), 50)

    for i, col in enumerate(colors):
        pygame.draw.rect(screen, col, (10 + i*50, 10, 40, 40))

    font = pygame.font.SysFont("Times New Roman", 14)

    pygame.draw.rect(screen, BLACK, (10, 60, 80, 30), 2)
    screen.blit(font.render("Brush", True, BLACK), (15, 65))

    pygame.draw.rect(screen, BLACK, (100, 60, 80, 30), 2)
    screen.blit(font.render("Rect", True, BLACK), (110, 65))

    pygame.draw.rect(screen, BLACK, (190, 60, 80, 30), 2)
    screen.blit(font.render("Circle", True, BLACK), (200, 65))

    pygame.draw.rect(screen, BLACK, (280, 60, 80, 30), 2)
    screen.blit(font.render("Eraser", True, BLACK), (290, 65))

    pygame.draw.rect(screen, BLACK, (370, 60, 80, 30), 2)
    screen.blit(font.render("Square", True, BLACK), (380, 65))

    pygame.draw.rect(screen, BLACK, (460, 60, 80, 30), 2)
    screen.blit(font.render("R.Tri", True, BLACK), (470, 65))

    pygame.draw.rect(screen, BLACK, (550, 60, 80, 30), 2)
    screen.blit(font.render("E.Tri", True, BLACK), (560, 65))

    pygame.draw.rect(screen, BLACK, (640, 60, 80, 30), 2)
    screen.blit(font.render("Rhomb", True, BLACK), (645, 65))

    pygame.display.update()