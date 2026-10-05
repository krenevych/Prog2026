l = [1, 2, 3, 4, 5, 6]
# s= l.copy()
s = l[:]
last = s.pop()  # ця операція допустима, бо l - список, а значить і s - список, а відтак змінюваний (mutable)
print(last)

print(s)
print(l)