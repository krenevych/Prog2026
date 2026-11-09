s = 'hello world, EEE'

vowel_set = {c.upper() for c in s if c.lower() in 'aeiou'}

print(vowel_set)