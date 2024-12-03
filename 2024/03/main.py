import re;

filename = 'input.txt'

def get_multiplication_list(matches, initial_enabled):
    instructions = []
    do = initial_enabled

    for match in matches:
        if match[0] == "do()":
            do = True
        elif match[0] == "don't()":
            do = False
        else:
            instructions.append((int(match[1]), int(match[2]), do))
    
    return instructions

def parse_line(line, initial_enabled):
    mul_regex = r'mul\((\d+),(\d+)\)'
    do_regex = r'(don\'t\(\)|do\(\))'
    matches = re.compile("(%s|%s)" % (mul_regex, do_regex)).findall(line)
    
    mutliplications = get_multiplication_list(matches, initial_enabled)
    return mutliplications

def calculate(multiplications):
    partial = list(map(lambda x: x[0] * x[1], multiplications))
    return sum(partial)

with open(filename, 'r') as f:
    memory = []

    for index, line in enumerate(f):
        # Spent hour debugging part 2 because I forgot it's multiple lines and instruction reset on each line (facepalm)
        initial_enabled = True if index == 0 else memory[len(memory) - 1][2]
        memory += parse_line(line.strip(), initial_enabled)
        
    resultA = calculate(memory)

    filtered_memory = list(filter(lambda x: x[2], memory))
    resultB = calculate(filtered_memory)

    print('Part 1:', resultA, ' - found lines:', len(memory))
    print('Part 2:', resultB, ' - found lines:', len(filtered_memory))