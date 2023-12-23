def hash_line(line):
    steps = line.split(',')

    result = 0
    for step in steps:
        result += hash_step(step)
    return result

def hash_step(step):
    result = 0
    for char in step:
        result = hash(result, char)
    return result

def hash(initial_value, char):
    result = initial_value

    result += ord(char)
    result *= 17
    result %= 256

    return result