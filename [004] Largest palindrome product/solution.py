def is_pal(x):
    s = str(x)
    return (s == s[::-1])

ans = 0
for x in range(1000):
    for y in range(x+1, 1000):
        res = x * y
        if is_pal(res) and res > ans:
            ans = res
print(ans)
        
