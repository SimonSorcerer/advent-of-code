from collections import deque

def annotate(memory):
    annotated = []
    for i, cellSize in enumerate(memory):
        isFile = i % 2 == 0
        fileIndex = int(i / 2) if isFile else '.'
        annotated.append((cellSize, fileIndex, False))
    return annotated

def findAvailableIndex(annotated, index):
    fileSize = annotated[index][0]

    for i in range(0, len(annotated)):
        (cellSize, cIndex, _) = annotated[i]
        if (cIndex == '.' and cellSize >= fileSize):
            return i
    return -1

def findNextMemoryIndexToPlace(annotated):
    for i in range(len(annotated) -1, 1, -1):
        isFile = annotated[i][1] != '.'
        placed = annotated[i][2]
        if (isFile and placed == False):
            return i
    return None

def joinEmptySpaces(annotated):
    for i in range(len(annotated) - 2, 0, -1):
        memoryBlock = annotated[i]
        nextMemoryBlock = annotated[i + 1]

        if (memoryBlock[1] == '.' and nextMemoryBlock[1] == '.'):
            annotated[i] = (memoryBlock[0] + nextMemoryBlock[0], '.', False)
            annotated.pop(i + 1)
        

def printAnnotated(annotated):
    for memoryBlock in annotated:
        length, fileIndex, placed = memoryBlock
        for j in range(length):
            print(fileIndex, end='')
    print(' ')

def unfrag(memory):
    annotated = annotate(memory)
    
    nextMemoryIndexToPlace = findNextMemoryIndexToPlace(annotated)
    debugCount = -1

    while (nextMemoryIndexToPlace != None and debugCount != 0):
        printAnnotated(annotated)
        debugCount -=1
        availableSpaceIndex = findAvailableIndex(annotated, nextMemoryIndexToPlace)
        
        if (availableSpaceIndex == -1 or availableSpaceIndex > nextMemoryIndexToPlace):
            annotated[nextMemoryIndexToPlace] = (annotated[nextMemoryIndexToPlace][0], annotated[nextMemoryIndexToPlace][1], True)
            nextMemoryIndexToPlace = findNextMemoryIndexToPlace(annotated)
            continue
        
        (fileSize, fileIndex, placed) = annotated[nextMemoryIndexToPlace]
        newEmptySpace = annotated[availableSpaceIndex][0] - fileSize
        annotated[nextMemoryIndexToPlace] = (fileSize, '.', False)

        if (newEmptySpace):
            annotated = annotated[:availableSpaceIndex] + [(fileSize, fileIndex, True)] + [(newEmptySpace, '.', False)] + annotated[availableSpaceIndex + 1:]
        else: 
            annotated = annotated[:availableSpaceIndex] + [(fileSize, fileIndex, True)] + annotated[availableSpaceIndex + 1:]
        
        joinEmptySpaces(annotated)
        nextMemoryIndexToPlace = findNextMemoryIndexToPlace(annotated)

    return annotated

def checkSumUnfraggedMemory(unfraggedMemory):
    checkSum = 0
    realIndex = 0

    for block in unfraggedMemory:
        (fileSize, fileIndex, _) = block
        for _ in range(fileSize):
            checkSum += realIndex * fileIndex if fileIndex != '.' else 0
            realIndex += 1
    return checkSum