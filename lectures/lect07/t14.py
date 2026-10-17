text = input("Введіть рядок: ")
words = text.split()
# count = len(words)
#
# print(f"Кількість слів: {count}")

text_without_spaces = " ".join(words)

print(f"|{text_without_spaces}|")

pass