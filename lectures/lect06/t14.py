lst = [1, 2, 3, 4, 5, 6, 7, 8, 6, 10, 11, 6, 13]
#      0  1  2  3  4  5  6  7  8   9  10  11  12

lst.append(777)
print(lst)

lst_copy = lst.copy()
print(lst_copy)
lst_copy.append(777)
print(lst_copy)
print(lst)