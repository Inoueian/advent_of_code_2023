def get_diff_list(numbers):
    return [curr - prev for prev, curr in zip(numbers[:-1], numbers[1:])]


def get_diff_lists(numbers):
    diff_lists = []
    while True:
        diff_list = get_diff_list(numbers)
        diff_lists.append(diff_list)
        if all(number == 0 for number in diff_list):
            return diff_lists
        numbers = diff_list


def get_next_number(numbers):
    diff_lists = get_diff_lists(numbers)
    return numbers[-1] + sum(diff_list[-1] for diff_list in diff_lists)


def get_prev_number(numbers):
    diff_lists = get_diff_lists(numbers)
    number = numbers[0]
    for index, diff_list in enumerate(diff_lists):
        number += (-1)**(index + 1) * diff_list[0]
    return number


def get_total(data, part_2=False):
    lines = data.splitlines()
    number_lists = [[int(item) for item in line.split()]
                    for line in lines]
    if part_2:
        return sum(get_prev_number(numbers) for numbers in number_lists)
    else:
        return sum(get_next_number(numbers) for numbers in number_lists)


if __name__ == "__main__":
    with open("data/day_9_input.txt", "r") as f:
        data = f.read()

    part_1 = get_total(data)
    part_2 = get_total(data, part_2=True)

    print(part_1)
    print(part_2)
