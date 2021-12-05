import numpy as np


def parse_data(data):
    lines = data.strip().split('\n')
    num_lines = len(lines)
    num_boards = (num_lines - 1) // 6
    order = [int(num_str) for num_str in lines[0].split(',')]
    boards = [[[int(num_str) for num_str in lines[6*board_index+row_index+2].split()]
               for row_index in range(5)]
              for board_index in range(num_boards)]
    return order, boards


def get_filled_spaces(board, order, num_draws):
    """Return a list of list that shows which slots on a bingo board are filled,
    after `num_draws` numbers are taken from `order`."""
    drawn_numbers = order[:num_draws]
    return [[col in drawn_numbers for col in row]
            for row in board]


def bingo(board, order, num_draws):
    """Returns if the board has a bingo after `num_draws`"""
    filled_array = np.array(get_filled_spaces(board, order, num_draws))
    has_full_row = np.any(np.all(filled_array, axis=1))
    has_full_col = np.any(np.all(filled_array, axis=0))
    return has_full_row or has_full_col


def get_winning_state(boards, order):
    """Returns the winning board, which spaces are filled,
    and the number that was last called when there's a winner."""
    for num_draws in range(len(order)):
        bingo_list = [bingo(board, order, num_draws) for board in boards]
        if any(bingo_list):
            winning_board = [board for board, has_won in zip(boards, bingo_list) if has_won][0]
            filled_spaces = get_filled_spaces(winning_board, order, num_draws)
            winning_number = order[num_draws-1]
            return winning_board, filled_spaces, winning_number


def get_score_and_winning_number(board, filled_spaces, winning_number):
    board_array = np.array(board)
    filled_array = np.array(filled_spaces)
    return board_array[~filled_array].sum(), winning_number

        
def get_score(boards, order):
    board, filled_spaces, winning_number = get_winning_state(boards, order)
    return get_score_and_winning_number(board, filled_spaces, winning_number)[0]


def get_winning_number(boards, order):
    _, _, winning_number = get_winning_state(boards, order)
    return winning_number


def get_last_winning_state(boards, order):
    """Returns the last board to get a bingo, which spaces are filled,
    and the number that was last called."""
    for num_draws in range(len(order)):
        bingo_list = [bingo(board, order, num_draws) for board in boards]
        if all(bingo_list):
            winning_board = [board for board, has_won in zip(boards, last_bingo_list) if not has_won][0]
            filled_spaces = get_filled_spaces(winning_board, order, num_draws)
            winning_number = order[num_draws-1]
            return winning_board, filled_spaces, winning_number
        last_bingo_list = bingo_list


def get_last_winner_score(boards, order):
    board, filled_spaces, winning_number = get_last_winning_state(boards, order)
    return get_score_and_winning_number(board, filled_spaces, winning_number)[0]


def get_last_winning_number(boards, order):
    _, _, winning_number = get_last_winning_state(boards, order)
    return winning_number


if __name__ == '__main__':
    with open('data/day_4_input.txt', 'r') as f:
        data = f.read()
    order, boards = parse_data(data)
    
    board_1, filled_spaces_1, winning_number_1 = get_winning_state(boards, order)
    score_1, winning_number_1 = get_score_and_winning_number(board_1, filled_spaces_1, winning_number_1)
    part_1 = score_1 * winning_number_1

    board_2, filled_spaces_2, winning_number_2 = get_last_winning_state(boards, order)
    score_2, winning_number_2 = get_score_and_winning_number(board_2, filled_spaces_2, winning_number_2)
    part_2 = last_winner_score_2 * last_winning_number_2
    
    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
