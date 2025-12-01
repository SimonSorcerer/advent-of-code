from colors import printC, WHITE, RED, YELLOW

filename = 'input.txt'

EMPTY_CELL = '.'
WALL = '#'
START = 'S'
END = 'E'

def parse_line(line):
    return list(line);

def print_map(map, antinodes = []):
    for i, line in enumerate(map):
        for j, cell in enumerate(line):
            if cell != EMPTY_CELL:
                printC(RED, cell, '')
            elif (j, i) in antinodes:
                printC(YELLOW, '#', '')
            else:
                printC(WHITE, cell, '')
        print('')

with open(filename, 'r') as f:
    map = []

    for index, line in enumerate(f):
        map.append(parse_line(line.strip()))

    resultA = 0
    resultB = 0

    print('Part 1:', resultA)
    print('Part 2:', resultB)