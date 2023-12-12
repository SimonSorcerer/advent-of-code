import time;
import re;
import itertools;

filename = 'input.txt'

class bcolors:
    DARKGREY = '\033[1;30m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

SYMBOLS = {
    'unknown': '?',
    'broken': '#',
    'fine': '.'
}

def parse_line(line):
    match = re.search(r'([?.#]+) ([\d,]+)', line)
    history = match.group(1)
    validation = list(map(int, match.group(2).split(',')))

    return history, validation

def history_is_valid(history, validation):
    control_nums = []
    broken_chain = 0

    for char in history:
        if char == SYMBOLS['broken']:
            broken_chain += 1
        elif char == SYMBOLS['fine']:
            if broken_chain > 0:
                control_nums.append(broken_chain)
                broken_chain = 0
        else:
            return False
    if broken_chain > 0:
        control_nums.append(broken_chain)
    
    return control_nums == validation

def unkonwn_count(history):
    return history.count(SYMBOLS['unknown'])

def update_history_with_permutation(history, permutation):
    new_history = list(history)
    for index, char in enumerate(history):
        if char == SYMBOLS['unknown']:
            new_history[index] = permutation.pop(0)
    return new_history

def find_permutations(record):
    history = record[0]
    permutations = list(itertools.product([SYMBOLS['fine'], SYMBOLS['broken']], repeat=unkonwn_count(history)))
    return permutations

def find_valid_permutations(record):
    permutations = find_permutations(record)
    history, validation = record
    valid_permutations = []

    for permutation in permutations:
        permutated_history = update_history_with_permutation(history, list(permutation))
        if history_is_valid(permutated_history, validation):
            valid_permutations.append(permutated_history)

    return valid_permutations

with open(filename, 'r') as f:
    result = 0
    records = []
    startT = time.time()

    for index, line in enumerate(f):
        records.append(parse_line(line.strip()))
      
    for record in records:
        count = len(find_valid_permutations(record))
        print(count, ' - ', record)
        result += count

    endT = time.time()
    print('time:', endT - startT)

    print('part 1:', result)