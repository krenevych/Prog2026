def two_max_values(lst: list):
    lst_copy = lst[:]
    lst_copy.sort()
    return lst_copy[-2], lst_copy[-1]  # підпрограма повертає ДВА значення, розділених комою - кортеж значень

######## Main #########

my_list = [1, 34, 45, 12, 7, 124, 11]
print(my_list)  # виведення на екран списку до виклику функції
prev_max, maximum = two_max_values(my_list)  # lst = my_list
print(my_list)  # виведення на екран списку до після функції
print(prev_max, maximum)