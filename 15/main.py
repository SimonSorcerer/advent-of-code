from signal import getLineCoverage
import re

def getData(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    return lines

def parseLine(line):
    result = re.findall(r'(-?\d+)', line)
    signal = int(result[0]), int(result[1])
    beacon = int(result[2]), int(result[3])

    return signal, beacon

def part1(lines):
    signals = []
    beacons = []

    for line in lines:
        signal, beacon = parseLine(line)
        signals.append(signal)
        beacons.append(beacon)

    return getLineCoverage(2000000, signals, beacons)

def part2(lines):
    return 

lines = getData('input.txt')
print('Part 1:', part1(lines))
#print('Part 2:', part2(lines))