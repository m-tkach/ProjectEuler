def calc():
    ans = 0
    p = 1
    last_start = 1
    while True:
        x = last_start
        last_start = -1
        
        while True:
            power_len = len(str(x**p))
            
            if power_len > p:
                break
            elif power_len == p:
                ans += 1
                if last_start == -1:
                    last_start = x
            
            x += 1
        
        if last_start == -1:
            break
        
        p += 1
    
    return ans


print(calc())
