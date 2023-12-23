from energy_map import energized
from beam_utils import DIRECTION

class bcolors:
    LIGHT_RED = "\033[1;31m"
    DARK_GRAY = '\033[1;30m'
    LIGHT_GRAY = "\033[0;37m"
    ENDC = '\033[0m'

def visualize(contraption):
    for y, line in enumerate(contraption):
        for x, _ in enumerate(line):
            if (len(energized((x, y))) > 0):
                print(bcolors.LIGHT_RED + '#' + bcolors.ENDC, end='')
            else:
                print(bcolors.LIGHT_GRAY + '.' + bcolors.ENDC, end='')
        print('\n')

def get_configurations(contraption):
    configurations = []
    height = len(contraption)
    width = len(contraption[0])

    for x in range(width):
        configurations.append(((x, 0), DIRECTION['down']))
        configurations.append(((x, height - 1), DIRECTION['up']))
    
    for y in range(height):
        configurations.append(((0, y), DIRECTION['right']))
        configurations.append(((width - 1, y), DIRECTION['left']))

    return configurations