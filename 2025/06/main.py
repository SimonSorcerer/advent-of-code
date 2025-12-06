import math
import re
import time

filename = 'input.txt'

def read_line(line):
    return line.strip();

def read_file(file):
    data = list()
    for line in file:
        matches = re.finditer(r'(\d+|[+*])', line)
        line_data = []
        for m in matches:
            line_data.append(m.group(1))
        data.append(line_data)
    return data

def rotate_file(file):
    data = [line.rstrip('\n') for line in file]
    return [''.join(col) for col in zip(*data)]

def cephalopod_math(members, operator):
    if operator == '+':
        return sum(members)
    elif operator == '*':
        return math.prod(members)
    return 0

def solve_as_cephalopod(file):
    rotated = rotate_file(file)

    members = list()
    operator = None
    result = 0

    for rota_index, rota_line in enumerate(rotated):
        tokens = re.findall(r'\d+|[+*]', rota_line)

        for token in tokens:
            if token in ['+', '*']:
                operator = token
            else:
                members.append(int(token))

        if len(tokens) == 0 or rota_index == len(rotated) - 1:
            result += cephalopod_math(members, operator)
            operator = None
            members.clear()
            continue

    return result

def get_cepalophod_numbers(token, numbers):
    for i in range(len(token)):
        if len(numbers) > i:
            numbers[i] += token[-(i+1)]
        else:
            numbers.append(token[-(i+1)])
    return numbers

def solve_as_human(file):
    data = read_file(file)
    result = 0

    for j in range(len(data[0])):
        members = list()
        for i in range(len(data)):
            token = data[i][j]
            if (token == '+'):
                result += sum(members)
            elif (token == '*'):
                result += math.prod(members)
            else:
                members.append(int(token))
    return result

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time.time()

    with open(filename, 'r') as f:
        lines = f.readlines()

    part1result = solve_as_human(lines)
    part2result = solve_as_cephalopod(lines)

    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)