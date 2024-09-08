l = [[5, 6], [4, 7, 10, 17]]
t =[]
for i in l:
    for j in i:
        t.append(tuple([j,]))

print(t)