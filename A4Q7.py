n = int(input("Enter the number of entries: "))
l = []
print("Enter in following format: name,age,score")
for i in range(n):
    l.append(tuple(input().split(',')))
l.sort()
print(l)