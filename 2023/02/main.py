import re;

filename = 'input.txt'

colors = ['red', 'green', 'blue']
maximums = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def parse_cube_sets(line):
    parsed = re.search(r'Game \d+: (.*)', line).group(1)
    sets = parsed.split(';')
    return sets

def get_color_counts(set):
    counts = {}
    for color in colors:
        match = re.search(rf"(\d+) {color}", set)
        if (match):
            count = int(match.group(1))
            counts[color] = count
        else:
            counts[color] = 0
    
    return counts

def get_game_power(sets):
    cube_max = {}
    result = 1

    for color in colors:
        cube_max[color] = 1
        for set in sets:
            cube_max[color] = set[color] if (set[color] > cube_max[color]) else cube_max[color]
        result *= cube_max[color]
    
    return result

with open(filename, 'r') as f:
    sum = 0
    power_sum = 0
    bag_info = {}

    for index, line in enumerate(f, 1):
        bag_info[index] = []
        sets = parse_cube_sets(line.strip())
        is_valid_set = True
        # print(index, ': ', sets)

        for set in sets:
            counts = get_color_counts(set)
            bag_info[index].append(counts)

            for count in counts:
                if (not is_valid_set):
                    break
                
                for color in maximums:
                    if (counts[color] > maximums[color]):
                        is_valid_set = False
                        break

        if (is_valid_set):  
          #print('Game ', index, ' is possible')
          sum += index

        game_power = get_game_power(bag_info[index])
        #print('Game ', index,' power: ', game_power)
        power_sum += game_power

    print('result:', sum)
    print('result 2:', power_sum)