from itertools import combinations

n, m = map(int, input().split())
city_map = []
house_list = []
chicken_list = []

for _ in range(n):
    city_map.append(list(map(int, input().split())))
for i, row in enumerate(city_map):
    for j, col in enumerate(row):
        if col == 1:
            house_list.append((i, j))
        elif col == 2:
            chicken_list.append((i, j))

def get_manhattan_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

dp = [[None for _ in range(len(chicken_list))] for _ in range(len(house_list))]

for x, house in enumerate(house_list):
    for y, chicken in enumerate(chicken_list):
        dp[x][y] = get_manhattan_dist(house, chicken)

closed_chicken_num = len(chicken_list) - m

total_min = int(1e10)
for closed_chicken in list(combinations(range(len(chicken_list)), closed_chicken_num)):
    cur_min = 0
    for dist_list in dp:
        buf = int(1e9)
        for idx, dist in enumerate(dist_list):
            if idx in closed_chicken:
                continue
            buf = min(buf, dist)
        cur_min += buf
    total_min = min(total_min, cur_min)

print(total_min)
