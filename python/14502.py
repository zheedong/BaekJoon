from copy import deepcopy
from itertools import combinations
n, m = map(int, input().split())

EMPTY = 0
WALL = 1
VIRUS = 2

virus_map = []

for _ in range(n):
    virus_map.append(list(map(int, input().split())))

empty_mask = []
for i in range(n):
    for j in range(m):
        if virus_map[i][j] == EMPTY:
            empty_mask.append((i, j))

max_safe = -1

def get_arround(poss):
    cur_x, cur_y = poss
    nx = [1, -1, 0, 0]
    ny = [0, 0, 1, -1]
    res = []
    for i in range(4):
        next_x = cur_x + nx[i]
        next_y = cur_y + ny[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            res.append((next_x, next_y))
    return res

def dfs():
    global virus_map
    expansion_lst = []
    for row in range(n):
        for col in range(m):
            if virus_map[row][col] == VIRUS:
                for arround in get_arround((row, col)):
                    x, y = arround
                    if virus_map[x][y] == EMPTY:
                        expansion_lst.append(arround)
    if expansion_lst:
        for expand in expansion_lst:
            x, y = expand
            virus_map[x][y] = VIRUS
        dfs()
    else:
        return

def count_empty():
    global virus_map
    cnt = 0
    for row in range(n):
        for col in range(m):
            if virus_map[row][col] == EMPTY:
                cnt += 1
    return cnt

for wall_info in combinations(empty_mask, 3):
    wall1 = wall_info[0]
    x1, y1 = wall1
    wall2 = wall_info[1]
    x2, y2 = wall2
    wall3 = wall_info[2]
    x3, y3 = wall3

    if virus_map[x1][y1] == EMPTY and virus_map[x2][y2] == EMPTY and virus_map[x3][y3] == EMPTY:
        buf = deepcopy(virus_map)
        virus_map[x1][y1] = WALL
        virus_map[x2][y2] = WALL
        virus_map[x3][y3] = WALL
        dfs()
        max_safe = max(max_safe, count_empty())
        virus_map = buf[:]

print(max_safe)