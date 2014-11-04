SIZE = 5


primes = [2, 3,]
def gen_primes(n):
    if primes[-1] >= n:
        return
    for x in range(primes[-1]+2, n+1, 2):
        for p in primes:
            if p * p > x:
                primes.append(x)
                break
            if x % p == 0:
                break


def is_prime(x):
    gen_primes(int(x**0.5) + 1)
    for p in primes:
        if p * p > x:
            return True
        if x % p == 0:
            return False
    return True


def is_div_by_3(x, y):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    while y > 0:
        s += y % 10
        y //= 10
    return s % 3 == 0


def is_ok(x, y):
    if is_div_by_3(x, y):
        return False
    a = int(str(x) + str(y))
    if not is_prime(a):
        return False
    b = int(str(y) + str(x))
    return is_prime(b)


def result(candidates):
    return sum(candidates)


def is_cut(candidates, last_index, current_answer):
    res = result(candidates)
    
    if res >= current_answer:
        return True

    for i, c in enumerate(candidates):
        if c > (SIZE - i) * current_answer:
            return True

    if last_index + 1 < len(primes):
        left = SIZE - len(candidates)
        min_left_weight = left * primes[last_index + 1]
        if res + min_left_weight >= current_answer:
            return True

    return False


def go(candidates, last_index, current_answer):
    if is_cut(candidates, last_index, current_answer):
        return current_answer
    
    if len(candidates) == SIZE:
        res = result(candidates)
        if res < current_answer:
            return res
        return current_answer

    for i, p in enumerate(primes[last_index+1:]):
        for c in candidates:
            if not is_ok(p, c):
                break
        else:
            candidates.append(p)
            res = go(candidates, i+last_index+1, current_answer)
            if current_answer > res:
                current_answer = res
            candidates.pop()

    return current_answer


def calc():
    answer = 1000000000
    gen_primes(2000)
    for i, p in enumerate(primes):
        res = go([p,], i, answer)
        if res < answer:
            answer = res
    return answer
        

print(calc())
