def next_word():
    with open('p042_words.txt', 'r') as ifs:
        for s in ifs.read().split(','):
            yield s.replace('"', '')


def char_number(c):
    return ord(c) - ord('A') + 1


def is_triangle(x):
    x *= 2
    r = int(x**0.5)
    return x == r * (r + 1)


def calc():
    ans = 0
    for word in next_word():
        t = 0
        for c in word:
            t += char_number(c)
        if is_triangle(t):
            ans += 1
    return ans
        

print(calc())
