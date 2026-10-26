# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
# 0  1  2  3  4  5   6   7   8   9

def F(n):
    if n == 0 or n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

print(
    F(8)
)