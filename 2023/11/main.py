import time;
import numpy as np;

filename = 'input.txt'

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

SYMBOLS = {
    'space': '.',
    'galaxy': '#',
}

def visualize(space):
    for line in space:
        for char in line:
            if (char == SYMBOLS['galaxy']):
                print(bcolors.WARNING + char + bcolors.ENDC, end='')
            else: 
                print(char, end='')
        print('\n')

def get_expandable_rows_and_cols(space):
  rows = []
  cols = []
  for index, row in enumerate(space):
    if SYMBOLS['galaxy'] not in row:
      rows.append(index)
  for index, col in enumerate(space[0]):
    if SYMBOLS['galaxy'] not in [row[index] for row in space]:
      cols.append(index)
  return rows, cols

def get_galaxies(space):
  galaxies = []
  for y, row in enumerate(space):
    for x, char in enumerate(row):
        if char == SYMBOLS['galaxy']:
            galaxies.append((x, y))
  return galaxies

def get_galaxy_pairs(galaxies):
  return [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]

def get_distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calculate_expanded_distance(a, b, expandadble_rows, expandadble_cols, expansion_rate = 1):
  distance = get_distance(a, b)
  scanned_rows = [row for row in range(min(a[1], b[1]) + 1, max(a[1], b[1]))]
  scanned_cols = [col for col in range(min(a[0], b[0]) + 1, max(a[0], b[0]))]

  hit_rows = [value for value in scanned_rows if value in expandadble_rows]
  hit_cols = [value for value in scanned_cols if value in expandadble_cols]

  hits = len(hit_rows) + len(hit_cols)

  return distance + hits * (expansion_rate - 1)

def get_galaxy_distances(galaxies, expandable_rows, expandadble_cols, expansion_rate = 1):
  return {pair: calculate_expanded_distance(*pair, expandable_rows, expandadble_cols, expansion_rate) for pair in get_galaxy_pairs(galaxies)}

def get_sum_of_distances(space, expansion_rate = 1):
  galaxy_distances = get_galaxy_distances(get_galaxies(space), expandable_rows, expandable_cols, expansion_rate)
  return sum(galaxy_distances.values())

with open(filename, 'r') as f:
    result = 0
    space = []

    startT = time.time()

    for index, line in enumerate(f):
        space.append([])
        for char in line.strip():
            space[index].append(char)

    #visualize(space)

    expandable_rows, expandable_cols = get_expandable_rows_and_cols(space)
    
    print('expandable_rows:', expandable_rows)
    print('expandable_cols:', expandable_cols)

    print('expansion 2:', get_sum_of_distances(space, 2))
    print('expansion 10', get_sum_of_distances(space, 10))
    print('expansion 100:', get_sum_of_distances(space, 100))
    print('expansion 1000000:', get_sum_of_distances(space, 1000000))

    endT = time.time()
    print('time:', endT - startT)