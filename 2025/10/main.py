import re
import time as time_module
from collections import deque
from pulp import *

filename = 'input.txt'

def parse_button_group(button_group):
    return list(map(int, re.findall(r'(\d+)[^,]?+', button_group)))

def parse_line(line):
    light_re = re.match(r'\[([.#]*)\]', line)
    button_groups_re = re.findall(r'\((\S*)\)', line)
    joltage_re = re.findall(r'\{(\S+)\}', line)

    return list(light_re.group(1)), list(map(parse_button_group, button_groups_re)), list(map(parse_button_group, joltage_re))[0]

# Breadth-First Search to find the shortest path
def lights_bfs(buttons, target, start):
    queue = deque([(tuple(start), [])])
    visited = {tuple(start)}
    
    while queue:
        state, presses = queue.popleft()
        # print('Current state:', ''.join(state), 'Presses:', presses)
        
        if state == tuple(target):
            return presses
        
        for i, button in enumerate(buttons):
            new_state = list(state)

            for light_idx in button:
                new_state[light_idx] = '#' if new_state[light_idx] == '.' else '.'
            
            new_state_tuple = tuple(new_state)
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state_tuple, presses + [i]))    

# Integer Linear Programming solution (using PuLP) - took some time to set up :(
def solve_joltage(buttons, target):
    n = len(target)
    
    # Create ILP problem
    prob = LpProblem("Joltage", LpMinimize)

    # Variables: how many times to press each button
    button_vars = [LpVariable(f"button_{i}", lowBound=0, cat='Integer') 
        for i in range(len(buttons))]
    
    # Objective: minimize total button presses
    prob += lpSum(button_vars)

    # Constraints: reach exact target joltage at each position
    for pos in range(n):
        # Sum of effects at this position = target[pos]
        effect = lpSum(button_vars[j] for j, button in enumerate(buttons) 
                      if pos in button)
        prob += effect == target[pos]
    
    # Solve
    prob.solve(PULP_CBC_CMD(msg=0))
    
    if prob.status == LpStatusOptimal:
        presses = [int(v.varValue) for v in button_vars]
        # print(f'ILP solution: {sum(presses)} presses - {presses}')
        return sum(presses)
    
    print(f'No solution found for target: {target}')
    return None

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time_module.time()

    with open(filename, 'r') as f:
        lines = list(map(parse_line, f.read().splitlines()))

    for target, buttons, joltage in lines:
        # print('Lights:', ''.join(target), 'Buttons:', buttons, 'Joltage:', joltage)
        button_presses = lights_bfs(buttons, target, ['.'] * len(target))
        joltage_increases = solve_joltage(buttons, joltage)
        
        part1result += len(button_presses)
        part2result += joltage_increases

    end = time_module.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)