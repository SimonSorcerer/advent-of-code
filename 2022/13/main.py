def updateStack(stack):
    result = [];
    item = stack.pop()

    while item != '[':
        result.append(item)
        item = stack.pop()

    result.reverse()
    stack.append(result)

def parse(line):
    stack = []
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

    for index in range(max(len(stack1), len(stack2))):
        if result != 0:
            break
        if index >= len(stack1):
            return 1
        if index >= len(stack2):
            return -1
        
        item1, item2 = stack1[index], stack2[index]

        if type(item1) == list and type(item2) == list:
            result = compareStacks(item1, item2)
        elif type(item1) == int and type(item2) == list:
            result = compareStacks([item1], item2)
        elif type(item1) == list and type(item2) == int:
            result = compareStacks(item1, [item2])
        elif type(item1) == int and type(item2) == int:
            result = item2 - item1
        elif item1 == None and item2 != None:
            result = 1
        elif item1 != None and item2 == None:
            result = -1
        else:
            result = 0

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
            if compareStacks(stackOstacks[j + 1], stackOstacks[j]) > 0: 
                helper = stackOstacks[j]
                stackOstacks[j] = stackOstacks[j + 1]
                stackOstacks[j + 1] = helper

def part2(lines):
    two = [[2]]
    six = [[6]]
    stackOstacks = [two, six]
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