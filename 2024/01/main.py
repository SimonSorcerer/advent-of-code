import re;

filename = 'input.txt'

def get_line(line):
    first, second = re.match(r'(\d+)\s+(\d+)', line).group(1, 2);

    return int(first), int(second)

def compare_lists(list1, list2):
    sum = 0

    for i in range(len(list1)):
        partial = abs(list1[i] - list2[i])
        sum += partial

    return sum

def get_similarity_map(list):
    map = {}

    for i in range(len(list)):
        map[list[i]] = map[list[i]] + 1 if list[i] in map else 1

    return map

def get_similarity_score(list, similarity_map):
    score = 0

    for i in range(len(list)):
        current = list[i]
        if current in similarity_map:
            score += current * similarity_map[current]

    return score

with open(filename, 'r') as f:
    leftCol = []
    rightCol = []

    for line in f:
        left, right = get_line(line.strip())
        leftCol.append(left)
        rightCol.append(right)

    leftColSorted = sorted(leftCol)
    rightColSorted = sorted(rightCol)

    part1result = compare_lists(leftColSorted, rightColSorted)

    similarity_map = get_similarity_map(rightColSorted)
    # print (similarity_map)
    part2result = get_similarity_score(leftColSorted, similarity_map)

    print('Part 1:', part1result)
    print('Part 2:', part2result)