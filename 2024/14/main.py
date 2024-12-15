import re
import math

filename = 'input.txt'
W = 101
H = 103

def parse_line(line):
    return list(map(int, re.findall(r'-?\d+', line)));

def parse_file(file):
    robots = []
    for _, line in enumerate(file):
        robots.append(parse_line(line.strip()))
    return robots

def move_robots(robots, time):
    quadrants = {'TL': 0, 'TR': 0, 'BL': 0, 'BR': 0}

    for px, py, dx, dy in robots:
        x = (px + dx * time) % W
        y = (py + dy * time) % H
        quad = get_quadrant((x, y))
        if (quad != '??'):
            quadrants[quad] += 1
    
    return quadrants

def get_quadrant(position):
    if position[0] < W // 2 and position[1] < H // 2:
        return "TL"
    if position[0] > W // 2 and position[1] < H // 2:
        return "TR"
    if position[0] < W // 2 and position[1] > H // 2:
        return "BL"
    if position[0] > W // 2 and position[1] > H // 2:
        return "BR"
    return "??"

def get_map(robots):
    robot_map = [[0 for _ in range(W)] for _ in range(H)]

    for robot in robots:
        px, py, _, _ = robot
        robot_map[py][px] += 1

    result = ''
    for row in robot_map:
        for cell in row:
            if cell > 0:
                result += '#'
            else:
                result += ' '
        result += '\n'
    
    return result

def count_safety_factor(robots, time, debug=False):
    quadrants = move_robots(robots, time)

    if debug:
        print(get_map(robots))

    return math.prod(quadrants.values())

def get_min_security(robots, max_time):
    return min(range(max_time), key=lambda t: count_safety_factor(robots, t))

with open(filename, 'r') as f:
    robots = parse_file(f)

    resultA = count_safety_factor(robots, 100)
    resultB = get_min_security(robots, 10_000)

    print('Part 1:', resultA)
    print('Part 2:', resultB)