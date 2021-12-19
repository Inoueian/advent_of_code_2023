class SnailfishNumber:
    def __init__(self, data, parent=None, is_left=False, is_right=False):
        if isinstance(data, int):
            self.data = data
            self.left = None
            self.right = None
            self.parent = parent
            self.is_left = is_left
            self.is_right = is_right
            self.depth = 0
        else:
            left, right = data
            self.data = None
            self.left = SnailfishNumber(left, parent=self, is_left=True)
            self.right = SnailfishNumber(right, parent=self, is_right=True)
            self.parent = parent
            self.is_left = is_left
            self.is_right = is_right
            self.depth = max(self.left.depth, self.right.depth) + 1

    def __eq__(self, other):
        """Equality does not check the parents"""
        if self.data is not None:
            return self.data == other.data
        elif other.data is not None:
            return False
        else:
            return (self.left == other.left) and (self.right == other.right)

    def __add__(self, other):
        list_ = [self.get_list(), other.get_list()]
        result = SnailfishNumber(list_)
        while True:
            if result.depth >= 5:
                result.explode()
                result.update_depth()
            else:
                two_digit = result.find_two_digit()
                if two_digit:
                    two_digit.split()
                    result.update_depth()
                else:
                    break
        return result

    def __str__(self):
        if self.data is not None:
            return str(self.data)
        else:
            return f'[{self.left.__str__()}, {self.right.__str__()}]'

    def get_list(self):
        if self.data is not None:
            return self.data
        else:
            return [self.left.get_list(), self.right.get_list()]

    def find_nested_pair(self):
        if self.depth == 1:
            return self
        elif self.depth > 1:
            if self.left.depth == self.depth - 1:
                return self.left.find_nested_pair()
            else:
                return self.right.find_nested_pair()

    def find_rightmost(self):
        if self.data is not None:
            return self
        else:
            return self.right.find_rightmost()

    def find_leftmost(self):
        if self.data is not None:
            return self
        else:
            return self.left.find_leftmost()

    def find_number_to_left(self):
        if self.parent is None:
            return None
        elif self.is_left:
            return self.parent.find_number_to_left()
        else:
            return self.parent.left.find_rightmost()

    def find_number_to_right(self):
        if self.parent is None:
            return None
        elif self.is_right:
            return self.parent.find_number_to_right()
        else:
            return self.parent.right.find_leftmost()

    def find_two_digit(self):
        if self.data is not None:
            if self.data >= 10:
                return self
            else:
                return None
        else:
            left_result = self.left.find_two_digit()
            if left_result:
                return left_result
            else:
                return self.right.find_two_digit()

    def explode(self):
        nested_pair = self.find_nested_pair()
        left_number = nested_pair.left.data
        right_number = nested_pair.right.data
        number_to_left = nested_pair.find_number_to_left()
        number_to_right = nested_pair.find_number_to_right()
        if number_to_left is not None:
            number_to_left.data += left_number
        if number_to_right is not None:
            number_to_right.data += right_number
        nested_pair.data = 0
        nested_pair.left = nested_pair.right = None

    def split(self):
        if self.data is None:
            pass
        else:
            self.left = SnailfishNumber(self.data // 2, parent=self, is_left=True)
            self.right = SnailfishNumber((self.data + 1) // 2, parent=self, is_right=True)
            self.data = None

    def update_depth(self):
        if self.data is not None:
            self.depth = 0
        else:
            self.left.update_depth()
            self.right.update_depth()
            self.depth = max(self.left.depth, self.right.depth) + 1

    def compute_magnitude(self):
        if self.data is not None:
            return self.data
        else:
            return 3 * self.left.compute_magnitude() + 2 * self.right.compute_magnitude()


class SnailfishNumberFromLines:
    def __init__(self, data):
        lines = data.split('\n')
        self.numbers = [SnailfishNumber(eval(line)) for line in lines]

    def sum(self):
        result = self.numbers[0]
        if len(self.numbers) > 1:
            for number in self.numbers[1:]:
                result += number
        return result

    def find_largest_magnitude(self):
        max_magnitude = 0
        for number_0 in self.numbers:
            for number_1 in self.numbers:
                if number_0 != number_1:
                    sum_ = number_0 + number_1
                    magnitude = sum_.compute_magnitude()
                    max_magnitude = max(max_magnitude, magnitude)
        return max_magnitude


if __name__ == '__main__':
    with open('data/day_18_input.txt', 'r') as f:
        data = f.read().strip()
    number_from_data = SnailfishNumberFromLines(data)
    number = number_from_data.sum()

    part_1 = number.compute_magnitude()
    part_2 = number_from_data.find_largest_magnitude()

    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
