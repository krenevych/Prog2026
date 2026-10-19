def sum_of_digits(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10

    return suma

#### MAIN ###

N = 256
print(sum_of_digits(N))  # N - 256, цілий тип дани, immutable, тому не переживаємо, що функція може якось змінити його
print(N)