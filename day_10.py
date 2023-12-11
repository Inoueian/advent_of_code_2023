import re

directions = ("up", "down", "right", "left")
connection_dict = {"|": ["up", "down"],
                   "-": ["left", "right"],
                   "L": ["up", "right"],
                   "J": ["up", "left"],
                   "7": ["left", "down"],
                   "F": ["right", "down"],
                   ".": []}
opposite_dict = {"left": "right",
                 "right": "left",
                 "up": "down",
                 "down": "up"}


def get_next_direction(direction, char):
    entry_direction = opposite_dict[direction]
    connections = connection_dict[char]
    if entry_direction == connections[0]:
        return connections[1]
    elif entry_direction == connections[1]:
        return connections[0]
    else:
        return None


def move_one_step(location, direction):
    x, y = location
    if direction == "up":
        return x - 1, y
    elif direction == "down":
        return x + 1, y
    elif direction == "left":
        return x, y - 1
    elif direction == "right":
        return x, y + 1


def find_start(lines):
    for x, line in enumerate(lines):
        match = re.search("S", line)
        if match:
            return (x, match.start())


def get_distance_dict(data):
    lines = data.splitlines()
    start = find_start(lines)
    distance_dict = {start: 0}

    current_moves = []
    for direction in directions:
        x, y = move_one_step(start, direction)
        char = lines[x][y]
        if opposite_dict[direction] in connection_dict[char]:
            current_moves.append([(x, y), direction, char])

    current_distance = 1
    while current_moves:
        next_moves = []
        for (x, y), direction, char in current_moves:
            if (x, y) not in distance_dict:
                distance_dict[(x, y)] = current_distance
                next_direction = get_next_direction(direction, char)
                next_x, next_y = move_one_step((x, y), next_direction)
                next_char = lines[next_x][next_y]
                next_moves.append([(next_x, next_y), next_direction, next_char])
        current_distance += 1
        current_moves = next_moves
    return distance_dict


def get_longest_distance(data):
    distance_dict = get_distance_dict(data)
    return max(distance_dict.values())


if __name__ == "__main__":
    with open("data/day_10_input.txt", "r") as f:
        data = f.read()

    part_1 = get_longest_distance(data)
    # part_2 = get_total(data, part_2=True)

    print(part_1)
    # print(part_2)
