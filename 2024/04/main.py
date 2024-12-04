filename = 'input.txt'

DIRECTIONS = {
    'up-left': (-1, -1),
    'up': (-1, 0),
    'up-right': (-1, 1),
    'down-left': (1, -1),
    'down': (1, 0),
    'down-right': (1, 1),
    'left': (0, -1),
    'right': (0, 1)
}

KEYWORD = 'XMAS'

def in_matrix_bounds(matrix, position):
    x, y = position
    return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0])


def find_xmas_in_position(matrix, start_position):
    positives = 0

    if (matrix[start_position[0]][start_position[1]] != 'X'):
        return 0

    for direction in DIRECTIONS:
        x, y = start_position
        dx, dy = DIRECTIONS[direction]
        found_word = ''
        
        for _ in range(len(KEYWORD)):
            found_word += matrix[x][y]
            x += dx
            y += dy
            if in_matrix_bounds(matrix, (x, y)) == False:
                break
            if found_word not in KEYWORD:
                break
        
        if found_word == KEYWORD:
            positives += 1

    return positives

def find_xmas(matrix):
    positives = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            positives += find_xmas_in_position(matrix, (x, y))
    
    return positives

def is_letter_in_matrix(matrix, position, letter):
    x, y = position
    return in_matrix_bounds(matrix, position) and matrix[x][y] == letter

def find_x_mas_in_position(matrix, start_position):
    positives = 0
    x, y = start_position

    if (matrix[x][y] != 'A'):
        return 0
    
    if (is_letter_in_matrix(matrix, (x-1, y-1), 'M') and is_letter_in_matrix(matrix, (x+1, y+1), 'S')):
        if (is_letter_in_matrix(matrix, (x+1, y-1), 'M') and is_letter_in_matrix(matrix, (x-1, y+1), 'S')):
            positives += 1
        if (is_letter_in_matrix(matrix, (x-1, y+1), 'M') and is_letter_in_matrix(matrix, (x+1, y-1), 'S')):
            positives += 1

    if (is_letter_in_matrix(matrix, (x-1, y-1), 'S') and is_letter_in_matrix(matrix, (x+1, y+1), 'M')):
        if (is_letter_in_matrix(matrix, (x+1, y-1), 'S') and is_letter_in_matrix(matrix, (x-1, y+1), 'M')):
            positives += 1
        if (is_letter_in_matrix(matrix, (x-1, y+1), 'S') and is_letter_in_matrix(matrix, (x+1, y-1), 'M')):
            positives += 1

    return positives

def find_x_mas(matrix):
    positives = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            positives += find_x_mas_in_position(matrix, (x, y))
    
    return positives

def parse_line(line):
    return list(line)

with open(filename, 'r') as f:
    matrix = []

    for index, line in enumerate(f):
        matrix.append(parse_line(line.strip()))

    resultA = find_xmas(matrix)
    resultB = find_x_mas(matrix)

    print('Part 1:', resultA)
    print('Part 2:', resultB)