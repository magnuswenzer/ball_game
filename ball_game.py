from game import Game
from player import Player
from map import Map


class BallGame(Game):

    def __init__(self):
        width = 16 * 26 * 2
        height = 16 * 10 * 2
        time_step = 60
        title = 'The Ball Game'

        super().__init__(title, width, height, time_step)
        self.initialize()

    def initialize(self):
        self.add_object(Map(self))
        self.add_object(Player(self, 100, 100))


if __name__ == '__main__':
    game = BallGame()
    game.run()
