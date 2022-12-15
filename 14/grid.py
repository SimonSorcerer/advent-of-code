import sys
import operator
from colors import COLORS

AIR = '.'
ROCK = '#'
SAND = 'O'
SAND_SOURCE = '+'

def getData(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    return lines

def findBoundaries(data, mode = 1):
    boundX = { 'min': sys.maxsize , 'max': 0 }
    boundY = { 'min': 0, 'max': 0 }

    for row in data:
        for point in row:
            x, y = point
            boundX['min'] = min(x, boundX['min'])
            boundX['max'] = max(x, boundX['max'])
            boundY['max'] = max(y, boundY['max'])

    if mode == 2:
        boundX['min'] -= boundY['max'] + 1
        boundX['max'] += boundY['max'] + 1

    return boundX, boundY

def getDirection(point1, point2):
    p1x, p1y = point1
    p2x, p2y = point2

    dirX = 0 if p2x == p1x else 1 if p2x > p1x else -1
    dirY = 0 if p2y == p1y else 1 if p2y > p1y else -1

    return dirX, dirY

def getInterPoints(point1, point2, direction):
    points = [point1]
    interPoint = point1

    while True:
        interPoint = tuple(map(operator.add, interPoint, direction))
        points.append(interPoint)
        ix, iy = interPoint
        p2x, p2y = point2
        if ix == p2x and iy == p2y:
            break
    
    return points

def getRockPoints(points):
    result = []

    for i in range(1, len(points)):
        direction = getDirection(points[i - 1], points[i])
        result += getInterPoints(points[i -1], points[i], direction)

    return result


def placeRocks(grid, borderPoints, delta):
    points = getRockPoints(borderPoints)

    for point in points:
        x, y = point
        dx, dy = delta
        grid[y - dy][x - dx] = ROCK

def placeInGrid(grid, to, element):
    x, y = to
    grid[y][x] = element

def createGrid(data, mode = 1):
    grid = []

    boundX, boundY = findBoundaries(data, mode)
    deltaX, deltaY = boundX['min'], boundY['min']

    for y in range(boundY['max'] - deltaY + 1):
        grid.append([])
        for x in range(boundX['max'] - deltaX + 1):
            grid[y].append(AIR)

    for borderPoints in data:
        placeRocks(grid, borderPoints, (deltaX, deltaY))

    grid[0][500 - deltaX] = SAND_SOURCE

    if mode == 2:
        airRow, rockRow = [], []
        for x in range(boundX['max'] - deltaX + 1):
            airRow.append(AIR)
            rockRow.append(ROCK)
        grid.append(airRow)
        grid.append(rockRow)

    return grid

def printGrid(grid):
    print()
    for row in grid:
        for char in row:
            color = COLORS['ANSI_YELLOW']
            if char == ROCK:
                color = COLORS['ANSI_PURPLE']
            elif char == SAND:
                color = COLORS['ANSI_CYAN']
            
            print(color + char, end=' ')
        print(COLORS['ANSI_RESET'])
    print()