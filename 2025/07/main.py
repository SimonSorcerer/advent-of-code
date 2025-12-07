import re
import time

filename = 'input.txt'

START = 'S'
VOID = '.'
SPLITTER = '^'

def find_start(line):
    return line.find(START);

with open(filename, 'r') as f:
    part1result = 0
    part2result = 1

    start = time.time()

    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    start_position = find_start(lines[0])
    rays = set([start_position]) # rays currently active at this depth
    traversals = { start_position: 1 } # different ray paths to positions marked by key at current depth

    for depth in range(2, len(lines), 2):
        new_rays = set()
        
        for ray in rays:
            if lines[depth][ray] == SPLITTER:
                new_rays.add(ray - 1)
                new_rays.add(ray + 1)
                part1result += 1
                traversals[ray - 1] = traversals.get(ray - 1, 0) + traversals[ray]
                traversals[ray + 1] = traversals.get(ray + 1, 0) + traversals[ray]
                traversals[ray] = 0
            elif lines[depth][ray] == VOID:
                new_rays.add(ray)
        rays = new_rays
        part2result = sum(traversals.values())

    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)