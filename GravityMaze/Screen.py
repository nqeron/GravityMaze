from enum import Enum

import pygame as py
from GravityMaze.GravityGame import GravityGame
from GravityMaze.Block import Block

BLACKISH = [50, 50, 50]
WHITE = [255, 255, 255]
FINISH = [50, 250, 50]
PLAYER = [100, 150, 200]


class Screen:

    def __init__(self, window: py.SurfaceType, height, width, columns=18, rows=9):
        self.window = window
        self.height = height
        self.width = width
        self.columns = columns
        self.rows = rows
        self.squareWidth = self.width/columns
        self.squareHeight = self.height/rows

    def draw(self, gravity_game: GravityGame):
        self.window.fill(WHITE)

        # draw horizontal/vertical lines
        for x in range(self.columns):
            x = self.x_to_screen_x(x)
            py.draw.line(self.window, BLACKISH, (x, 0), (x, self.height))
        for y in range(self.rows):
            y = self.y_to_screen_y(y)
            py.draw.line(self.window, BLACKISH, (0, y), (self.width, y))

        # draw game grid
        for pos in gravity_game.grid:
            if gravity_game.grid[pos] is Block.Empty:
                continue
            elif gravity_game.grid[pos] is Block.Filled:
                py.draw.rect(self.window, BLACKISH, (self.x_to_screen_x(pos[0]), self.y_to_screen_y(pos[1]),
                                                     self.squareWidth, self.squareHeight))
            elif gravity_game.grid[pos] is Block.Finish:
                py.draw.rect(self.window, FINISH, (self.x_to_screen_x(pos[0]), self.y_to_screen_y(pos[1]),
                                                   self.squareWidth, self.squareHeight))
            elif gravity_game.grid[pos] is Block.Player:
                py.draw.rect(self.window, PLAYER, (self.x_to_screen_x(pos[0]), self.y_to_screen_y(pos[1]),
                                                   self.squareWidth, self.squareHeight))
        py.display.update()

    def x_to_screen_x(self, x):
        return self.width*(x/self.columns)

    def y_to_screen_y(self, y):
        return self.height*(y/self.rows)
