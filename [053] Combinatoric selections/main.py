N = 100
MAX = 1000000


def calc():
    ans = 0
    c = [[1], [1, 1]]
    
    for i in range(2, N+1):
        j = i & 1
        p = 1 - j
        
        c[j].append(1)
        c[j].append(1)
        
        for k in range(0, i+1):
            c[j][k] = c[p][k-1] if k > 0 else 0
            c[j][k] += c[p][k] if k < i else 0
            
            if c[j][k] > MAX:
                c[j][k] = MAX + 1
                ans += 1
    
    return ans
        

print(calc())
