import pygame
from game import GameObject
import physics


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.game = game

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        # self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

        self.physics = physics.get_game_object_physics('player', self.game, self.rect)

    def update(self):
        self.physics.move_horizontal()
        # self.physics ._move_vertical()
        self.physics.fall()
        self.physics.bounce_vertical()
        self.physics.stop_border_bottom()
        self.physics.stop_border_left()

    def draw(self, screen):
        screen.blit(self.image, self.physics.position)
        # pygame.draw.circle(screen, (200, 0, 0), (int(self.x), int(self.y)), self.radius)



