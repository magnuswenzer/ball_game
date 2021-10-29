import pygame
import physics


IDENTIFIERS = {'s': 'images/tile_bottom.png',
               'f': 'images/tile_fill.png'}


class Tile(pygame.sprite.Sprite):

    def __init__(self, image_path, game, x, y):
        super().__init__()
        self.image_path = image_path
        self.game = game

        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        # self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

        self.physics = physics.get_game_object_physics('tile', self.game, self.rect)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.physics.position)


class TestTile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


def get_tile(pos, size):
    return TestTile(pos, size)


def old_get_tile(identifier, game, x, y):
    image_path = IDENTIFIERS.get(identifier)
    if not image_path:
        return
    return Tile(image_path, game, x, y)
