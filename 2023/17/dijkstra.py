from heapq import heappop, heappush
from position import Position, Direction

State = tuple[int, Position, int]

def get_value(matrix, position):
    return matrix[position.location[1]][position.location[0]]

def in_matrix(matrix, position):
    pos = position.location
    return pos[0] >= 0 and pos[0] < len(matrix) and pos[1] >= 0 and pos[1] < len(matrix[0])

def not_dijkstra_really(matrix, min_steps = 0, max_steps = 3):
    # last item is the target
    target = len(matrix) - 1, len(matrix[-1]) - 1

    # from start go down and right
    queue: list[State] = [
        (0, Position((0, 0), Direction.DOWN), 0),
        (0, Position((0, 0), Direction.RIGHT), 0),
    ]
    seen: set[tuple[Position, int]] = set()

    while queue:
        cost, pos, num_steps = heappop(queue)
        #print(queue)

        if pos.location == target:
            return cost

        if (pos, num_steps) in seen:
            continue
        seen.add((pos, num_steps))

        if num_steps >= min_steps and in_matrix(matrix, left := pos.rotate_and_step("CCW")):
            heappush(queue, (cost + get_value(matrix, left), left, 1))
        if num_steps >= min_steps and in_matrix(matrix, right := pos.rotate_and_step("CW")):
            heappush(queue, (cost + get_value(matrix, right), right, 1))
        if num_steps < max_steps and in_matrix(matrix, forward := pos.step()):
            heappush(queue, (cost + get_value(matrix, forward), forward, num_steps + 1))

    return -1

# # Example graph represented as a 2D array
# graph = [[0, 7, 9, 0, 0, 14],
#          [7, 0, 10, 15, 0, 0],
#          [9, 10, 0, 11, 0, 2],
#          [0, 15, 11, 0, 6, 0],
#          [0, 0, 0, 6, 0 , 9],
#          [14, 2, 0, 9, 8, 10]]
