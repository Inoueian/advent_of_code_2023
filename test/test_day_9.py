from day_9 import *

data = ("0 3 6 9 12 15\n" +
        "1 3 6 10 15 21\n" +
        "10 13 16 21 30 45")


def test_get_diff_list():
    assert get_diff_list([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]
    assert get_diff_list([1, 3, 6, 10, 15, 21]) == [2, 3, 4, 5, 6]
    assert get_diff_list([10, 13, 16, 21, 30, 45]) == [3, 3, 5, 9, 15]


def test_get_diff_lists():
    assert get_diff_lists([0, 3, 6, 9, 12, 15]) == [[3, 3, 3, 3, 3],
                                                    [0, 0, 0, 0]]
    assert get_diff_lists([1, 3, 6, 10, 15, 21]) == [[2, 3, 4, 5, 6],
                                                     [1, 1, 1, 1],
                                                     [0, 0, 0]]
    assert get_diff_lists([10, 13, 16, 21, 30, 45]) == [[3, 3, 5, 9, 15],
                                                        [0, 2, 4, 6],
                                                        [2, 2, 2],
                                                        [0, 0]]


def test_get_next_number():
    assert get_next_number([0, 3, 6, 9, 12, 15]) == 18
    assert get_next_number([1, 3, 6, 10, 15, 21]) == 28
    assert get_next_number([10, 13, 16, 21, 30, 45]) == 68


def test_get_total():
    assert get_total(data) == 114


def test_get_prev_number():
    assert get_prev_number([0, 3, 6, 9, 12, 15]) == -3
    assert get_prev_number([1, 3, 6, 10, 15, 21]) == 0
    assert get_prev_number([10, 13, 16, 21, 30, 45]) == 5


def test_get_total_2():
    assert get_total(data, part_2=True) == 2
