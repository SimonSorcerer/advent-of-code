class bcolors:
    LIGHT_RED = "\033[1;31m"
    DARK_GRAY = '\033[1;30m'
    LIGHT_GRAY = "\033[0;37m"
    ENDC = '\033[0m'

def parse_matrix(file):
    matrix = []

    for index, line in enumerate(file):
            matrix.append([])
            for char in line.strip():
                matrix[index].append(int(char))
    
    return matrix

def visualize(matrix):
    for _, line in enumerate(matrix):
            print()
            for char in line:
                print(bcolors.DARK_GRAY + str(char) + bcolors.ENDC, end=' ')
    print()