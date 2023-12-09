import re;
import time;

filename = 'input.txt'

def parse_history(line):
    numbers = re.findall(r'(-?\d+)', line)
    return list(map(int, numbers))
    
def list_not_zero(history):
    for value in history:
        if (value != 0):
            return True
    return False

def calculate_differences(history):
    result = {}
    depth = 0
    result[0] = history

    while list_not_zero(result[depth]):
      last_values = result[depth]
      depth += 1
      result[depth] = []
      for key in range(1, len(last_values)):
          result[depth].append(last_values[key] - last_values[key - 1])
      #print(result[depth])

    return result


with open(filename, 'r') as f:
    result = 0
    result_2 = 0
    startT = time.time()

    for index, line in enumerate(f, 1):
        history = parse_history(line)
        diffs = calculate_differences(history)

        sub_result = 0
        sub_result_part_2 = 0
        pivot = 1
        for index, depth in enumerate(diffs):
            sub_result += diffs[depth][-1]
            sub_result_part_2 = sub_result_part_2 + diffs[depth][0] * pivot
            pivot *= -1

        result += sub_result
        result_2 += sub_result_part_2

    endT = time.time()
    
    print('time:', endT - startT)
    print('part 1:', result)
    print('part 2:', result_2)