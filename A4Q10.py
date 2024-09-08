test_list = [(15, 6), (16, 7), (16, 8), (16, 10), (17, 13)]
test_list.sort()
l = []
prev = -1
for t in test_list:
    if prev != t[0]:
        l.append(list(t))
    else:
        l[len(l) - 1].append(t[1])
    prev = t[0]

ans = []
for i in l:
    ans.append(tuple(i))

print(ans)