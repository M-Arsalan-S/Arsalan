def fact(no):
    pro = 1
    for i in range(1, no):
        pro *= i
    return pro


l = []
n = int(input("Enter size of list: "))
print("Enter the numbers whose factorials are to be found: ")
for i in range(n):
    l.append(int(input()))

for no in l:
    print(fact(no), end=", ")

