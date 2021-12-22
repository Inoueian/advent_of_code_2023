import pytest

from day_21 import *

test_data = 'Player 1 starting position: 4\nPlayer 2 starting position: 8'


def test_positions():
    game = DiceGame(test_data)
    assert game.position_1 == 4
    assert game.position_2 == 8


def test_roll_one_set():
    game = DiceGame(test_data)
    game.roll_player_1()
    game.roll_player_2()
    assert game.score_1 == 10
    assert game.score_2 == 3


def test_roll_until_win():
    game = DiceGame(test_data)
    game.roll_until_win()
    assert game.score_1 == 1000
    assert game.score_2 == 745
    assert game.roll_count == 993


def test_dirac_roll_one_set():
    game = DiracDice(test_data)
    assert game.state_dict_1 == {(4, 0): 1}
    assert game.state_dict_2 == {(8, 0): 1}
    game.roll_player_1()
    game.roll_player_2()
    assert game.state_dict_1 == {(7, 7): 1, (8, 8): 3, (9, 9): 6, (10, 10): 7,
                                 (1, 1): 6, (2, 2): 3, (3, 3): 1}
    assert game.state_dict_2 == {(1, 1): 1, (2, 2): 3, (3, 3): 6, (4, 4): 7,
                                 (5, 5): 6, (6, 6): 3, (7, 7): 1}


def test_count_winning_universes():
    game = DiracDice(test_data)
    wins_1, wins_2 = game.count_winning_universes()
    assert wins_1 == 444356092776315
    assert wins_2 == 341960390180808
