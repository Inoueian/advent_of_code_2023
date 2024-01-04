from day_18 import *

data = ("R 6 (#70c710)\n" +
        "D 5 (#0dc571)\n" +
        "L 2 (#5713f0)\n" +
        "D 2 (#d2c081)\n" +
        "R 2 (#59c680)\n" +
        "D 2 (#411b91)\n" +
        "L 5 (#8ceee2)\n" +
        "U 2 (#caa173)\n" +
        "L 1 (#1b58a2)\n" +
        "U 2 (#caa171)\n" +
        "R 2 (#7807d2)\n" +
        "U 3 (#a77fa3)\n" +
        "L 2 (#015232)\n" +
        "U 2 (#7a21e3)")


def test_is_trench():
    trench = Trench(data)
    assert is_trench(0, 0, trench)
    assert is_trench(5, 0, trench)
    assert is_trench(0, 6, trench)
    assert not is_trench(1, 2, trench)


def test_compute_volume():
    assert compute_volume(data) == 62


def test_convert_instructions():
    trench = Trench(data, part_2=True)
    assert trench.tuples[0] == ("R", 461937)
    assert trench.tuples[1] == ("D", 56407)
    assert trench.tuples[-1] == ("U", 500254)


def test_compute_volume_mixed():
    trench = Trench(data)
    trench.part_2 = True
    assert trench.compute_volume() == 62


def test_compute_volume_2():
    assert compute_volume(data, part_2=True) == 952408144115
