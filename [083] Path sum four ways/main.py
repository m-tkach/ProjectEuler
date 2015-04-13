import heapq


INF = 10**9
MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def load_matrix():
    matrix = []
    N = -1
    with open('p083_matrix.txt', 'r') as ifs:
        for line in ifs:
            stroke = [int(x) for x in line.strip().split(',')]
            if N == -1:
                N = len(stroke)
            assert N == len(stroke)
            matrix.append(stroke)
    assert N == len(matrix)
    return matrix


def calc():
    matrix = load_matrix()
    costs = [[INF]*len(matrix) for line in matrix]
    pq = []

    costs[0][0] = matrix[0][0]
    heapq.heappush(pq, (costs[0][0], (0, 0)))
    while len(pq) > 0:
        t = heapq.heappop(pq)
        dist, i, j = t[0], t[1][0], t[1][1]
        if dist > costs[i][j]:
            continue
        for move in MOVE:
            y = i + move[0]
            x = j + move[1]
            if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[y]):
                continue
            if dist + matrix[y][x] < costs[y][x]:
                costs[y][x] = dist + matrix[y][x]
                heapq.heappush(pq, (costs[y][x], (y, x)))
    return costs[-1][-1]
    

print(calc())

