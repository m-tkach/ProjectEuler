t = []
with open("triangle.txt", "r") as ifs:
    for line in ifs:
        t.append(list(map(int, line.split())))

i = 1
while i < len(t):
    j = 0
    while j < len(t[i]):
        a = 0
        if j < len(t[i-1]):
            a = t[i-1][j]
        b = 0
        if j-1 >= 0:
            b = t[i-1][j-1]
        t[i][j] += max(a, b)
        j += 1
    i += 1

ans = max(t[-1])
print(ans)
