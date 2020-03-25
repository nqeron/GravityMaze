import math as m
import numpy as np
import os
import random as r
import sys

def AddDirectionDuple(direction, pos):
    if direction=='left': return (pos[0]-1,pos[1])
    if direction=='right': return (pos[0]+1,pos[1])
    if direction=='up': return (pos[0],pos[1]-1)
    if direction=='down': return (pos[0],pos[1]+1)

def AmAtEdge(pos):
    if pos[0]==0 or pos[0]==17 or pos[1]==0 or pos[1]==8:
        return True
    else:
        return False

def AmPassedEdge(pos):
    if pos[0]==-1 or pos[0]==18 or pos[1]==-1 or pos[1]==9:
        return True
    else:
        return False

def CreateDirectionList(lastDirection):
    directionList = ['left', 'right', 'up', 'down']
    directionList.remove(lastDirection)
    directionList.remove(GetDirectionCounterpart(lastDirection))
    return directionList

def DoAnInstruction(directions, lastDirection, grid, i, pathPoints, pathPositions, pos):
    #Get a direction not in conflict with last direction
    pdirections, plastDirection, pgrid, ppathPoints, ppathPositions, ppos = directions, lastDirection, grid, pathPoints, pathPositions, pos
    direction = GetValidDirection(lastDirection, pos)
    #Go in direction until...
    stopMoving = False
    while stopMoving == False:
        #Go direction
        pos = AddDirectionDuple(direction, pos)\
        #Am at edge
        if AmAtEdge(pos):
            stopMoving = True
        #Am inside another block
        if grid[pos[1]][pos[0]]==1:
            stopMoving = True
        #Random chance of stopping
        if r.randint(1,100)>80:
            stopMoving = True
        #If its the first movement, keep moving
        if pos == AddDirectionDuple(direction, ppos):
            stopMoving = False
        #Also record position in path positions if not stopMoving
        if not stopMoving:
            pathPositions.append(pos)
    #If our position (which is where the block will be) isnt in the path
    if not pos in pathPositions:
        #Record block position in grid
        grid[pos[1]][pos[0]] = 1
        #Go back a square
        pos = SubtractDirectionDuple(direction, pos)
        #Record path point
        pathPoints.append(pos)
        #Record direction
        directions.append(direction)
        #If last then record finishLinePosition in grid
        if i == 7:
            grid[pos[1]][pos[0]] = 2
    #If it is in the path
    else:
        #Scrap this path and to a new one
        directions, direction, grid, pathPoints, pathPositions, pos = DoAnInstruction(pdirections, plastDirection, pgrid, i, ppathPoints, ppathPositions, ppos)
    return directions, direction, grid, pathPoints, pathPositions, pos

def GetDirectionCounterpart(direction):
    if direction=='left': return 'right'
    if direction=='right': return 'left'
    if direction=='up': return 'down'
    if direction=='down': return 'up'

def GetGrid():
    #Make blank grid
    directions, grid, pathPoints, pathPositions = [], [], [], []
    for i1 in range(9):
        horizontal = []
        for i2 in range(18):
            horizontal.append(0)
        grid.append(horizontal)
    #Pick start position and store it in the grid
    startPos = pos = r.randint(1,16), r.randint(1,7)
    grid[startPos[1]][startPos[0]] = 3
    lastDirection = 'none'
    #Make line segment (IN OTHER FUNCTION)
    for i in range(8):
        directions, lastDirection, grid, pathPoints, pathPositions, pos = DoAnInstruction(directions, lastDirection, grid, i, pathPoints, pathPositions, pos)
    #Create other blocks not in path
    for i in range(15):
        x, y = r.randint(0,17), r.randint(0,8)
        while grid[y][x] != 0 or (x,y) in pathPositions:
            x, y = r.randint(0,17), r.randint(0,8)
        grid[y][x] = 1
    #If impossible or too easy
    if TooEasy(grid, startPos):
        return 'too easy'
    elif TestRoute(directions, grid, startPos) != 'finish':
        return 'impossible'
    else:
        print(directions)
        return grid

def GetValidDirection(lastDirection, pos):
    choices = []
    if lastDirection!='left' and lastDirection!='right' and pos[0]!=1: choices.append('left')
    if lastDirection!='left' and lastDirection!='right' and pos[0]!=16: choices.append('right')
    if lastDirection!='up' and lastDirection!='down' and pos[1]!=1: choices.append('up')
    if lastDirection!='up' and lastDirection!='down' and pos[1]!=7: choices.append('down')
    return r.choice(choices)

def SubtractDirectionDuple(direction, pos):
    if direction=='left': return (pos[0]+1,pos[1])
    if direction=='right': return (pos[0]-1,pos[1])
    if direction=='up': return (pos[0],pos[1]+1)
    if direction=='down': return (pos[0],pos[1]-1)

def TestDirection(direction, grid, pos):
    die, finish, stopMoving = False, False, False
    while stopMoving == False:
        pos = AddDirectionDuple(direction, pos)
        if AmPassedEdge(pos):
            die = True
            stopMoving = True
            break
        if grid[pos[1]][pos[0]] == 1:
            pos = SubtractDirectionDuple(direction, pos)
            stopMoving = True
        if grid[pos[1]][pos[0]] == 2:
            finish = True
            stopMoving = True
    return die, finish, pos

def TestRoute(directions, grid, pos):
    for direction in directions:
        die, finish, pos = TestDirection(direction, grid, pos)
        if die or finish:
            break
    if die:
        return 'die'
    elif finish:
        return 'finish'
    else:
        return 'not solution'

def TooEasy(grid, startPos):
    for d1 in ['left','right','up','down']:
        for d2 in CreateDirectionList(d1):
            for d3 in CreateDirectionList(d2):
                for d4 in CreateDirectionList(d3):
                    for d5 in CreateDirectionList(d4):
                        for d6 in CreateDirectionList(d5):
                            for d7 in CreateDirectionList(d6):
                                if TestRoute([d1,d2,d3,d4,d5,d6,d7], grid, startPos) == 'finish':
                                    return True
    return False
