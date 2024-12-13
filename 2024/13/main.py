import re
import math
import numbers
from sympy import symbols, solve, Eq, diophantine
from colors import printC, WHITE, RED, YELLOW

filename = 'input.txt'

def parse_line(line):
    return tuple(map(int, re.findall(r'\d+', line)));

def parse_file(file):
    machine_configs = []

    config = {}
    for index, line in enumerate(f):
        if index % 4 == 0:
            config['A'] = parse_line(line.strip())
        elif index % 4 == 1:
            config['B'] = parse_line(line.strip())
        elif index % 4 == 2:
            config['prize'] = parse_line(line.strip())
            machine_configs.append(config)
        else:
            config = {}
    
    return machine_configs

MAX_LEVER_MOVEMENTS = 100

def find_best_variant(config):
    Ax, Ay = config['A']
    Bx, By = config['B']
    targetX, targetY = config['prize']

    min_cost = math.inf 
    best_c1 = None
    best_c2 = None
    
    for c1 in range(0, MAX_LEVER_MOVEMENTS + 1):  
        for c2 in range(0, MAX_LEVER_MOVEMENTS + 1):
            # Check if the current c1 and c2 hit the target
            if (c1 * Ax + c2 * Bx == targetX) and (c1 * Ay + c2 * By == targetY):
                cost = c1 * 3 + c2
                # Update the minimum cost if needed
                if cost < min_cost:
                    min_cost = cost
                    best_c1 = c1
                    best_c2 = c2
    
    # There is no solution
    if (min_cost == math.inf):
        return None

    return best_c1, best_c2, min_cost

PART_2_MODIFIER = 10000000000000

def minimize_cost_with_diophantine(config):
    Ax, Ay = config['A']
    Bx, By = config['B']
    targetX, targetY = config['prize']

    # Addding huge number, so first algo won't work :)
    targetX += PART_2_MODIFIER
    targetY += PART_2_MODIFIER

    # Define variables c1 and c2
    c1, c2 = symbols('c1 c2')
    
    # Define the equations
    eq1 = Eq(c1 * Ax + c2 * Bx, targetX)
    eq2 = Eq(c1 * Ay + c2 * By, targetY)

    c2_expr = solve(eq1, c2)[0]  # This solves for c2 in terms of c1

    # Substitute c2 into eq2
    reduced_eq2 = eq2.subs(c2, c2_expr)

    # Solve the system of Diophantine equations
    c1_solutions = diophantine(reduced_eq2)
    
    solutions = []
    for c1_solution in c1_solutions:
        c1_val = c1_solution[0]  # c1 is the solution from the Diophantine equation
        c2_val = c2_expr.subs(c1, c1_val)  # Get corresponding c2
        solutions.append((c1_val, c2_val))
    
    min_cost = math.inf
    best_c1, best_c2 = None, None
    
    for solution in solutions:
        c1_val, c2_val = solution

        # There was a strange result with fraction, so added this check
        if not isinstance(c1_val, numbers.Integral) or not isinstance(c2_val, numbers.Integral):
            continue    
        
        cost = 3 * c1_val + c2_val
        
        # Update if this is the lowest cost found
        if cost < min_cost:
            min_cost = cost
            best_c1 = c1_val
            best_c2 = c2_val
    
    if (min_cost == math.inf):
        return None

    return best_c1, best_c2, min_cost

def get_tokens_needed(config_list, use_diophantine = False):
    tokens = 0
    
    for config in config_list:
        best_variant = find_best_variant(config) if not use_diophantine else minimize_cost_with_diophantine(config)
        if best_variant != None:
            tokens += best_variant[2]
    
    return tokens


with open(filename, 'r') as f:
    machine_configs = parse_file(f)

    resultA = get_tokens_needed(machine_configs)
    resultB = get_tokens_needed(machine_configs, True)

    print('Part 1:', resultA)
    print('Part 2:', resultB)