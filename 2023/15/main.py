import time;
from hash_utils import hash_line
from part_2_utils import parse_sequence, get_focusing_power
from box_utils import visualize, get_boxes

filename = 'input.txt'

with open(filename, 'r') as f:
    result = 0
    result2 = 0

    startT = time.time()

    for line in f:
        # part 1
        result = hash_line(line.strip())
        # part 2
        parse_sequence(line.strip())
        visualize()
        result2 = get_focusing_power(get_boxes())

    endT = time.time()
    
    print('time:', endT - startT)
    print('part 1:', result)
    print('part 2:', result2)