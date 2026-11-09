d = {
    1: 13,
    2: 21,
    3: 31,
}

# for k in d:  # обхід по ключах
#     print(k, d[k])

# for v in d.values():  # обхід по значеннях
#     print(v)

for k, v in d.items():  # обхід по парах ключ-значення
    print(k, v)