# треба знайти суму чисел послідовності
def suma(*tpl):  # * - підказує Python, що tpl - кортеж з довільної кількості елементів
    res = 0
    for el in tpl:
        res += el
    return res


#### MAIN #####


sequence_sum = suma(1, 2, 3)
print(sequence_sum)
