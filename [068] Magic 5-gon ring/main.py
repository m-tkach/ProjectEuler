from itertools import permutations


MAX = 10
FIGURE_LEN = 5
ANSWER_LEN = 16


def check(figure):
    N = len(figure)
    double_figure = [x for x in figure]
    for x in figure:
        double_figure.append(x)
    
    non_used = [x for x in range(MAX, 0, -1) if not x in figure]
    non_used.sort()

    added_numbers = [-1] * len(double_figure)

    max_index = 0
    for i in range(1, N):
        lhs = double_figure[i] + double_figure[i + 1]
        rhs = double_figure[max_index] + double_figure[max_index + 1]
        if lhs > rhs:
            max_index = i
    
    added_numbers[max_index] = non_used[0]
    cur_sum = added_numbers[max_index] + double_figure[max_index] + double_figure[max_index + 1]
    for j in range(max_index+1, max_index+N):
        z = double_figure[j] + double_figure[j+1]
        delta = cur_sum - z
        if delta in non_used and not delta in added_numbers:
            added_numbers[j] = delta
        else:
            return (False, "")

    res = ""
    for i in range(max_index, max_index+N):
        res += str(added_numbers[i])
        res += str(double_figure[i])
        res += str(double_figure[i+1])

    if len(res) != ANSWER_LEN:
        return (False, int(res))

    return (True, int(res))


def calc():
    answer = 0
    for perm in permutations(range(1, MAX), FIGURE_LEN):
        res = check(perm)
        if res[0]:
            answer = max(answer, res[1])
    return answer


print(calc())
