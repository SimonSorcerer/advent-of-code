import re;

filename = 'input.txt'

code_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six' : 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4' : 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8' : 8,
    '9': 9,
}

def get_calibration_num(line):
    matches = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9))', line)
    
    first_num = code_map[matches[0]]
    last_num = code_map[matches[-1]]

    return int(first_num) * 10 + int(last_num);


with open(filename, 'r') as f:
    sum = 0

    for line in f:
        calibration_num = get_calibration_num(line.strip())

        sum += calibration_num
        #print('line:',  line.strip(), ' - ', calibration_num)

    print('result:', sum)