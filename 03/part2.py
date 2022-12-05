def findSharedChar(line1, line2, line3):
    dict = {}
    dict2 = {}
    result = ''

    for letter in line1:
        dict[letter] = 1

    for letter in line2:
        if letter in dict:
            dict2[letter] = 1

    for letter in line3:
        if letter in dict2:
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
    line1, line2, line3 = '', '', ''

    for line in f:
        stripped = line.strip()

        if not line1:
            line1 = stripped
        elif not line2:
            line2 = stripped
        elif not line3:
            line3 = stripped

        if line1 and line2 and line3:
            sharedChar = findSharedChar(line1, line2, line3)
            sum += getCharValue(sharedChar)
            line1, line2, line3 = '', '', ''

    print(sum)
