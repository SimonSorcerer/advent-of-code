import re;
import math;

filename = 'input.txt'

SAFE_SIZE = 100
START_POSITION = 50

def read_line(line):
    first, second = re.match(r'([LR])(\d+)', line).group(1, 2);
    return first, int(second)

def rotate_left(pt, value):
    return (pt - value) % SAFE_SIZE
def rotate_right(pt, value):
    return (pt + value) % SAFE_SIZE

def zero_passes(pos, dir, rotation):
    if (dir == 'R' or pos == 0):
        return math.floor((pos + rotation) / 100)
    else:
        return math.floor((100 - pos + rotation) / 100)

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    pos = START_POSITION

    for line in f:
        dir, value = read_line(line.strip())

        part2result += zero_passes(pos, dir, value)

        if dir == 'L':
            pos = rotate_left(pos, value)
        else:
            pos = rotate_right(pos, value)
        if pos == 0:
            part1result += 1

    print('Part 1:', part1result)
    print('Part 2:', part2result)