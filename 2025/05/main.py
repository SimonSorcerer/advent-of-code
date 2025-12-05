import re;
import time

filename = 'input.txt'

def read_range(line):
    first, second = re.match(r'(\d+)-(\d+)', line).group(1, 2);
    return [int(first), int(second)]

def read_ingredient(line):
    return int(line.strip())
    
def is_fresh(ingredient, fresh_ranges):
    for r in fresh_ranges:
        if r[0] <= ingredient <= r[1]:
            return True
    return False

def is_included(fresh_rangeB, fresh_rangeA):
    return fresh_rangeA[0] <= fresh_rangeB[0] and fresh_rangeA[1] >= fresh_rangeB[1]

def ranges_overlap(fresh_rangeA, fresh_rangeB):
    return fresh_rangeA[1] >= fresh_rangeB[0]

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time.time()

    fresh_ranges = []

    for line in f:
        if line.strip() == '':  # Empty line (or only whitespace)
            break;
        fresh_ranges.append(read_range(line))
        
    fresh_ranges.sort(key=lambda x: x[0])
    for i in range(len(fresh_ranges)):
        rangeA = fresh_ranges[i]
        rangeB = fresh_ranges[i + 1] if i < len(fresh_ranges) - 1 else None

        if (rangeB is not None and ranges_overlap(rangeA, rangeB)):
            if (is_included(rangeB, rangeA)):
                fresh_ranges[i + 1][1] = rangeA[1]
                fresh_ranges[i][1] = rangeB[0] - 1
            else: 
                fresh_ranges[i][1] = rangeB[0] - 1

        if (fresh_ranges[i][0] <= fresh_ranges[i][1]):
            part2result += fresh_ranges[i][1] - fresh_ranges[i][0] + 1

    for line in f:
        ingredient = read_ingredient(line)
        if is_fresh(ingredient, fresh_ranges):
            part1result += 1
   
    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)