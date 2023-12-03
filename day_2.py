cube_counts = {"red": 12,
               "green": 13,
               "blue": 14}


def get_id(line):
    left, _ = line.split(":")
    _, id_str = left.split()
    return int(id_str)


def get_game_dicts(line):
    _, right = line.split(":")
    reveals = right.split(";")
    game_dicts = []
    for reveal in reveals:
        colors = reveal.split(",")
        game_dict = {}
        for color in colors:
            num_str, color = color.split()
            game_dict[color] = int(num_str)
        game_dicts.append(game_dict)
    return game_dicts


def game_is_possible(line, cube_counts=cube_counts):
    game_dicts = get_game_dicts(line)
    for game_dict in game_dicts:
        for color, num in game_dict.items():
            if num > cube_counts[color]:
                return False
    return True


def possible_game_sum(data, cube_counts=cube_counts):
    lines = data.splitlines()
    sum_ = 0
    for line in lines:
        if game_is_possible(line, cube_counts):
            sum_ += get_id(line)
    return sum_


def get_power(line):
    game_dicts = get_game_dicts(line)
    max_dict = {"red": 0, "green": 0, "blue": 0}
    for game_dict in game_dicts:
        for color, num in game_dict.items():
            max_dict[color] = max(max_dict[color], num)
    return max_dict["red"] * max_dict["green"] * max_dict["blue"]


def power_sum(data):
    lines = data.splitlines()
    return sum(get_power(line) for line in lines)


if __name__ == "__main__":
    with open("data/day_2_input.txt", "r") as f:
        data = f.read()

    part_1 = possible_game_sum(data)
    part_2 = power_sum(data)

    print(part_1)
    print(part_2)
