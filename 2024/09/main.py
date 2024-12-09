from collections import deque
from colors import printC, YELLOW, WHITE
from part2 import unfrag, checkSumUnfraggedMemory

filename = 'input.txt'

def parse_line(line):
    return map(int,list(line));

def getFileCells(fileSize, index):
    stack = []
    for _ in range(0, fileSize):
        stack.append(index)
    return stack

def fileIndexes(files):
    stack = deque()
    for i, fileSize in enumerate(files):
        stack.extend(getFileCells(fileSize, i))
    return stack

def unwrap(memory):
    fileQ = fileIndexes(memory[0::2])

    stack = deque()
    for i, cellSize in enumerate(memory):
        isFile = i % 2 == 0

        for j in range(0, cellSize):
            if len(fileQ) == 0:
                return stack
            if isFile:
                stack.append(fileQ.popleft())
            else:
                stack.append(fileQ.pop())
    
    return stack

def checkSum(memoryQ):
    sum = 0
    for i, num in enumerate(memoryQ):
        sum += i * num
    return sum

def printMemory(memoryQ):
    copyQ = memoryQ.copy()
    lastFileIndex = 0
    color = WHITE

    while len(copyQ) > 0:
        fileIndex = copyQ.popleft()
        if (lastFileIndex != fileIndex):
            color = YELLOW if color == WHITE else WHITE
            lastFileIndex = fileIndex
        printC(color, str(fileIndex), '')
    print(' ')

with open(filename, 'r') as f:
    memory = []

    for index, line in enumerate(f):
        memory += parse_line(line.strip())

    memoryQ = unwrap(memory)
    unfragged = unfrag(memory)

    resultA = checkSum(memoryQ)
    resultB = checkSumUnfraggedMemory(unfragged)

    print('Part 1:', resultA)
    print('Part 2:', resultB)