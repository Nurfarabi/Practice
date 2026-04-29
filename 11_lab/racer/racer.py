import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
pygame.mixer.init()


FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
LEVEL = 0

SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

 
background = pygame.image.load("AnimatedStreet.png")


crash_sound = pygame.mixer.Sound("crash.wav")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        
        
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
      
        self.rect.move_ip(0, SPEED)

        
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        
        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)

        
        if pressed_keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, 5)

       
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        
        self.weight = random.choice([1, 3, 5])

        original = pygame.image.load("coin.png")

       
        if self.weight == 1:
            size = 20
        elif self.weight == 3:
            size = 30
        else:
            size = 40

        self.image = pygame.transform.scale(original, (size, size))
        self.rect = self.image.get_rect()

        self.rect.center = (
            random.randint(self.rect.width, SCREEN_WIDTH - self.rect.width),
            0
        )

        self.speed = 3

    def move(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (
                random.randint(self.rect.width, SCREEN_WIDTH - self.rect.width),
                0
            )
    def move(self):
       
        self.rect.move_ip(0, self.speed)

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (
                random.randint(self.rect.width, SCREEN_WIDTH - self.rect.width),
                0
            )

# Objects
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()


for _ in range(1):
    c = Coin()
    coins.add(c)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

for c in coins:
    all_sprites.add(c)

# Events 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN, 4000)


while True:

    for event in pygame.event.get():

        if event.type == INC_SPEED:
            SPEED += 0.3  

        if event.type == ADD_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    DISPLAYSURF.blit(background, (0, 0))

    # Ui
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    level_text = font_small.render(f"Level: {LEVEL}", True, BLACK)
    DISPLAYSURF.blit(level_text, (10, 40))

   
    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 130, 10))

   
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

  
    collected = pygame.sprite.spritecollide(P1, coins, True)

    if collected:
       
        for coin in collected:
            COINS_COLLECTED += coin.weight

       
        for _ in range(len(collected)):
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    
    if COINS_COLLECTED // 10 > LEVEL:
        LEVEL += 1
        SPEED += 1

     
    if pygame.sprite.spritecollideany(P1, enemies):

        crash_sound.play()
        time.sleep(0.5)

        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))

        pygame.display.update()

        
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)