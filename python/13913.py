from collections import deque

n, k = map(int, input().split())

search_queue = deque([(n, [])])

while search_queue:
    cur_n, mov_his = search_queue.popleft()
    mov_his += [cur_n]
    if cur_n == k:
        print(len(mov_his))
        print(*mov_his)
        break
    search_queue.append((2 * cur_n, mov_his[:]))
    search_queue.append((cur_n + 1, mov_his[:]))
    if 0 <= cur_n - 1:
        search_queue.append((cur_n - 1, mov_his[:]))
