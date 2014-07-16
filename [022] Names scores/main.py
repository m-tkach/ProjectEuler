import re

total = 0
with open("names.txt", "r") as ifs:
    names = [re.sub('["]', '', name) for name in ifs.readline().split(",")]
    names.sort()
    for i, name in enumerate(names, start=1):
        for c in name:
            total += i * (ord(c) - ord('A') + 1)
print(total)
