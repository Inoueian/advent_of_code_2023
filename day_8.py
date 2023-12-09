import math
import re


class Node:
    def __init__(self, line):
        name, left, right = re.findall(r"(.+) = \((.+), (.+)\)", line)[0]
        self.name = name
        self.left = left
        self.right = right


class Tree:
    def __init__(self, data, part_2=False):
        lines = data.splitlines()
        self.instruction = lines[0]
        self.node_dict = {}
        for line in lines[2:]:
            node = Node(line)
            self.node_dict[node.name] = node

        self.steps = 0
        self.part_2 = part_2
        if self.part_2:
            self.current = [key for key in self.node_dict.keys()
                            if key.endswith("A")]
        else:
            self.current = "AAA"

    def go_right(self):
        if self.part_2:
            nodes = [self.node_dict[name] for name in self.current]
            self.current = [node.right for node in nodes]
        else:
            node = self.node_dict[self.current]
            self.current = node.right

    def go_left(self):
        if self.part_2:
            nodes = [self.node_dict[name] for name in self.current]
            self.current = [node.left for node in nodes]
        else:
            node = self.node_dict[self.current]
            self.current = node.left

    def take_step(self):
        direction = self.instruction[self.steps % len(self.instruction)]
        if direction == "R":
            self.go_right()
        else:
            self.go_left()
        self.steps += 1


def compute_end_point(end_steps):
    """Strictly not correct.
    I'd actually need to check that if the node ends in "Z" at step N,
    the node ends in "Z" at step n*N, where n is any integer.

    This happens to be true for the problem."""
    first_z_steps = [item[0] for item in end_steps]
    end_point = first_z_steps.pop()
    while first_z_steps:
        next_point = first_z_steps.pop()
        end_point = int(end_point * next_point / math.gcd(end_point, next_point))
    return end_point


def count_steps(data, part_2=False):
    tree = Tree(data, part_2)
    if part_2:
        end_steps = [[] for _ in tree.current]
        while not all(name.endswith("Z") for name in tree.current):
            tree.take_step()
            for index, name in enumerate(tree.current):
                if name.endswith("Z"):
                    end_steps[index].append(tree.steps)
            if all(len(item) > 0 for item in end_steps):
                return compute_end_point(end_steps)
    else:
        while tree.current != "ZZZ":
            tree.take_step()
    return tree.steps


if __name__ == "__main__":
    with open("data/day_8_input.txt", "r") as f:
        data = f.read()

    part_1 = count_steps(data)
    part_2 = count_steps(data, part_2=True)

    print(part_1)
    print(part_2)
