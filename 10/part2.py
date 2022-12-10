from main import createArchive

CRT_WIDTH = 40
CRT_HEIGHT = 6

LIGHT_PIXEL = '#'
DARK_PIXEL = '.'

def getSpritePositions(center):
    return [center - 1, center, center + 1]

def getPixel(x, archive, time):
    spritePosition = getSpritePositions(archive[time])

    if x in spritePosition:
        return LIGHT_PIXEL

    return DARK_PIXEL


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    archive = createArchive(lines)
    time = 0

    for row in range(0, CRT_HEIGHT):
        print('/n')
        for col in range(0, CRT_WIDTH):
            time += 1
            print(getPixel(col, archive, time), end='')
