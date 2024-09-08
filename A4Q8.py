import math

steps = [('UP', 5), ('DOWN', 3), ('LEFT', 3), ('RIGHT', 2)]
v, h = 0, 0
for t in steps:
    if t[0] == 'UP':
        v += t[1]
    elif t[0] == 'DOWN':
        v -= t[1]
    elif t[0] == 'LEFT':
        h += t[1]
    elif t[0] == 'RIGHT':
        h -= t[1]

dis = int(math.sqrt(h**2 + v**2))
print(dis)
