from collections import deque

n = int(input())
math_map = []
for _ in range(n):
    math_map.append(list(input().split()))

search_queue = deque([(0, 0, [math_map[0][0]])])

nx = (1, 0)
ny = (0, 1)

max_res = -int(1e9)
min_res = int(1e9)

def get_sum(seq):
    res = int(seq[0])
    for idx, val in enumerate(seq):
        if idx % 2 == 1:
            if val == '*':
                res *= int(seq[idx + 1])
            if val == '+':
                res += int(seq[idx + 1])
            if val == '-':
                res -= int(seq[idx + 1])
    return res

while search_queue:
    cur_x, cur_y, history = search_queue.popleft()

    if cur_x == cur_y == n - 1:
        cur_res = get_sum(history)
        max_res = max(max_res, cur_res)
        min_res = min(min_res, cur_res)

    for next in range(2):
        next_x = cur_x + nx[next]
        next_y = cur_y + ny[next]
        if 0 <= next_x < n and 0 <= next_y < n:
            search_queue.append((next_x, next_y, history + [math_map[next_x][next_y]]))

print(f"{max_res} {min_res}")

