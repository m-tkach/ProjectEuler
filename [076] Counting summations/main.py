N = 100


dp = [[-1] * (N+1) for t in range(N+1)]


def go(x, s):
    if s == N:
        return 1

    if dp[x][s] != -1:
        return dp[x][s]
    
    res = 0
    z = x
    while s + z <= N:
        res += go(z, s+z)
        z += 1

    dp[x][s] = res
    return res


def calc():
    ans = go(1, 0)
    return ans - 1


print(calc())
