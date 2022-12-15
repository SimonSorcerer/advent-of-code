import sys

def getTaxiCabDistance(point1, point2):
    p1x, p1y = point1
    p2x, p2y = point2
    return abs(p2x - p1x) + abs(p2y - p1y)

def getSignalRangesOnLine(lineNo, signals, beacons):
    ranges = []
    min = sys.maxsize
    max = -sys.maxsize
    
    for i in range(len(signals)):
        signalX, signalY = signals[i]
        signalStrength = getTaxiCabDistance(signals[i], beacons[i])
        strengthReduction = abs(signalY - lineNo)
        signalStrengthReduced = signalStrength - strengthReduction

        # signal is too weak on the line we are checking
        if signalStrengthReduced <= 0:
            continue

        signalMin = signalX - signalStrengthReduced
        signalMax = signalX + signalStrengthReduced

        if signalMin < min: 
            min = signalMin
        if signalMax > max: 
            max = signalMax
        
        ranges.append((signalMin, signalMax))
    
    return ranges, min, max

def getBeaconsOnLine(lineNo, beacons):
    beaconX = {}

    for bX, bY in beacons:
        if bY == lineNo:
            beaconX[bX] = True

    return len(beaconX.keys())

def getLineCoverage(lineNo, signals, beacons):
    signalRanges, gridMin, gridMax = getSignalRangesOnLine(lineNo, signals, beacons)
    covered = 0

    for i in range(gridMin, gridMax + 1):
        for signalRange in signalRanges:
            rangeMin, rangeMax = signalRange
            if rangeMin <= i and rangeMax >= i:
                covered += 1
                break

    # substract beacons on line
    covered -= getBeaconsOnLine(lineNo, beacons)
        
    return covered