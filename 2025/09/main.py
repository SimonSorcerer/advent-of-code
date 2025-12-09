import re
import time
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

filename = 'input.txt'

def parse_line(line):
    return tuple(map(int, line.split(',')))

def plot_polygon(polygon, rectange_points):
    _, ax = plt.subplots()
    
    x, y = polygon.exterior.xy
    ax.fill(x, y, alpha=0.3, fc='lightblue', ec='blue', linewidth=2)

    rect_x, rect_y = Polygon(get_rectangle_corners(*rectange_points)).exterior.xy
    ax.fill(rect_x, rect_y, alpha=0.5, fc='red', ec='darkred')

    ax.set_aspect('equal')
    plt.grid(True)
    plt.show()

def get_area(pointA, pointB):
    return (abs(pointA[0] - pointB[0]) + 1) * (abs(pointA[1] - pointB[1]) + 1)

def get_largest_area(points):
    max_area = 0            # Largest area without constraints - part 1
    max_inset_area = 0      # Largest area fully inside polygon - part 2
    polygon = Polygon(points)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            area = get_area(points[i], points[j])
            if is_valid_rectangle(points[i], points[j], polygon):
                if area > max_inset_area:
                    max_inset_area = area
                    # max_inset_points = [points[i], points[j]]
            max_area = max(max_area, area)

    # plot_polygon(polygon, max_inset_points)
    return max_area, max_inset_area

def get_rectangle_corners(pointA, pointB):
    return [
        (pointA[0], pointA[1]),
        (pointA[0], pointB[1]),
        (pointB[0], pointB[1]),
        (pointB[0], pointA[1])
    ]

def is_valid_rectangle(pointA, pointB, polygon):
    rectangle = Polygon(get_rectangle_corners(pointA, pointB))
    return polygon.contains(rectangle)

with open(filename, 'r') as f:
    part1result = 0
    part2result = 0

    start = time.time()

    with open(filename, 'r') as f:
        points = list(map(parse_line, f.read().splitlines()))

    part1result, part2result = get_largest_area(points)

    end = time.time()
    print('Execution time:', end - start)

    print('Part 1:', part1result)
    print('Part 2:', part2result)