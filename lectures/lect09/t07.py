# Визначення чисел фібоначчі не рекурсивно
def F(n):
    f2, f1 = 1, 1
    for i in range(1, n+1):
        f2, f1 = f1, f2 + f1

    return f2

print(F(100))