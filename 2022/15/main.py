from signal import getLineCoverage, findMissingBeacon
import re
import time

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
    signals = []
    beacons = []
    limit = 4000000

    for line in lines:
        signal, beacon = parseLine(line)
        signals.append(signal)
        beacons.append(beacon)

    beaconX, beaconY = findMissingBeacon(signals, beacons, limit)

    return beaconX * 4000000 + beaconY

lines = getData('input.txt')

st = time.time()
result1 = part1(lines)
mt = time.time()

print('Part 1 (', round(mt - st, 2), 'sec ):', result1)

result2 = part2(lines)

et = time.time()

print('Part 2 (', round(et - mt, 2), 'sec ):', result2)