import pygame as py
from GravityMaze.GravityGame import GravityGame

BLACKISH = [50, 50, 50]
WHITE = [255, 255, 255]


class Screen:

    def __init__(self, window: py.SurfaceType, height, width, columns=18, rows=9):
        self.window = window
        self.height = height
        self.width = width
        self.columns = columns
        self.rows = rows

    def draw(self, gravity_game: GravityGame):
        self.window.fill(WHITE)
        # py.draw.rect(self.window, BLACKISH, (100, 100, 400, 400))
        for x in range(self.columns):
            x = self.x_to_screen_x(x)
            py.draw.line(self.window, BLACKISH, (x, 0), (x, self.height))
        for y in range(self.rows):
            y = self.y_to_screen_y(y)
            py.draw.line(self.window, BLACKISH, (0, y), (self.width, y))
        py.display.update()

    def x_to_screen_x(self, x):
        return self.width*(x/self.columns)

    def y_to_screen_y(self, y):
        return self.height*(y/self.rows)
