N = 21

dp = [[0] * N] * N

for i in range(N):
    dp[i][0] = dp[0][i] = 1

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N-1][N-1])
