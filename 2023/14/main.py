import time;
from utils import rotate_matrix, detect_sequence
import numpy
import math

filename = 'input.txt'

class bcolors:
    LIGHT_RED = "\033[1;31m"
    DARK_GRAY = '\033[1;30m'
    LIGHT_GRAY = "\033[0;37m"
    ENDC = '\033[0m'

SYMBOLS = {
    'ground': '.',
    'rock': 'O',
    'beam': '#',
}

def visualize(space):
    for line in space:
        for char in line:
            if (char == SYMBOLS['rock']):
                print(bcolors.LIGHT_RED + char + bcolors.ENDC, end='')
            elif (char == SYMBOLS['beam']):
                print(bcolors.LIGHT_GRAY + char + bcolors.ENDC, end='')
            else: 
                print(bcolors.DARK_GRAY + char + bcolors.ENDC, end='')
        print('\n')

def parse_platform(file):
    platform = []
    for index, line in enumerate(file):
            platform.append([])
            for char in line.strip():
                platform[index].append(char)
    return platform

def tilt_row(row):
    tilted_row = []

    sub_rows = "".join(numpy.flip(row.copy())).split(SYMBOLS['beam'])
    for index, sub_row in enumerate(sub_rows):
        if (len(sub_row) != 0):
            sorted_sub = "".join(sorted(sub_row, reverse=True))
            sub_rows[index] = sorted_sub
            tilted_row.extend(sorted_sub)
        if (index != len(sub_rows) - 1):
            tilted_row.extend(SYMBOLS['beam'])

    return numpy.flip(tilted_row)
            
def tilt_platform(platform, rotation = 1):
    for _ in range(rotation):
        platform = rotate_matrix(platform)
    
    new_platform = []
    
    for line in platform:
        new_platform.append(tilt_row(line))

    for _ in range(rotation):
        new_platform = rotate_matrix(new_platform, True)
    return new_platform

def count_load(platform):
    result = 0
    size = len(platform)

    for index, line in enumerate(platform):
        for char in line:
            if (char == SYMBOLS['rock']):
                result += size - index
    return result

with open(filename, 'r') as f:
    result = 0
    result2 = 0
    platform = []

    startT = time.time()

    platform = parse_platform(f)
    new_platform = tilt_platform(platform, 1)

    visualize(new_platform)
    result = count_load(new_platform)

    print('-----------------------------')
    
    # PART 2
    cycles = 200 # has to be high enough to detect the sequence
    sequence = []

    for cycle in range(cycles):
        for i in range(1, 5):
            new_platform = tilt_platform(new_platform, i)
        
        sequence.append(count_load(new_platform))
    print('-----------------------------')

    sequence_start, sequence_length = detect_sequence(sequence)

    desired_cycle = 1000000000 - 1 # -1 because we start counting from 0
    result2 = sequence[sequence_start + (desired_cycle - sequence_start) % sequence_length]

    endT = time.time()
    
    print('time:', endT - startT)
    print('part 1:', result)
    print('part 2:', result2)