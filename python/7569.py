import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

# 0
tomato_not_ripen = set([])
# 1
tomato_ripen = set([])
# 토마토가 없는 칸은 저장할 필요가 없다.

for cur_h in range(h):
    for cur_n in range(n):
        for cur_m, tomato in enumerate(list(map(int, input().split()))):
            if tomato == 0:
                tomato_not_ripen.add((cur_m, cur_n, cur_h))
            elif tomato == 1:
                tomato_ripen.add((cur_m, cur_n, cur_h))

def get_adj_tomatos(cur_tomato):
    cur_m, cur_n, cur_h = cur_tomato
    ret = []
    if cur_m > 0:
        ret.append((cur_m - 1, cur_n, cur_h))
    if cur_m < m:
        ret.append((cur_m + 1, cur_n, cur_h))
    if cur_n > 0:
        ret.append((cur_m, cur_n - 1, cur_h))
    if cur_n < n:
        ret.append((cur_m, cur_n + 1, cur_h))
    if cur_h > 0:
        ret.append((cur_m, cur_n, cur_h - 1))
    if cur_h < h:
        ret.append((cur_m, cur_n, cur_h + 1))
    return ret

search_queue = deque(list(map(lambda x : (x, 0) ,tomato_ripen)))

while search_queue:
    cur_tomato, depth = search_queue.popleft()
    adj_tomatos = get_adj_tomatos(cur_tomato)
    for adj_tomato in adj_tomatos:
        if adj_tomato in tomato_not_ripen:
            # List의 remove는 O(n), Set의 remove는 O(1) !!
            tomato_not_ripen.remove(adj_tomato)
            tomato_ripen.add(adj_tomato)
            search_queue.append((adj_tomato, depth + 1))

print(-1 if tomato_not_ripen else depth)