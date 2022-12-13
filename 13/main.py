from collections import deque
import copy

def updateStack(stack):
    result = deque();
    item = stack.pop()

    while item != '[':
        result.appendleft(item)
        item = stack.pop()

    stack.append(result)

def parse(line):
    stack = deque()
    readingNumber = None
    
    for char in line:
        if not char.isnumeric() and readingNumber:
            stack.append(int(readingNumber))
            readingNumber = None
        if char == '[':
            stack.append('[')
        if char.isnumeric():
            if readingNumber:
                readingNumber += char
            else:
                readingNumber = char
        if char == ']':
            updateStack(stack)

    return stack

def getData(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    return lines
    
def compareStacks(stack1, stack2):
    result = 0

    while result == 0:
        if len(stack1) == 0 and len(stack2) == 0:
            return 0
        elif len(stack2) == 0:
            return -1
        elif len(stack1) == 0:
            return 1

        item1 = stack1.popleft()
        item2 = stack2.popleft()

        if item1 == None and item2 == None:
            result = 0
        elif item1 == None:
            result = 1
        elif item2 == None:
            result = -1
        else:
            if isinstance(item1, deque):
                if not isinstance(item2, deque):
                    result = compareStacks(item1, deque([item2]))
                else:
                    result = compareStacks(item1, item2)
            else:
                if isinstance(item2, deque):
                    result = compareStacks(deque([item1]), item2)
                else:
                    result = item2 - item1
        
    return result

def part1(lines):
    stack1 = None
    stack2 = None
    pairIndex = 1
    result = 0

    for line in lines:
        if line.startswith('['):
            if not stack1:
                stack1 = parse(line)
            elif not stack2:
                stack2 = parse(line)
        if stack1 and stack2:
            isInRightOrder = compareStacks(stack1, stack2) > 0    
            if isInRightOrder:
                result += pairIndex
            stack1 = None
            stack2 = None
            pairIndex += 1
            
    return result
    
def bubblySort(stackOstacks):
    stackSize = len(stackOstacks)

    for i in range(0, stackSize - 1):
        for j in range(0, stackSize - i - 1):
            if compareStacks(copy.deepcopy(stackOstacks[j + 1]), copy.deepcopy(stackOstacks[j])) > 0: 
                helper = stackOstacks[j]
                stackOstacks[j] = stackOstacks[j + 1]
                stackOstacks[j + 1] = helper

def part2(lines):
    two = deque([deque([2])])
    six = deque([deque([6])])
    stackOstacks = deque([two, six])
    result = 1

    for line in lines:
        if line.startswith('['):
            stack = parse(line)
            stackOstacks.append(stack)

    bubblySort(stackOstacks)

    for index, stack in enumerate(stackOstacks):
        if stack == two or stack == six:
            result *= index + 1
    
    return result

lines = getData('input.txt')
print('Part 1:', part1(lines))
print('Part 2:', part2(lines))