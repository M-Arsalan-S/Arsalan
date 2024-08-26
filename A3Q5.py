a = list(map(int, input("Enter the numbers: ").split()))
sum = 0
for i in a:
    sum += i
mean = sum/len(a)
print("Mean:", mean)
s = set(a)
mode = -1
M = 0
for i in s:
    if a.count(i) > M:
        M = a.count(i)
        mode = i
print("Mode:", mode)

a.sort()
s = len(a)
if s % 2 == 0:
    median = (a[int(s/2)] + a[int(s/2) + 1]) / 2
else:
    median = a[int(s/2)]
print("Median:", median)
