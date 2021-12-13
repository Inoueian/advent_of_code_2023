import pytest

from day_12 import *


small_input = ('start-A\n' +
               'start-b\n' +
               'A-c\n' +
               'A-b\n' +
               'b-d\n' +
               'A-end\n' +
               'b-end')
small_input_lines = small_input.split('\n')

medium_input = ('dc-end\n' +
                'HN-start\n' +
                'start-kj\n' +
                'dc-start\n' +
                'dc-HN\n' +
                'LN-dc\n' +
                'HN-end\n' +
                'kj-sa\n' +
                'kj-HN\n' +
                'kj-dc')
medium_input_lines = medium_input.split('\n')

large_input = ('fs-end\n' +
               'he-DX\n' +
               'fs-he\n' +
               'start-DX\n' +
               'pj-DX\n' +
               'end-zg\n' +
               'zg-sl\n' +
               'zg-pj\n' +
               'pj-he\n' +
               'RW-he\n' +
               'fs-DX\n' +
               'pj-RW\n' +
               'zg-RW\n' +
               'start-pj\n' +
               'he-WI\n' +
               'zg-he\n' +
               'pj-fs\n' +
               'start-RW')
large_input_lines = large_input.split('\n')


def test_neighbor_dict():
    caves = CaveSystem(small_input_lines)
    assert set(caves.neighbor_dict['start']) == {'A', 'b'}
    assert set(caves.neighbor_dict['A']) == {'start', 'c', 'b', 'end'}


def test_create_path_blank():
    caves = CaveSystem(small_input_lines)
    choices, path = caves.create_path([])
    print(choices, path)
    for choice, cave_prev, cave in zip(choices, path[:-1], path[1:]):
        assert caves.neighbor_dict[cave_prev][choice] == cave


def test_create_path():
    caves = CaveSystem(small_input_lines)
    choices, path = caves.create_path([])
    for choice, cave_prev, cave in zip(choices, path[:-1], path[1:]):
        assert caves.neighbor_dict[cave_prev][choice] == cave

    choices, path = caves.create_path([0])
    for choice, cave_prev, cave in zip(choices, path[:-1], path[1:]):
        assert caves.neighbor_dict[cave_prev][choice] == cave


def test_small_system_paths():
    caves = CaveSystem(small_input_lines)
    paths = caves.find_all_paths()
    assert ['start', 'A', 'b', 'A', 'c', 'A', 'end'] in paths
    assert len(paths) == 10


def test_medium_system_paths():
    caves = CaveSystem(medium_input_lines)
    paths = caves.find_all_paths()
    assert ['start', 'HN', 'kj', 'dc', 'end'] in paths
    assert len(paths) == 19


def test_large_system_paths():
    caves = CaveSystem(large_input_lines)
    paths = caves.find_all_paths()
    assert len(paths) == 226


def test_small_system_paths_twice():
    caves = CaveSystem(small_input_lines)
    paths = caves.find_all_paths(small_cave_twice=True)
    print(paths)
    assert len(paths) == 36


def test_medium_system_paths_twice():
    caves = CaveSystem(medium_input_lines)
    paths = caves.find_all_paths(small_cave_twice=True)
    assert len(paths) == 103

def test_large_system_paths_twice():
    caves = CaveSystem(large_input_lines)
    paths = caves.find_all_paths(small_cave_twice=True)
    assert len(paths) == 3509
