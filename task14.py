from utils import get_input


def get_test_input():
    a = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
    return [i.strip() for i in a.split('\n')]


def main0(input_lines: list):
    template = input_lines[0]
    rules = {i.split(' -> ')[0]: i.split(' -> ')[1] for i in input_lines[2:]}
    unique_symbols = set(template) | set(''.join(rules.keys())) | set(''.join(rules.values()))
    for _ in range(10):
        new_template = []
        for i in range(len(template)):
            new_template.append(template[i])
            if template[i:i + 2] in rules:
                new_template.append(rules[template[i:i + 2]])
        template = ''.join(new_template)
    max_s = template.count(template[0])
    min_s = template.count(template[0])
    for s in unique_symbols:
        c = template.count(s)
        if c > max_s:
            max_s = c
        if c < min_s:
            min_s = c
    return max_s - min_s


def main1(input_lines: list):
    template = input_lines[0]
    rules = {i.split(' -> ')[0]: i.split(' -> ')[1] for i in input_lines[2:]}

    pairs = {}
    for i in range(len(template) - 1):
        key = template[i: i + 2]
        pairs[key] = pairs.get(key, 0) + 1

    for _ in range(40):
        new_pairs = {}
        for pair, count in pairs.items():
            new_pair_1 = pair[0] + rules[pair]
            new_pair_2 = rules[pair] + pair[1]
            new_pairs[new_pair_1] = new_pairs.get(new_pair_1, 0) + count
            new_pairs[new_pair_2] = new_pairs.get(new_pair_2, 0) + count
        pairs = new_pairs

    stat = {}
    for pair, count in pairs.items():
        stat[pair[0]] = stat.get(pair[0], 0) + count
        stat[pair[1]] = stat.get(pair[1], 0) + count
    stat = {k: v // 2 for k, v in stat.items()}

    stat[template[0]] += 1
    if template[0] != template[-1]:
        stat[template[-1]] += 1

    sorted_stat_values = list(sorted(stat.values()))
    return sorted_stat_values[-1] - sorted_stat_values[0]


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0, test:', main0(test_input_lines))
    print('Answer 1, test:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, real:', main0(real_input))
    print('Answer 1, real:', main1(real_input))
