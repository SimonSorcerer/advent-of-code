import re;
import time

filename = 'input.txt'

def read_line(line):
    return list(line.strip())

def find_multi_max(batteryBlock, size = 12):
    max_values = [0] * size

    for i in range(len(batteryBlock)):
        current_value = int(batteryBlock[i])

        for j in range(size):
            if current_value > max_values[j] and i <= len(batteryBlock) - size + j:
                max_values.insert(j, current_value)
                max_values.pop()
                for k in range(j + 1, size):
                    max_values[k] = 0
                break

    # print('Max values:', max_values)
    result = 0

    for i in range(size):
        result = result * 10 + max_values[i]

    return result
    
with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time.time()
    
    for line in f:
        batteryBlock = read_line(line)
        part1result += find_multi_max(batteryBlock, 2)
        part2result += find_multi_max(batteryBlock, 12)
    
    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)