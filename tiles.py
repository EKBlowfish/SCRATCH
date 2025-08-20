import pygame
from settings import tile_size

# Simple sample level: 15x12 tiles
LEVEL_DATA = [
    [1]*15,
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]+[0]*13+[1],
    [1]*15
]

SOLID_IDS = {1}

class TileMap:
    def __init__(self, data):
        self.data = data
        self.width = len(data[0])
        self.height = len(data)
        self.background = {0: self._colored_surface('sienna'), 1: self._colored_surface('grey')}

    def _colored_surface(self, color):
        surf = pygame.Surface((tile_size, tile_size))
        surf.fill(pygame.Color(color))
        return surf

    def draw(self, surface, cam_x, cam_y):
        for y, row in enumerate(self.data):
            for x, tile_id in enumerate(row):
                surf = self.background.get(tile_id)
                if surf:
                    surface.blit(surf, (x*tile_size - cam_x, y*tile_size - cam_y))

    def collide(self, rect):
        for y, row in enumerate(self.data):
            for x, tile_id in enumerate(row):
                if tile_id in SOLID_IDS:
                    tile_rect = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                    if rect.colliderect(tile_rect):
                        return True
        return False

    def tile_rect(self, x, y):
        tx = int(x // tile_size)
        ty = int(y // tile_size)
        return pygame.Rect(tx*tile_size, ty*tile_size, tile_size, tile_size)
