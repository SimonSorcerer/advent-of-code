def isInMap(map, x, y):
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[y])

def getScorePartial(map, x, y, deltaX, deltaY):
    score = 0
    max = int(map[y][x])
    xx = x + deltaX
    yy = y + deltaY

    while isInMap(map, xx, yy):
        treeSize = int(map[yy][xx])
        score += 1
        if (treeSize >= max):
            break   
        xx += deltaX
        yy += deltaY

    return score

def getScore(map, x, y):
    return getScorePartial(map, x, y, -1, 0) * getScorePartial(map, x, y, 1, 0) * getScorePartial(map, x, y, 0, -1) * getScorePartial(map, x, y, 0, 1)

with open('input.txt', 'r') as f:
    maxScore = 0
    map = f.read().splitlines()

    for indexY, line in enumerate(map):
        for indexX, char in enumerate(line):
            score = getScore(map, indexX, indexY)
            if score > maxScore:
                maxScore = score

    print('part2 :', maxScore)