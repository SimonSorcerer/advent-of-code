import time;
from parse_utils import parse_contraption_matrix
from beam_utils import move_beam, DIRECTION
from energy_map import mark, count_energized_tiles, is_in_map, clear_energy_map
from contraption_utils import visualize, get_configurations

filename = 'input.txt'

def run(configuration, display = False):
    stack = [configuration]
    mark(configuration[0], configuration[1])
    while (len(stack) > 0):
        position, direction = stack.pop()
        new_moves = move_beam(contraption_matrix, position, direction)
        for move in new_moves:
            if is_in_map(contraption_matrix, move[0]) and mark(move[0], move[1]):
                stack.append(move)
    
    if display:
        visualize(contraption_matrix)
    return count_energized_tiles()

with open(filename, 'r') as f:
    result = 0
    result2 = 0

    startT = time.time()
    # -----------------------------------------------
    # part 1
    # -----------------------------------------------
    contraption_matrix = parse_contraption_matrix(f)

    result = run(((0, 0), DIRECTION['right']), True)

    # -----------------------------------------------
    # part 2
    # -----------------------------------------------
    configurations = get_configurations(contraption_matrix)
    result2 = 0
    max_config = None

    for configuration in configurations:
        clear_energy_map()
        run_score = run(configuration)
        if run_score > result2:
            result2 = run_score
            max_config = configuration

    print('max config', max_config)
    # -----------------------------------------------
    endT = time.time()
    
    print('time:', endT - startT)
    print('part 1:', result)
    print('part 2:', result2)