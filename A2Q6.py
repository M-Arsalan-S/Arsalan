c = input("Enter C or F: ").upper()
t = float((input("Temperature : ")))
if c == "F":
    print(5*(t-32)/9, "degree C")
elif c == "C":
    print(9*t/5 + 32)