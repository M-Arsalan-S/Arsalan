s = list(input("Enter a string: "))
s[0], s[-1] = s[-1], s[0]
string = ""
for c in s:
    string += c
print("New string:", string)
