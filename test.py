import pygame
import sys


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level()

        self.world_shift = 0

    def setup_level(self):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for r, row in enumerate(self.level_data):
            for c, cell in enumerate(row):
                pos = (c*tile_size, r*tile_size)
                if cell == 'P':
                    self.player.add(Player(pos))
                if cell == 'X':
                    self.tiles.add(Tile(pos, tile_size))

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((250, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self, *args):
        self.get_input()
        self.rect.x += self.direction.x * self.speed


pygame.init()

level_map = [
    '                         ',
    '                         ',
    '            XXXXX        ',
    '                         ',
    '            P            ',
    'XXXX        XX           ',
    'XX     X  XXXX    XX XX  ',
    '       X  XXXX    XX XXX ',
    '   XXXXX  XXXXXX  XX XXXX',
    'XXXXXXXX  XXXXXX  XX XXXX',
]

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

test_tile = pygame.sprite.Group(Tile((100, 100), 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)