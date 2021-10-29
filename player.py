import pygame
import physics


class Player(pygame.sprite.Sprite):

    def __init__(self, game, pos):
        super().__init__()
        self.game = game

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect(topleft=pos)
        # self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

        self.physics = physics.get_game_object_physics('player', game, self.rect)

        # self.physics.set_movement(3, 5)

        # self.physics.bounce_border = dict(top=True,
        #                                   bottom=True,
        #                                   left=True,
        #                                   right=True)


    def update(self):
        self.physics.update()

        # self.physics.reset_movement()
        # self.physics.move_horizontal()
        # self.physics ._move_vertical()
        # self.physics.apply_gravity()
        # self.physics.jump()
        # self.physics.update()
        # self.physics.bounce_vertical()
        # self.physics.stop_border_bottom()
        # self.physics.stop_border_left()
        # self.physics.stop_border_top()
        # self.physics.stop_border_right()

    def draw(self, screen):
        screen.blit(self.image, self.physics.position)
        # pygame.draw.circle(screen, (200, 0, 0), (int(self.x), int(self.y)), self.radius)



