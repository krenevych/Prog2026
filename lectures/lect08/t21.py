# треба знайти суму чисел послідовності
def suma(*tpl):  # * - підказує Python, що tpl - кортеж з довільної кількості елементів
    res = 0
    for el in tpl:
        res += el
    return res


#### MAIN #####

# print(suma(1, 2, 3))
print(f"{suma=}") # <= suma - "змінна", за якою ми можемо дістатися до "коду" підпрограми

hello_world = suma

print(f"{hello_world=}")

res_from_hello_world = hello_world(1, 2, 3, 4)
print(f"{res_from_hello_world=}")
