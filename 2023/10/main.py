import math;
import time;
import sys;

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

sys.setrecursionlimit(10000)
filename = 'input.txt'

SYMBOLS = {
    'start': 'S',
    'ground': '.',
    'pipe': '┼',
    'flood': '░',
    'hiding_spot': 'x'
}

DIRECTIONS = ['north', 'east', 'south', 'west']

LOOK_AHEAD = {
    'north': (0, -1),
    'east': (1, 0),
    'south': (0, 1),
    'west': (-1, 0),
}

PIPE_RULES_FROM = {
    'north': {
        '|': (0, 1),
        'L': (1, 0),
        'J': (-1, 0),
    },
    'east': {
        '-': (-1, 0),
        'L': (0, -1),
        'F': (0, 1),
    },
    'south': {
        '|': (0, -1),
        '7': (-1, 0),
        'F': (1, 0),
    },
    'west': {
        '-': (1, 0),
        'J': (0, -1),
        '7': (0, 1),
    },
}

def sum_tuples(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

def find_first_symbol(file, symbol = SYMBOLS['start']):
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == symbol:
                return x, y
    return None

def is_pipe(symbol):
    return symbol in ['|', '-', '7', 'L', 'J', 'F']

def is_ascii_pipe(symbol):
    return symbol in ['└', '┘', '┐', '┌', '|', '-', 'S']

def can_move(file, look_ahead_position, from_direction):
    symbol = get_symbol(file, look_ahead_position)
    return is_pipe(symbol) and symbol in PIPE_RULES_FROM[from_direction]

def get_symbol(file, position):
    x, y = position
    if y >= 0 and y < len(file) and x >= 0 and x < len(file[y]):
        return file[y][x]
    else:
        return SYMBOLS['ground']

def find_open_pipes(file):
    start = find_first_symbol(file)
    results = []

    for direction in DIRECTIONS:
        look_ahead_position = sum_tuples(start, LOOK_AHEAD[direction])
        if can_move(file, look_ahead_position, get_opposite_direction(direction)):
            results.append((look_ahead_position, get_opposite_direction(direction)))

    return results

def get_opposite_direction(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) + 2) % len(DIRECTIONS)]

def get_other_pipe_direction(from_direction, pipe):
  if pipe in ['|', '-']:
    return from_direction
  elif pipe == 'L' and from_direction in ['north', 'east']:
    return 'south' if from_direction == 'east' else 'west'
  elif pipe == '7' and from_direction in ['south', 'west']:
    return 'north' if from_direction == 'west' else 'east'
  elif pipe == 'J' and from_direction in ['north', 'west']:
    return 'south' if from_direction == 'west' else 'east'
  elif pipe == 'F' and from_direction in ['east', 'south']:
    return 'west' if from_direction == 'south' else 'north'
  
def get_ascii_symbol(symbol):
    if symbol == 'L':
        return '└'
    elif symbol == 'J':
        return '┘'
    elif symbol == '7':
        return '┐'
    elif symbol == 'F':
        return '┌'
    else:
        return symbol

def traverse_pipes(file, current_position, from_direction):
    counter = 0
    dirty_map = []

    while file[current_position[1]][current_position[0]] != SYMBOLS['start']:
        dirty_map.append((current_position, from_direction, get_ascii_symbol(get_symbol(file, current_position))))
        symbol = get_symbol(file, current_position)
        # print('before:', symbol, 'from_direction:', from_direction, 'current_position:', current_position)
        current_position = sum_tuples(current_position, PIPE_RULES_FROM[from_direction][symbol])
        from_direction = get_other_pipe_direction(from_direction, symbol)
        # print('from_direction:', from_direction, 'current_position:', current_position)
        counter += 1

    return counter, dirty_map

def is_within_bounds(matrix, position):
    x, y = position
    return x >= 0 and x < len(matrix[0]) and y >= 0 and y < len(matrix)

def is_floodable(matrix, position):
    x, y = position

    if (is_within_bounds(matrix, position)):
        is_not_pipe = is_ascii_pipe(matrix[y][x]) == False
        is_not_flooded = matrix[y][x] != SYMBOLS['flood']
        is_not_hiding_spot = matrix[y][x] != SYMBOLS['hiding_spot']
        return is_not_pipe and is_not_flooded and is_not_hiding_spot
    
    return False

