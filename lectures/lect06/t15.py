s = [3, 4, 5, "Hello", "World"]
#    0  1  2       3        4
print(s)

s.append("Last")
print(s)

p = "Hello1"
if p in s:
    hello_position = s.index(p)
    print(hello_position)
else:
    print(f"{p} НЕ міститься у списку")
