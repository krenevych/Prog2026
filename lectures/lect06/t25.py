# Знайти найбільший елемент у списку та його номер

l = [int(el) for el in input("Задайте список: ").split() ]
# print(l)

max = -100500 # милиця
max_i = -1

for i, el in enumerate(l):  # обхід списку по індесках та елементах
    if el > max:
        max = el
        max_i = i

print(max, max_i)
