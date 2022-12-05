import re

def readStackLine(line):
    index = 0
    crates = []

    for index, char in enumerate(line):
        if char == '[':
            stackIndex = int(index / 4) + 1
            stackChar = line[index + 1]
            crates.append((stackIndex, stackChar))
    
    return crates

def readInstruction(line):
    result = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    return result.groups() 

def createStacks(crates):
    stacks = {}

    for index, row in enumerate(crates):
        for item in row:
            if item[0] in stacks: stacks[item[0]].insert(0, item[1])
            else: stacks[item[0]] = [item[1]]
    
    return stacks

def runInstruction9000(stacks, instruction):
    count = int(instruction[0])
    start = int(instruction[1])
    end = int(instruction[2])

    for i in range(count):
        crate = stacks[start].pop()
        stacks[end].append(crate)

def runInstruction9001(stacks, instruction):
    count = int(instruction[0])
    start = int(instruction[1])
    end = int(instruction[2])
    helperStack = []

    for i in range(count):
        crate = stacks[start].pop()
        helperStack.append(crate)
    
    for i in range(len(helperStack)):
        crate = helperStack.pop()
        stacks[end].append(crate)


def getTopCrates(stacks):
    result = ''
    index = 1

    while index in stacks:
        stack = stacks[index]
        result += stack.pop()
        index += 1

    return result

with open('input.txt', 'r') as f:
    crates = []
    instructions = []
    readingStack = True

    for line in f:
        if line.startswith(' 1'):
            readingStack = False
        
        if readingStack:
            crates.append(readStackLine(line))

        if line.startswith('move'):
            instructions.append(readInstruction(line))

    stackedCratesA = createStacks(crates)
    stackedCratesB = createStacks(crates)

    # print(instructions)
    # print(stackedCrates)

    for instruction in instructions:
        runInstruction9000(stackedCratesA, instruction)
        runInstruction9001(stackedCratesB, instruction)

    # print(stackedCratesA)
    # print(stackedCratesB)
    print(getTopCrates(stackedCratesA))
    print(getTopCrates(stackedCratesB))

