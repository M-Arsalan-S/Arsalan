l = input("Enter comma separated 4-digit binary numbers: ").split(',')
for n in l:
    x = int(n, 2)
    if x % 5 == 0:
        print(n, end=" ")
