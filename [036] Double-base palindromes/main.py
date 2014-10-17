LEN = 6


def is_bin_palindrome(x):
    n = x
    s = ''
    while n > 0:
        s += str(n % 2)
        n //= 2
    return (s == s[::-1])


def gen_palindromes():
    pal = [[] for _ in range(LEN+1)]
    
    pal[0] = [0]
    pal[1] = [x for x in range(10)]
    
    for size in range(2, LEN+1):
        for x in range(10):
            for p in pal[size-2]:
                y = x * 10**(size-1) + p * 10 + x
                pal[size].append(y)

    for i in range(1, LEN+1):
        j = 0
        while j < len(pal[i]) and pal[i][j] // 10**(i-1) == 0:
            j += 1
        for p in pal[i][j:]:
            yield p


def calc():
    ans = 0
    pal = gen_palindromes()
    for p in pal:
        if is_bin_palindrome(p):
            ans += p
    return ans    
    

print(calc())

    
