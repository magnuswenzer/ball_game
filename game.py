import pygame
import sys
from pygame.locals import *
from abc import ABC, abstractmethod


class GameObject(ABC):
    physics = None

    @abstractmethod
    def update(self):
        """ Update the game object """

    @abstractmethod
    def draw(self, window):
        """ Draw the game object"""

    def collides(self, other_game_object):
        """ Returns collide information """
        return self.physics.collides(other_game_object)

    # @property
    # @abstractmethod
    # def position(self):
    #     """ Returns the current position """
    #
    # @property
    # @abstractmethod
    # def top(self):
    #     pass
    #
    # @property
    # @abstractmethod
    # def bottom(self):
    #     pass
    #
    # @property
    # @abstractmethod
    # def left(self):
    #     pass
    #
    # @property
    # @abstractmethod
    # def right(self):
    #     pass


class Game:

    def __init__(self,
                 title: str,
                 width: int,
                 height: int,
                 time_stem: int = 60):

        self.title = title

        self.window_width = width
        self.window_height = height
        self.window_size = (self.window_width, self.window_height)

        self.display_width = int(self.window_width/2)
        self.display_height = int(self.window_height/2)
        self.display_size = (self.display_width, self.display_height)

        self.time_step = time_stem

        pygame.init()

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(self.title)

        self.screen = pygame.display.set_mode(self.window_size, 0, 32)
        self.display = pygame.Surface(self.display_size)

        self.objects: list[GameObject] = []

    def add_object(self, obj: GameObject):
        self.objects.append(obj)

    def remove_object(self, obj: GameObject):
        if obj not in self.objects:
            return
        self.objects.remove(obj)

    def update_objects(self):
        """ Updates the game objects """
        for obj in self.objects:
            obj.update()

    def draw_objects(self):
        """ Draws the game objects """
        """"""
        for obj in self.objects:
            obj.draw(self.display)

    def update_game(self):
        self.display.fill((150, 150, 150))
        self.update_objects()
        self.draw_objects()
        surf = pygame.transform.scale(self.display, self.window_size)
        self.screen.blit(surf, (0, 0))
        pygame.display.update()
        self.clock.tick(self.time_step)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        KeysPressed.LEFT = 1
                    if event.key == K_RIGHT:
                        KeysPressed.RIGHT = 1
                    if event.key == K_UP:
                        KeysPressed.UP = 1
                    if event.key == K_DOWN:
                        KeysPressed.DOWN = 1
                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        KeysPressed.LEFT = 0
                    if event.key == K_RIGHT:
                        KeysPressed.RIGHT = 0
                    if event.key == K_UP:
                        KeysPressed.UP = 0
                    if event.key == K_DOWN:
                        KeysPressed.DOWN = 0
            self.update_game()


# def test_collision(obj: GameObject,
#                    other_obj: list[GameObject]):
#     collides = []
#     for other in other_obj:
#         if obj.rect.colliderect(other.rect):
#             collides.append(other)
#     return collides




class KeysPressed:
    LEFT = 0
    RIGHT = 0
    UP = 0
    DOWN = 0


class GamePhysics:
    GRAVITY = 1


class GameProp:
    TILE_SIZE = 16


if __name__ == '__main__':
    print(KeysPressed.DOWN)
    KeysPressed.DOWN = True
    print(KeysPressed.DOWN)




