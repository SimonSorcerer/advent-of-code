def create_summary(elf):
    sum = 0

    for calories in elf:
        sum += calories

    return sum

def find_max(sums):
    max = 0
    maxIndex = 0

    for index, item in enumerate(sums):
        if item > max:
            max = item
            maxIndex = index
        
    return max, maxIndex

with open('input.txt', 'r') as f:
    elf = []
    summaries = []
    index = 0

    for line in f:
        if len(line.strip()) == 0:
            summaries.append(create_summary(elf))
            index += 1
            elf = []
        else: 
            calories = int(line.strip())
            elf.append(calories)

    summaries.append(create_summary(elf))

    for index, item in enumerate(summaries):
        print('sum[', index, '] is: ', item)

    max_1, maxI_1 = find_max(summaries)
    summaries[maxI_1] = 0

    max_2, maxI_2 = find_max(summaries)
    summaries[maxI_2] = 0

    max_3, maxI_3 = find_max(summaries)

    print(maxI_1, ': ', max_1)
    print(maxI_2, ': ', max_2)
    print(maxI_3, ': ', max_3)

    print(max_1 + max_2 + max_3)