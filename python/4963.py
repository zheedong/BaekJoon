from collections import deque
import sys
input = sys.stdin.readline

nx = (0, 1, 1, 1, 0, -1, -1, -1)
ny = (1, 1, 0, -1, -1, -1, 0, 1)

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    land_map = []
    for _ in range(h):
        land_map.append(list(map(int, input().split())))

    search_queue = deque([])

    for i in range(h):
        for j in range(w):
            if land_map[i][j] == 1:
                search_queue.append((i, j, True))

    visited = set([])
    island_cnt = 0
    while search_queue:
        cur_x, cur_y, is_new_island = search_queue.pop()
        if (cur_x, cur_y) in visited:
            continue
        visited.add((cur_x, cur_y))
        if is_new_island:
            island_cnt += 1
        for next in range(8):
            next_x, next_y = cur_x + nx[next], cur_y + ny[next]
            if 0 <= next_x < h and 0 <= next_y < w and land_map[next_x][next_y] == 1:
                search_queue.append((next_x, next_y, False))
    print(island_cnt)
    
