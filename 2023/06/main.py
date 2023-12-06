import re;
import time;

filename = 'input2.txt'

def parse_line(line):
    result = []
    numbers = re.findall(r'(\d+)', line)
    
    for number in numbers:
        result.append(int(number))
    
    return result

def get_successes(max_time, max_distance):
    distance = 0
    charge_time = 0

    while (distance <= max_distance):
        charge_time += 1
        travel_time = max_time - charge_time
        distance = travel_time * charge_time

    success_scenarios_count = max_time + 1 - 2 * charge_time
    #print(success_scenarios_count, charge_time)
    return success_scenarios_count


with open(filename, 'r') as f:
    result = 1

    startT = time.time()

    for index, line in enumerate(f, 1):
        if index == 1:
            times = parse_line(line)
        elif index == 2:
            distances = parse_line(line)
        
    for index, race_time in enumerate(times):
        result *= get_successes(race_time, distances[index])

    endT = time.time()
    
    print('time:', endT - startT)
    print('result:', result)