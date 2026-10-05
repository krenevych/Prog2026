# Знайти найбільший елемент у списку та його номер

l = [int(el) for el in input("Задайте список: ").split() ]
# print(l)

max = -100500 # милиця
max_i = -1
# i = 0
# for el in l:  # обхід списку по елементах
#     if el > max:
#         max = el
#         max_i = i
#
#     i = i + 1

for i in range(len(l)):  # обхід списку по індексах
    el = l[i]
    if el > max:
        max = el
        max_i = i

print(max, max_i)
