import re;

filename = 'input.txt'

def is_digit(char):
    return char.isdigit()

def is_symbol(char): 
    return char != '.' and not char.isdigit()

def is_gear(char):
    return char == '*'

def get_numbers(line, y_modifier):
    numbers = []

    for match in re.finditer(r'(\d+)', line):
        (start, end) = match.span()
        value = int(match.group())
        numbers.append((value, start + y_modifier, end + y_modifier))
    return numbers

def get_symbol_map(line, y_modifier, gears_only = False):
    symbol_map = []

    for x, char in enumerate(line):
        if ((gears_only and is_gear(char)) or (not gears_only and is_symbol(char))):
            symbol_map.append(x + y_modifier)

    return symbol_map

def get_heat_map(symbol_map, line_size):
    heat_map = []

    for position in symbol_map:
        for delta in (-line_size - 1, -line_size, -line_size + 1, -1, 1, line_size - 1, line_size, line_size + 1):
            if (position + delta >= 0):
              heat_map.append(position + delta)
    return heat_map

with open(filename, 'r') as f:
    sum = 0
    gear_sum = 0
    numbers = []
    symbol_map = []
    gear_map = []

    for y, line in enumerate(f):
        line_size = len(line.strip())

        numbers += get_numbers(line.strip(), y * line_size)
        symbol_map += get_symbol_map(line.strip(), y * line_size)
        gear_map += get_symbol_map(line.strip(), y * line_size, True)

    heat_map = get_heat_map(symbol_map, line_size)

    for (number, start, end) in numbers:
        for number_position in range(start, end):
            if (number_position in heat_map):
                sum += number
                break
            
    for gear in gear_map:
        ratios = []
        gear_heat_map = get_heat_map([gear], line_size)

        for (number, start, end) in numbers:
            for number_position in range(start, end):
                if (number_position in gear_heat_map):
                    ratios.append(number)
                    break
        
        if len(ratios) == 2:
            #print('ratios:', ratios)
            gear_sum += ratios[0] * ratios[1]
      
    # print('numbers:', numbers)
    # print('----------------')
    # print('symbol_map:', symbol_map)
    # print('----------------')
    # print('heat_map:', heat_map)
    # print('----------------')
    # print('gear_map:', gear_map)
    # print('----------------')
    # print('gear_heat_map:', gear_heat_map)
    print('result:', sum)
    print('result 2:', gear_sum)