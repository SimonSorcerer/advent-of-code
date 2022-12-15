import sys

def getTaxiCabDistance(point1, point2):
    p1x, p1y = point1
    p2x, p2y = point2
    return abs(p2x - p1x) + abs(p2y - p1y)

def getSignalDistances(signals, beacons):
    distances = []

    for i in range(len(signals)):
        distances.append(getTaxiCabDistance(signals[i], beacons[i]))

    return distances

def getSignalRangesOnLine(lineNo, signals, distances):
    min = sys.maxsize
    max = -sys.maxsize
    result = []
    
    for i in range(len(signals)):
        signalX, signalY = signals[i]
        signalStrength = distances[i]
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
        
        result.append((signalMin, signalMax))
    
    return result, min, max

def getSurroundingPoints(signal, signalStrength):
    points = []
    sX, sY = signal

    distance = signalStrength + 1

    points.append((sX, sY + distance))
    points.append((sX, sY - distance))
    for delta in range(1, distance):
        points.append((sX + delta, sY + distance - delta))
        points.append((sX - delta, sY + distance - delta))
        points.append((sX + delta, sY - distance + delta))
        points.append((sX - delta, sY - distance + delta))
    points.append((sX + distance, sY))
    points.append((sX - distance, sY))

    return points

def isPointCovered(point, signals, distances, limit):
    x, y = point
    if x < 0 or y < 0 or x > limit or y > limit:
        return True

    for i in range(len(signals)):
        distance = getTaxiCabDistance(point, signals[i])
        if distance <= distances[i]:
            return True
    return False

def findMissingBeacon(signals, beacons, limit):
    distances = getSignalDistances(signals, beacons)

    for i in range(len(signals)):
        surroundingPoints = getSurroundingPoints(signals[i], distances[i])

        for point in surroundingPoints:
            if not isPointCovered(point, signals, distances, limit):
                return point

def getBeaconsOnLine(lineNo, beacons):
    beaconX = {}

    for bX, bY in beacons:
        if bY == lineNo:
            beaconX[bX] = True

    return len(beaconX.keys())

def getLineCoverage(lineNo, signals, beacons):
    signalDistances = getSignalDistances(signals, beacons)
    signalRangesOnLine, gridMin, gridMax = getSignalRangesOnLine(lineNo, signals, signalDistances)
    covered = 0

    for i in range(gridMin, gridMax + 1):
        for signalRange in signalRangesOnLine:
            rangeMin, rangeMax = signalRange
            if rangeMin <= i and rangeMax >= i:
                covered += 1
                break

    # substract beacons on line
    covered -= getBeaconsOnLine(lineNo, beacons)
        
    return covered