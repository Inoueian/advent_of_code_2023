import pytest

from day_14 import *

test_data = ('NNCB\n' +
             '\n' +
             'CH -> B\n' +
             'HH -> N\n' +
             'CB -> H\n' +
             'NH -> C\n' +
             'HB -> C\n' +
             'HC -> B\n' +
             'HN -> C\n' +
             'NN -> C\n' +
             'BH -> H\n' +
             'NC -> B\n' +
             'NB -> B\n' +
             'BN -> B\n' +
             'BB -> N\n' +
             'BC -> B\n' +
             'CC -> N\n' +
             'CN -> C')


def test_parse_data():
    template, rules = parse_data(test_data)
    assert template == 'NNCB'
    assert len(rules) == 16


def test_parse_rules_pairs():
    _, rules = parse_data(test_data)
    rule_dict = parse_rules_pairs(rules)
    assert rule_dict['CH'] == ('CB', 'BH')


def test_convert_to_pair_counts():
    polymer = 'NNCB'
    start, end, count = convert_to_pair_counts(polymer)
    assert start == 'N'
    assert end == 'B'
    assert count == {'NN': 1, 'NC': 1, 'CB': 1}


def test_count_after_1_step():
    template, rules = parse_data(test_data)
    count = count_after_n_steps(template, rules, 1)
    assert count == {'N': 2, 'C': 2, 'B': 2, 'H': 1}


def test_count_after_n_steps():
    template, rules = parse_data(test_data)
    count = count_after_n_steps(template, rules, 10)
    assert count['B'] == 1749
    assert count['H'] == 161
