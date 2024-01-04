direction_dict = {"0": "R", "1": "D", "2": "L", "3": "U"}


class Trench:
    def __init__(self, data, part_2=False):
        self.lines = data.splitlines()
        self.part_2 = part_2
        self.tuples = self.parse_lines()
        if self.part_2:
            self.corner_list = self.get_corners()
            xs = set(x for x, _ in self.corner_list)
            ys = set(y for _, y in self.corner_list)
        else:
            self.trench_set = self.populate_trench()
            xs = set(x for x, _ in self.trench_set)
            ys = set(y for _, y in self.trench_set)
        self.min_x = min(xs)
        self.max_x = max(xs)
        self.min_y = min(ys)
        self.max_y = max(ys)
        if not self.part_2:
            self.corner_inside_set = self.get_corner_inside_set()

    def parse_lines(self):
        tuples = []
        for line in self.lines:
            if self.part_2:
                _, _, code = line.split()
                direction = direction_dict[code[-2]]
                length = int(code[2:-2], 16)
            else:
                direction, len_str, color_code = line.split()
                length = int(len_str)
            tuples.append((direction, length))
        return tuples

    def populate_trench(self):
        curr_x = curr_y = 0
        trench_list = [(curr_x, curr_y)]
        for direction, length in self.tuples:
            if direction == "R":
                new_points = [(curr_x, curr_y + inc + 1) for inc in range(length)]
                curr_y = curr_y + length
            elif direction == "L":
                new_points = [(curr_x, curr_y - inc - 1) for inc in range(length)]
                curr_y = curr_y - length
            elif direction == "D":
                new_points = [(curr_x + inc + 1, curr_y) for inc in range(length)]
                curr_x = curr_x + length
            else:
                new_points = [(curr_x - inc - 1, curr_y) for inc in range(length)]
                curr_x = curr_x - length
            trench_list += new_points
        return set(trench_list)

    def get_corners(self):
        curr_x = curr_y = 0
        corner_list = [(curr_x, curr_y)]
        for direction, length in self.tuples:
            if direction == "R":
                curr_y = curr_y + length
            elif direction == "L":
                curr_y = curr_y - length
            elif direction == "D":
                curr_x = curr_x + length
            else:
                curr_x = curr_x - length
            corner_list.append((curr_x, curr_y))
        return corner_list

    def get_corner_inside_set(self):
        grid = [(x - 0.5, y - 0.5)
                for x in range(self.min_x, self.max_x + 1)
                for y in range(self.min_y, self.max_y + 1)]
        inside_dict = {(self.min_x - 0.5, y - 0.5): False
                       for y in range(self.min_y, self.max_y + 1)}
        for x, y in grid:
            tl_is_inside = inside_dict[(x, y)]
            tr = (int(x - 0.5), int(y + 0.5))
            bl = (int(x + 0.5), int(y - 0.5))
            br = (int(x + 0.5), int(y + 0.5))
            if (tr in self.trench_set) and (br in self.trench_set):
                inside_dict[(x, y + 1)] = not tl_is_inside
            else:
                inside_dict[(x, y + 1)] = tl_is_inside
            if (bl in self.trench_set) and (br in self.trench_set):
                inside_dict[(x + 1, y)] = not tl_is_inside
            else:
                inside_dict[(x + 1, y)] = tl_is_inside
        return set((x, y) for (x, y), is_inside in inside_dict.items()
                   if is_inside)

    def char_is_inside(self, x, y):
        corners = [(x - 0.5, y - 0.5),
                   (x - 0.5, y + 0.5),
                   (x + 0.5, y - 0.5),
                   (x + 0.5, y + 0.5)]
        return all(corner in self.corner_inside_set for corner in corners)

    def inside_set(self):
        inside_list = []
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                if self.char_is_inside(x, y):
                    inside_list.append((x, y))
        return set(inside_list)

    def compute_volume(self):
        if self.part_2:
            return
        else:
            return len(self.trench_set) + len(self.inside_set())


def is_trench(x, y, trench):
    return (x, y) in trench.trench_set


def compute_volume(data, part_2=False):
    trench = Trench(data, part_2)
    return trench.compute_volume()


if __name__ == "__main__":
    with open("data/day_18_input.txt", "r") as f:
        data = f.read()

    part_1 = compute_volume(data)
    part_2 = compute_volume(data, part_2=True)

    print(part_1)
    print(part_2)
