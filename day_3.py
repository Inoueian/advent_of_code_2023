import re


class Symbol:
    def __init__(self, char, x, y):
        self.char = char
        self.location = (x, y)


class EnginePart:
    def __init__(self, string, x, y):
        self.number = int(string)
        self.locations = [(x, y + index) for index in range(len(string))]


def get_symbol_list(data):
    lines = data.splitlines()
    symbol_list = []
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if (not char.isdigit()) and char != ".":
                symbol = Symbol(char, x, y)
                symbol_list.append(symbol)
    return symbol_list


def get_engine_parts(data):
    lines = data.splitlines()
    engine_parts = []
    for x, line in enumerate(lines):
        matches = re.finditer("[0-9]+", line)
        for match in matches:
            string = match.group()
            start = match.start()
            engine_part = EnginePart(string, x, start)
            engine_parts.append(engine_part)
    return engine_parts


def is_connected(engine_part, symbol_list):
    locations = engine_part.locations
    for symbol in symbol_list:
        x_symbol, y_symbol = symbol.location
        for x_engine, y_engine in locations:
            if (abs(x_symbol - x_engine) <= 1) and (abs(y_symbol - y_engine) <= 1):
                return True
    return False


def get_connected_engine_parts(data):
    symbol_list = get_symbol_list(data)
    engine_parts = get_engine_parts(data)
    return [engine_part for engine_part in engine_parts
            if is_connected(engine_part, symbol_list)]


def get_engine_sum(data):
    engine_parts = get_connected_engine_parts(data)
    return sum(engine_part.number for engine_part in engine_parts)


def get_gear_ratios(data):
    stars = [symbol for symbol in get_symbol_list(data)
             if symbol.char == "*"]
    engine_parts = get_engine_parts(data)
    gear_ratios = []
    for star in stars:
        connected_parts = [part for part in engine_parts
                           if is_connected(part, [star])]
        if len(connected_parts) == 2:
            gear_ratio = connected_parts[0].number * connected_parts[1].number
            gear_ratios.append(gear_ratio)
    return gear_ratios


def get_gear_ratio_sum(data):
    return sum(get_gear_ratios(data))


if __name__ == "__main__":
    with open("data/day_3_input.txt", "r") as f:
        data = f.read()

    part_1 = get_engine_sum(data)
    part_2 = get_gear_ratio_sum(data)

    print(part_1)
    print(part_2)
