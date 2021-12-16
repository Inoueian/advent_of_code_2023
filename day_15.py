import numpy as np


def parse_data(data):
    lines = data.split('\n')
    return np.array([[int(char) for char in line]
                     for line in lines])


def down(array, x, y):
    if x < array.shape[0] - 1:
        return array[x + 1, y]
    else:
        return np.inf


def up(array, x, y):
    if x > 0:
        return array[x - 1, y]
    else:
        return np.inf


def left(array, x, y):
    if y > 0:
        return array[x, y - 1]
    else:
        return np.inf


def right(array, x, y):
    if y < array.shape[0] - 1:
        return array[x, y + 1]
    else:
        return np.inf


def get_risk_forward(array, total_array, x, y):
    """Populate the (x, y) entry in the total risk array"""
    if x == y == 0:
        return 0
    else:
        return array[x, y] + min(left(total_array, x, y), up(total_array, x, y))


def get_risk(array, total_array, x, y):
    """Include possibility of going backwards."""
    if x == y == 0:
        return 0
    else:
        return array[x, y] + min(left(total_array, x, y), up(total_array, x, y),
                                 right(total_array, x, y), down(total_array, x, y))


def total_risk_initial(array):
    x_max, y_max = array.shape
    total_array = np.zeros(array.shape)
    for x in range(x_max):
        for y in range(y_max):
            total_array[x, y] = get_risk_forward(array, total_array, x, y)
    return total_array


def total_risk_iterate(array, total_array):
    x_max, y_max = array.shape
    return np.array([[get_risk(array, total_array, x, y) for y in range(y_max)]
                     for x in range(x_max)])


# def total_risk(array):
#     total_array = total_risk_initial(array)
#     while True:
#         new_total_array = total_risk_iterate(array, total_array)
#         if np.all(new_total_array == total_array):
#             break
#         total_array = new_total_array
#     return new_total_array[-1, -1]
def total_risk(array):
    total_array = total_risk_initial(array)
    return total_array[-1, -1]


def expand_cave(array):
    five_x_five = [[(array.copy() + i + j - 1) % 9 + 1 for i in range(5)]
                   for j in range(5)]
    rows = [np.concatenate(row, axis=0) for row in five_x_five]
    return np.concatenate(rows, axis=1)


if __name__ == '__main__':
    with open('data/day_15_input.txt', 'r') as f:
        data = f.read().strip()
    array = parse_data(data)

    part_1 = total_risk(array)
    # part_2 = total_risk(expand_cave(array))

    print(f'Part 1 answer: {part_1}')
    # print(f'Part 2 answer: {part_2}')
