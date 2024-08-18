s = input("Enter a sentence: ")
rev = s[::-1]
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
S = list()  # []
for c in s:
    if c not in S:
        S.append(c)

for i in S:
    count = 0
    for c in s:
        if i == c:
            count += 1
    print(i, "comes", count, "times")
