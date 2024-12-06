import copy
from colors import printC, RED, GREEN, WHITE, YELLOW

filename = 'test.txt'

OBSTACLE = '#'
EMPTY = '.'
VISITED = 'X'
GUARD = {
    'UP': '^',
    'RIGHT': '>',
    'DOWN': 'v',
    'LEFT': '<',
}

GUARD_MOVES = {
    GUARD['UP']: (0, -1),
    GUARD['DOWN']: (0, 1),
    GUARD['LEFT']: (-1, 0),
    GUARD['RIGHT']: (1, 0),
}

def parse_line(line):
    return list(line)

def print_map(map):
    for line in map:
        for cell in line:
            if cell == OBSTACLE:
                printC(RED, cell, '')
            elif cell == VISITED:
                printC(GREEN, cell, '')
            elif cell == EMPTY:
                printC(WHITE, cell, '')
            else:
                printC(YELLOW, cell,'')
        print('\n')

def get_guard_position(map):
    width = len(map[0])
    height = len(map)

    for y in range(height):
        for x in range(width):
            if map[y][x] in GUARD.values():
                return (x, y)
    return None

def is_in_map(map, position):
    x, y = position
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])

def turn_guard(guard):
    directions = [GUARD['UP'], GUARD['RIGHT'], GUARD['DOWN'], GUARD['LEFT']]
    return directions[(directions.index(guard) + 1) % 4]

def move_guard(map):
    guard_position = get_guard_position(map)
    current_guard = map[guard_position[1]][guard_position[0]]

    dx, dy = GUARD_MOVES[current_guard]
    new_guard_position = (guard_position[0] + dx, guard_position[1] + dy)

    if not is_in_map(map, new_guard_position):
        return False

    if map[new_guard_position[1]][new_guard_position[0]] == OBSTACLE:
        map[guard_position[1]][guard_position[0]] = turn_guard(current_guard)
        return new_guard_position

    map[guard_position[1]][guard_position[0]] = VISITED
    map[new_guard_position[1]][new_guard_position[0]] = current_guard

    return new_guard_position

def fast_move_guard(map, guard):
    position, direction = guard
    dx, dy = GUARD_MOVES[direction]
    new_position = (position[0] + dx, position[1] + dy)

    if not is_in_map(map, new_position):
        return False
    
    if map[new_position[1]][new_position[0]] == OBSTACLE:
        return [], position, turn_guard(direction)
    
    visited = [new_position]
    guard_update = (new_position, direction)

    return visited, guard_update


def play(map):
    map_copy = copy.deepcopy(map)

    while True:
        new_guard_position = move_guard(map_copy)
        if not new_guard_position:
            break

    return map_copy

def detect_loop(map):
    map_1 = copy.deepcopy(map)
    map_2 = copy.deepcopy(map)
    
    guard1 = (0, 0)
    guard2 = (0, 1)

    while not (guard1 == guard2 and guard1_direction == guard2_direction):
        move_guard(map_1)
        update_2 = move_guard(map_2)
        update_2 = move_guard(map_2)
        if not update_2:
            return False

        guard1 = get_guard_position(map_1)
        guard2 = get_guard_position(map_2)
        guard1_direction = map_1[guard1[1]][guard1[0]]
        guard2_direction = map_2[guard2[1]][guard2[0]]
    
    return True

def count_visited(map):
    result = 0
    visited_map = play(map)
    
    for line in visited_map:
        result += line.count(VISITED)

    # adding one for last position of the guard
    return result + 1

def get_loop_candidates(map):
    loop_candidates = []
    visited_map = play(map)

    for i, line in enumerate(visited_map):
        for j, cell in enumerate(line):
            if cell == VISITED or cell in GUARD.values():
                loop_candidates.append((j, i))

    return loop_candidates

def count_loop_variants(map):
    loop_variants = 0
    loop_candidates = get_loop_candidates(map)

    for candidate in loop_candidates:
        map_copy = copy.deepcopy(map)
        guard_position = get_guard_position(map_copy)

        if (guard_position != candidate):
            map_copy[candidate[1]][candidate[0]] = OBSTACLE

        if detect_loop(map_copy):
            # print('LOOP:', candidate)
            loop_variants += 1

    return loop_variants

with open(filename, 'r') as f:
    map = []

    for index, line in enumerate(f):
        map.append(parse_line(line.strip()))

    resultA = count_visited(map)
    resultB = count_loop_variants(map)

    print('Part 1:', resultA)
    print('Part 2:', resultB)