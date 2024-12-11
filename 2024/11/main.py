import re
import time
# lib for fast multiplication
from karatsuba import multiply, removeLeadingZeros

filename = 'input.txt'

results_cache = {
    0: ['1'],
}

def parse_line(line):
    return list(re.findall(r'\d+', line));

def split_stone(stone):
    length = len(stone)

    part1 = removeLeadingZeros(stone[:length//2])
    part2 = removeLeadingZeros(stone[length//2:])

    return [part1, part2]

def stone_tick(stone):
    if stone in results_cache:
        return results_cache[stone]
    
    if (stone == '0'):
        result = ['1']
    elif len(stone) % 2 == 0:
        result = split_stone(stone)
    else:
        result = [multiply(stone, '2024')]
    
    results_cache[stone] = result
    return result;

def add_stones_to_pile(stones, repeat, stone_pile):
    for stone in stones:
        stone_pile[stone] = stone_pile.get(stone, 0) + repeat

def remove_stone_from_pile(stone, stone_pile):
    del stone_pile[stone]

def get_stones_to_calculate(stone_pile):
    return list(stone_pile.keys())

def tick(stones, times):
    stone_pile = {}
    # grouping stones by their value to lower the number of calculations
    add_stones_to_pile(stones, 1, stone_pile) 

    for _ in range(times):
        stones = get_stones_to_calculate(stone_pile)
        
        new_pile = {}
        for stone in stones:
            results = stone_tick(stone)
            repeat = stone_pile[stone]
            add_stones_to_pile(results, repeat, new_pile)
        
        stone_pile = new_pile
        # print("stones after tick:", stone_pile)

    return stone_pile

def count_stones(stone_pile):
    return sum(stone_pile.values())

with open(filename, 'r') as f:
    stones = []

    for index, line in enumerate(f):
        stones += parse_line(line.strip())

    future_stones = tick(stones, 25)

    start = time.time()
    far_future_stones = tick(stones, 75)
    end = time.time()

    print('Time:', end - start)

    resultA = count_stones(future_stones)
    resultB = count_stones(far_future_stones)

    print('Part 1:', resultA)
    print('Part 2:', resultB)