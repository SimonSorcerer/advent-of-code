import re;
import time;

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

    for index in range(0, len(seeds), 2):
        seed_start_no = int(seeds[index])
        count = int(seeds[index + 1])
        result.append((seed_start_no, seed_start_no + count, False))

    return result

def parse_set(line):
    numbers = re.findall(r'(\d+)', line)
    
    destination_start = int(numbers[0])
    source_start = int(numbers[1])
    count = int(numbers[2])

    return (destination_start, source_start, count)

def remap_interval(interval, source_start, destination_start):
    (start, end) = interval
    return (destination_start + (start - source_start), destination_start + (end - source_start), True)

def split_and_apply_rule(interval, rule):
    (destination_start, source_start, count) = rule
    (start1, end1, isMapped) = interval
    (start2, end2) = (source_start, source_start + count)

    if (start1 >= start2 and start1 < end2):
        if (end1 <= end2):
            return [remap_interval((start1, end1), source_start, destination_start)]
        else:
            return [remap_interval((start1, end2), source_start, destination_start), (end2, end1, False)]
    elif (start2 >= start1 and start2 < end1):
        if (end2 <= end1):
            return [(start1, start2, False), remap_interval((start2, end2), source_start, destination_start), (end2, end1, False)]
        else:
            return [(start1, start2, False), remap_interval((start2, end1), source_start, destination_start)]
    else:
        return [(start1, end1, False)]

def find_lowest_location(seed_map):
    lowest_location = None

    for interval in seed_map:
        (start, end, isMapped) = interval
        if (lowest_location is None or start < lowest_location):
            lowest_location = start

    return lowest_location

def reset_seed_intervals(seed_map):
    result = []
    for interval in seed_map:
        (start, end, isMapped) = interval
        result.append((start, end, False))
    return result

def print_seed_map(seed_map):  
    for seed_list in seed_map:
        print(seed_list)

with open(filename, 'r') as f:    
    seed_map = []
    seed_map_copy = []
    rules = []
    depth = 0

    startT = time.time()
    for index, line in enumerate(f, 1):
        if len(seed_map_copy) > 0:
            seed_map = seed_map_copy
            seed_map_copy = []

        if (index == 1):
            seed_map = parse_seeds(line.strip())

        elif (is_header_line(line)):
            depth += 1
            seed_map = reset_seed_intervals(seed_map)
            #print_seed_map('depth: ', depth, seed_map)
           
        elif (is_data_line(line)):
            rule = parse_set(line.strip())

            for interval in seed_map:
                (start, end, isMapped) = interval
                if not isMapped:
                    seed_map_copy += split_and_apply_rule(interval, rule)
                    #print(index, ': ', interval, ' into: ', seed_map_copy)
                else:
                    seed_map_copy.append(interval)

    #print_seed_map(seed_map)
    endT = time.time()
    print('time: ', endT - startT)
    print('seed_count:', len(seed_map))
    print('result:', find_lowest_location(seed_map))