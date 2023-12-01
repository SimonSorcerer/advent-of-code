import re, math
from collections import deque

def getNumber(line):
    result = re.search(r'(\d+)', line)
    return int(result.group(1))

def getStartingItems(line):
    result = re.findall(r'(\d+)', line)
    reverse = deque(result[::-1])
    return reverse

def getOperation(line):
    result = re.search(r'Operation: new = (.*)', line)
    return result.group(1)


def createMonkey(index, startingItems, operation, test, testTrue, testFalse):
    return {
        'index': index,
        'items': startingItems,
        'operation': operation,
        'test': test,
        'testTrue': testTrue,
        'testFalse': testFalse,
        'inspections': 0
    }

def getMonkeys(filename):
    monkeys = []

    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        monkeyIndex = -1
        startingItems = [],
        operation = '',
        test, testTrue, testFalse = 0, 0, 0

        for line in lines:
            if line.startswith('Monkey'):
                monkeyIndex += 1
            if line.strip().startswith('Starting items:'):
                startingItems = getStartingItems(line)
            if line.strip().startswith('Operation:'):
                operation = getOperation(line)
            if line.strip().startswith('Test:'):
                test = getNumber(line)
            if line.strip().startswith('If true:'):
                testTrue = getNumber(line)
            if line.strip().startswith('If false:'):
                testFalse = getNumber(line)
                monkeys.append(createMonkey(monkeyIndex, startingItems, operation, test, testTrue, testFalse))
    
    return monkeys

def giveItemToMonkey(item, monkeys, monkeyIndex):
    #print(monkeys[monkeyIndex]['items'])
    monkeys[monkeyIndex]['items'].appendleft(item)
    #print(monkeys[monkeyIndex]['items'])

def playMonkeyRound(monkeys, relief, cm = None):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            old = int(monkey['items'].pop())
            operation = monkey['operation']
            # if operation == 'old * old':
            #     operation = 'old'
            wrap = eval('lambda old: ' + operation)
            if (relief > 1):
                new = math.floor(wrap(old) // relief)
            else:
                new = wrap(old)

            if cm:
                new = new % cm
            monkey['inspections'] += 1
            
            if new % monkey['test'] == 0:
                giveItemToMonkey(new, monkeys, monkey['testTrue'])
            else: 
                giveItemToMonkey(new, monkeys, monkey['testFalse'])

def getMonkeyBusiness(monkeys):
    inspections = []

    for monkey in monkeys:
        inspections.append(monkey['inspections'])

    inspections = sorted(inspections, reverse=True)

    return inspections[0] * inspections[1]

def part1():
    RELIEF = 3
    ROUNDS_TO_PLAY = 20
    monkeys = getMonkeys('test.txt')
    
    for i in range(0, ROUNDS_TO_PLAY):
        playMonkeyRound(monkeys, RELIEF)
    
    #print(monkeys)
    return getMonkeyBusiness(monkeys)

def getCommonMultiple(monkeys):
    result = 1

    for monkey in monkeys:
        result *= monkey['test']

    return result

def part2():
    RELIEF = 1
    ROUNDS_TO_PLAY = 10000
    monkeys = getMonkeys('input.txt')
    cm = getCommonMultiple(monkeys)

    for i in range(0, ROUNDS_TO_PLAY):
        playMonkeyRound(monkeys, RELIEF, cm)
    
    # print(monkeys)
    return getMonkeyBusiness(monkeys)

print('Part 1:', part1())
print('Part 2:', part2())
