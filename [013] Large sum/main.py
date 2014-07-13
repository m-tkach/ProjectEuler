s = 0
with open("digits.txt", "r") as ifs:
    for line in ifs:
        x = int(line)
        s += x
print(str(s)[:10])
