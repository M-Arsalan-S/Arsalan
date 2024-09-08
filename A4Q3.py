import math
l = eval(input("Enter comma separated values of D: "))
C, H = 50, 30
for D in l:
    Q = int(math.sqrt((2 * C * D)/H))
    print(Q, end=", ")

