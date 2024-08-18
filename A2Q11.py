s = input("Enter a sentence: ")
l = s.split()
print("This sentence has", len(l), "words.")
up, low, n = 0, 0, 0
for c in s:
    if c.isupper():
        up += 1
    elif c.islower():
        low += 1
    elif c.isdigit():
        n += 1

print("This sentence has", n, "digit(s)")
print(up, "uppercase character(s)")
print(low, "lowercase character(s)")
