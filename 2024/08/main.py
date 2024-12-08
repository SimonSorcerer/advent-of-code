from colors import printC, WHITE, RED, YELLOW

filename = 'input.txt'

EMPTY_CELL = '.'

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

def is_in_map(map, position):
    x, y = position
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])

def get_signal_groups(map):
    signalGroups = {}
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] != EMPTY_CELL:
                signal = map[y][x]
                if signal not in signalGroups:
                    signalGroups[signal] = [(x, y)]
                else:
                    signalGroups[signal].append((x, y))
    return signalGroups

def get_antinode_candidates(map, signalA, signalB):
    candidates = []
    ax, ay = signalA
    bx, by = signalB

    v1 = (bx - ax, by - ay)
    v2 = (-v1[0], -v1[1])

    while is_in_map(map, (bx, by)):
        candidates.append((bx, by))
        bx += v1[0]
        by += v1[1]
    while is_in_map(map, (ax, ay)):
        candidates.append((ax, ay))
        ax += v2[0]
        ay += v2[1]
    return candidates

def get_antinodes_for_signals(map, signalA, signalB, repeating = False):
    ax, ay = signalA
    bx, by = signalB

    v1 = (bx - ax, by - ay)
    v2 = (-v1[0], -v1[1])

    candidates = [
        (bx + v1[0], by + v1[1]),
        (ax + v2[0], ay + v2[1]),
    ] if not repeating else get_antinode_candidates(map, signalA, signalB)

    filterLambda = lambda pos: is_in_map(map, pos)
    return list(filter(filterLambda, candidates))

def get_antinodes(map, repeating = False):
    antinodes = set([])
    signalGroups = get_signal_groups(map)

    for signal, positions in signalGroups.items():
        if len(positions) > 1:
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    antinodes.update(get_antinodes_for_signals(map, positions[i], positions[j], repeating))
    return antinodes

with open(filename, 'r') as f:
    map = []

    for index, line in enumerate(f):
        map.append(parse_line(line.strip()))

    antinodes = get_antinodes(map)
    #print_map(map, antinodes)

    antinodes2 = get_antinodes(map, repeating=True)
    print_map(map, antinodes2)

    resultA = len(antinodes)
    resultB = len(antinodes2)

    print('Part 1:', resultA)
    print('Part 2:', resultB)