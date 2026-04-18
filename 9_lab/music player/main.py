import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

W, H = 600, 450
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("KBTU Music Player")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 26, bold=True)
small_font = pygame.font.SysFont("Arial", 18)

# Colors
BG = (20, 22, 26)
CARD = (35, 38, 45)
BTN = (97, 175, 239)
BTN_HOVER = (120, 190, 255)
TEXT = (240, 240, 240)
ACCENT = (152, 195, 121)
RED = (224, 108, 117)

songs = [
    "music/Skillet - The Resistance.mp3",
    "music/giragira.mp3",
]

current_track_index = 0
is_playing = False


def play_song(index):
    global is_playing, current_track_index
    try:
        pygame.mixer.music.load(songs[index])
        pygame.mixer.music.play()
        current_track_index = index
        is_playing = True
    except pygame.error as e:
        print(e)


def next_song():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(songs)
    play_song(current_track_index)


def prev_song():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(songs)
    play_song(current_track_index)


def draw_button(rect, text, mouse):
    color = BTN_HOVER if rect.collidepoint(mouse) else BTN
    pygame.draw.rect(screen, color, rect, border_radius=10)

    txt = small_font.render(text, True, TEXT)
    screen.blit(txt, txt.get_rect(center=rect.center))


running = True
while running:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.collidepoint(mouse):
                if not is_playing:
                    play_song(current_track_index)
                else:
                    pygame.mixer.music.unpause()

            if pause_btn.collidepoint(mouse):
                pygame.mixer.music.pause()

            if next_btn.collidepoint(mouse):
                next_song()

            if prev_btn.collidepoint(mouse):
                prev_song()

    screen.fill(BG)

    # Card
    card_rect = pygame.Rect(50, 50, 500, 300)
    pygame.draw.rect(screen, CARD, card_rect, border_radius=20)

    # Track info
    track_name = os.path.basename(songs[current_track_index])
    status = "Playing" if is_playing else "Paused"

    title = font.render(track_name, True, BTN)
    status_text = small_font.render(
        status, True, ACCENT if is_playing else RED
    )

    screen.blit(title, title.get_rect(center=(W // 2, 120)))
    screen.blit(status_text, status_text.get_rect(center=(W // 2, 160)))

    # Buttons
    play_btn = pygame.Rect(200, 220, 80, 40)
    pause_btn = pygame.Rect(300, 220, 80, 40)
    prev_btn = pygame.Rect(120, 220, 60, 40)
    next_btn = pygame.Rect(400, 220, 60, 40)

    draw_button(play_btn, "Play", mouse)
    draw_button(pause_btn, "Pause", mouse)
    draw_button(prev_btn, "<<", mouse)
    draw_button(next_btn, ">>", mouse)

    # Progress bar
    pygame.draw.rect(screen, (60, 60, 60), (120, 280, 360, 8), border_radius=5)
    if is_playing:
        pos = (pygame.time.get_ticks() // 30) % 360
        pygame.draw.rect(screen, BTN, (120, 280, pos, 8), border_radius=5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()