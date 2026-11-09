# кількість входжень кожного слова до рядка.
s = "матан матан матан супер супер матан"

words = s.split()
print(words)
words_set = set(words)
print(words_set)

d = {}
for word in words_set:
    print(word, words.count(word))
    d[word] = words.count(word)

print(d)