from enum import Enum
from typing import NamedTuple, Literal

Rotation = Literal["CCW", "CW"]
Position = tuple[int, int]

def add_points(a: Position, b: Position) -> Position:
    return a[0] + b[0], a[1] + b[1]

def rotate(facing: "Direction", rotation: Rotation):
    rotation_map = {
        "CCW": {
            Direction.UP: Direction.LEFT,
            Direction.LEFT: Direction.DOWN,
            Direction.DOWN: Direction.RIGHT,
            Direction.RIGHT: Direction.UP
        },
        "CW": {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP
        }
    }
    return rotation_map[rotation][facing]

class Direction(Enum):
    __order__ = 'UP RIGHT DOWN LEFT'

    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value

    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

class Position(NamedTuple):
    location: Position
    facing: Direction

    @property
    def next_location(self) -> Position:
        return add_points(self.location, Direction(self.facing).value)

    def step(self) -> "Position":
        return Position(self.next_location, self.facing)

    def rotate_and_step(self, towards: Rotation):
        return Position(self.location, rotate(self.facing, towards)).step()