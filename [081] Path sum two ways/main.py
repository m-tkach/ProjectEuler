INF = 10**9


def load_matrix():
    matrix = []
    assert_size = -1
    with open('p081_matrix.txt', 'r') as ifs:
        for line in ifs:
            stroke = [int(x) for x in line.strip().split(',')]
            if assert_size == -1:
                assert_size = len(stroke)
            assert assert_size == len(stroke)
            matrix.append(stroke)
    assert assert_size == len(matrix)
    return matrix


def calc():
    matrix = load_matrix()
    for i, line in enumerate(matrix):
        for j, value in enumerate(line):
            if i == 0 and j == 0:
                continue
            up = matrix[i-1][j] if i > 0 else INF
            left = line[j-1] if j > 0 else INF
            line[j] += min(up, left)
    return matrix[-1][-1]
    

print(calc())
