from enum import Enum
from GravityMaze import MakeGrid as make_g


class Direction(Enum):
    UP = 1
    DOWN = -1
    RIGHT = 2
    LEFT = -2

    @staticmethod
    def get_opposite(direction):
        return Direction(-direction.value)


class GravityGame:

    def __init__(self, columns, rows):
        self.grid = make_g.get_grid(columns, rows)
        self.player_pos = (0, 0)  # TODO start player in reasonable position
        self.player_velocity = (0, 0)  # TODO arbitrary #
        self.direction = None


