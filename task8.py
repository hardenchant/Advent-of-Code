import itertools

from utils import get_input


def get_test_input():
    a = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def main0(input_lines: list):
    count_to_nums_precise = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    answer = 0
    for line in input_lines:
        prepare, focus = line.split(' | ')
        focus = focus.split(' ')
        focus_counters = [len(i) for i in focus]
        for count in count_to_nums_precise.keys():
            answer += focus_counters.count(count)
    return answer


def main1(input_lines):
    num_to_letters = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg'
    }
    num_to_letters = {num: ''.join(sorted(letters)) for num, letters in num_to_letters.items()}
    letters_to_num = {letters: num for num, letters in num_to_letters.items()}
    alp = 'abcdefg'

    result = 0
    for line in input_lines:
        prepare, focus = line.split(' | ')
        prepare = prepare.split(' ')
        focus = focus.split(' ')
        pool = set(''.join(sorted(i)) for i in prepare) | set(''.join(sorted(i)) for i in focus)
        true_perm = None
        for permutation in list(itertools.permutations(alp)):
            perm = {permutation[i]: alp[i] for i in range(len(alp))}
            new_pool = set()
            bad_perm = False
            for word in pool:
                decoded_word = ''.join(sorted([perm[c] for c in word]))
                if decoded_word in letters_to_num and decoded_word not in new_pool:
                    new_pool.add(decoded_word)
                else:
                    bad_perm = True
                    break
            if not bad_perm:
                true_perm = perm
                break
        decodes = []
        for word in focus:
            decodes.append(
                letters_to_num[''.join(sorted([true_perm[c] for c in word]))]
            )
        result += int(''.join([str(i) for i in decodes]))
    return result


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))
