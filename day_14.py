from collections import Counter, defaultdict


def parse_data(data):
    template, rule_data = data.split('\n\n')
    rules = rule_data.split('\n')
    return template, rules


def parse_rule_pairs(rule):
    """Keep track of character pairs"""
    pair, _, char = rule.split()
    return pair, (pair[0] + char[0], char[0] + pair[1])


def parse_rules_pairs(rules):
    rule_dict = {}
    for rule in rules:
        pair, pair_tuple = parse_rule_pairs(rule)
        rule_dict[pair] = pair_tuple
    return rule_dict


def convert_to_pair_counts(polymer):
    start = polymer[0]
    end = polymer[-1]
    pairs = [prev + cur for prev, cur in zip(polymer[:-1], polymer[1:])]
    return start, end, Counter(pairs)


def apply_rule_pairs(start, end, count, rules):
    rule_dict = parse_rules_pairs(rules)
    new_count = defaultdict(int)
    for key, value in count.items():
        pair_0, pair_1 = rule_dict[key]
        new_count[pair_0] += value
        new_count[pair_1] += value
    return start, end, new_count


def count_chars(start, end, count):
    char_count = defaultdict(float)
    for key, value in count.items():
        char_0, char_1 = key
        char_count[char_0] += value / 2
        char_count[char_1] += value / 2
    char_count[start] += 1/2
    char_count[end] += 1/2
    return char_count


def count_after_n_steps(polymer, rules, n):
    start, end, count = convert_to_pair_counts(polymer)
    for _ in range(n):
        start, end, count = apply_rule_pairs(start, end, count, rules)
    return count_chars(start, end, count)


if __name__ == '__main__':
    with open('data/day_14_input.txt', 'r') as f:
        data = f.read().strip()

    template, rules = parse_data(data)

    count_1 = count_after_n_steps(template, rules, 10)
    part_1 = max(count_1.values()) - min(count_1.values())

    count_2 = count_after_n_steps(template, rules, 40)
    part_2 = max(count_2.values()) - min(count_2.values())

    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
