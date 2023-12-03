from day_2 import *

data = ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n" +
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n" +
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n" +
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n" +
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
cube_counts = {"red": 12,
               "green": 13,
               "blue": 14}


def test_get_game_dicts():
    lines = data.splitlines()
    assert get_game_dicts(lines[0]) == [{"blue": 3, "red": 4},
                                        {"red": 1, "green": 2, "blue": 6},
                                        {"green": 2}]


def test_game_is_possible():
    lines = data.splitlines()
    assert game_is_possible(lines[0], cube_counts)
    assert game_is_possible(lines[1], cube_counts)
    assert not game_is_possible(lines[2], cube_counts)
    assert not game_is_possible(lines[3], cube_counts)
    assert game_is_possible(lines[4], cube_counts)


def test_possible_game_sum():
    assert possible_game_sum(data) == 8


def test_get_power():
    lines = data.splitlines()
    assert get_power(lines[0]) == 48
    assert get_power(lines[1]) == 12
    assert get_power(lines[2]) == 1560
    assert get_power(lines[3]) == 630
    assert get_power(lines[4]) == 36


def test_power_sum():
    assert power_sum(data) == 2286
