import re;

filename = 'input.txt'

def parse_numbers(set):
    numbers = re.findall(r'([\d]+)', set)
    return map(int, numbers)

def parse_ticket(line):
    match = re.search(r'Card +\d+: ([^|]+) \| ([\d ]+)', line)
        
    winning_numbers = parse_numbers(match.group(1))
    my_numbers = parse_numbers(match.group(2))
    
    return (winning_numbers, my_numbers)

def get_overlapping_numbers(winning_numbers, my_numbers):
    return set(winning_numbers).intersection(set(my_numbers))

def update_card_pile(card_pile, starting_index, count):
    if (starting_index not in card_pile):
        card_pile[starting_index] = 1
    else:
        card_pile[starting_index] += 1

    factor = card_pile[starting_index]

    for index in range(starting_index + 1, starting_index + count + 1):
        card_pile[index] = card_pile[index] + factor if (index in card_pile) else factor
    
    #print('updated card_pile:', card_pile)
    return card_pile

def count_card_pile(card_pile, size):
    result = 0
    for index in range(1, size + 1):
       result += card_pile[index]
    return result 

with open(filename, 'r') as f:
    score = 0
    card_pile = {}

    for index, line in enumerate(f, 1):
        (winning_numbers, my_numbers) = parse_ticket(line.strip())
        overlapping_numbers = get_overlapping_numbers(winning_numbers, my_numbers)
        sub_score = 2 ** (len(overlapping_numbers) - 1)

        # part 1
        score += sub_score if (sub_score >= 1) else 0
        # part 2
        update_card_pile(card_pile, index, len(overlapping_numbers))

    print('result:', score)
    print('result 2:', count_card_pile(card_pile, index))