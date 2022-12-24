import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
sadari = [None for _ in range(101)]

for _ in range(n + m):
    x, y = map(int, input().split())
    sadari[x] = y

search_queue = deque([(1, 0)])
visited = set([])

while search_queue:
    cur_pos, cur_depth = search_queue.popleft()

    if cur_pos == 100:
        print(cur_depth)
        break

    if sadari[cur_pos]:
        cur_pos = sadari[cur_pos]
    
    for dice in [1, 2, 3, 4, 5, 6]:
        if cur_pos + dice not in visited:
            visited.add((cur_pos + dice))
            search_queue.append((cur_pos + dice, cur_depth + 1))