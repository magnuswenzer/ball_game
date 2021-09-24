from game import GameObject
from game import GameProp
import tiles

s = 's'
f = 'f'

LAYOUT = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, s, s, s, s, s, s, s, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, f, f, f, f, f, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, s],
          [f, s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, s, f],
          [f, f, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, f, f],
          [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f]]


class Map(GameObject):

    def __init__(self, game):
        self.game = game
        self.tile_list = []

    def update(self):
        pass

    def draw(self, screen):
        for y, row in enumerate(LAYOUT):
            for x, tile in enumerate(row):
                obj = tiles.get_tile(tile, self.game, x * GameProp.TILE_SIZE, y * GameProp.TILE_SIZE)
                if obj is None:
                    continue
                obj.draw(screen)
