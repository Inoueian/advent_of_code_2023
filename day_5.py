import numpy as np


def inclusive_range(x1, x2):
    """Returns a version of `range` where both endpoints are included."""
    if x1 < x2:
        return range(x1, x2 + 1)
    else:
        return range(x1, x2 - 1, -1)


def parse_line(line):
    start, _, end = line.split()
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    return int(x1), int(y1), int(x2), int(y2)


def parse_input(data):
    lines = data.split('\n')
    return [parse_line(line) for line in lines]


def get_line_locations(x1, y1, x2, y2):
    if x1 == x2:
        return [(x1, y) for y in inclusive_range(y1, y2)]
    elif y1 == y2:
        return [(x, y1) for x in inclusive_range(x1, x2)]
    return []


def get_diagonal_line_locations(x1, y1, x2, y2):
    if abs(x1 - x2) == abs(y1 - y2):
        return [(x, y) for x, y in zip(inclusive_range(x1, x2),
                                       inclusive_range(y1, y2))]
    else:
        return []


def count_lines(data):
    lines = parse_input(data)
    max_int = max(pos for line in lines for pos in line)
    floor = np.zeros((max_int+1, max_int+1), dtype=int)
    for line in lines:
        line_locations = get_line_locations(*line)
        for loc in line_locations:
            x, y = loc
            floor[y,x] += 1
    return floor


def count_lines_with_diagonals(data):
    lines = parse_input(data)
    max_int = max(pos for line in lines for pos in line)
    floor = np.zeros((max_int+1, max_int+1), dtype=int)
    for line in lines:
        line_locations = get_line_locations(*line)
        if not line_locations:
            line_locations = get_diagonal_line_locations(*line)
        for loc in line_locations:
            x, y = loc
            floor[y,x] += 1
    return floor


if __name__ == '__main__':
    with open('data/day_5_input.txt', 'r') as f:
        data = f.read().strip()
    
    line_count_1 = count_lines(data)
    part_1 = (line_count_1 >= 2).sum()

    line_count_2 = count_lines_with_diagonals(data)
    part_2 = (line_count_2 >= 2).sum()
    
    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
