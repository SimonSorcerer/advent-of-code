import re;
import time

filename = 'input.txt'

def read_line(line):
    return re.finditer(r'(\d+)-(\d+)', line)

def is_doubled(text):
    if len(text) % 2 != 0:
        return False

    mid = len(text) // 2
    first_half = text[:mid]
    second_half = text[mid:]
    return first_half == second_half

def is_repeated(text):
    size = len(text)

    for c in range(1, size // 2 + 1):
        if size % c == 0:
            expected_string = text[:c] * (size // c)
            if expected_string == text:
                return True
    return False
    
def get_doubles(start, end):
    sum = 0
    for num in range(int(start), int(end + 1)):
        if is_doubled(str(num)):
            sum += num
    return sum

def get_repeats(start, end):
    sum = 0
    for num in range(int(start), int(end + 1)):
        if is_repeated(str(num)):
            sum += num
    return sum


with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time.time()
    matches = read_line(f.readline().strip())
    
    for m in matches:
        first, second = int(m.group(1)), int(m.group(2))
        part1result += get_doubles(first, second)
        part2result += get_repeats(first, second)

    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)