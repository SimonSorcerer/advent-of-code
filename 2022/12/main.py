from collections import deque

def isVisited(visited, position):
    for pos in visited:
        if pos == position:
            return True
    return False

def inMap(heightMap, position):
    x, y = position
    return x >= 0 and y >= 0 and x < len(heightMap[0]) and y < len(heightMap)

def getHeight(heightMap, position):
    x, y = position
    char = heightMap[y][x]

    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'

    return ord(char)

def canHike(heightMap, pos1, pos2):
    height1 = getHeight(heightMap, pos1)
    height2 = getHeight(heightMap, pos2)

    return height2 - 1 <= height1

def find(heightMap, char):
    for y in range(0, len(heightMap)):
        for x in range(0, len(heightMap[y])):
            if heightMap[y][x] == char:
                return x, y

def findAll(heightMap, char):
    results = set([])

    for y in range(0, len(heightMap)):
        for x in range(0, len(heightMap[y])):
            if heightMap[y][x] == char:
                results.add((x, y))

    return results

def traverse(heightMap, startPoints):
    hikeBest = None
    end = find(heightMap, 'E')

    for start in startPoints:
        visited = set([start])
        todo = deque([(start, [(list(visited), start)])])
        
        while len(todo) > 0:
            lastStep, steps = todo.popleft()
            for option in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dx, dy = option
                x, y = lastStep
                nextStep = x + dx, y + dy
                if inMap(heightMap, nextStep) and not isVisited(visited, nextStep) and canHike(heightMap, lastStep, nextStep):
                    if end == nextStep:
                        if hikeBest == None or hikeBest > len(steps):
                            hikeBest = len(steps)
                        todo.clear()
                    else:
                        visited.add(nextStep)
                        if hikeBest == None or len(steps) < hikeBest:
                            todo.append((nextStep, steps + [(list(visited), nextStep)]))

    return hikeBest

def getData(filename):
    data = []

    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            data.append([])
            for char in line:
                data[len(data) - 1].append(char)
    
    return data

def getStartPointsPart2(heightMap):
    lowestPoints = findAll(heightMap, 'a')
    lowestPoints.add(find(heightMap, 'S'))

    return lowestPoints
    
def part1(heightMap):
    start = find(heightMap, 'S')
    return traverse(heightMap, [start])

def part2(heightMap):
    startPoints = getStartPointsPart2(heightMap)
    return traverse(heightMap, startPoints)

heightMap = getData('input.txt')
print('Part 1:', part1(heightMap))
print('Part 2:', part2(heightMap))