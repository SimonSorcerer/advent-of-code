from collections import deque
import re;

filename = 'input.txt'

def is_empty_line(line):
    return line == '\n'

def is_header_line(line):
    return not is_empty_line(line) and line[0].isalpha()

def is_data_line(line):
    return not is_empty_line(line) and line[0].isdigit()

def parse_seeds(line):
    result = []
    seeds = re.findall(r'(\d+)', line)
    
    for seed_number in seeds:
        result.append(deque([int(seed_number)]))
    
    return result

def parse_set(line):
    numbers = re.findall(r'(\d+)', line)
    
    destination_start = int(numbers[0])
    source_start = int(numbers[1])
    count = int(numbers[2])

    return (destination_start, source_start, count)

def apply_rule(key, rule):
    (destination_start, source_start, count) = rule
    
    if (key >= source_start and key < (source_start + count)):
        destination = destination_start + (key - source_start)
    else:
        destination = None
    
    return destination

def find_lowest_location(seed_map):
    lowest_location = None

    for seed_list in seed_map:
        location = seed_list[-1]
        if (lowest_location == None or location < lowest_location):
            lowest_location = location

    return lowest_location

def print_seed_map(seed_map):
    for seed_list in seed_map:
        print(seed_list)

with open(filename, 'r') as f:
    seed_map = []
    rules = []
    depth = 0

    for index, line in enumerate(f, 1):
        if (index == 1):
            seed_map = parse_seeds(line.strip())
        elif (is_header_line(line)):
            depth += 1
            for seed_list in seed_map:
                if (len(seed_list) < depth):
                  seed_list.append(seed_list[-1])
        elif (is_data_line(line)):
            rule = parse_set(line.strip())
            for seed_list in seed_map:
                new_value = apply_rule(seed_list[-1], rule)
                if (new_value != None and len(seed_list) <= depth):
                    seed_list.append(new_value)
    
    # print_seed_map(seed_map)

    print('result:', find_lowest_location(seed_map))