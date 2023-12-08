import re;
import time;
from itertools import cycle
from functools import reduce
from math import gcd

filename = 'input.txt'

def parse_node(line):
    nodes = re.findall(r'(\w+)', line)
    node_key = nodes[0]
    node_value = { 'L': nodes[1], 'R': nodes[2] }
    
    result = {}
    result[node_key] = node_value
    return result
    
def calculate_part1(node_map, current_node, move_instructions):
    counter = 0
    while current_node != 'ZZZ':
        instruction = next(move_instructions)
        #print(current_node, instruction, counter)
        current_node = node_map[current_node][instruction]
        counter += 1
    return counter

def get_starting_nodes(node_map):
    starting_nodes = []
    for key in node_map:
        if (key[2] == 'A'):
            starting_nodes.append(key)
    return starting_nodes

def is_ending_node(node):
    return node[2] == 'Z'

def all_nodes_are_ending(node_list):
    for node in node_list:
        if (not is_ending_node(node)):
            return False
    return True

def get_next_nodes(node_map, current_nodes, instruction):
    new_nodes = []
    for node in current_nodes:
        new_nodes.append(node_map[node][instruction])
    return new_nodes

# I stole this from ze internet :)
def lcm(numbers):
    # Use the 'reduce' function to apply a lambda function that calculates the LCM for a pair of numbers.
    # The lambda function multiplies two numbers and divides the result by their greatest common divisor (gcd).
    # This process is applied cumulatively to all numbers in the list.
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)

def calculate_part2(node_map, move_instructions):
    counter = 0
    current_nodes = get_starting_nodes(node_map)
    node_z_distances = {}

    while len(node_z_distances) != len(current_nodes):
        instruction = next(move_instructions)
        current_nodes = get_next_nodes(node_map, current_nodes, instruction)
        counter += 1
        for key in current_nodes:
            if key[2] == 'Z' and key not in node_z_distances:
                node_z_distances[key] = counter

    return lcm(node_z_distances.values())

with open(filename, 'r') as f:
    node_map = {}
    starting_nodes = []
    PART = 2

    startT = time.time()

    for index, line in enumerate(f, 1):
        if (index == 1):
            move_instructions = cycle(list(line.strip()))
        if (index >= 3):
            node_map |= parse_node(line.strip())
    
    # part 1
    if (PART == 1):
        result = calculate_part1(node_map, 'AAA', move_instructions)

    # part 2
    if (PART == 2):
        result = calculate_part2(node_map, move_instructions)

    endT = time.time()
    
    print('time:', endT - startT)
    print('result:', result)