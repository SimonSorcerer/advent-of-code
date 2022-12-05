def getIntersect(a, b):
    intersect = { 'start': 0, 'end': 0 }

    if not a['start'] > b['end'] and not b['start'] > a['end']:
        intersect['start'] = max(a['start'], b['start'])
        intersect['end'] = min(a['end'], b['end'])
  
    return intersect

def getSection(pair):
    split = pair.split('-')
    return { 'start': int(split[0]), 'end': int(split[1]) }

def getPairs(line):
    pairs = line.split(',')
    a = getSection(pairs[0])
    b = getSection(pairs[1])
    return a, b

def sectionsEqual(section1, section2):
    return section1['start'] == section2['start'] and section1['end'] == section2['end']

with open('input.txt', 'r') as f:
    uselessSections = 0
    overlappingSections = 0

    for line in f:
        a, b = getPairs(line.strip())
        intersect = getIntersect(a, b)
        
        if sectionsEqual(a, intersect) or sectionsEqual(b, intersect):
            uselessSections += 1
        
        if intersect['start'] > 0 and intersect['end'] > 0:
            overlappingSections += 1
    
    print('with useless section: ', uselessSections)
    print('overlapping sections: ', overlappingSections)
