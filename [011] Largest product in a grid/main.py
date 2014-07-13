grid = []

with open("grid.in", "r") as ifs:
    for line in ifs:
        stroke = list(map(int, line.split()))
        grid.append(stroke)

max_diag, max_up, max_right = 0, 0, 0
i = 0
while i < len(grid):
    j = 0
    while j < len(grid[i]):
        try:
            up = grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j]
            max_up = max(max_up, up)
        except IndexError:
            pass

        try:
            right = grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3]
            max_right = max(max_right, right)
        except IndexError:
            pass

        try:
            diag = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
            max_diag = max(max_diag, diag)
        except IndexError:
            pass

        try:
            diag = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            max_diag = max(max_diag, diag)
        except IndexError:
            pass

        j += 1
    i += 1

print(max(max_up, max_right, max_diag))
