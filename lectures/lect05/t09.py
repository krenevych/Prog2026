# 5 -4 11 22 -78 9 0

maxi = 0  # оскільки за умовою шукаємо найбільше серед додатніх
while True:
    a = int(input("a = "))

    if a < 0:
        continue

    if a == 0:
        break

    # a - додатнє число
    if maxi < a:
        maxi = a


print(maxi)