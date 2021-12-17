import pytest

from day_17 import *

test_input = 'target area: x=20..30, y=-10..-5'


def test_parse_input():
    launcher = Launcher(test_input)
    assert launcher.x_min == 20
    assert launcher.x_max == 30
    assert launcher.y_min == -10
    assert launcher.y_max == -5


def test_check():
    launcher = Launcher(test_input)
    assert launcher.test_initial_velocity(v_x=7, v_y=2)
    assert launcher.test_initial_velocity(v_x=6, v_y=3)
    assert launcher.test_initial_velocity(v_x=9, v_y=0)
    assert not launcher.test_initial_velocity(v_x=17, v_y=-4)


def test_count_possible_velocities():
    launcher = Launcher(test_input)
    assert launcher.count_possible_velocities() == 112
