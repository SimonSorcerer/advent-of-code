import time;
import numpy as np;

filename = 'test.txt'

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
    

def expand_rows(space):
  new_space = []
  for row in space:
    if SYMBOLS['galaxy'] not in row:
      new_space.extend([row] * 2)
    else:
      new_space.append(row)
  return new_space

def rotate_matrix(matrix, clockwise=True):
    return np.rot90(matrix) if clockwise else np.rot90(matrix, k=1, axes=(1, 0))

def expand(space):
  new_space = expand_rows(space)
  new_space = rotate_matrix(new_space)
  new_space = expand_rows(new_space)
  new_space = rotate_matrix(new_space, clockwise=False)
  return new_space

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

def get_galaxy_distances(galaxies):
  return {pair: get_distance(*pair) for pair in get_galaxy_pairs(galaxies)}

def get_sum_of_distances(galaxy_distances):
  return sum(galaxy_distances.values())

with open(filename, 'r') as f:
    result = 0
    space = []

    startT = time.time()

    for index, line in enumerate(f):
        space.append([])
        for char in line.strip():
            space[index].append(char)

    expanded_space = expand(space)
    visualize(expanded_space)

    galaxy_distances = get_galaxy_distances(get_galaxies(expanded_space))

    endT = time.time()
    
    print('time:', endT - startT)
    print('part 1:', get_sum_of_distances(galaxy_distances))