s = 'hello world!'

vowel_set = {c.lower() for c in s if c.lower() in 'aeiou'}
print(vowel_set)


# Видалити з множини літер, літеру 'o'

vowel_set.remove('o')
print(vowel_set)
# vowel_set.discard('o')
vowel_set.remove('o')

print(vowel_set)
