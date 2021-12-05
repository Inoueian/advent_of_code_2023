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


def test_count_lines():
    assert np.all(count_lines(test_input) == np.array([[0,0,0,0,0,0,0,1,0,0],
                                                       [0,0,1,0,0,0,0,1,0,0],
                                                       [0,0,1,0,0,0,0,1,0,0],
                                                       [0,0,0,0,0,0,0,1,0,0],
                                                       [0,1,1,2,1,1,1,2,1,1],
                                                       [0,0,0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0,0,0],
                                                       [2,2,2,1,1,1,0,0,0,0]]))
    

def test_get_diagonal_line_locations():
    assert get_diagonal_line_locations(1, 1, 3, 3) == [(1, 1), (2, 2), (3, 3)]
    assert get_diagonal_line_locations(9, 7, 7, 9) == [(9, 7), (8, 8), (7, 9)]
    assert get_diagonal_line_locations(6, 4, 2, 0) == [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0)]
    assert get_diagonal_line_locations(0, 9, 5, 9) == []

    
def test_count_lines_with_diagonals():
    assert np.all(count_lines_with_diagonals(test_input) == np.array([[1,0,1,0,0,0,0,1,1,0],
                                                                      [0,1,1,1,0,0,0,2,0,0],
                                                                      [0,0,2,0,1,0,1,1,1,0],
                                                                      [0,0,0,1,0,2,0,2,0,0],
                                                                      [0,1,1,2,3,1,3,2,1,1],
                                                                      [0,0,0,1,0,2,0,0,0,0],
                                                                      [0,0,1,0,0,0,1,0,0,0],
                                                                      [0,1,0,0,0,0,0,1,0,0],
                                                                      [1,0,0,0,0,0,0,0,1,0],
                                                                      [2,2,2,1,1,1,0,0,0,0]]))
