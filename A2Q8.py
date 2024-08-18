a, b, c = [int(i) for i in input(f"Enter 3 sides: ").split()]

if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print("Form a Right Angled Triangle.")
else:
    print("Do NOT form a Right Angled Triangle.")
