# S = input("Введіть рядок ")

S = "ABCCBA"  # симетричний
#    012345
# S = "12345"  # не симетричний

for i in range(len(S) // 2):
    # print(S[len(S) - 1 - i])
    # print(S[i])
    if S[i] != S[len(S) - 1 - i]:
    # if S[i] != S[-1 - i]:
        print("Не симетричний!")
        break
else:
    print("Симетричний")


