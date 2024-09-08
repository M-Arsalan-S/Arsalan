s = input("Enter the sentence: ").split()
d = {}
for word in s:
    if word not in d:
        d[word] = s.count(word)

for e in sorted(d):
    print(e, ":", d[e])
