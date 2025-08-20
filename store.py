import pygame

class Store:
    def __init__(self, text_engine):
        self.text_engine = text_engine
        self.scenes = {
            'welcome': 'Welcome to the store!\nPress ESC to close.'
        }
        self.active = False

    def trigger(self, name):
        msg = self.scenes.get(name)
        if msg:
            self.text_engine.show(msg)
            self.active = True

    def update(self, events):
        if self.active:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.text_engine.hide()
                        self.active = False
