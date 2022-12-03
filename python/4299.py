xy_sum, xy_dif = map(int, input().split())
x = (xy_sum - xy_dif) // 2
y1 = abs(xy_sum - x)
y2 = abs(xy_dif + x)

if y1 == y2:
    if x < 0 or y1 < 0:
        print(-1)
    elif x > y1:
        print(x, y1)
    else:
        print(y1, x)
else:
    print(-1)