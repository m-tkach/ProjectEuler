N = 10**6
LEN = 60


f = [-1] * 10
def fact(x):
    if f[x] == -1:
        if x < 2:
            f[x] = 1
        else:
            f[x] = x * fact(x - 1)
    return f[x]


fact_sum = [-1] * N
def get_digit_fact_sum(x):
    if x == 0:
        return fact(0)

    if x < len(fact_sum) and fact_sum[x] != -1:
        return fact_sum
    
    res = 0
    while x > 0:
        res += fact(x % 10)
        x //= 10
    
    if x < len(fact_sum):
        fact_sum[x] = res
    
    return res


def calc():
    ans = 0
    cache = dict()
    
    for x in range(1, N):
        ans_len = 0
        if x in cache:
            ans_len = cache[x]
        else:
            used = [x, ]
            ans_len = 1
            z = get_digit_fact_sum(x)
            while not z in used:
                if z in cache:
                    ans_len += cache[z]
                    break
                used.append(z)
                ans_len += 1
                z = get_digit_fact_sum(z)

            i, p = 0, used[0]
            while i < len(used) and used[i] != z:
                p = used[i]
                cache[p] = ans_len - i
                i += 1

            cycle = ans_len - i
            while i < len(used):
                p = used[i]
                cache[p] = cycle
                i += 1
        
        if ans_len == LEN:
            ans += 1
    
    return ans


print(calc())


