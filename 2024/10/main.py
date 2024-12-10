from colors import printC, WHITE, RED, CYAN;
from graph import DirectedGraph;

filename = 'input.txt'

def parse_line(line):
    return list(map(int, list(line)))

def print_map(map):
    for i, line in enumerate(map):
        for j, cell in enumerate(line):
            if cell == 9: color = RED
            elif cell == 0: color = CYAN
            else: color = WHITE
            printC(color, cell, ' ')
        print('')

def get_trail_heads(hike_map):
    trail_heads = []
    for i, line in enumerate(hike_map):
        for j, cell in enumerate(line):
            if cell == 0:
                trail_heads.append((j, i))
    print("trailHeads", trail_heads)
    return trail_heads

def is_in_map(hike_map, pos):
    x, y = pos
    return x >= 0 and x < len(hike_map[0]) and y >= 0 and y < len(hike_map)

def add_edge(graph, pos1, pos2):
    if is_in_map(hike_map, pos1) and is_in_map(hike_map, pos2):
        cell1 = hike_map[pos1[1]][pos1[0]]
        cell2 = hike_map[pos2[1]][pos2[0]]
        if (cell1 + 1 == cell2):
            graph.add_edge((pos1, cell1), (pos2, cell2))

def create_hike_graph(hike_map):
    graph = DirectedGraph()
    start_vertices = []

    for i, line in enumerate(hike_map):
        for j, cell in enumerate(line):
            vertex = ((j, i), cell)
            graph.add_vertex(vertex)
            if cell == 0:
                start_vertices.append(vertex)
    
    for i, line in enumerate(hike_map):
        for j, cell in enumerate(line):
            add_edge(graph, (j, i), (j + 1, i))
            add_edge(graph, (j, i), (j, i + 1))
            add_edge(graph, (j, i), (j - 1, i))
            add_edge(graph, (j, i), (j, i - 1))

    return graph, start_vertices

def count_peaks(graph, start_vertices):
    peaks_traversed = 0

    for vertex in start_vertices: 
        traversed = graph.traverse(vertex)
        for node in traversed:
            if node[1] == 9:
                peaks_traversed += 1

    return peaks_traversed

def count_trails(graph, start_vertices):
    trails_discovered = 0

    for vertex in start_vertices:
        trails = graph.find_all_paths(vertex)
        trails_discovered += len(trails)

    return trails_discovered

with open(filename, 'r') as f:
    hike_map = []

    for index, line in enumerate(f):
        hike_map.append(parse_line(line.strip()))

    print_map(hike_map)
    
    hike_graph, start_vertices = create_hike_graph(hike_map)
    # hike_graph.print_graph()

    resultA = count_peaks(hike_graph, start_vertices)
    resultB = count_trails(hike_graph, start_vertices)

    print('Part 1:', resultA)
    print('Part 2:', resultB)