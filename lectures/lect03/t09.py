x = int(input("x = "))

# if x >= 0:
#     modul_x = x
# else:
#     modul_x = -x

modul_x = x if x >= 0 else -x

print(f"|{x}| = {modul_x}")
