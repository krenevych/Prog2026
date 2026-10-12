# hello_world = "Hello World"
#
# print(hello_world)

# greeting = input()
# print(greeting)

# for letter in hello_world:
#     print(letter)

# digits = "0123456789 Hello World! ^&(@(*#@#"

s = "hello"
#    01234

# print(s[2])
#
# lst = [1, 2, 3]
# lst[1] = 888  # lst = [1, 888, 3]

# s[0] = "H" # помилка, бо рядок не змінюваний

#  "hello" =>  "Hello"
s = "H" + s[1:]  # рядок підтримує операцію зрізу, крім випадків коли ми намагаємося змінити сам рядок
print(s)

print(len(s))
print(max(s))  # "hello" => o