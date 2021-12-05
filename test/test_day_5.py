import pytest

from day_5 import *


test_input = ('0,9 -> 5,9\n' +
              '8,0 -> 0,8\n' +
              '9,4 -> 3,4\n' +
              '2,2 -> 2,1\n' +
              '7,0 -> 7,4\n' +
              '6,4 -> 2,0\n' +
              '0,9 -> 2,9\n' +
              '3,4 -> 1,4\n' +
              '0,0 -> 8,8\n' +
              '5,5 -> 8,2')


def test_parse_line():
    assert parse_line('0,9 -> 5,9') == (0, 9, 5, 9)
    assert parse_line('8,0 -> 0,8') == (8, 0, 0, 8)


def test_get_line_locations():
    assert get_line_locations(1, 1, 1, 3) == [(1, 1), (1, 2), (1, 3)]
    assert get_line_locations(9, 7, 7, 7) == [(9, 7), (8, 7), (7, 7)]
    assert get_line_locations(0, 9, 5, 9) == [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
    assert get_line_locations(8, 0, 0, 8) == []


def test_count_lines_dict():
    assert count_lines_dict(test_input) == {(0, 9): 2, (1, 4): 1, (1, 9): 2, (2, 1): 1, (2, 2): 1,
                                            (2, 4): 1, (2, 9): 2, (3, 4): 2, (3, 9): 1, (4, 4): 1,
                                            (4, 9): 1, (5, 4): 1, (5, 9): 1, (6, 4): 1, (7, 0): 1,
                                            (7, 1): 1, (7, 2): 1, (7, 3): 1, (7, 4): 2, (8, 4): 1,
                                            (9, 4): 1}
    

def test_get_diagonal_line_locations():
    assert get_diagonal_line_locations(1, 1, 3, 3) == [(1, 1), (2, 2), (3, 3)]
    assert get_diagonal_line_locations(9, 7, 7, 9) == [(9, 7), (8, 8), (7, 9)]
    assert get_diagonal_line_locations(6, 4, 2, 0) == [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0)]
    assert get_diagonal_line_locations(0, 9, 5, 9) == []


def test_count_lines_with_diagonals_dict():
    assert count_lines_with_diagonals_dict(test_input) == {(0, 0): 1, (0, 8): 1, (0, 9): 2, (1, 1): 1,
                                                           (1, 4): 1, (1, 7): 1, (1, 9): 2, (2, 0): 1,
                                                           (2, 1): 1, (2, 2): 2, (2, 4): 1, (2, 6): 1,
                                                           (2, 9): 2, (3, 1): 1, (3, 3): 1, (3, 4): 2,
                                                           (3, 5): 1, (3, 9): 1, (4, 2): 1, (4, 4): 3,
                                                           (4, 9): 1, (5, 3): 2, (5, 4): 1, (5, 5): 2,
                                                           (5, 9): 1, (6, 2): 1, (6, 4): 3, (6, 6): 1,
                                                           (7, 0): 1, (7, 1): 2, (7, 2): 1, (7, 3): 2,
                                                           (7, 4): 2, (7, 7): 1, (8, 0): 1, (8, 2): 1,
                                                           (8, 4): 1, (8, 8): 1, (9, 4): 1}
