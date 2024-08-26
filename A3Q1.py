st = input("Enter a string: ").lower()
s = {}
for i in st:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
print(s)
