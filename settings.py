

def get_level_map():

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
        'XXXXXXXX  XXXXXX  XX XXXX']
    return level_map


class GamePhysics:
    GRAVITY = 1


class GameProperties:
    TILE_SIZE = 64
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 10 * TILE_SIZE