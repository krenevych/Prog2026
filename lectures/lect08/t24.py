import math
#
# def sqr(x):
#     return x ** 2
#
# def table(xs, f = sqr): # f - змінна функціонального типу
#     for x in xs:
#         print(f"f({x}) = { f(x) }")  # f(x) - виклик функції f для параметра x
#


def table(xs, f = lambda x: x ** 2): # f - змінна функціонального типу
    for x in xs:
        print(f"f({x}) = { f(x) }")  # f(x) - виклик функції f для параметра x



######## MAIN

pi = math.pi

table((1, 2, 3, 4))
# table((0, 1, 2, 3, 4, 5, 6), math.sin )
table((0, 1, 2, 3), lambda x: x**3 + 1)