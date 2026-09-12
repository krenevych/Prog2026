x, y = [float(el) for el in input().split()]

# condition1 = x < 0 and x**2 + y**2 <= 4
# condition2 = x >= 0 and abs(x) + abs(y) <= 2
# condition = condition1 or condition2

condition = ((x < 0 and x**2 + y**2 <= 4)
             or (x >= 0 and abs(x) + abs(y) <= 2))

print(condition)