def inSameRow(head, tail):
    return head['y'] == tail['y']

def inSameColumn(head, tail):
    return head['x'] == tail['x']

def isAdjacent(head, tail):
    return abs(head['x'] - tail['x']) <= 1 and abs(head['y'] - tail['y']) <= 1

def getDelta(a, b):
    delta = 0

    if a - b > 0:
        delta = 1
    elif a - b < 0:
        delta = -1
    
    return delta

def moveHead(head, direction):
    newHead = { 'x': head['x'], 'y': head['y'] }

    if direction == 'R':
        newHead['x'] += 1
    elif direction == 'L':
        newHead['x'] -= 1
    elif direction == 'U':
        newHead['y'] -= 1
    elif direction == 'D':
        newHead['y'] += 1
    
    return newHead

def moveTail(head, tail):
    newTail = { 'x': tail['x'], 'y': tail['y'] }
    deltaX = getDelta(head['x'], tail['x'])
    deltaY = getDelta(head['y'], tail['y'])

    if not isAdjacent(head, tail):
        if inSameRow(head, tail):
            newTail['x'] = tail['x'] + deltaX
        if inSameColumn(head, tail):
            newTail['y'] = tail['y'] + deltaY
        else:
            newTail['x'] = tail['x'] + deltaX
            newTail['y'] = tail['y'] + deltaY

    return newTail

def part1(lines):
    visitedPlaces = {}
    head = { 'x': 0, 'y': 0 }
    tail = { 'x': 0, 'y': 0 }

    for line in lines:
        direction, rep = line.split()
        
        for i in range(0, int(rep)):
            head = moveHead(head, direction)
            tail = moveTail(head, tail)
            visitedPlaces[str(tail['x']) + ':' + str(tail['y'])] = True

    return visitedPlaces

TAIL_COUNT = 9

def createTails(count):
    tails = []
    
    for i in range(0, count):
        tails.append({ 'x': 0, 'y': 0 })

    return tails

def part2(lines):
    visitedPlaces = {}
    head = { 'x': 0, 'y': 0 }
    tails = createTails(TAIL_COUNT)
    
    for line in lines:
        direction, rep = line.split()
        
        for i in range(0, int(rep)):
            head = moveHead(head, direction)
            tails[0] = moveTail(head, tails[0])
            for j in range(1, TAIL_COUNT):
                tails[j] = moveTail(tails[j - 1], tails[j])

            visitedPlaces[str(tails[8]['x']) + ':' + str(tails[8]['y'])] = True

    return visitedPlaces

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    print('Part 1:', len(part1(lines).keys()))
    print('Part 2:', len(part2(lines).keys()))