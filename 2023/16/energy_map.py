energy_map = {}

def clear_energy_map():
    energy_map.clear()

def energized(position):
    result = energy_map.get(position)
    if result == None:
        energy_map[position] = []
    
    return energy_map[position]

def mark(position, direction):
    energy = energized(position)

    if (direction in energy):
        return False
    else:
        energy_map[position].append(direction)
        return True
    
def count_energized_tiles():
    result = 0
    for item in energy_map:
        result += 1 if len(energy_map[item]) > 0 else 0
    return result
    
def is_in_map(contraption, position):
    x, y = position
    return 0 <= y < len(contraption) and 0 <= x < len(contraption[0])