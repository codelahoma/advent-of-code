import re
from collections import namedtuple
from functools import reduce

with open('input.txt', 'r') as f:
    slurp = f.read()

Coordinate = namedtuple('Coordinate', 'x, y')
coord_pattern = r'(\d+), (\d+)'

coordinates = []

for c in slurp.splitlines():
    coords = re.search(coord_pattern, c).groups()
    coords = map(int, coords)
    coordinates.append(Coordinate(*coords))


def distance(coord1, coord2):
    return (abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y))


max_x = max_y = 0

max_x = reduce(lambda max, coord: coord.x if coord.x > max else max,
               coordinates, 0)

max_y = reduce(lambda max, coord: coord.y if coord.y > max else max,
               coordinates, 0)
