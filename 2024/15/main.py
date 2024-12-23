from colors import printC, WHITE, RED, YELLOW

filename = 'input.txt'

INSTRUCTIONS = ['<', '>', '^', 'v']
ROBOT = '@'
BOX = 'O'
BOX_A = '['
BOX_B = ']'
WALL = '#'
EMPTY = '.'

def print_map(layout):
    for row in layout:
        for cell in row:
            if cell == ROBOT:
                printC(RED, cell, end='')
            elif cell == BOX or cell == BOX_A or cell == BOX_B:
                printC(YELLOW, cell, end='')
            elif cell == WALL:
                printC(WHITE, cell, end='')
            else:
                print(' ', end='')
        print()

def parse_file(file):
    layout = []
    instructions = []

    for _, line in enumerate(file):
        parsed = list(line.strip())
        if len(parsed) > 1:
            if parsed[0] in INSTRUCTIONS:
                instructions += parsed
            else:
                layout.append(parsed)
    
    return layout, instructions

def widen(layout):
    wide_layout = []

    for row in layout:
        wide_row = []
        for cell in row:
            if cell == ROBOT:
                wide_row += [ROBOT, EMPTY]
            elif cell == BOX:
                wide_row += [BOX_A, BOX_B]
            elif cell == WALL:
                wide_row += [WALL, WALL]
            elif cell == EMPTY:
                wide_row += [EMPTY, EMPTY]
        wide_layout.append(wide_row)
    return wide_layout

def get_direction_vector(instruction):
    dx, dy = 0, 0

    if instruction == '<':
        dx = -1
    elif instruction == '>':
        dx = 1
    elif instruction == '^':
        dy = -1
    elif instruction == 'v':
        dy = 1

    return dx, dy

def shift(layout, from_pos, to_pos):
    from_x, from_y = from_pos
    to_x, to_y = to_pos
    current_cell = layout[from_y][from_x]

    layout[to_y][to_x] = current_cell
    layout[from_y][from_x] = EMPTY
    return True

def move(layout, object_position, instruction):
    x, y = object_position
    dx, dy = get_direction_vector(instruction)
    move_stack = []

    next_cell = layout[y + dy][x + dx]

    # print('Moving:', layout[y][x], object_position, '[', instruction, ']', next_cell)

    if next_cell == WALL:
        return []
    if next_cell == BOX:
        next_position = (x + dx, y + dy)
        move_stack = move(layout, next_position, instruction)
        
        if len(move_stack) > 0 and next_position == move_stack[-1][0]:
            move_stack.append((object_position, next_position))

    if next_cell == BOX_A:
        next_position_A = (x + dx, y + dy)
        next_position_B = (x + dx + 1, y + dy)

        if (dx == 0):
            stack_A = move(layout, next_position_A, instruction)
            stack_B = move(layout, next_position_B, instruction)
        
            if len(stack_A) > 0 and len(stack_B) > 0:
                if stack_A[-1][0] == next_position_A and stack_B[-1][0] == next_position_B:
                    move_stack = stack_A + stack_B
                    move_stack.append((object_position, next_position_A))
        elif (dx == -1):
            move_stack.append((object_position, next_position_A))
        else: # (dx == 1)
            move_stack = move(layout, next_position_B, instruction)
            if len(move_stack) > 0 and next_position_B == move_stack[-1][0]:
                move_stack.append((next_position_A, next_position_B))
                move_stack.append((object_position, next_position_A))

    if next_cell == BOX_B:
        next_position_A = (x + dx - 1, y + dy)
        next_position_B = (x + dx, y + dy)
        
        if (dx == 0):
            stack_A = move(layout, next_position_A, instruction)
            stack_B = move(layout, next_position_B, instruction)

            if len(stack_A) > 0 and len(stack_B) > 0:
                if stack_A[-1][0] == next_position_A and stack_B[-1][0] == next_position_B:
                    move_stack = stack_A + stack_B
                    move_stack.append((object_position, next_position_B))
        elif (dx == 1):
            move_stack.append((object_position, next_position_B))
        else: # (dx == -1)
            move_stack = move(layout, next_position_A, instruction)
            if len(move_stack) > 0 and next_position_A == move_stack[-1][0]:
                move_stack.append((next_position_B, next_position_A))
                move_stack.append((object_position, next_position_B))
            
    if next_cell == EMPTY:
        move_stack.append(((x, y), (x + dx, y + dy)))
        
    #print('Move stack:', move_stack)
    return move_stack
    
def get_robot_position(layout):
    for y, row in enumerate(layout):
        for x, cell in enumerate(row):
            if cell == ROBOT:
                return x, y

def remove_duplicates(move_stack):
    return list(dict.fromkeys(move_stack))

def process_move_stack(layout, move_stack, debug=False):
    move_stack = remove_duplicates(move_stack)

    if debug: print('Processing move stack:', move_stack)
    for move in move_stack:
        if debug: print('Shifting:', move[0], move[1])
        shift(layout, move[0], move[1])

def run_instructions(layout, instructions, debug=False):
    robot_position = get_robot_position(layout)
    for instruction in instructions:
        moves = move(layout, robot_position, instruction)
        process_move_stack(layout, moves, debug)
        robot_position = get_robot_position(layout)
        if debug:
            print('Instruction:', instruction)
            print_map(layout)

def get_score(layout):
    score = 0
    for y, row in enumerate(layout):
        for x, cell in enumerate(row):
            if cell == BOX or cell == BOX_A:
                score += y * 100 + x
    return score

with open(filename, 'r') as f:
    layout, instructions = parse_file(f)
    wide_layout = widen(layout)

    print_map(layout)
    print_map(wide_layout)

    run_instructions(layout, instructions, debug=False)
    run_instructions(wide_layout, instructions, debug=False)

    resultA = get_score(layout)
    resultB = get_score(wide_layout)

    print('Part 1:', resultA)
    print('Part 2:', resultB)