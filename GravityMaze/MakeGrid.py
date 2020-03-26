import random as r
from GravityMaze.Block import Block


def get_grid(columns, rows, prob=0.50):
    grid = {(x, y): Block(int(r.random() > prob)) for x in range(columns) for y in range(rows)}
    player_pos = (r.randint(0, columns), r.randint(0, rows))
    finish_pos = player_pos
    while finish_pos == player_pos:
        finish_pos = (r.randint(0, columns), r.randint(0, rows))
    grid[player_pos] = Block.Player
    grid[finish_pos] = Block.Finish
    return grid
