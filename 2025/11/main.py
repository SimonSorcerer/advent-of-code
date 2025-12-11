import re
import time as time_module
from collections import deque

filename = 'input.txt'

def parse_line(line):
    match = re.findall(r'([a-z]+)', line)

    return match[0], list(match)[1:]

# Breadth-First Search to find all the paths (without infinite loop detection - no need)
def find_paths(routing_map, start, target):
    queue = deque([(start)])
    out_count = 0
    
    while queue:
        state = queue.popleft()    
        
        if state == target:
            # print('Found path to', target)
            out_count += 1
        else:
            if state in routing_map:
                for node in routing_map[state]:
                    queue.append(node)   
    return out_count 
    print("Computing svr -> fft...")
    svr_to_fft = find_paths(routing_map, 'svr', 'fft')
    print(f"  Result: {svr_to_fft}")
    
    print("Computing svr -> dac...")
    svr_to_dac = find_paths(routing_map, 'svr', 'dac')
    print(f"  Result: {svr_to_dac}")
    
    print("Computing fft -> dac...")
    fft_to_dac = find_paths(routing_map, 'fft', 'dac')
    print(f"  Result: {fft_to_dac}")
    
    print("Computing dac -> fft...")
    dac_to_fft = find_paths(routing_map, 'dac', 'fft')
    print(f"  Result: {dac_to_fft}")
    
    print("Computing fft -> out...")
    fft_to_out = find_paths(routing_map, 'fft', 'out')
    print(f"  Result: {fft_to_out}")
    
    print("Computing dac -> out...")
    dac_to_out = find_paths(routing_map, 'dac', 'out')
    print(f"  Result: {dac_to_out}")
    
    # Now compute the combinations
    paths1 = svr_to_fft * fft_to_dac * dac_to_out
    paths2 = svr_to_dac * dac_to_fft * fft_to_out
    
    print(f"\nPath 1 (svr->fft->dac->out): {paths1}")
    print(f"Path 2 (svr->dac->fft->out): {paths2}")
    
    return paths1 + paths2

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time_module.time()

    with open(filename, 'r') as f:
        lines = { key: values for key, values in map(parse_line, f.read().splitlines())}

    part1result = find_paths(lines, start='you', target='out')
        
    end = time_module.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)