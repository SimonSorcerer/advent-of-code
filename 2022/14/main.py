from grid import createGrid, printGrid, placeInGrid, AIR, SAND, SAND_SOURCE
import os

def parseLine(line):
    result = []
    coords = line.split(' -> ')

    for point in coords:
        x, y = point.split(',')
        result.append((int(x), int(y)))
    
    return result

def getData(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    return lines

def isInGrid(grid, pos):
    x, y = pos
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])

def moveGrain(grid, toPos):
    toX, toY = toPos

    if not isInGrid(grid, toPos):
        return True, False
    elif grid[toY][toX] == AIR:
        return False, True
    else:
        return False, False

def getSandSource(grid):
    x = 0
    for el in grid[0]:
        if el == SAND_SOURCE:
            return x, 0
        x += 1

def simulate(grid):
    inMotion = False
    sandGrainCount = 0
    outOfGrid = False
    sandSource = getSandSource(grid)
    sourceX, sourceY = sandSource
    sandX, sandY = None, None

    while not outOfGrid:
        if not inMotion:
            sandX, sandY = sourceX, sourceY
            sandGrainCount += 1
            inMotion = True
        else:
            for x, y in [(0, 1), (-1, 1), (1, 1)]:
                outOfGrid, inMotion = moveGrain(grid, (sandX + x, sandY + y))
                if outOfGrid:
                    break
                elif inMotion:
                    placeInGrid(grid, (sandX, sandY), AIR)
                    sandX += x
                    sandY += y
                    placeInGrid(grid, (sandX, sandY), SAND)
                    break
                elif not inMotion and sandX == sourceX and sandY == sourceY:
                    placeInGrid(grid, (sandX, sandY), SAND)
                    outOfGrid = True
    return sandGrainCount

def part1(lines):
    data = []
    result = 0

    for line in lines:
        data.append(parseLine(line))

    grid = createGrid(data)

    result = simulate(grid)
    printGrid(grid)

    return result - 1

def part2(lines):
    data = []
    result = 0

    for line in lines:
        data.append(parseLine(line))

    grid = createGrid(data, 2)

    result = simulate(grid)
    printGrid(grid)

    return result 

lines = getData('input.txt')
print('Part 1:', part1(lines))
print('Part 2:', part2(lines))