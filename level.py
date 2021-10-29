import pygame

from settings import GameProperties
from player import Player
import tiles


class Level:
    def __init__(self, game, level_data, surface):
        self.game = game
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level()

        self.world_shift = 0

    def setup_level(self):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for r, row in enumerate(self.level_data):
            for c, cell in enumerate(row):
                pos = (c * GameProperties.TILE_SIZE, r * GameProperties.TILE_SIZE)
                if cell == 'P':
                    self.player.add(Player(self.game, pos))
                if cell == 'X':
                    self.tiles.add(tiles.get_tile(pos, GameProperties.TILE_SIZE))

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)


def get_level(game, level_data, surface):
    return Level(game, level_data, surface)