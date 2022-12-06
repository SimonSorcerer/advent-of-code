from collections import deque

START_OF_PACKET_LEN = 4
START_OF_MESSAGE_LEN = 14

def isValidMarker(marker, validLength):
    map = {}

    for char in marker:
        map[char] = True

    return len(map) == validLength

def getMarkerIndex(line, markerLength):
    sequence = deque([])
    result = 0

    for index, char in enumerate(line):
        if len(sequence) == markerLength:
            sequence.popleft()      
        sequence.append(char)

        if isValidMarker(sequence, markerLength):
            result = index + 1
            break

    return result

with open('input.txt', 'r') as f:
    for line in f:
        print('start of packet: ', getMarkerIndex(line.strip(), START_OF_PACKET_LEN))
        print('start of message:', getMarkerIndex(line.strip(), START_OF_MESSAGE_LEN))
