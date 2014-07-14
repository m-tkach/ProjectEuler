w = {}

w[0] = ""
w[1] = "one"
w[2] = "two"
w[3] = "three"
w[4] = "four"
w[5] = "five"
w[6] = "six"
w[7] = "seven"
w[8] = "eight"
w[9] = "nine"

w[10] = "ten"
w[11] = "eleven"
w[12] = "twelve"
w[13] = "thirteen"
w[14] = "fourteen"
w[15] = "fifteen"
w[16] = "sixteen"
w[17] = "seventeen"
w[18] = "eighteen"
w[19] = "nineteen"

w[20] = "twenty"
w[30] = "thirty"
w[40] = "forty"
w[50] = "fifty"
w[60] = "sixty"
w[70] = "seventy"
w[80] = "eighty"
w[90] = "ninety"

w[100] = "hundred"
w[1000] = "thousand"


N = 1001
ans = 0
for x in range(1, N):
    t = x

    q = t // 1000
    if q:
        s = "%s %s" % (w[q], w[1000])
        ans += len(s) - 1
    t %= 1000

    q = t // 100
    if q:
        s = "%s %s" % (w[q], w[100])
        ans += len(s) - 1
    t %= 100

    if t != 0 and x >= 100:
        ans += 3

    if t < 20:
        s = "%s" % w[t]
        ans += len(s)
    else:
        s = "%s %s" % (w[t // 10 * 10], w[t % 10])
        ans += len(s) - 1

print(ans)

    
    
