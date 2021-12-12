import numpy as np


def flash_neighbors(flashing):
    x_size, y_size = flashing.shape
    matrix = np.array([[int(abs(x - y) <= 1) for x in range(x_size)]
                       for y in range(y_size)])
    return np.matmul(np.matmul(matrix, flashing), matrix)

class Octopus:
    def __init__(self, data):
        lines = data.split('\n')
        self.array = np.array([[int(num) for num in line]
                               for line in lines], dtype=int)
        self.has_flashed = np.zeros(self.array.shape, dtype=bool)
        self.flash_count = 0

    def apply_flash(self):
        while True:
            flashing = (self.array > 9) & (~self.has_flashed)
            if ~np.any(flashing):
                break
            self.has_flashed = (self.array > 9)
            self.array = self.array + flash_neighbors(flashing)
        self.array[self.has_flashed] = 0
        self.flash_count += self.has_flashed.sum()
        self.has_flashed = np.zeros(self.array.shape, dtype=bool)

    def take_step(self):
        self.array = self.array + np.ones(self.array.shape, dtype=int)
        self.apply_flash()

    def take_n_steps(self, n):
        for _ in range(n):
            self.take_step()

    def find_synchronized_flash(self):
        step_count = 0
        while True:
            step_count += 1
            self.take_step()
            if ~np.any(self.array):
                return step_count


if __name__ == '__main__':
    with open('data/day_11_input.txt', 'r') as f:
        data = f.read().strip()

    octopus_1 = Octopus(data)
    octopus_1.take_n_steps(100)
    part_1 = octopus_1.flash_count

    octopus_2 = Octopus(data)
    part_2 = octopus_2.find_synchronized_flash()

    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
