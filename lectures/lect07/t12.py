lst = ["hello", "world", "!"]

s = "___".join(lst) # "hello___world___!"

print(s)

lst2 = s.split("___")

print(lst2)

s1 = " \t \n \r   Hello     world12312    \n  \t   "
lst3 = s1.split()

print(lst3)

s3 = s1.strip()
print(f"|{s1}|")
print(f"|{s3}|")

