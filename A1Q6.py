s = input("Enter a string to check if it is a Palindrome: ").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
