import math


def ball_collide(a, b):
    dis = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    if dis <= a[2]+b[2]:
        return True
    else:
        return False


def main():

    print("For Ball A: ")
    a = (int(input("Enter x: ")), int(input("Enter y: ")), int(input("Enter r: ")))
    print("For Ball B: ")
    b = (int(input("Enter x: ")), int(input("Enter y: ")), int(input("Enter r: ")))
    print(ball_collide(a, b))


main()
