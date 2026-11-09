s = "матан матан матан супер супер матан"

words = s.split()

d = {}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

print(d)

maxword = ""
maxcount = 0

for word, count in d.items():
    if count > maxcount:
        maxword = word
        maxcount = count

print(maxword)