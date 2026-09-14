# Написати програму для обчислення
# найбільшого спільного дільника двох цілих
# чисел за допомогою алгоритма Евкліда

#  N   M     reminder
# 12  15
# 15  12  # N > M
# 15 % 12 -> 3
# 12 % 3  -> 0
# 3   0

N = int(input("Введіть перше число "))
M = int(input("Введіть друге число "))

# print(N, M, N > M) # N > M
if N < M:
    # поміняти значення змінних N, M місцями
    P = N
    N = M
    M = P

# print(N, M, N > M) # N > M

# while N % M != 0:
#     remainder = N % M
#     N = M
#     M = remainder
# print(M)

while M > 0:
    remainder = N % M
    N = M
    M = remainder
print(N)





