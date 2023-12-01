import re;

filename = 'input.txt'

def get_calibration_num(line):
    first_num = re.search(r'([0123456789])', line).group();
    last_num = re.search(r'([0123456789])(?!.*\d)', line).group();

    return int(first_num) * 10 + int(last_num)

with open(filename, 'r') as f:
    sum = 0

    for line in f:
        calibration_num = get_calibration_num(line.strip())

        sum += calibration_num
        #print('line:', line.strip(), ' - ', calibration_num)

    print('result:', sum)