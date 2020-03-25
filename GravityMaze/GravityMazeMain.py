#Import and Setup-------------------------------------------------------------------------------------------
import datetime
import MakeGrid
import math as m
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame as p
import random as r
import sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (0,30)
p.init()
p.display.set_caption('Gravity Maze')

#Tweakable Variables----------------------------------------------------------------------------------------
screenWidth, screenHeight = 1920, 1080

#Classes----------------------------------------------------------------------------------------------------

#Variable Initialization------------------------------------------------------------------------------------
BLACKISH = [50,50,50]
clock = p.time.Clock()
direction = 'none'
FINISH = [50,250,50]
PLAYER = [100,150,200]
RED = [250,50,50]
squareWidth = round(screenWidth/18)
squareHeight = round(screenHeight/9)
vel = 0,0
w = p.display.set_mode((screenWidth,screenHeight))
WHITE = [255,255,255]

#Functions--------------------------------------------------------------------------------------------------
def ChangeDirection(s1):
    global direction, xMax, yMax, vel
    direction = s1
    vel = 0,0
    xMax, yMax = round(pos[0]), round(pos[1])
    while -1<xMax<18 and -1<yMax<9 and grid[yMax][xMax] != 1:
        xMax += (direction=='right') - (direction=='left')
        yMax += (direction=='down') - (direction=='up')
    xMax -= (direction=='right') - (direction=='left')
    yMax -= (direction=='down') - (direction=='up')

def DrawAll():
    global grid, positions
    finishLinePos = 'none'
    for y, horizontal in enumerate(grid):
        for x, point in enumerate(horizontal):
            if point == 2:
                finishLinePos = (x,y)
                break
        if finishLinePos != 'none':
            break
    w.fill(WHITE)
    #Blocks
    for y, horizontal in enumerate(grid):
        for x, point in enumerate(horizontal):
            if point == 1: #If block
                p.draw.rect(w, BLACKISH, (XToScreenX(x),YToScreenY(y),squareWidth,squareHeight))
            if point == 2: #If finish line
                p.draw.rect(w, FINISH, (XToScreenX(x)+1,YToScreenY(y)+1,squareWidth-1,squareHeight-1))
    #Horizontal grid lines
    for i in range(9):
        y = YToScreenY(i)
        p.draw.line(w, BLACKISH, (0,y), (screenWidth,y));
    #Vertical grid lines
    for i in range(18):
        x = XToScreenX(i)
        p.draw.line(w, BLACKISH, (x,0), (x,screenHeight));
    #Player
    p.draw.rect(w, PLAYER, (XToScreenX(pos[0])+1,YToScreenY(pos[1])+1,squareWidth-1,squareHeight-1))
    p.display.update()

def PlayerStop():
    global direction, pos, vel, xMax, yMax
    if MakeGrid.AmAtEdge((xMax, yMax)):
        Reset()
    pos = xMax, yMax
    vel = 0,0
    direction = 'none'

def Reset():
    global direction, pos, startPos, vel
    direction, pos, vel = 'none', startPos, (0,0)

def Start():
    global direction, finishLinePos, grid, pos, startPos, vel
    direction, vel = 'none', (0,0)
    grid = MakeGrid.GetGrid()
    while grid=='too easy' or grid=='impossible':
        print(grid)
        grid = MakeGrid.GetGrid()
    for y, horizontal in enumerate(grid):
        for x, square in enumerate(horizontal):
            if square == 2:
                finishLinePos = (x,y)
            elif square == 3:
                startPos = pos = (x,y)

def UpdatePlayerPos():
    global direction, pos, vel, xMax, yMax
    if direction == 'none':
        xMax, yMax = 0,0
    if direction == 'left':
        if pos[0] + (vel[0]-0.01) > xMax:
            vel = (vel[0] - 0.01, 0)
        else:
            PlayerStop()
    elif direction == 'right':
        if pos[0] + (vel[0]+0.01) < xMax:
            vel = (vel[0] + 0.01, 0)
        else:
            PlayerStop()
    elif direction == 'up':
        if pos[1] + (vel[1]-0.01) > yMax:
            vel = (0, vel[1] - 0.01)
        else:
            PlayerStop()
    elif direction == 'down':
        if pos[1] + (vel[1]+0.01) < yMax:
            vel = (0, vel[1] + 0.01)
        else:
            PlayerStop()
    pos = (pos[0]+vel[0], pos[1]+vel[1])
    if MakeGrid.AmAtEdge(pos):
        Reset()

def XToScreenX(x):
    return screenWidth*(x/18)

def YToScreenY(y):
    return screenHeight*(y/9)

#Start------------------------------------------------------------------------------------------------------
Start()

#Main Loop--------------------------------------------------------------------------------------------------
stop = False
while not stop:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            stop = True
        if event.type == p.KEYDOWN:
            keys = p.key.get_pressed()
            if keys[p.K_n]:
                Start()
            if keys[p.K_r]:
                Reset()
            if vel == (0,0):
                if keys[p.K_LEFT]:
                    ChangeDirection('left')
                elif keys[p.K_RIGHT]:
                    ChangeDirection('right')
                elif keys[p.K_UP]:
                    ChangeDirection('up')
                elif keys[p.K_DOWN]:
                    ChangeDirection('down')
    UpdatePlayerPos()
    if (round(pos[0]), round(pos[1])) == finishLinePos:
        Start()
    DrawAll()
p.quit()

#Useful Syntax----------------------------------------------------------------------------------------------
#font = p.font.Font('C:\Windows\Fonts\Arial.ttf', 12)
#text = font.render(s1, True, [255,255,255]) 
#w.blit(text, (x-text.get_width()//2,y-text.get_height()//2))