def max2(a, b):
    print(f"Шукаємо максимум від чисел {a}, {b}")
    if a > b:
        return a
    else:
        return b

def max3(a, b, c):
    return max2(a, max2(b, c))

##### Головна програма #######
# max_ab = max2(3, 4)
# max_ab = max2(33, 24)
max_abc = max3(33, 22, 11)
pass
