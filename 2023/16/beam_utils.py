
SYMBOLS = {
    'empty': '.',
    'mirror45': '/',
    'mirror135': '\\', # Backslash has to be escaped :D
    'splitter180': '-',
    'splitter0': '|',
}

DIRECTION = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
}

def move(point, direction):
    x, y = point
    dx, dy = direction
    return (x + dx, y + dy)

def get_symbol(contraption, position):
    x, y = position
    return contraption[y][x]

def move_beam(contraption, position, direction):
    results = []
    symbol = get_symbol(contraption, position)

    if symbol == SYMBOLS['empty']:
        results.append((move(position, direction), direction))
    elif symbol == SYMBOLS['mirror45']:
        results.extend(move_mirror45(position, direction))
    elif symbol == SYMBOLS['mirror135']:
        results.extend(move_mirror135(position, direction))
    elif symbol == SYMBOLS['splitter180']:
        results.extend(move_splitter180(position, direction))
    elif symbol == SYMBOLS['splitter0']:
        results.extend(move_splitter0(position, direction))

    return results

def move_mirror45(position, direction):
    if direction == DIRECTION['up']:
        return [(move(position, DIRECTION['right']), DIRECTION['right'])]
    elif direction == DIRECTION['right']:
        return [(move(position, DIRECTION['up']), DIRECTION['up'])]
    elif direction == DIRECTION['down']:
        return [(move(position, DIRECTION['left']), DIRECTION['left'])]
    elif direction == DIRECTION['left']:
        return [(move(position, DIRECTION['down']), DIRECTION['down'])]

def move_mirror135(position, direction):
    if direction == DIRECTION['up']:
        return [(move(position, DIRECTION['left']), DIRECTION['left'])]
    elif direction == DIRECTION['right']:
        return [(move(position, DIRECTION['down']), DIRECTION['down'])]
    elif direction == DIRECTION['down']:
        return [(move(position, DIRECTION['right']), DIRECTION['right'])]
    elif direction == DIRECTION['left']:
        return [(move(position, DIRECTION['up']), DIRECTION['up'])]

def move_splitter180(position, direction):
    if direction in [DIRECTION['up'], DIRECTION['down']]:
        return [(move(position, DIRECTION['left']), DIRECTION['left']), (move(position, DIRECTION['right']), DIRECTION['right'])]
    elif direction in [DIRECTION['right'], DIRECTION['left']]:
        return [(move(position, direction), direction)]

def move_splitter0(position, direction):
    if direction in [DIRECTION['up'], DIRECTION['down']]:
        return [(move(position, direction), direction)]
    elif direction in [DIRECTION['right'], DIRECTION['left']]:
        return [(move(position, DIRECTION['up']), DIRECTION['up']), (move(position, DIRECTION['down']), DIRECTION['down'])]