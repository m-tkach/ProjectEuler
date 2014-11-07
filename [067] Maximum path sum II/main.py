def calc():
    with open('p067_triangle.txt', 'r') as ifs:
        dp = [[0]]
        for line in ifs:
            stroke = [int(s) for s in line.split()]
            for i, x in enumerate(stroke):
                from_value = 0
                if i-1 >= 0:
                    from_value = dp[-1][i-1]
                if i < len(dp[-1]):
                    from_value = max(from_value, dp[-1][i])
                stroke[i] += from_value
            dp.append(stroke)
        return max(dp[-1])


print(calc())
