import random


def neighborhood_search(digits, space):
    MAX = 100

    for _ in range(MAX):
        temp_digits = list(digits)
        right = random.randint(0, len(digits) - 1)
        left = random.randint(0, right - 1) if right > 0 else 0
        temp_digits[left] = temp_digits[right]
        temp_digits.pop(right)
        ok = True
        for item in space:
            index = 0
            for d in item:
                if d not in temp_digits[index:]:
                    ok = False
                    break
                else:
                    index += temp_digits[index:].index(d) + 1
            if not ok:
                break
        if ok:
            digits = list(temp_digits)
    return digits


def solve(v):
    SEED = 42
    random.seed(SEED)

    start_stage = []
    for item in v:
        digits = list(item)
        index = 0
        for d in digits:
            if d in start_stage[index:]:
                index += start_stage[index:].index(d) + 1
            else:
                start_stage.append(d)
                index = len(start_stage)

    MAX = 25
    ans = list(start_stage)
    for _ in range(MAX):
        ret = neighborhood_search(list(start_stage), v)
        if len(ret) < len(ans):
            ans = ret
    
    return ''.join(ans)


def calc():
    values = []
    with open('p079_keylog.txt', 'r') as ifs:
        for line in ifs:
            values.append(list(line.strip()))
    return solve(values)


print(calc())
