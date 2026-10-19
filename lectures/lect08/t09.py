def sort_decline(lst: list):  # lst - список - mutable
    lst.sort(reverse=True)

##### MAIN ########

my_list = [1, 34, 45, 12, 7, 124, 11]
print(my_list)
sort_decline(my_list)
print(my_list) # нормально, що функція змінила цей список, бо це її призначення сортувати переданий їй список

