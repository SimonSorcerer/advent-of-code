import time;
import re;
import numpy;

filename = 'input.txt'

class bcolors:
    DARKGREY = '\033[1;30m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

SYMBOLS = {
    'rock': '#',
    'ash': '.'
}

alternative_patterns_h = []
alternative_patterns_v = []

def visualize(space):
    for line in space:
        for char in line:
            if (char == SYMBOLS['rock']):
                print(bcolors.WARNING + '#' + bcolors.ENDC, end='')
            else: 
                print(bcolors.DARKGREY + '░' + bcolors.ENDC, end='')
        print('\n')

def is_empty_line(line):
    return len(line) == 0

def parse_line(line):
    match = re.search(r'([.#]+)', line)
    return list(match.group(1))

def parse_file(file):
    patterns = []
    current_pattern = []

    for line in file:
        if is_empty_line(line.strip()):
            print('empty line')
            patterns.append(current_pattern)
            current_pattern = []
        else:
            current_pattern.append(parse_line(line.strip()))
    patterns.append(current_pattern)

    return patterns

def rotate_matrix(matrix, clockwise=False):
    return numpy.rot90(matrix) if clockwise else numpy.rot90(matrix, k=1, axes=(1, 0))

def rows_are_identical(row1, row2):
    return list(row1) == list(row2)

def find_possible_reflection_centers(pattern, is_rotated, find_alternatives = True):
    possible_reflection_points = []

    for index in range(1, len(pattern)):
        if rows_are_identical(pattern[index - 1], pattern[index]):
            possible_reflection_points.append(index - 1)
        if find_alternatives:
            differences = rows_can_have_smudge(pattern[index - 1], pattern[index])
            if len(differences) == 1:
                alt_matrix = create_alternative_pattern(pattern, (index - 1, differences[0]))
                if (is_rotated):
                    alternative_patterns_v.append(alt_matrix)
                    # print('adding V alt', len(alternative_patterns_v), '[', index, differences[0], ']')
                else:
                    alternative_patterns_h.append(alt_matrix)
                    # print('adding H alt', len(alternative_patterns_h), '[', index, differences[0], ']')

    return possible_reflection_points

def find_horizontal_reflections(pattern, is_rotated = False, find_alternatives = True):
    #visualize(pattern)
    possible_reflection_points = find_possible_reflection_centers(pattern, is_rotated, find_alternatives)
    reflections = []

    for possible_center in possible_reflection_points:
        is_reflection = True
        pivot = possible_center + 1
        for index in range(2, min(pivot, len(pattern) - pivot) + 1):
            if not rows_are_identical(pattern[pivot - index], pattern[pivot + index - 1]):
                #print('rows are not identical', pattern[pivot - index], pattern[pivot + index - 1])
                is_reflection = False
            if (find_alternatives):
                differences = rows_can_have_smudge(pattern[pivot - index], pattern[pivot + index - 1])
                if len(differences) == 1:
                    alt_matrix = create_alternative_pattern(pattern, (pivot - index, differences[0]))
                    if (is_rotated):
                        alternative_patterns_v.append(alt_matrix)
                        # print('koko adding V alt', len(alternative_patterns_v), '[', pivot - index, differences[0], ']')
                    else:
                        alternative_patterns_h.append(alt_matrix)
                        # print('koko adding H alt', len(alternative_patterns_h), '[', pivot - index, differences[0], ']')
                
        if is_reflection:
            reflections.append(possible_center)

        #print('reflections', reflections)

    return reflections

def find_reflections(pattern, find_alternatives = True):
    horizontal_reflections = find_horizontal_reflections(pattern, False, find_alternatives)
    
    rotated_pattern = rotate_matrix(pattern)
    vertical_reflections = find_horizontal_reflections(rotated_pattern, True, find_alternatives)
    
    print ('reflections: ', horizontal_reflections, ' - ', vertical_reflections)
    return horizontal_reflections, vertical_reflections

def find_alternative_reflections(original_reflections):
    vertical_reflections = []
    horizontal_reflections = []
    
    for pattern in alternative_patterns_v:
        vertical_reflections.extend(find_horizontal_reflections(pattern, True, False))
    
    vertical_reflections = numpy.setdiff1d(vertical_reflections, original_reflections[1])

    for pattern in alternative_patterns_h:
        horizontal_reflections.extend(find_horizontal_reflections(pattern, False, False))
    
    horizontal_reflections = numpy.setdiff1d(horizontal_reflections, original_reflections[0])

    print('alt reflections: ', horizontal_reflections, ' - ', vertical_reflections)
    return horizontal_reflections, vertical_reflections

def get_score(reflections):
    score = 0
    horizontal_reflections, vertical_reflections = reflections
    for reflection in vertical_reflections:
        score += reflection + 1
    for reflection in horizontal_reflections:
        score += (reflection + 1) * 100
    return score

# PART 2 methods
def rows_can_have_smudge(row1, row2):
    differences = []
    for index, (first, second) in enumerate(zip(row1, row2)):
        if first != second:
            differences.append(index)
    return differences

def create_alternative_pattern(pattern, difference):
    row, col = difference
    new_pattern = []

    for index, line in enumerate(pattern):
        new_pattern.append(list(line))
        if index == row:
            new_pattern[index][col] = SYMBOLS['rock'] if line[col] == SYMBOLS['ash'] else SYMBOLS['ash']

    return new_pattern

with open(filename, 'r') as f:
    result = 0
    result2 = 0
    startT = time.time()
    patterns = parse_file(f)

    for index, pattern in enumerate(patterns, 1):
        alternative_patterns_h = []
        alternative_patterns_v = []
        print('------------------------------------')
        print('PATTERN no.: ', index)
        reflections = find_reflections(pattern)
        score = get_score(reflections)
        alternatives = find_alternative_reflections(reflections)
        score2 = get_score(alternatives)
        print('score: ', score)
        print('score2: ', score2)
        print('------------------------------------')
        result += score
        result2 += score2
        
    endT = time.time()
    print('time:', endT - startT)

    print('part 1:', result)
    print('part 2:', result2)