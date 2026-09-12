# Записати умову можливості існування трикутника
# із заданими сторонами a,b,c.

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

a, b, c = [int(el)  for el in input().split()]
print(a + b > c and b + c > a and c + a > b)

# print(a, b, c)

