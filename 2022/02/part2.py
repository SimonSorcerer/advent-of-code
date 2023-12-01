def evalResult(val):
    if val == 'X':
        return 0
    elif val == 'Y':
        return 3
    elif val == 'Z':
        return 6

def evalMe(val):
    if val == 'A':
        return 1
    elif val == 'B':
        return 2
    elif val == 'C':
        return 3

def getMe(them, result):
    rock = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    paper = [('A', 'Z'), ('B', 'Y'), ('C', 'X')]
    # scissors = [('A', 'X'), ('B', 'Z'), ('C', 'Y')]

    if (them, result) in rock:
        return 'A'
    elif (them, result) in paper:
        return 'B'
    else: 
        return 'C'

def evalRound(them, result):
    return evalResult(result) + evalMe(getMe(them, result))

with open('input.txt', 'r') as f:
    score = 0

    for line in f:
        them = line[0]
        result = line[2]
        score += evalRound(them, result)
        print(them, ' ', result, evalRound(them, result))
    
    print(score)