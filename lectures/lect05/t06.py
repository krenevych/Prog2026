# Знайти суму парних чисел з діапазону від 1 до N.


# 1, 2, 3, 4, 5, 6, 7, ... , N

N = int(input("N="))
suma = 0

# counter = 0
# while counter <= N:
#     if counter % 2 == 0: # якщо counter парне число
#         suma = suma + counter
#
#     counter = counter + 1

for counter in range(2, N+1, 2):
    suma = suma + counter

print(suma)