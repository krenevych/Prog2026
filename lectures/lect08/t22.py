import math
# def table(xs: list):
#     for x in xs:
#         print(f"f({x}) = {x ** 2}")

def table(xs: list, f): # f - змінна функціонального типу
    for x in xs:
        print(f"f({x}) = { f(x) }")  # f(x) - виклик функції f для параметра x

def sqr(x):
    return x**2

def cubic(x):
    return x**3

######## MAIN

# table([1, 2, 3], sqr)
# table([1, 2, 3], cubic)

pi = math.pi

# table([0, pi/6, pi/4, pi/3, pi/2], math.sin)
table([0, pi/6, pi/4, pi/3, pi/2], math.cos)
