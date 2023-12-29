import time;
from parse_utils import parse_matrix, visualize
from dijkstra import not_dijkstra_really

filename = 'input.txt'

with open(filename, 'r') as f:
    result = 0
    result2 = 0

    startT = time.time()
    # -----------------------------------------------
    # part 1
    # -----------------------------------------------
    matrix = parse_matrix(f)
    result = not_dijkstra_really(matrix, 0, 3)
    visualize(matrix)

    # -----------------------------------------------
    # part 2
    # -----------------------------------------------
    result2 = not_dijkstra_really(matrix, 4, 10)

    # -----------------------------------------------
    endT = time.time()
    
    print('time:', endT - startT)
    print('part 1:', result)
    print('part 2:', result2)