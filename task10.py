from utils import get_input


def get_test_input():
    a = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


open_to_close_brackets = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}
close_to_open_brackets = {b_c: b_o for b_o, b_c in open_to_close_brackets.items()}
bracket_score = {
    '}': 1197,
    ']': 57,
    ')': 3,
    '>': 25137
}

bracket_complete_score = {
    '}': 3,
    ']': 2,
    ')': 1,
    '>': 4
}


def main0(input_lines: list):
    score = 0
    for line in input_lines:
        stack = [line[0]]
        for bracket in line[1:]:
            if bracket in open_to_close_brackets:
                stack.append(bracket)
            elif bracket in close_to_open_brackets:
                if stack[-1] == close_to_open_brackets[bracket]:
                    stack.pop()
                else:
                    score += bracket_score[bracket]
                    break
            else:
                raise Exception('wtf')
    return score


def main1(input_lines: list):
    scores = []
    for line in input_lines:
        stack = [line[0]]
        corrupted = False
        for bracket in line[1:]:
            if bracket in open_to_close_brackets:
                stack.append(bracket)
            elif bracket in close_to_open_brackets:
                if stack[-1] == close_to_open_brackets[bracket]:
                    stack.pop()
                else:
                    corrupted = True
                    break
            else:
                raise Exception('wtf')
        complete = False if stack else True
        if not complete and not corrupted:
            score = 0
            for bracket in reversed(stack):
                score *= 5
                score += bracket_complete_score[open_to_close_brackets[bracket]]
            scores.append(score)
    return list(sorted(scores))[(len(scores) - 1) // 2]


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))
