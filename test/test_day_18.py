import pytest

from day_18 import *

test_input = ('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]\n' +
              '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]\n' +
              '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]\n' +
              '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]\n' +
              '[7,[5,[[3,8],[1,4]]]]\n' +
              '[[2,[2,2]],[8,[8,1]]]\n' +
              '[2,9]\n' +
              '[1,[[[9,3],9],[[9,0],[0,7]]]]\n' +
              '[[[5,[7,4]],7],1]\n' +
              '[[[[4,2],2],6],[8,7]]')

test_input_1 = ('[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]\n' +
                '[[[5,[2,8]],4],[5,[[9,9],0]]]\n' +
                '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]\n' +
                '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]\n' +
                '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]\n' +
                '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]\n' +
                '[[[[5,4],[7,7]],8],[[8,3],8]]\n' +
                '[[9,3],[[9,9],[6,[4,9]]]]\n' +
                '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]\n' +
                '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]')


def test_equality():
    num_0 = SnailfishNumber([[[[[9, 8], 1], 2], 3], 4])
    num_1 = SnailfishNumber([[[[[9, 8], 1], 2], 3], 4])
    assert num_0 == num_1


def test_depth():
    num_0 = SnailfishNumber([[[[[9, 8], 1], 2], 3], 4])
    assert num_0.depth == 5


def test_find_nested_pair():
    num_0 = SnailfishNumber([[[[[9, 8], 1], 2], 3], 4])
    assert num_0.find_nested_pair() == SnailfishNumber([9, 8])

    num_1 = SnailfishNumber([7, [6, [5, [4, [3, 2]]]]])
    assert num_1.find_nested_pair() == SnailfishNumber([3, 2])


def test_find_number_to_left():
    num_0 = SnailfishNumber([[[[[9, 8], 1], 2], 3], 4])
    nested_0 = num_0.find_nested_pair()
    assert nested_0.find_number_to_left() is None

    num_1 = SnailfishNumber([7, [6, [5, [4, [3, 2]]]]])
    nested_1 = num_1.find_nested_pair()
    assert nested_1.find_number_to_left() == SnailfishNumber(4)


def test_find_number_to_right():
    num_0 = SnailfishNumber([[[[[9, 8], 1], 2], 3], 4])
    nested_0 = num_0.find_nested_pair()
    assert nested_0.find_number_to_right() == SnailfishNumber(1)

    num_1 = SnailfishNumber([7, [6, [5, [4, [3, 2]]]]])
    nested_1 = num_1.find_nested_pair()
    assert nested_1.find_number_to_right() is None


def test_explode():
    num_0 = SnailfishNumber([[[[[9, 8], 1], 2], 3], 4])
    num_0.explode()
    assert num_0 == SnailfishNumber([[[[0, 9], 2], 3], 4])

    num_1 = SnailfishNumber([7, [6, [5, [4, [3, 2]]]]])
    num_1.explode()
    assert num_1 == SnailfishNumber([7, [6, [5, [7, 0]]]])

    num_2 = SnailfishNumber([[6, [5, [4, [3, 2]]]], 1])
    num_2.explode()
    assert num_2 == SnailfishNumber([[6, [5, [7, 0]]], 3])

    num_3 = SnailfishNumber([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])
    num_3.explode()
    assert num_3 == SnailfishNumber([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])

    num_4 = SnailfishNumber([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])
    num_4.explode()
    assert num_4 == SnailfishNumber([[3, [2, [8, 0]]], [9, [5, [7, 0]]]])


def test_split():
    num_0 = SnailfishNumber(10)
    num_1 = SnailfishNumber(11)
    num_2 = SnailfishNumber(12)
    num_0.split()
    num_1.split()
    num_2.split()
    assert num_0 == SnailfishNumber([5, 5])
    assert num_1 == SnailfishNumber([5, 6])
    assert num_2 == SnailfishNumber([6, 6])


def test_addition():
    num_0 = SnailfishNumber([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
    num_1 = SnailfishNumber([1, 1])
    assert num_0 + num_1 == SnailfishNumber([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])


def test_multiple_addition():
    num_1 = SnailfishNumber([1, 1])
    num_2 = SnailfishNumber([2, 2])
    num_3 = SnailfishNumber([3, 3])
    num_4 = SnailfishNumber([4, 4])
    num_5 = SnailfishNumber([5, 5])
    num_6 = SnailfishNumber([6, 6])
    assert num_1 + num_2 + num_3 + num_4 == SnailfishNumber([[[[1, 1], [2, 2]], [3, 3]], [4, 4]])
    assert num_1 + num_2 + num_3 + num_4 + num_5 == SnailfishNumber([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])
    assert num_1 + num_2 + num_3 + num_4 + num_5 + num_6 == SnailfishNumber([[[[5, 0], [7, 4]], [5, 5]], [6, 6]])


def test_failed_explode():
    num = SnailfishNumber([[[[4, 0], [5, 4]], [[7, 0], [15, 5]]], [10, [[0, [11, 3]], [[6, 3], [8, 8]]]]])
    num.explode()
    assert num == SnailfishNumber([[[[4, 0], [5, 4]], [[7, 0], [15, 5]]], [10, [[11, 0], [[9, 3], [8, 8]]]]])


def test_snailfish_number_from_lines():
    num = SnailfishNumberFromLines(test_input)
    assert num.sum() == SnailfishNumber([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])


def test_snailfish_number_from_lines_1():
    num = SnailfishNumberFromLines(test_input_1)
    assert num.sum() == SnailfishNumber([[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]])


def test_compute_magnitude():
    num_0 = SnailfishNumber([9, 1])
    num_1 = SnailfishNumber([1, 9])
    num_2 = SnailfishNumber([[9, 1], [1, 9]])

    assert num_0.compute_magnitude() == 29
    assert num_1.compute_magnitude() == 21
    assert num_2.compute_magnitude() == 129


def test_find_largest_magnitude():
    num = SnailfishNumberFromLines(test_input_1)
    assert num.find_largest_magnitude() == 3993
