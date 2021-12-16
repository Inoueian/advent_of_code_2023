import pytest

from day_15 import *


test_input = ('1163751742\n' +
              '1381373672\n' +
              '2136511328\n' +
              '3694931569\n' +
              '7463417111\n' +
              '1319128137\n' +
              '1359912421\n' +
              '3125421639\n' +
              '1293138521\n' +
              '2311944581')
test_array = parse_data(test_input)


def test_total_risk():
    assert total_risk(test_array) == 40


def test_expand_small_cave():
    array = np.array([[8]])
    expanded_cave = expand_cave(array)
    assert np.all(expanded_cave == np.array([[8, 9, 1, 2, 3],
                                             [9, 1, 2, 3, 4],
                                             [1, 2, 3, 4, 5],
                                             [2, 3, 4, 5, 6],
                                             [3, 4, 5, 6, 7]]))


def test_expand_cave():
    expanded_cave = expand_cave(test_array)
    assert expanded_cave.shape == (50, 50)


def test_total_risk_expanded_cave():
    assert total_risk(expand_cave(test_array)) == 315
