import itertools


def triangle(n):
    return n * (n + 1) // 2


def square(n):
    return n * n


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return n * (5 * n - 3) // 2


def octagonal(n):
    return n * (3 * n - 2)


def is_polygonal(x, function):
    l, r = 0, x+1
    while l + 1 < r:
        mid = (l + r) // 2
        if function(mid) > x:
            r = mid
        else:
            l = mid
    return function(l) == x


def first_two(x):
    return x // 100


def last_two(x):
    return x % 100


def check_non_eq(path):
    for i, v in enumerate(path):
        for u in path[i+1:]:
            if u == v:
                return False
    return True


def go(graph, v, path, level, MAX):
 
    if len(path) == MAX:
        v, u = path[-1], path[0]
        if last_two(v) == first_two(u) and check_non_eq(path):
            return path
        return []

    index = (level + 1) % len(graph)
    for u in graph[index]:
        if last_two(v) == first_two(u):
            path.append(u)
            res = go(graph, u, path, index, MAX)
            if len(res) > 0:
                return res
            path.pop()
    return []


def calc():
    functions = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
    polygonal = [[] for f in functions]

    for x in range(1000, 10000):
        for i, f in enumerate(functions):
            if is_polygonal(x, f):
                polygonal[i].append(x)

    for perm in itertools.permutations(polygonal):
        for v in perm[0]:
            ans = go(perm, v, [v,], 0, len(perm))
            if len(ans) > 0:
                return sum(ans)
    
    return None

      
print(calc())
