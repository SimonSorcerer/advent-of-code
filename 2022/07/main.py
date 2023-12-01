from anytree import Node, PreOrderIter, RenderTree, AsciiStyle

TOTAL_DISK_SIZE = 70000000
NEEDED_DISK_SIZE = 30000000

def changeDir(line):
    return line.strip()[5:]

def parseDir(line):
    return line.strip()[4:]

def parseFile(line):
    split = line.split()
    return split[0]

def setNode(nodeValue, parent):
    if parent:    
        return Node(nodeValue, parent=parent)
    else: 
        return Node(nodeValue)

def getDirSize(node):
    result = 0

    for node in PreOrderIter(node):
        value = node.name

        if value.isnumeric():
            result += int(value)

    return result

def getAllParents(node):
    parents = []
    currentNode = node

    while True:
        if currentNode.parent:
            parents.append(currentNode.parent)
            currentNode = currentNode.parent
        else:
            break

    return parents

def updateMap(sizeMap, keysToUpdate, value):
    for key in keysToUpdate:
        if not key in sizeMap:
            sizeMap[key] = 0
        sizeMap[key] += int(value)

def getFilteredSizeMap(sizeMap):
    filtered = {}

    for key in sizeMap.keys():
        if (sizeMap[key] <= 100000):
            filtered[key] = sizeMap[key]
    
    return filtered

def getSum(sizeMap):
    result = 0

    for val in sizeMap.values():
        result += val

    return result

def filterSizeMapByMinSize(sizeMap, minSize):
    filtered = {}

    for key in sizeMap.keys():
        if (sizeMap[key] >= minSize):
            filtered[key] = sizeMap[key]
    
    return filtered

def findSmallest(sizeMap):
    result = TOTAL_DISK_SIZE

    for val in sizeMap.values():
        if val < result:
            result = val
    
    return result


with open('input.txt', 'r') as f:
    root = None
    currentNode = None
    newDir = None

    # create tree
    for line in f:
        if line.startswith('$ cd'):
            nodeValue = changeDir(line)
            if nodeValue == '..':
                currentNode = currentNode.parent
            else:
                node = setNode(nodeValue, currentNode)
                currentNode = node
                if nodeValue == '/':
                    root = node
            
        if line.startswith('dir'):
            nodeValue = parseDir(line)
        
        if line[0].isdigit():
            nodeValue = parseFile(line)
            setNode(nodeValue, currentNode)

    sizeMap = {}
    nodesToUpdate = []

    for node in PreOrderIter(root):
        value = node.name
        parent = node.parent

        if value.isnumeric():
            keysToUpdate = getAllParents(node)
            updateMap(sizeMap, keysToUpdate, value)
    
    print(RenderTree(root, style=AsciiStyle()).by_attr())
    print('Part 1: ', getSum(getFilteredSizeMap(sizeMap)))

    freeSpace = TOTAL_DISK_SIZE - sizeMap[root]
    spaceToFree = NEEDED_DISK_SIZE - freeSpace
    
    print('Part 2: ', findSmallest(filterSizeMapByMinSize(sizeMap, spaceToFree)))