from day_8 import *

data_0 = ("RL\n" +
          "\n" +
          "AAA = (BBB, CCC)\n" +
          "BBB = (DDD, EEE)\n" +
          "CCC = (ZZZ, GGG)\n" +
          "DDD = (DDD, DDD)\n" +
          "EEE = (EEE, EEE)\n" +
          "GGG = (GGG, GGG)\n" +
          "ZZZ = (ZZZ, ZZZ)")

data_1 = ("LLR\n" +
          "\n" +
          "AAA = (BBB, BBB)\n" +
          "BBB = (AAA, ZZZ)\n" +
          "ZZZ = (ZZZ, ZZZ)")

data_2 = ("LR\n" +
          "\n" +
          "11A = (11B, XXX)\n" +
          "11B = (XXX, 11Z)\n" +
          "11Z = (11B, XXX)\n" +
          "22A = (22B, XXX)\n" +
          "22B = (22C, 22C)\n" +
          "22C = (22Z, 22Z)\n" +
          "22Z = (22B, 22B)\n" +
          "XXX = (XXX, XXX)")


def test_go_right():
    tree = Tree(data_0)
    assert tree.current == "AAA"
    tree.go_right()
    assert tree.current == "CCC"
    tree.go_right()
    assert tree.current == "GGG"


def test_go_left():
    tree = Tree(data_0)
    tree.go_left()
    assert tree.current == "BBB"
    tree.go_left()
    assert tree.current == "DDD"


def test_take_step():
    tree = Tree(data_0)
    tree.take_step()
    assert tree.current == "CCC"
    tree.take_step()
    assert tree.current == "ZZZ"
    tree.take_step()
    assert tree.current == "ZZZ"

    tree = Tree(data_1)
    tree.take_step()
    assert tree.current == "BBB"
    tree.take_step()
    assert tree.current == "AAA"
    tree.take_step()
    assert tree.current == "BBB"
    tree.take_step()
    assert tree.current == "AAA"
    tree.take_step()
    assert tree.current == "BBB"
    tree.take_step()
    assert tree.current == "ZZZ"


def test_count_steps():
    assert count_steps(data_0) == 2
    assert count_steps(data_1) == 6


def test_go_right_2():
    tree = Tree(data_2, part_2=True)
    assert tree.current == ["11A", "22A"]
    tree.go_right()
    assert tree.current == ["XXX", "XXX"]


def test_go_left_2():
    tree = Tree(data_2, part_2=True)
    tree.go_left()
    assert tree.current == ["11B", "22B"]


def test_take_step_2():
    tree = Tree(data_2, part_2=True)
    tree.take_step()
    assert tree.current == ["11B", "22B"]
    tree.take_step()
    assert tree.current == ["11Z", "22C"]
    tree.take_step()
    assert tree.current == ["11B", "22Z"]
    tree.take_step()
    assert tree.current == ["11Z", "22B"]


def test_count_steps_2():
    assert count_steps(data_2, part_2=True) == 6
