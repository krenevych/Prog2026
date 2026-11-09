s = "матан матан матан супер супер матан"

words = s.split()

d = {}
# for word in words:
#     if word not in d:
#         print(word, words.count(word))
#         d[word] = words.count(word)

for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

print(d)
pass