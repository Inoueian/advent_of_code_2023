from day_3 import *

data = ("467..114..\n" +
        "...*......\n" +
        "..35..633.\n" +
        "......#...\n" +
        "617*......\n" +
        ".....+.58.\n" +
        "..592.....\n" +
        "......755.\n" +
        "...$.*....\n" +
        ".664.598..")


def test_get_symbol_list():
    symbol_list = get_symbol_list(data)
    assert [symbol.char for symbol in symbol_list] == ["*", "#", "*", "+", "$", "*"]
    assert [symbol.location for symbol in symbol_list] == [(1, 3), (3, 6), (4, 3),
                                                           (5, 5), (8, 3), (8, 5)]


def test_get_engine_parts():
    engine_parts = get_engine_parts(data)
    assert len(engine_parts) == 10
    part_0 = engine_parts[0]
    part_last = engine_parts[-1]
    assert part_0.number == 467
    assert part_0.locations == [(0, 0), (0, 1), (0, 2)]
    assert part_last.number == 598
    assert part_last.locations == [(9, 5), (9, 6), (9, 7)]


def test_get_connected_engine_parts():
    engine_parts = get_connected_engine_parts(data)
    len(engine_parts) == 8
    part_1 = engine_parts[1]
    assert part_1.number == 35
    assert part_1.locations == [(2, 2), (2, 3)]


def test_get_engine_sum():
    assert get_engine_sum(data) == 4361


def test_get_gear_ratios():
    assert get_gear_ratios(data) == [16345, 451490]


def test_get_gear_ratio_sum():
    assert get_gear_ratio_sum(data) == 467835
