def perform_all_moves(instructions):
    horizontal = depth = 0
    for instruction in instructions:
        direction, num_str = instruction.split()
        num = int(num_str)
        if direction == 'forward':
            horizontal += num
        elif direction == 'down':
            depth += num
        elif direction == 'up':
            depth -= num
        else:
            raise ValueError("Instruction needs to start with 'forward', 'down', or 'up'.")    
    return horizontal, depth


def move_with_aim(horizontal, depth, aim, instruction):
    direction, num_str = instruction.split()
    num = int(num_str)
    if direction == 'forward':
        horizontal += num
        depth += aim*num
    elif direction == 'down':
        aim += num
    elif direction == 'up':
        aim -= num
    else:
        raise ValueError("Instruction needs to start with 'forward', 'down', or 'up'.")
    return horizontal, depth, aim


def perform_all_moves_with_aim(instructions):
    horizontal = depth = aim = 0
    for instruction in instructions:
        horizontal, depth, aim = move_with_aim(horizontal,
                                               depth,
                                               aim,
                                               instruction)
    return horizontal, depth, aim


if __name__ == '__main__':
    with open('data/day_2_input.txt', 'r') as f:
        data = f.read()
    instructions = data.strip().split('\n')
    
    horizontal_1, depth_1 = perform_all_moves(instructions)
    part_1 = horizontal_1 * depth_1

    horizontal_2, depth_2, _ = perform_all_moves_with_aim(instructions)
    part_2 = horizontal_2 * depth_2
    
    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
