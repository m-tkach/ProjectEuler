def possible_values():
    for c in range(ord('a'), ord('z') + 1):
        yield c
    for c in range(ord('A'), ord('Z') + 1):
        yield c
    for c in ' .,!?()':
        yield ord(c)


def get_cypher():
    with open('p059_cipher.txt', 'r') as ifs:
        line = ifs.readline().replace(',', ' ')
        return [int(c) for c in line.split()]


def calc():
    cypher = get_cypher()

    possible_keys = [[0]*256, [0]*256, [0]*256]
    for i, e, in enumerate(cypher):
        for v in possible_values():
            k = e ^ v
            possible_keys[i%3][k] += 1

    best_key = []
    for keys in possible_keys:
        best = 0
        for key, value in enumerate(keys):
            if value > keys[best]:
                best = key
        best_key.append(best)

    plaintext = []
    for i, c in enumerate(cypher):
        p = c ^ best_key[i%3]
        plaintext.append(p)

    text = "";
    for p in plaintext:
        text += chr(p)
    print(text)

    return sum(plaintext)


print(calc())
