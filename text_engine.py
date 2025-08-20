import pygame
from settings import WIDTH, HEIGHT

PAGE_L, PAGE_T, PAGE_R, PAGE_B = -190, -100, 220, -162
LINE_HEIGHT = 22

class TextEngine:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 20)
        self.lines = []
        self.visible = False

    def show(self, text):
        self.lines = text.split('\n')
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, surface):
        if not self.visible:
            return
        box = pygame.Rect(WIDTH//2 + PAGE_L, HEIGHT//2 + PAGE_T,
                          PAGE_R - PAGE_L, PAGE_B - PAGE_T)
        pygame.draw.rect(surface, (0, 0, 0), box)
        pygame.draw.rect(surface, (255, 255, 255), box, 2)
        for i, line in enumerate(self.lines):
            txt_surf = self.font.render(line, True, (255,255,255))
            surface.blit(txt_surf, (box.x + 4, box.y + 4 + i*LINE_HEIGHT))
