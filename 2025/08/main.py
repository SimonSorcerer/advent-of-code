import re
import sys
import time
import math

filename = 'input.txt'

MAX_ITERATIONS_10 = 10
MAX_ITERATIONS_1000 = 1000
MAX_ITERATIONS_INFINITE = sys.maxsize

def parse_line(line):
    return list(map(int, line.split(',')))

def squared_distance(p1, p2):
    return math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2) + math.pow(p2[2] - p1[2], 2)

def create_distance_map(lines):
    distance_map = dict()

    for i in range(len(lines)):
        pointA = lines[i]
        for j in range(i + 1, len(lines)):
            pointB = lines[j]
            distance = squared_distance(pointA, pointB)
            distance_map[(i, j)] = distance
    
    return sorted(distance_map.items(), key=lambda x: x[1])

def find_circuits(distance_map, iterations, points_count):
    circuits = list()
    circuit_ref = dict()
    last_connection = None
    
    for k in range(iterations):
        if k >= len(distance_map):
            break

        # part 2 - stop if we have a full circuit of all point
        if len(circuits) == 1 and len(circuits[0]) == points_count:
            last_connection = (point_a, point_b)
            break

        dist = distance_map[k]
        point_a, point_b = dist[0][0], dist[0][1]

        if point_a not in circuit_ref and point_b not in circuit_ref:
            circuit = set([point_a, point_b])
            circuits.append(circuit)
            circuit_ref[point_a] = circuit
            circuit_ref[point_b] = circuit
        elif point_a in circuit_ref and point_b not in circuit_ref:
            circuit = circuit_ref[point_a]
            circuit.add(point_b)
            circuit_ref[point_b] = circuit
        elif point_b in circuit_ref and point_a not in circuit_ref:
            circuit = circuit_ref[point_b]
            circuit.add(point_a)
            circuit_ref[point_a] = circuit
        else:
            circuit_a = circuit_ref[point_a]
            circuit_b = circuit_ref[point_b]
            
            # case for merging two different circuits
            if circuit_a is not circuit_b:
                circuit_a.update(circuit_b)
                for point in circuit_b:
                    circuit_ref[point] = circuit_a
                circuits.remove(circuit_b)

    return sorted(circuits, key=lambda x: len(x), reverse=True), last_connection

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time.time()

    with open(filename, 'r') as f:
        lines = list(map(parse_line, f.read().splitlines()))

    distance_map = create_distance_map(lines)
    circuits, _ = find_circuits(distance_map, iterations=MAX_ITERATIONS_1000, points_count=len(lines))
    _, last_connection = find_circuits(distance_map, iterations=MAX_ITERATIONS_INFINITE, points_count=len(lines))
    
    # print('Circuits created:', circuits)
    # print('Last connection:', last_connection)

    part1result = math.prod(len(c) for c in circuits[:3])
    if (last_connection is not None):
        part2result = lines[last_connection[0]][0] * lines[last_connection[1]][0]

    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)