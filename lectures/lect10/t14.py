s = 'hello world, EEE, land, united'

vowel_set = {c.lower() for c in s if c.lower() in 'aeiou'}
print(vowel_set)

all_vowels = set('aeiou')
print(all_vowels)

print(vowel_set <= all_vowels)