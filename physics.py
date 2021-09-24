
from game import KeysPressed
from game import GamePhysics


class Physics:
    """ Holds attributes and methods involving physical properties like position and movement etc. """
    game = None
    rect = None

    speed = None
    fall_factor = None
    x_momentum = None
    y_momentum = None

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

    def fall(self):
        self.y_momentum += self.fall_factor * GamePhysics.GRAVITY
        self.rect.y += self.y_momentum

    def bounce_vertical(self):
        print(self.bottom, self.game.display_height, self.game.window_height)
        if self.bottom > self.game.display_height:
            self.y_momentum = -self.y_momentum

    def move_horizontal(self):
        self.rect.x = self.rect.x + self.speed * KeysPressed.RIGHT - self.speed * KeysPressed.LEFT

    def move_vertical(self):
        self.rect.y = self.rect.y + self.speed * KeysPressed.DOWN - self.speed * KeysPressed.UP

    def stop_border_top(self):
        self.top = max(0, self.top)

    def stop_border_bottom(self):
        self.bottom = min(self.game.display_height, self.bottom)

    def stop_border_left(self):
        self.left = max(0, self.left)

    def stop_border_right(self):
        self.right = min(self.game.display_width, self.right)

    def is_colliding(self, other):
        if not self.rect.colliderect(other.rect):
            return False


class PlayerPhysics(Physics):
    def __init__(self, game, rect):

        self.game = game
        self.rect = rect

        self.speed = 5
        self.fall_factor = .5
        self.x_momentum = 0
        self.y_momentum = 0


class TilePhysics(Physics):
    def __init__(self, game, rect):

        self.game = game
        self.rect = rect


def get_game_object_physics(name, game, rect):
    all_objects = {'player': PlayerPhysics,
                   'tile': TilePhysics}
    obj = all_objects.get(name)
    if not obj:
        return
    return obj(game, rect)
