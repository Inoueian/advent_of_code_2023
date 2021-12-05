import pytest

from day_4 import *

test_data = ('7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n' +
             '22 13 17 11  0\n' +
             '8  2 23  4 24\n' +
             '21  9 14 16  7\n' +
             '6 10  3 18  5\n' +
             '1 12 20 15 19\n\n' +
             '3 15  0  2 22\n' +
             '9 18 13 17  5\n' +
             '19  8  7 25 23\n' +
             '20 11 10 24  4\n' +
             '14 21 16 12  6\n\n' +
             '14 21 17 24  4\n' +
             '10 16 15  9 19\n' +
             '18  8 23 26 20\n' +
             '22 11 13  6  5\n' +
             '2  0 12  3  7')

test_order = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14,
              21, 24, 10, 16, 13, 6, 15, 25, 12, 22,
              18, 20, 8, 19, 3, 26, 1]

test_board_0 = [[22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19]]
test_board_1 = [[3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6]]
test_board_2 = [[14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7]]


def test_parse_data():
    assert parse_data(test_data) == (test_order, [test_board_0, test_board_1, test_board_2])


def test_filled_spaces_5():
    assert get_filled_spaces(test_board_0, test_order, 5) == [[False, False, False, True, False],
                                                              [False, False, False, True, False],
                                                              [False, True, False, False, True],
                                                              [False, False, False, False, True],
                                                              [False, False, False, False, False]]
    assert get_filled_spaces(test_board_1, test_order, 5) == [[False, False, False, False, False],
                                                              [True, False, False, False, True],
                                                              [False, False, True, False, False],
                                                              [False, True, False, False, True],
                                                              [False, False, False, False, False]]
    assert get_filled_spaces(test_board_2, test_order, 5) == [[False, False, False, False, True],
                                                              [False, False, False, True, False],       
                                                              [False, False, False, False, False],
                                                              [False, True, False, False, True],
                                                              [False, False, False, False, True]]

    
def test_bingo_5():
    assert bingo(test_board_0, test_order, 5) == False
    assert bingo(test_board_1, test_order, 5) == False
    assert bingo(test_board_2, test_order, 5) == False


def test_filled_spaces_11():
    assert get_filled_spaces(test_board_0, test_order, 11) == [[False, False, True, True, True],
                                                               [False, True, True, True, False],
                                                               [True, True, True, False, True],
                                                               [False, False, False, False, True],
                                                               [False, False, False, False, False]]
    assert get_filled_spaces(test_board_1, test_order, 11) == [[False, False, True, True, False],
                                                               [True, False, False, True, True],
                                                               [False, False, True, False, True],
                                                               [False, True, False, False, True],
                                                               [True, True, False, False, False]]
    assert get_filled_spaces(test_board_2, test_order, 11) == [[True, True, True, False, True],
                                                               [False, False, False, True, False],
                                                               [False, False, True, False, False],
                                                               [False, True, False, False, True],
                                                               [True, True, False, False, True]]

    
def test_bingo_11():
    assert bingo(test_board_0, test_order, 11) == False
    assert bingo(test_board_1, test_order, 11) == False
    assert bingo(test_board_2, test_order, 11) == False


def test_filled_spaces_12():
    assert get_filled_spaces(test_board_0, test_order, 12) == [[False, False, True, True, True],
                                                               [False, True, True, True, True],
                                                               [True, True, True, False, True],
                                                               [False, False, False, False, True],
                                                               [False, False, False, False, False]]
    assert get_filled_spaces(test_board_1, test_order, 12) == [[False, False, True, True, False],
                                                               [True, False, False, True, True],        
                                                               [False, False, True, False, True],
                                                               [False, True, False, True, True],
                                                               [True, True, False, False, False]]
    assert get_filled_spaces(test_board_2, test_order, 12) == [[True, True, True, True, True],
                                                               [False, False, False, True, False],
                                                               [False, False, True, False, False],
                                                               [False, True, False, False, True],
                                                               [True, True, False, False, True]]


def test_bingo_12():
    assert bingo(test_board_0, test_order, 12) == False
    assert bingo(test_board_1, test_order, 12) == False
    assert bingo(test_board_2, test_order, 12) == True


def test_score():
    assert get_score([test_board_0, test_board_1, test_board_2], test_order) == 188


def test_winning_number():
    assert get_winning_number([test_board_0, test_board_1, test_board_2], test_order) == 24


def test_last_winner_score():
    assert get_last_winner_score([test_board_0, test_board_1, test_board_2], test_order) == 148


def test_last_winning_number():
    assert get_last_winning_number([test_board_0, test_board_1, test_board_2], test_order) == 13
