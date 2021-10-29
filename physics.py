import pygame

import game
import settings


class Physics:
    """ Holds attributes and methods involving physical properties like position and movement etc. """

    def __init__(self):
        # self.game = None
        self.rect = None

        self._pos = pygame.math.Vector2(0, 0)
        self._acc= pygame.math.Vector2(0, 0)
        self._vel = pygame.math.Vector2(0, 0)

        self.speed = 0
        self.jump_speed = 0
        self.fall_factor = 0
        self.slide = False

        self.move_direction = {}
        self.stop_border = {}
        self.bounce_border = {}

    @property
    def top(self):
        return self.rect.top

    @top.setter
    def top(self, value):
        self.rect.top = value

    @property
    def bottom(self):
        return self.rect.bottom

    @bottom.setter
    def bottom(self, value):
        self.rect.bottom = value

    @property
    def left(self):
        return self.rect.left

    @left.setter
    def left(self, value):
        self.rect.left = value

    @property
    def right(self):
        return self.rect.right

    @right.setter
    def right(self, value):
        self.rect.right = value

    @property
    def position(self):
        return self.rect.topleft

    def set_movement(self, x=None, y=None):
        self._movement.x = x or self._movement.x
        self._movement.y = y or self._movement.y

    def reset_movement(self):
        self._movement = pygame.math.Vector2(0, 0)

    def jump(self):
        self._movement.y += self.jump_speed * game.KeysPressed.JUMP

    def update(self):
        self._update_move_direction()
        self._update_gravity()
        self._calc_velocity()
        self._update_rect()
        self._update_stop_borders()
        self._update_bounce_border()

        # self.test_collision(self.game.all_objects)
        if not self.slide:
            self.reset_movement()
        print(self._velocity, self._acceleration)

    def _calc_velocity(self):
        self._velocity = self._movement + self._acceleration

    def _update_move_direction(self):
        if not self.move_direction:
            return
        if self.move_direction.get('left'):
            self._movement.x += -game.KeysPressed.LEFT * self.speed
        if self.move_direction.get('right'):
            self._movement.x += game.KeysPressed.RIGHT * self.speed
        if self.move_direction.get('up'):
            self._movement.y += -game.KeysPressed.UP * self.speed
        if self.move_direction.get('down'):
            self._movement.y += game.KeysPressed.DOWN * self.speed

    def _update_bounce_border(self):
        if not self.bounce_border:
            return
        if self.bounce_border.get('top') and self.top < 0:
            # self._movement.y *= -1
            self._velocity.y *= -1
            self.top = abs(self.top)
        if self.bounce_border.get('bottom') and self.bottom >= settings.GameProperties.SCREEN_HEIGHT:
            # self._movement.y *= -1
            self._velocity.y *= -1
            self.bottom = settings.GameProperties.SCREEN_HEIGHT - (self.bottom - settings.GameProperties.SCREEN_HEIGHT)
        if self.bounce_border.get('left') and self.left < 0:
            # self._movement.x *= -1
            self._velocity.x *= -1
            self.left = abs(self.left)
        if self.bounce_border.get('right') and self.right >= settings.GameProperties.SCREEN_WIDTH:
            # self._movement.x *= -1
            self._velocity.x *= -1
            self.right = settings.GameProperties.SCREEN_WIDTH - (self.right - settings.GameProperties.SCREEN_WIDTH)

    def _update_stop_borders(self):
        if not self.stop_border:
            return
        if self.stop_border.get('left'):
            self.left = max(0, self.left)
        if self.stop_border.get('right'):
            self.right = min(settings.GameProperties.SCREEN_WIDTH, self.right)
        if self.stop_border.get('top'):
            self.top = max(0, self.top)
        if self.stop_border.get('bottom'):
            self.bottom = min(settings.GameProperties.SCREEN_HEIGHT, self.bottom)
            if self.bottom == settings.GameProperties.SCREEN_HEIGHT:
                self._acceleration.y = 0

    def _update_gravity(self):
        if not self.fall_factor:
            return
        self._acceleration.y += self.fall_factor * settings.GamePhysics.GRAVITY

    def _update_rect(self):
        self.rect.topleft += self._velocity
        # self.rect.x += self._movement.x
        # self.rect.x += (self.movement.x + self.acceleration.x)
        # self.rect.y += self._movement.y
        # self.rect.y += (self._movement.y + self._acceleration.y)

    def test_collision(self, other_objects):
        self._test_collision_hotizontal(other_objects)

    def _test_collision_hotizontal(self, other_objects):
        for other in other_objects:
            if not self.rect.colliderect(other.rect):
                continue
            # if self.dx > 0:


class PlayerPhysics(Physics):
    def __init__(self, game, rect):
        super().__init__()

        self.game = game
        self.rect = rect

        # self.speed = 5
        # self.jump_speed = -15
        self.fall_factor = 1

        # self.move_direction = dict(right=True,
        #                            left=True,
        #                            up=True,
        #                            down=True)
        #
        # self.stop_border = dict(right=True)

        self.bounce_border = dict(bottom=True)


class TilePhysics(Physics):
    def __init__(self, game, rect):
        super().__init__()

        self.game = game
        self.rect = rect


def get_game_object_physics(name, game, rect):
    all_objects = {'player': PlayerPhysics,
                   'tile': TilePhysics}
    obj = all_objects.get(name)
    if not obj:
        return
    return obj(game, rect)
