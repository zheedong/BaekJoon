import sys
from collections import deque

input = sys.stdin.readline

night_move = [(1, 2), 
              (2, 1),
              (-1, 2),
              (-2, 1),
              (-1, -2),
              (-2, -1),
              (1, -2),
              (2, -1)]

def bfs(length, night_x, night_y, target_x, target_y):
    search_queue = deque([(night_x, night_y, 0)])
    visited = set([])

    while search_queue:
        cur_x, cur_y, cnt = search_queue.popleft()
        if (cur_x, cur_y) in visited:
            continue
        visited.add((cur_x, cur_y))
        if cur_x == target_x and cur_y == target_y:
            return cnt
        for (nx, ny) in night_move:
            next_x = cur_x + nx
            next_y = cur_y + ny
            if next_x < 0 or next_y < 0 or next_x >= length or next_y >= length:
                continue
            search_queue.append((next_x, next_y, cnt + 1))

t = int(input().rstrip())
for _ in range(t):
    length = int(input().rstrip())
    night_x, night_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    print(bfs(length, night_x, night_y, target_x, target_y))