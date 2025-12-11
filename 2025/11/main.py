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

# recursive DFS with memoization to find all paths that pass through required nodes
# Thanks to AsirisPava for super simple solution
def find_paths_dp(routing_map, start, target, required_nodes):
    cache = {}
    
    def solve(node, found_node1, found_node2):
        # Mark as found if we're at the required node
        found_node1 = found_node1 or (node == required_nodes[0])
        found_node2 = found_node2 or (node == required_nodes[1])
        
        # Check cache
        key = (node, found_node1, found_node2)
        if key in cache:
            return cache[key]
        
        if node == target:
            return 1 if (found_node1 and found_node2) else 0
        
        if node not in routing_map:
            return 0
        
        total_paths = 0
        for next_node in routing_map[node]:
            total_paths += solve(next_node, found_node1, found_node2)
        
        cache[key] = total_paths
        return total_paths
    
    return solve(start, False, False)

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time_module.time()

    with open(filename, 'r') as f:
        lines = { key: values for key, values in map(parse_line, f.read().splitlines())}

    part1result = find_paths(lines, 'you', 'out')
    part2result = find_paths_dp(lines, 'svr', 'out', ['fft', 'dac'])
        
    end = time_module.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)