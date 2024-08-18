s1 = list(input("Enter string 1: "))
s2 = list(input("Enter string 2: "))
s1[0], s2[0] = s2[0], s1[0]
s1.append(" ")
s = s1 + s2
string = ""
for ele in s:
    string += ele
print("Resultant string:", string)

