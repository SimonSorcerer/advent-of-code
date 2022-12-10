from collections import deque 

ADDX_DELAY = 2
NOOP_DELAY = 1

def parseLine(line):
    if line.startswith('addx'):
        instruction, val = line.split()
    else:
        instruction = 'noop'
        val = 0

    return instruction, int(val)

def tickWorker(worker):
    if len(worker) == 0:
        return

    next = worker[len(worker) - 1]
    next[0] = next[0] - 1

def readWorker(worker):
    update = worker.pop()

    if (update[0] == 0):
        return update[1]
    
    worker.append(update)
    return 0

def getSignalStrength(archive):
    CYCLE_STEP = 40
    result = 0

    for index, record in enumerate(archive):
        if (index - 20) % CYCLE_STEP == 0:
            result += index * record

    return result

def createArchive(lines):
    regX = 1
    archive = [1]
    worker = deque([])

    for line in lines:
        instruction, val = parseLine(line)

        tickWorker(worker)

        if instruction == 'addx':
            worker.appendleft([ADDX_DELAY, val])
        else: worker.appendleft([NOOP_DELAY, 0])

        regX += readWorker(worker)
        archive.append(regX)

    while len(worker) > 0:
        tickWorker(worker)
        regX += readWorker(worker)
        archive.append(regX)

    return archive

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    archive = createArchive(lines)
    print('Part 1:', getSignalStrength(archive))