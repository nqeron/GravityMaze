import pygame as py
import random as rand
from GravityMaze.GravityGame import GravityGame
from GravityMaze.Screen import Screen

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1080


def process_events():
    for event in py.event.get():
        if event.type == py.QUIT:
            return True


def run_game():
    py.init()
    py.display.set_caption("Gravity Maze")
    window = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gravity_game = GravityGame()
    screen = Screen(window, SCREEN_HEIGHT, SCREEN_WIDTH)
    clock = py.time.Clock()
    while True:
        clock.tick(60)
        break_out = process_events()
        if break_out:
            break
        screen.draw(gravity_game)
    py.quit()


if __name__ == '__main__':
    run_game()
