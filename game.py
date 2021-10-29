import pygame
import sys
from pygame.locals import *
from abc import ABC, abstractmethod
import settings
from settings import GameProperties
import level


class Game:

    def __init__(self,
                 title: str):

        self.title = title
        self.time_step = 60

        self.screen = pygame.display.set_mode((GameProperties.SCREEN_WIDTH, GameProperties.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = level.get_level(self, settings.get_level_map(), self.screen)

        # self.window_width = width
        # self.window_height = height
        # self.window_size = (self.window_width, self.window_height)
        #
        # self.display_width = int(self.window_width/2)
        # self.display_height = int(self.window_height/2)
        # self.display_size = (self.display_width, self.display_height)
        #
        # self.time_step = time_step
        #
        # pygame.init()
        #
        # self.clock = pygame.time.Clock()
        # self.level = level.get_level(settings.get_level_map(), self.)
        #
        # pygame.display.set_caption(self.title)
        #
        # self.screen = pygame.display.set_mode(self.window_size, 0, 32)
        # self.display = pygame.Surface(self.display_size)

    #     self.all_objects = pygame.sprite.Group()
    #
    # def add_object(self, obj):
    #     self.all_objects.add(obj)
    #
    # def add_objects(self, objs):
    #     for obj in objs:
    #         self.add_object(obj)

    # def remove_object(self):
    #     if obj not in self.objects:
    #         return
    #     self.objects.remove(obj)

    def update_game(self):
        self.screen.fill((0, 0, 0))
        self.level.run()

        pygame.display.update()
        self.clock.tick(self.time_step)

        # self.display.fill((150, 150, 150))
        # self.all_objects.update()
        # self.all_objects.draw(self.display)
        # surf = pygame.transform.scale(self.display, self.window_size)
        # self.screen.blit(surf, (0, 0))
        # pygame.display.update()
        # self.clock.tick(self.time_step)

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
                    if event.key == K_SPACE:
                        KeysPressed.JUMP = 1
                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        KeysPressed.LEFT = 0
                    if event.key == K_RIGHT:
                        KeysPressed.RIGHT = 0
                    if event.key == K_UP:
                        KeysPressed.UP = 0
                    if event.key == K_DOWN:
                        KeysPressed.DOWN = 0
                    if event.key == K_SPACE:
                        KeysPressed.JUMP = 0
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
    JUMP = 0


if __name__ == '__main__':
    print(KeysPressed.DOWN)
    KeysPressed.DOWN = True
    print(KeysPressed.DOWN)




