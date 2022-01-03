from collections import deque

start, end = map(int, input().split())

search_queue = deque([(0, start)])
searched_pos = set()        # Dynamic Programming

while True:
    depth, cur_pos = search_queue.popleft()
    if cur_pos == end:
        break
    elif cur_pos not in searched_pos:
        if cur_pos < end:        # Heuristic 하게 저장
            search_queue.append((depth + 1, 2 * cur_pos))
            search_queue.append((depth + 1, cur_pos + 1))
        if cur_pos > 0:
            search_queue.append((depth + 1, cur_pos - 1))
        searched_pos.add(cur_pos)
print(depth)