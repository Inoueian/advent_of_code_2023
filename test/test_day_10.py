from day_10 import *

data = ("-L|F7\n" +
        "7S-7|\n" +
        "L|7||\n" +
        "-L-J|\n" +
        "L|-JF")
data_1 = ("7-F7-\n" +
          ".FJ|7\n" +
          "SJLL7\n" +
          "|F--J\n" +
          "LJ.LJ")


def test_get_next_direction():
    assert get_next_direction("up", "|") == "up"
    assert get_next_direction("up", "7") == "left"
    assert get_next_direction("right", "-") == "right"
    assert get_next_direction("right", "J") == "up"
    assert get_next_direction("down", "L") == "right"
    assert get_next_direction("down", "|") == "down"
    assert get_next_direction("left", "F") == "down"
    assert get_next_direction("left", "-") == "left"


def test_move_one_step():
    assert move_one_step((1, 1), "right") == (1, 2)
    assert move_one_step((3, 1), "left") == (3, 0)
    assert move_one_step((2, 2), "up") == (1, 2)
    assert move_one_step((4, 3), "down") == (5, 3)


def test_find_start():
    lines = data.splitlines()
    assert find_start(lines) == (1, 1)
    lines_1 = data_1.splitlines()
    assert find_start(lines_1) == (2, 0)


def test_get_distance_dict():
    distance_dict = get_distance_dict(data)
    assert distance_dict[(1, 1)] == 0
    assert distance_dict[(1, 2)] == 1
    assert distance_dict[(3, 1)] == 2
    assert distance_dict[(2, 3)] == 3
    assert distance_dict[(3, 3)] == 4
    assert (0, 0) not in distance_dict
    assert (2, 2) not in distance_dict


def test_get_longest_distance():
    assert get_longest_distance(data) == 4
    assert get_longest_distance(data_1) == 8
