a = float(input("Enter marks for test1 : "))
b = float(input("Enter marks for test2 : "))
c = float(input("Enter marks for test3 : "))
m = min(a, b, c)
print("Average of best two test marks out of the three tests' marks:", (a+b+c-m)/2)
