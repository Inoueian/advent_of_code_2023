import numpy as np


def count_increase(numbers, shift=1):
    """Count the number of times that there's an increase in a list of numbers.
    Default is to compare individual numbers.
    When `shift` is specified,
    the comparison is between moving averages over that many numbers
    Inputs:
      numbers: List of numbers
      shift: int
    Returns:
      int, number of times that the number increases
    """
    num_array = np.array(numbers)
    return (num_array[shift:] > num_array[:-shift]).sum()


if __name__ == '__main__':
    with open('data/day_1_input.txt', 'r') as f:
        data = f.read()
    numbers = [int(line) for line in data.strip().split('\n')]
    
    part_1 = count_increase(numbers)
    part_2 = count_increase(numbers, shift=3)
    
    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
    