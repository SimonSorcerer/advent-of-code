def splitLine(line):
    linesize = len(line)
    pivot = int(linesize / 2)
    part1 = line[0:pivot]
    part2 = line[pivot:linesize]

    return part1, part2

def findSharedChar(part1, part2):
    dict = {}
    result = ''

    for letter in part1:
        dict[letter] = 1

    for letter in part2:
        if letter in dict:
            result = letter

    return result

def getCharValue(char):
    if char.isupper():
        correction = ord('A') - 27
    else:
        correction = ord('a') - 1
    
    return ord(char) - correction

with open('input.txt', 'r') as f:
    sum = 0

    for line in f:
        part1, part2 = splitLine(line.strip())
        sharedChar = findSharedChar(part1, part2)
        sum += getCharValue(sharedChar)

    print(sum)