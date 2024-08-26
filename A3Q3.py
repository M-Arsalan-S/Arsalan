def gcd(n, m):
    if min(n, m) == 0:
        return n
    return gcd(min(n, m), max(n, m) % min(n, m))


def lcm(n, m):
    for i in range(max(n,m), n*m+1):
        if i % m == 0 and i % n == 0:
            return i


def main():
    n1 = int(input("n1 = "))
    n2 = int(input("n1 = "))
    print("GCD: ", gcd(n1, n2))
    print("LCM: ", lcm(n1, n2))


main()
