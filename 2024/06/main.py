from colors import printC, RED, GREEN, WHITE, YELLOW

filename = 'input.txt'

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

def isObstacle(map, position, extra_obstacle = None):
    return position == extra_obstacle or map[position[1]][position[0]] == OBSTACLE

def fast_move_guard(map, guard, extra_obstacle = None):
    position, direction = guard
    dx, dy = GUARD_MOVES[direction]
    new_position = (position[0] + dx, position[1] + dy)

    if not is_in_map(map, new_position):
        return None, None
    
    if isObstacle(map, new_position, extra_obstacle):
        guard_update = (position, turn_guard(direction))
        return None, guard_update
    
    visited = new_position
    guard_update = (new_position, direction)

    return visited, guard_update

def get_initial_guard(map):
    guard_position = get_guard_position(map)
    guard_direction = map[guard_position[1]][guard_position[0]]
    return (guard_position, guard_direction)

def get_visited(map):
    visited = set([])
    guard = get_initial_guard(map)

    while True:
        new_visited, updated_guard = fast_move_guard(map, guard)
        if updated_guard == None:
            break
        if new_visited != None:
            visited.add(new_visited)
        guard = updated_guard

    return visited

def detect_loop(map, extra_obstacle):
    initial_guard = get_initial_guard(map)
    first_iteration = True
    guard1 = initial_guard
    guard2 = initial_guard

    while guard1 != guard2 or first_iteration:
        _, new_guard_1 = fast_move_guard(map, guard1, extra_obstacle)
        _, new_guard_2 = fast_move_guard(map, guard2, extra_obstacle)
        if not new_guard_2: return False
        _, new_guard_2 = fast_move_guard(map, new_guard_2, extra_obstacle)
        if not new_guard_2: return False
        guard1 = new_guard_1
        guard2 = new_guard_2
        first_iteration = False
    
    return True

def count_loop_variants(map):
    loop_variants = 0
    initial_guard = get_initial_guard(map)
    loop_candidates = get_visited(map)

    for candidate in loop_candidates:
        if candidate == initial_guard[0]:
            continue
        if detect_loop(map, candidate):
            loop_variants += 1

    return loop_variants

with open(filename, 'r') as f:
    map = []

    for index, line in enumerate(f):
        map.append(parse_line(line.strip()))

    resultA = len(get_visited(map))
    resultB = count_loop_variants(map)

    print('Part 1:', resultA)
    print('Part 2:', resultB)