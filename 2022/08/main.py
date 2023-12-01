def isInMap(map, x, y):
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[y])

def isVisiblePartial(map, x, y, deltaX, deltaY):
    result = True
    treeSize = map[y][x]
    xx = x + deltaX
    yy = y + deltaY

    while isInMap(map, xx, yy):
        if map[yy][xx] >= treeSize:
            result = False
            break
        xx += deltaX
        yy += deltaY

    return result

def isVisible(map, x, y):
    return isVisiblePartial(map, x, y, -1, 0) or isVisiblePartial(map, x, y, 1, 0) or isVisiblePartial(map, x, y, 0, -1) or isVisiblePartial(map, x, y, 0, 1)

with open('input.txt', 'r') as f:
    visibleTrees = 0
    visibleTrees2 = 0
    map = f.read().splitlines()

    for indexY, line in enumerate(map):
        for indexX, char in enumerate(line):
            if isVisible(map, indexX, indexY):
                visibleTrees += 1

    print('part 1:', visibleTrees)