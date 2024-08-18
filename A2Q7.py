print("Prime numbers less than 20: ")
for i in range(2, 20):
    c = 0
    for j in range(2, i-1):
        if i % j == 0:
            c = 1
            break
    if c == 1:
        continue
    print(i, end=" ")