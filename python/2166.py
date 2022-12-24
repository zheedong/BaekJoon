n = int(input())

# https://mathworld.wolfram.com/PolygonArea.html
area = 0
init_x, init_y = map(int, input().split())
cur_x, cur_y = init_x, init_y
for _ in range(n - 1):
    new_x, new_y = map(int, input().split())
    area += cur_x * new_y - new_x * cur_y
    cur_x, cur_y = new_x, new_y
area += cur_x * init_y - init_x * cur_y
area /= 2
print(round(abs(area), 1))