def bubble(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def selection(a):
    for i in range(0, len(a)):
        small, pos = a[i], i
        for j in range(i+1, len(a)):
            if a[j] < small:
                small = a[j]
                pos = j
        a[i], a[pos] = a[pos], a[i]
    return a


def insertion(a):
    n = len(a)
    if n <= 1:
        return
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge(a, beg, m, end):
    a1 = a[beg:m+1]
    a2 = a[m+1:end+1]
    k = []
    idx, i1, i2 = 0, 0, 0
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            k.append(a1[i1])
            i1 += 1
        else:
            k.append(a2[i2])
            i2 += 1
        idx += 1

    while i1 < len(a1):
        k.append(a1[i1])
        i1 += 1

    while i2 < len(a2):
        k.append(a2[i2])
        i2 += 1

    a[beg:end+1] = k


def mergesort(a, beg, end):
    if beg < end:
        m = (beg + end) // 2
        mergesort(a, beg, m)
        mergesort(a, m + 1, end)
        merge(a, beg, m, end)
    return a


def main():
    l = [3, 6, 2, 7, 8, 1, 9]
    print("Enter 1 for Bubble sort\nEnter 2 for Selection sort\nEnter 3 for Insertion sort\nEnter 4 for Merge sort")
    c = input()
    match c:
        case '1':
            print(bubble(l))
        case'2':
            print(selection(l))
        case '3':
            print(insertion(l))
        case '4':
            print(mergesort(l, 0, len(l) - 1))
        case _:
            print("Invalid Input!")


main()
