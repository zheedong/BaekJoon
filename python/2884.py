h, m = map(int, input().split())

x, y = h, m - 45

while x < 0 or y < 0:
    if y < 0:
        x -=1
        y += 60
    elif x < 0:
        x += 24
print(x, y)