def flood_fill(matrix, position, symbol = SYMBOLS['flood']):
    x, y = position
    if (is_floodable(matrix, position)):
        matrix[y][x] = symbol

    if (is_floodable(matrix, sum_tuples(position, (0, -1)))):
        flood_fill(matrix, sum_tuples(position, (0, -1)), symbol)
    if (is_floodable(matrix, sum_tuples(position, (1, 0)))):
        flood_fill(matrix, sum_tuples(position, (1, 0)), symbol)
    if (is_floodable(matrix, sum_tuples(position, (0, 1)))):
        flood_fill(matrix, sum_tuples(position, (0, 1)), symbol)
    if (is_floodable(matrix, sum_tuples(position, (-1, 0)))):
        flood_fill(matrix, sum_tuples(position, (-1, 0)), symbol)

    return matrix

def find_pipe_direction(position, dirty_map):
    x, y = position
    for (cx, cy), direction, symbol in dirty_map:
        if cx == x and cy == y:
            #print('coords:', cx, cy, 'direction:', direction)
            return direction
        
def find_pipe_symbol(position, dirty_map):
    x, y = position
    for (cx, cy), direction, symbol in dirty_map:
        if cx == x and cy == y:
            #print('coords:', cx, cy, 'direction:', direction)
            return symbol
        
def is_pipe_direction_correct(direction, pipe_from_direction):
    if direction == 'north':
        return pipe_from_direction in ['north', 'west']
    elif direction == 'east':
        return pipe_from_direction in ['north', 'east']
    elif direction == 'south':
        return pipe_from_direction in ['south', 'east']
    elif direction == 'west':
        return pipe_from_direction in ['south', 'west']

def is_within_loop(matrix, position, dirty_map):
    result = True
    for direction in DIRECTIONS:
        look_ahead_position = sum_tuples(position, LOOK_AHEAD[direction])
        while is_within_bounds(matrix, look_ahead_position) and not is_ascii_pipe(get_symbol(matrix, look_ahead_position)):
            look_ahead_position = sum_tuples(look_ahead_position, LOOK_AHEAD[direction])

        # print('look_ahead_position:', look_ahead_position, 'direction:', direction)
        if is_within_bounds(matrix, look_ahead_position):
            symbol = get_symbol(matrix, look_ahead_position)
            pipe_direction = find_pipe_direction(look_ahead_position, dirty_map)
            is_pipe_correct = is_pipe_direction_correct(direction, pipe_direction)
            # print('symbol:', symbol, 'pipe_direction:', pipe_direction, 'is_pipe_correct:', is_pipe_correct)
            if is_pipe(symbol) and not is_pipe_correct:
                result = False
                break
        else:
            result = False
            break
    
    return result                

def count_symbols(matrix, symbol):
    result = 0
    for row in matrix:
        for char in row:
            if char == symbol:
                result += 1
    return result

def visualize(matrix):
    print('\n')
    for line in matrix:
        for char in line:
            if (char == SYMBOLS['hiding_spot']):
                print(bcolors.WARNING + char + bcolors.ENDC, end='')
            elif (char == SYMBOLS['flood']):
                print(bcolors.OKBLUE + char + bcolors.ENDC, end='')
            else: 
                print(char, end='')
        print('\n')

with open(filename, 'r') as f:
    result = 0
    startT = time.time()
    
    matrix = [line.strip() for line in f]

    # for index, line in enumerate(f, 1):
    initials = find_open_pipes(matrix)
    initial_position, from_direction = initials[0]
    counter, dirty_map = traverse_pipes(matrix, initial_position, from_direction)
    dirty_map.append((find_first_symbol(matrix, SYMBOLS['start']), None, SYMBOLS['start']))
    dirty_map_coords = list(map(lambda x: x[0], dirty_map))
        
    # part 2
    clean_matrix = []
    for row in range(0, len(matrix)):
        clean_matrix.append([])
        for col in range(0, len(matrix[0])):
            if (col, row) not in dirty_map_coords:
                clean_matrix[row].append(SYMBOLS['ground'])
            else: 
                clean_matrix[row].append(find_pipe_symbol((col, row), dirty_map))

    #visualize(clean_matrix)

    flood_start = find_first_symbol(clean_matrix, SYMBOLS['ground'])
    while flood_start != None:
        if is_within_loop(clean_matrix, flood_start, dirty_map):
            print('hiding spot', flood_start)
            flood_fill(clean_matrix, flood_start, SYMBOLS['hiding_spot'])
        else:
            print('flood', flood_start)
            flood_fill(clean_matrix, flood_start)
        #visualize(clean_matrix)
        flood_start = find_first_symbol(clean_matrix, SYMBOLS['ground'])

    visualize(clean_matrix)
    endT = time.time()
    
    print('time:', endT - startT)
    print('part_1:', math.ceil(counter / 2))
    print('part 2:', count_symbols(clean_matrix, SYMBOLS['hiding_spot']))