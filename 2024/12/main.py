from copy import deepcopy
from colors import printC, WHITE, RED, YELLOW, BRIGHT_RED, LIGHT_GRAY, GREEN, BLUE, BRIGHT_MAGENTA, CYAN, MAGENTA

filename = 'test.txt'

def parse_line(line):
    return list(line);

def print_map(map):
    for i, line in enumerate(map):
        for j, cell in enumerate(line):
            code = ord(cell) - ord('A')
            colors = {
                0: WHITE,
                1: RED,
                2: YELLOW,
                3: BRIGHT_RED,
                4: LIGHT_GRAY,
                5: GREEN,
                6: BLUE,
                7: BRIGHT_MAGENTA,
                8: CYAN,
                9: MAGENTA,
            }
            
            printC(colors[code % 10], cell, '')
        print('')

LAND_CACHE = []

def is_in_map(map, position):
    x, y = position
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])

def floodfill(map, mark_map, position, target):
    land = 1
    fence = 0
    cells = []

    x, y = position
    if not is_in_map(map, position) or map[y][x] != target:
        return 0, 1, []
    
    if mark_map[y][x] == True:
        return 0, 0, []
    
    mark_map[y][x] = True
    
    landA, fenceA, cellsA = floodfill(map, mark_map, (x + 1, y), target)
    landB, fenceB, cellsB = floodfill(map, mark_map, (x - 1, y), target)
    landC, fenceC, cellsC = floodfill(map, mark_map, (x, y + 1), target)
    landD, fenceD, cellsD = floodfill(map, mark_map, (x, y - 1), target)

    land_count = land + landA + landB + landC + landD
    fence_count = fence + fenceA + fenceB + fenceC + fenceD
    new_cells = cells + [position] + cellsA + cellsB + cellsC + cellsD

    return land_count, fence_count, new_cells

def get_land_limits(land_map):
    min_x = min(land_map, key=lambda pos: pos[0])[0]
    min_y = min(land_map, key=lambda pos: pos[1])[1]
    max_x = max(land_map, key=lambda pos: pos[0])[0]
    max_y = max(land_map, key=lambda pos: pos[1])[1]

    return min_x, min_y, max_x, max_y

def add_tuples(a, b):
    return tuple(map(lambda i, j: i + j, a, b))

def find_first_wall_hit(cells, start_pos, direction):
    new_pos = add_tuples(start_pos, direction)
    current_pos = start_pos

    while new_pos in cells:
        current_pos = new_pos
        new_pos = add_tuples(current_pos, direction)
    
    return current_pos

def right_hand_dir(direction):
    # (0, -1) -> (1, 0)
    # (1, 0) -> (0, 1)
    # (0, 1) -> (-1, 0)
    # (-1, 0) -> (0, -1)
    return (-direction[1], direction[0])

def left_hand_dir(direction):
    # (0, -1) -> (-1, 0)
    # (1, 0) -> (0, -1)
    # (0, 1) -> (1, 0)
    # (-1, 0) -> (0, 1)
    return (direction[1], -direction[0])

def check_right_side_for_wall(cells, position, direction):
    right_hand_pos = add_tuples(position, right_hand_dir(direction))
    
    if (right_hand_pos in cells):
        return False
    return right_hand_pos

def follow_walls(cells):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    current_pos = find_first_wall_hit(cells, cells[0], directions[0])
    current_dir = directions[1]
    wall_cells = set([])
    wall_switches = 0
    right_hand_wall = check_right_side_for_wall(cells, current_pos, current_dir)

    print("Starting position:", current_pos, "Starting direction:", current_dir, "Right hand wall:", right_hand_wall)
    
    debug_limit = 9000
    # find the outer walls of the land plot
    while (right_hand_wall, current_dir) not in wall_cells and debug_limit > 0:        
        # if there is no wall we need to turn clockwise to follow the wall
        if right_hand_wall == False:
            print("WE TURN RIGHT (+1)")
            current_dir = right_hand_dir(current_dir)
            wall_switches += 1
        # we don't need to turn
        else:
            wall_cells.add((right_hand_wall, current_dir))

        next_pos = add_tuples(current_pos, current_dir)

        # if we hit a wall, we need to turn counter-clockwise
        degub_limit = 3
        while degub_limit > 0:
            next_pos = add_tuples(current_pos, current_dir)

            if next_pos in cells:
                break

            print("WE TURN LEFT (+1)")
            wall_cells.add((next_pos, current_dir))
            current_dir = left_hand_dir(current_dir)
            wall_switches += 1
            degub_limit -= 1
        
        
        # move forward
        current_pos = next_pos
        print("WE MOVE TO:", current_pos)
        right_hand_wall = check_right_side_for_wall(cells, current_pos, current_dir)
        print("Right hand wall:", right_hand_wall, current_dir)
        debug_limit -= 1
        if (right_hand_wall, current_dir) in wall_cells:
            print("We finish because right hand wall already marked")
    
    print("Outer walls:", len(wall_cells), " - ", wall_cells, "Wall switches:", wall_switches)

    return wall_switches

def count_inner_walls(cells):
    inner_walls = 0
    min_x, min_y, max_x, max_y = get_land_limits(cells)

    border_cells = set([])
    for y in range(min_y + 1, max_y):
        for x in range(min_x + 1, max_x):
            border_cells.add((x, y))

    for cached_land in LAND_CACHE:
        cached_cells = set(cached_land[2])
        if set(cached_cells) < border_cells:
            inner_walls += cached_land[3]

    return inner_walls

def get_cost(land_map):
    mark_map = deepcopy(land_map)
    cost = 0
    discount_cost = 0

    for y in range(len(land_map)):
        for x in range(len(land_map[0])):
            if mark_map[y][x] != True:
                land, fence, cells = floodfill(land_map, mark_map, (x, y), land_map[y][x])
                outer_walls = follow_walls(cells)
                
                LAND_CACHE.append((land, fence, cells, outer_walls, land_map[y][x]))
                # print("Adding land:", land, "Fence", fence, "Cells", cells, "Outer walls", outer_walls)

    for cached_plot in LAND_CACHE:
        outer_walls = cached_plot[3]
        fence = cached_plot[1]
        cells = set(cached_plot[2])
        land_size = cached_plot[0]
        letter = cached_plot[4]
        walls = outer_walls + count_inner_walls(cells)
        
        plot_cost = land_size * fence
        cost += plot_cost
        # print(letter, '- Land:', land_size, 'Fence:', fence, 'Cost:', plot_cost)

        discounted_plot_cost = land_size * walls
        discount_cost += discounted_plot_cost
        print(letter, '- Land:', land_size, 'Walls:', walls, 'Discounted cost:', discounted_plot_cost)

    return cost, discount_cost

with open(filename, 'r') as f:
    land_map = []

    for index, line in enumerate(f):
        land_map.append(parse_line(line.strip()))

    print_map(land_map)
    cost, discount_cost = get_cost(land_map)

    resultA = cost
    resultB = discount_cost

    print('Part 1:', resultA)
    print('Part 2:', resultB)