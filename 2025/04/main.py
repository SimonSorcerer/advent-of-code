import re;
import time

filename = 'input.txt'

PAPER_ROLL = '@'
EMPTY = '.'
MAX_ROLLS_AROUND = 4

def read_line(line):
    return list(line.strip())

def get_available_directions(rolls, index, size):
    directions = set([-1, 1, -size, size, -size - 1, -size + 1, size - 1, size + 1])

    if (index < size):
        directions.remove(-size)
        directions.remove(-size - 1)
        directions.remove(-size + 1)
    if (index >= len(rolls) - size):
        directions.remove(size)
        directions.remove(size - 1)
        directions.remove(size + 1)
    if (index % size == 0):
        if size - 1 in directions: directions.remove(size - 1)
        if -1 in directions: directions.remove(-1)
        if -size - 1 in directions: directions.remove(-size - 1)
    if (index % size == size - 1):
        if -size + 1 in directions: directions.remove(-size + 1)
        if 1 in directions: directions.remove(1)
        if size + 1 in directions: directions.remove(size + 1)

    return directions

def num_of_paper_rolls_around(rolls, index, size):
    sum = 0
    directions = get_available_directions(rolls, index, size)

    for d in directions:
        neighbor_index = index + d
        if 0 <= neighbor_index < len(rolls) and rolls[neighbor_index] == PAPER_ROLL:
            sum += 1
    return sum
    
with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time.time()

    rolls = []
    surrounding_rolls_map = []
    marked_for_removal = set()
    size = -1

    for line in f:
        rolls += read_line(line)
        if (size == -1):
            size = len(rolls)

    for i in range(len(rolls)):
        surrounding_rolls_map.append(num_of_paper_rolls_around(rolls, i, size))
        if rolls[i] == PAPER_ROLL and surrounding_rolls_map[i] < MAX_ROLLS_AROUND:
            marked_for_removal.add(i)

    part1result = len(marked_for_removal) # first iteration result

    removed_rolls = set(marked_for_removal)
    while len(marked_for_removal) > 0:
        # print('Removing ', len(marked_for_removal), ' rolls at indices:', marked_for_removal)

        new_marked_for_removal = set()

        for index in marked_for_removal:
            rolls[index] = EMPTY
            directions = get_available_directions(rolls, index, size)

            for d in directions:
                neighbor_index = index + d
                if 0 <= neighbor_index < len(rolls) and rolls[neighbor_index] == PAPER_ROLL:
                    surrounding_rolls_map[neighbor_index] -= 1
                    if surrounding_rolls_map[neighbor_index] < MAX_ROLLS_AROUND and neighbor_index not in removed_rolls:
                        new_marked_for_removal.add(neighbor_index)    
        marked_for_removal = new_marked_for_removal
        removed_rolls.update(marked_for_removal)
    
    part2result = len(removed_rolls)
   
    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)