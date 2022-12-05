def evalMe(val):
    if val == 'X':
        return 1
    elif val == 'Y':
        return 2
    elif val == 'Z':
        return 3

def evalResult(them, me):
    wins = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
    ties = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
    
    if (them, me) in wins:
        return 6
    elif (them, me) in ties:
        return 3
    else:
        return 0

with open('input.txt', 'r') as f:
    score = 0

    for line in f:
        them = line[0]
        me = line[2]
        print(them, ' ', me)
        score += evalMe(me)
        score += evalResult(them, me)
        print(score)