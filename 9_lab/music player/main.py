import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

W = 500
H = 400
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("KBTU Music Player")

font = pygame.font.SysFont("Arial", 22, bold=True)
small_font = pygame.font.SysFont("Arial", 18)


BG_COLOR = (30, 33, 39)
BTN_COLOR = (97, 175, 239)
TEXT_COLOR = (255, 255, 255)
ACCENT_COLOR = (152, 195, 121)

songs = [
    "music/giragira.mp3",
    "music/Skillet - The Resistance.mp3"
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
        print(f"Ошибка загрузки: {e}")

def stop_song():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False

def next_song():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(songs)
    play_song(current_track_index)

def prev_song():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(songs)
    play_song(current_track_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not is_playing:
                    play_song(current_track_index)
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:

                pygame.mixer.music.pause()
                is_playing = False
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_b:
                prev_song()
            elif event.key == pygame.K_q:
                running = False

    screen.fill(BG_COLOR)
    track_name = os.path.basename(songs[current_track_index])
    status = "Playing" if is_playing else "Paused/Stopped"
    
    title_surface = font.render(f"Track: {track_name}", True, BTN_COLOR)
    status_surface = small_font.render(f"Status: {status}", True, ACCENT_COLOR if is_playing else (200, 100, 100))
    
    screen.blit(title_surface, (50, 50))
    screen.blit(status_surface, (50, 90))

    controls = [
        "P - Play/Unpause",
        "S - Stop (Pause)",
        "N - Next Track",
        "B - Previous Track",
        "Q - Quit"
    ]
    
    for i, text in enumerate(controls):
        ctrl_surf = small_font.render(text, True, (150, 150, 150))
        screen.blit(ctrl_surf, (50, 150 + (i * 30)))

    pygame.draw.rect(screen, (60, 60, 60), (50, 330, 400, 10))
    if is_playing:
        pos = (pygame.time.get_ticks() // 50) % 400
        pygame.draw.rect(screen, BTN_COLOR, (50, 330, pos, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()