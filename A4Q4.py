s = list(input("Enter comma separated words: ").split(','))
s.sort(key=str.lower)
print(s)
