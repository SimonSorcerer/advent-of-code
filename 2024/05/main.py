import re;
from tree import Node;

filename = 'input.txt'

def parse_line(line):
    return list(map(int, re.findall(r'\d+', line)));

def customCompare(a, b, rules):
    for rule in rules:
        if rule[0] == a and rule[1] == b:
            return -1
        if rule[0] == b and rule[1] == a:
            return 1
        
def getCorrectOrder(update, rules):
    compareFn = lambda a, b : customCompare(a, b, rules)
    for index, number in enumerate(update):
        if index == 0:
            root = Node(number, compareFn)
        else:
            root.insert(number)

    return list(root.inorderTraversal(root))

def getMiddleElement(list):
    # works only for odd-length lists!!!
    middleIndex = int((len(list) - 1) / 2)
    return list[middleIndex]

def getMiddleSums(updates, rules):
    correctOrdersSum = 0
    incorrectOrdersSum = 0

    for update in updates:
        correctOrder = getCorrectOrder(update, rules)

        if correctOrder == update:
            correctOrdersSum += getMiddleElement(update)
        else:
            incorrectOrdersSum += getMiddleElement(correctOrder)
    return correctOrdersSum, incorrectOrdersSum

with open(filename, 'r') as f:
    rules = []
    updates = []

    for index, line in enumerate(f):
        numbers = parse_line(line)
        if len(numbers) == 2:
            rules.append(numbers)
        elif len(numbers) > 2:
            updates.append(numbers)

    resultA, resultB = getMiddleSums(updates, rules)

    print('Part 1:', resultA)
    print('Part 2:', resultB)