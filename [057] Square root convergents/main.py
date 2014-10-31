N = 1000


def calc():
    ans = 0
    
    nom, denom = 1, 1
    for i in range(N+1):
        if len(str(nom)) > len(str(denom)):
            ans += 1
        nom, denom = nom + 2 * denom, nom + denom

    return ans
        

print(calc())
