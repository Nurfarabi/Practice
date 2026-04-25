import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
pygame.mixer.init()

#  Game Settings 
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

#  Colors 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#  Fonts 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

#  Load Assets 
background = pygame.image.load("AnimatedStreet.png")

# Load sound ONCE (important!)
crash_sound = pygame.mixer.Sound("crash.wav")

#  Screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

#  Enemy Class 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        
        # Spawn at random X position
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        
        # Move enemy downward
        self.rect.move_ip(0, SPEED)

        # Respawn at top if off screen
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

#  Player Class 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        # Move up (stay inside screen)
        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)

        # Move down
        if pressed_keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, 5)

        # Move left
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        # Move right
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

#  Coin Class 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and resize coin image
        original = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(original, (30, 30))
        self.rect = self.image.get_rect()

        # Random spawn position
        self.rect.center = (
            random.randint(self.rect.width, SCREEN_WIDTH - self.rect.width),
            0
        )

        self.speed = 3  # independent speed from enemy

    def move(self):
        # Move coin downward
        self.rect.move_ip(0, self.speed)

        # Respawn when off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (
                random.randint(self.rect.width, SCREEN_WIDTH - self.rect.width),
                0
            )

#  Create Objects 
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()

# Start with 3 coins
for _ in range(3):
    c = Coin()
    coins.add(c)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

for c in coins:
    all_sprites.add(c)

# Events 
# Increase enemy speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Optional: spawn new coins every few seconds
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN, 4000)

# Game Loop
while True:

    for event in pygame.event.get():

        if event.type == INC_SPEED:
            SPEED += 0.3  # gradually increase difficulty

        if event.type == ADD_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    #  UI 
    # Score (top-left)
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    # Coins (top-right)
    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 130, 10))

    #  Update Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Coin Collection 
    collected = pygame.sprite.spritecollide(P1, coins, True)

    if collected:
        # Increase counter
        COINS_COLLECTED += len(collected)

        # Replace collected coins
        for _ in range(len(collected)):
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # Collision with Enemy 
    if pygame.sprite.spritecollideany(P1, enemies):

        crash_sound.play()
        time.sleep(0.5)

        # Show Game Over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))

        pygame.display.update()

        # Remove all sprites
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)