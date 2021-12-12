from collections import defaultdict


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
    lines = data.strip().split('\n')
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


def count_lines_dict(data):
    lines = parse_input(data)
    count_dict = defaultdict(int)
    for line in lines:
        line_locations = get_line_locations(*line)
        for loc in line_locations:
            count_dict[loc] += 1
    return count_dict
    

def count_lines_with_diagonals_dict(data):
    lines = parse_input(data)
    count_dict = defaultdict(int)
    for line in lines:
        line_locations = get_line_locations(*line)
        if not line_locations:
            line_locations = get_diagonal_line_locations(*line)
        for loc in line_locations:
            count_dict[loc] += 1
    return count_dict
    

if __name__ == '__main__':
    with open('data/day_5_input.txt', 'r') as f:
        data = f.read()
    
    count_dict_1 = count_lines_dict(data)
    part_1 = sum([count >= 2 for count in count_dict_1.values()])

    count_dict_2 = count_lines_with_diagonals_dict(data)
    part_2 = sum([count >= 2 for count in count_dict_2.values()])
    
    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
