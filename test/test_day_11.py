import pytest

from day_11 import *

small_input = ('11111\n' +
               '19991\n' +
               '19191\n' +
               '19991\n' +
               '11111')

small_input_2 = ('34543\n' +
                 '40004\n' +
                 '50005\n' +
                 '40004\n' +
                 '34543')

large_input = ('5483143223\n' +
               '2745854711\n' +
               '5264556173\n' +
               '6141336146\n' +
               '6357385478\n' +
               '4167524645\n' +
               '2176841721\n' +
               '6882881134\n' +
               '4846848554\n' +
               '5283751526')

large_input_1 = ('6594254334\n' +
                 '3856965822\n' +
                 '6375667284\n' +
                 '7252447257\n' +
                 '7468496589\n' +
                 '5278635756\n' +
                 '3287952832\n' +
                 '7993992245\n' +
                 '5957959665\n' +
                 '6394862637')


def test_flash_neighbors():
    flashing = np.array([[False, False, False, False, False],
                         [False, True, True, True, False],
                         [False, True, False, True, False],
                         [False, True, True, True, False],
                         [False, False, False, False, False]])
    assert np.all(np.array(flash_neighbors(flashing) == np.array([[1, 2, 3, 2, 1],
                                                                  [2, 3, 5, 3, 2],
                                                                  [3, 5, 8, 5, 3],
                                                                  [2, 3, 5, 3, 2],
                                                                  [1, 2, 3, 2, 1]])))


def test_octopus():
    octopus = Octopus(small_input)
    assert np.all(octopus.array == np.array([[1, 1, 1, 1, 1],
                                             [1, 9, 9, 9, 1],
                                             [1, 9, 1, 9, 1],
                                             [1, 9, 9, 9, 1],
                                             [1, 1, 1, 1, 1]]))


def test_has_flash():
    octopus = Octopus(small_input)
    octopus.take_step()
    assert np.all(octopus.array == np.array([[3, 4, 5, 4, 3],
                                             [4, 0, 0, 0, 4],
                                             [5, 0, 0, 0, 5],
                                             [4, 0, 0, 0, 4],
                                             [3, 4, 5, 4, 3]]))

def test_no_flash():
    octopus = Octopus(small_input_2)
    octopus.take_step()
    assert np.all(octopus.array == np.array([[4, 5, 6, 5, 4],
                                             [5, 1, 1, 1, 5],
                                             [6, 1, 1, 1, 6],
                                             [5, 1, 1, 1, 5],
                                             [4, 5, 6, 5, 4]]))


def test_large_input():
    octopus_0 = Octopus(large_input)
    octopus_0.take_step()
    octopus_1 = Octopus(large_input_1)

    assert np.all(octopus_0.array == octopus_1.array)


def test_flash_count():
    octopus = Octopus(large_input)
    octopus.take_n_steps(10)
    assert octopus.flash_count == 204

    octopus.take_n_steps(90)
    assert octopus.flash_count == 1656


def test_find_synchronized_flash():
    octopus = Octopus(large_input)
    assert octopus.find_synchronized_flash() == 195
