s = 'hello world!'

vowel_set = {c.lower() for c in s if c.lower() in 'aeiou'}
print(vowel_set)

all_vowels = set('aeiou') # {'a', 'u', 'o', 'e', 'i'}
print(all_vowels)

# Вияснити, які голосні літери, не входять до нашого рядка

print(all_vowels - vowel_set)