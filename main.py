import os

# Only use the headless "dummy" video driver when a display is not available.
# This allows a real window to open in normal environments while still letting
# the game run in testing or CI setups without a graphical display.
if os.environ.get("DISPLAY", "") == "" and os.name != "nt" and not os.environ.get("SDL_VIDEODRIVER"):
    os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
from settings import WIDTH, HEIGHT, FPS
from tiles import TileMap, LEVEL_DATA
from player import Player
from text_engine import TextEngine
from store import Store
from ui import UI


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    tilemap = TileMap(LEVEL_DATA)
    player = Player(64, 64)
    text_engine = TextEngine()
    store = Store(text_engine)
    ui = UI(lives=3)

    cam_x = cam_y = 0
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                store.trigger('welcome')
        store.update(events)

        player.update(dt, tilemap)
        cam_x = player.rect.centerx - WIDTH // 2
        cam_y = player.rect.centery - HEIGHT // 2

        screen.fill((0, 0, 0))
        tilemap.draw(screen, cam_x, cam_y)
        player.draw(screen, cam_x, cam_y)
        text_engine.draw(screen)
        ui.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
