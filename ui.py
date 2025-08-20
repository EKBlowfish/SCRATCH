import pygame

class UI:
    def __init__(self, lives):
        self.lives = lives
        self.font = pygame.font.SysFont(None, 24)

    def set_lives(self, lives):
        self.lives = lives

    def draw(self, surface):
        text = f'Lives: {self.lives}'
        surf = self.font.render(text, True, (255,255,255))
        surface.blit(surf, (10,10))
