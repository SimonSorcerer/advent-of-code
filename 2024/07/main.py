import re;
import itertools;

filename = 'input.txt'

OPERATIONS = [
    lambda a,b : a * b,
    lambda a,b : a + b,
]

OPERATIONS_PART_2 = OPERATIONS + [
    lambda a,b : int(str(a) + str(b))
]

def parse_line(line):
    return list(map(int, re.findall(r'\d+', line)));

def get_cartesian_operators(count, operations):
    return list(itertools.product(operations, repeat=count))

def is_solvable(equation, operations):
    solution = equation[0]

    operatorCount = len(equation) - 2
    operatorCartesianProduct = get_cartesian_operators(operatorCount, operations)

    for permutation in operatorCartesianProduct:
        partial = equation[1]
        for i in range(2, len(equation)):
            b = equation[i]
            partial = permutation[i - 2](partial, b)
        if (partial == solution):
            return True
    return False

def count_solvable_solutions(equations, operations):
    sum = 0
    for equation in equations:
        if (is_solvable(equation, operations)):
            sum += equation[0]
    return sum

with open(filename, 'r') as f:
    equations = []

    for index, line in enumerate(f):
        equations.append(parse_line(line.strip()))

    resultA = count_solvable_solutions(equations, OPERATIONS)
    resultB = count_solvable_solutions(equations, OPERATIONS_PART_2)

    print('Part 1:', resultA)
    print('Part 2:', resultB)