import pygame
from settings import tile_size

DIRECTIONS = {
    0: pygame.Vector2(1, 0),
    90: pygame.Vector2(0, -1),
    180: pygame.Vector2(0, 1),
    -90: pygame.Vector2(-1, 0),
}

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = self._load_animations()
        self.dir = 180  # Facing down initially
        self.state = 'idle'
        self.frame_index = 0
        self.image = self.animations['idle'][self.dir][0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.attack_timer = 0

    def _load_animations(self):
        animations = {'idle': {}, 'walk': {}, 'attack': {}}
        for direction in DIRECTIONS.keys():
            idle_frames = [self._colored_surface(pygame.Color('blue'))]
            walk_frames = [self._colored_surface(pygame.Color('green')) for _ in range(6)]
            attack_frames = [self._colored_surface(pygame.Color('red')) for _ in range(6)]
            animations['idle'][direction] = idle_frames
            animations['walk'][direction] = walk_frames
            animations['attack'][direction] = attack_frames
        return animations

    def _colored_surface(self, color):
        surf = pygame.Surface((tile_size, tile_size))
        surf.fill(color)
        return surf

    def handle_input(self, keys):
        move = pygame.Vector2(0, 0)
        for dir_angle, vec in DIRECTIONS.items():
            if dir_angle == 0 and keys[pygame.K_RIGHT]:
                move += vec
                self.dir = 0
            elif dir_angle == 180 and keys[pygame.K_DOWN]:
                move += vec
                self.dir = 180
            elif dir_angle == 90 and keys[pygame.K_UP]:
                move += vec
                self.dir = 90
            elif dir_angle == -90 and keys[pygame.K_LEFT]:
                move += vec
                self.dir = -90
        if move.length_squared() > 0:
            self.state = 'walk'
            move = move.normalize()
        else:
            self.state = 'idle'
        return move

    def update(self, dt, tilemap):
        keys = pygame.key.get_pressed()
        move = self.handle_input(keys)
        speed = 60
        displacement = move * speed * dt
        self._move(displacement, tilemap)
        if keys[pygame.K_SPACE] and self.attack_timer <= 0:
            self.state = 'attack'
            self.attack_timer = 0.4
            self.frame_index = 0
        if self.attack_timer > 0:
            self.attack_timer -= dt
            if self.attack_timer <= 0:
                self.state = 'idle'
        self._animate(dt)

    def _move(self, displacement, tilemap):
        self.rect.x += displacement.x
        if tilemap.collide(self.rect):
            if displacement.x > 0:
                self.rect.right = tilemap.tile_rect(self.rect.right, self.rect.centery).left
            elif displacement.x < 0:
                self.rect.left = tilemap.tile_rect(self.rect.left, self.rect.centery).right
        self.rect.y += displacement.y
        if tilemap.collide(self.rect):
            if displacement.y > 0:
                self.rect.bottom = tilemap.tile_rect(self.rect.centerx, self.rect.bottom).top
            elif displacement.y < 0:
                self.rect.top = tilemap.tile_rect(self.rect.centerx, self.rect.top).bottom

    def _animate(self, dt):
        frames = self.animations[self.state][self.dir]
        frame_speed = 10
        self.frame_index += frame_speed * dt
        if self.frame_index >= len(frames):
            if self.state == 'attack':
                self.state = 'idle'
            self.frame_index = 0
        self.image = frames[int(self.frame_index)]

    def draw(self, surface, cam_x, cam_y):
        surface.blit(self.image, (self.rect.x - cam_x, self.rect.y - cam_y))
