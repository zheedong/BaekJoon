from collections import deque

n = int(input())

search_queue = deque([(n, [n])])

while search_queue:
    cur_x, cur_history = search_queue.popleft()
    if cur_x == 1:
        print(len(cur_history) - 1)
        print(*cur_history)
        break
    if cur_x % 3 == 0:
        search_queue.append((cur_x // 3, cur_history + [cur_x // 3]))
    if cur_x % 2 == 0:
        search_queue.append((cur_x // 2, cur_history + [cur_x // 2]))
    search_queue.append((cur_x - 1, cur_history + [cur_x - 1]))